# Manim
[Manim Community](https://docs.manim.community/en/stable/index.html)

## installation
- [MacOS](https://docs.manim.community/en/stable/installation/macos.html)
- [Google Colaboratory](https://docs.manim.community/en/stable/installation/jupyter.html#google-colaboratory)

## Getting Started
```py
# scene.py

from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
```

```
manim -pql scene.py SquareToCircle
```
`media/videos/scene/480p15/SquareToCircle.mp4`にvideoができる．

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
