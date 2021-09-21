# manimGL
[home](https://3b1b.github.io/manim/)
## manimのインストール
参考: [manimgl](https://github.com/3b1b/manim#mac-osx)
### for Mac
```
brew install ffmpeg
```

```
git clone https://github.com/3b1b/manim.git
cd manim
pip install -e .
manimgl example_scenes.py OpeningManimExample -w
```
`-w`でmp4として出力できる．`manim/videos/OpeningManimExample.mp4`が生成される．

または
```
cd ..
mkdir videos
manimgl manim/example_scenes.py OpeningManimExample -w --file_name opening_manim_exmaple.mp4
```
とすると`videos/opening_manim_exmaple.mp4`が生成される．

## メモ
Mac OS Big Sur ではopenGLに関するエラーが出るので以下のように修正．
`.venv/lib/python3.7/site-packages/OpenGL/platform/ctypesloader.py`
```
# before
fullName = util.find_library( name )
# after
fullName = "/System/Library/Frameworks/{}.framework/{}".format(name,name)
```

## 参考
- [manimgl](https://github.com/3b1b/manim)