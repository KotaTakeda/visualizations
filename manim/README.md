# Manim
[Manim Community](https://docs.manim.community/en/stable/index.html)

## Guide

### installation
- [MacOS](https://docs.manim.community/en/stable/installation/macos.html)
- [Google Colaboratory](https://docs.manim.community/en/stable/installation/jupyter.html#google-colaboratory)

### Docs
- [docs](https://azarzadavila-manim.readthedocs.io/en/latest/index.html)

## Getting Started
`project/scene.py`
```py
from manim import *

class SquareToCircle(Scene):
    def construct(self): # derives from Scene
        # create a circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        # create a square
        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(Create(circle)) # show the circle on screen
```

```
manim -pql scene.py SquareToCircle
```
`media/videos/scene/480p15/SquareToCircle.mp4`にvideoができる．

![SquareToCircle](https://github.com/KotaTakeda/visualizations/blob/main/manim/project/media/videos/scene/1080p60/SquareToCircle_ManimCE_v0.10.0.gif)


## Command options
- play
  - `-p`: 描画後，再生．
  - `-f`: 描画後，ファイルブラウザを開く．
- quality
  - `-ql`: 低品質で描画．
  - `-qm`: 中品質で描画．
  - `-qh`: 高品質で描画．
  - `-qk`: 4K品質で描画．
- その他形式
  - `-s`: 最後のフレームを.pngで保存．
  - `-i`: .gifで保存．
- `-a`: ファイル内の全ての`Scene`クラスを描画．

## Mobjects
`project/mobjects.py`

![PlacingMobjects](https://github.com/KotaTakeda/visualizations/blob/main/manim/project/media/images/mobjects/PlacingMobjects_ManimCE_v0.10.0.png)

## Animations
`project/animations.py`

![ExampleRotation](https://github.com/KotaTakeda/visualizations/blob/main/manim/project/media/videos/animations/480p15/ExampleRotation_ManimCE_v0.11.0.gif)
