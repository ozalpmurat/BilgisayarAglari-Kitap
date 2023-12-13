import fnmatch
import os.path
import re
import subprocess
from plantuml import PlantUML
import requests

IMAGE_RE = re.compile('(<img[^>]+src=")([^">]+)("\s*\/?>)')

class SourceUML:
    source_embed_code = None
    source = None
    source_relative = None
    source_embed_relative = None

    def __init__(self, source_embed_code):
        self.source = source_embed_code
        self.source_embed_code = source_embed_code[:-5]


    def resolve_relative(self, page_destination_path):
        self.source_relative = os.path.normpath(os.path.join(
            os.path.dirname(page_destination_path),
            self.source))
        self.source_embed_relative = os.path.normpath(os.path.join(
            os.path.dirname(page_destination_path),
            self.source_embed_code))

class PlantUMLColocator:
    log = None

    def __init__(self, log):
        self.log = log
    
    def rewrite_image_embeds(self, output_content):
        """Rewrite the image embeds in the markdown
        """
   
        sources = "*.puml"
        embed_format = '{img_open}{img_src}{img_close}'
        content_sources = []

        def replace(match):
        
            filename = match.group(2)
            if fnmatch.fnmatch(filename, sources):
                content_sources.append(SourceUML(filename))
                img_src = "{}.png".format(filename[:-5])

                return embed_format.format(
                        img_open=match.group(1), img_close=match.group(3),
                        img_src=img_src)
            else:
                return match.group(0)
        output_content = IMAGE_RE.sub(replace, output_content)
        return (output_content, content_sources)

    def export_file(self, source, dest):
        self.log.debug("Export file %s -> %s" % (source, dest))

        plantuml_code = ""
        with open(source, 'r') as f:
            plantuml_code += f.read()

        image_url = PlantUML("http://www.plantuml.com/plantuml/png/").get_url(plantuml_code)

        with requests.get(image_url) as r:
            if r.status_code >= 400:
                self.log.warn('WARNING running uml: remote server has returned error %d' % r.status_code)
            
            
        with open(dest, 'wb') as w:
            w.write(r.content)