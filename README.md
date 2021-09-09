# Visualizations of Science
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
`-w`でmp4として出力できる．

## メモ
Mac OS Big Sur ではopenGLに関するエラーが出るので以下のように修正．
`venv/lib/python3.7/site-packages/OpenGL/platform/ctypesloader.py`
```
# before
fullName = util.find_library( name )
# after
fullName = "/System/Library/Frameworks/{}.framework/{}".format(name,name)
```

## 参考
- [manimgl](https://github.com/3b1b/manim)