# Üst seviye başlık: import edilen dosya
...

## Callouts eklentisi
TIP: **Writing custom titles.**
	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
	nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
	massa, nec semper lorem quam in massa.

>? NOTE: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
> nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
> massa, nec semper lorem quam in massa.

> NOTE: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
> nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
> massa, nec semper lorem quam in massa.

## PlantUML Grafiği
::uml:: format="png" classes="uml myDiagram" alt="My super diagram placeholder" title="My super diagram" width="300px" height="300px"
  Goofy ->  MickeyMouse: calls
  Goofy <-- MickeyMouse: responds
::end-uml::

## Mermaid Grafiği
```mermaid
graph LR
    hello --> world
    world --> again
    again --> hello
```
## Diğer Mermaid
https://pypi.org/project/mkdocs-pymdownx-material-extras/
```diagram
...
```

## Markdown-Blockdiag
blockdiag {
    A -> B -> C -> D;
    A -> E -> F -> G;
}

## Formül denemesi
math kütüphanesi
### Satır içi formül
When $a \ne 0$, there are two solutions to $(ax^2 + bx + c = 0)$ and they are

### satır arası formül
$$ x = {-b \pm \sqrt{b^2-4ac} \over 2a} $$

## İkinci seviye başka başlık
...
```plantuml
@startuml
Bob -> Alice : Can you solve: <math>ax^2+bx+c=0</math>
Alice --> Bob: <math>x = (-b+-sqrt(b^2-4ac))/(2a)</math>
@enduml
```
---

::uml::
Bob -> Alice : Can you solve: <math>ax^2+bx+c=0</math>
Alice --> Bob: <math>x = (-b+-sqrt(b^2-4ac))/(2a)</math>
::end-uml::

---
