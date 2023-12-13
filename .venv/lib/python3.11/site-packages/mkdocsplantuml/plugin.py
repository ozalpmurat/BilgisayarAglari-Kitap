import os.path
import sys

import mkdocs
from mkdocs.config import config_options
import mkdocs.plugins
from mkdocs.structure.files import Files
from mkdocs.utils import copy_file
from .colocator import PlantUMLColocator


log = mkdocs.plugins.log.getChild('plantuml-exporter')

class PlantumlCoLocatedPlugin(mkdocs.plugins.BasePlugin):
    """Plantuml Colocator MkDocs pluging.

    This handles the bindings to the MkDocs events.
    """

    generator = None
    sources = []

    def on_config(self, config):
        self.colocator = PlantUMLColocator(log)
        log.debug("PlantUML debug on config")

    def on_post_page(self, output_content, page, **kwargs):
        output_content, content_sources = self.colocator.rewrite_image_embeds(
            output_content)

        for source in content_sources:
            source.resolve_relative(page.file.dest_path)

        self.sources += content_sources

        return output_content

    def on_post_build(self, config):
        sources = set(self.sources)
        self.sources = []

        for source in sources:
            
            dest_rel_path = '{}.{}'.format(
                    source.source_embed_relative, 'png')
            abs_src_path = os.path.join(config['docs_dir'], source.source_relative)
            abs_dest_path = os.path.join(config['site_dir'], dest_rel_path)
            exit_status = self.colocator.export_file(
                    abs_src_path, abs_dest_path)

            if exit_status not in (None, 0):
                log.error('Export failed with exit status {}; skipping copy'.format(exit_status))
                continue


