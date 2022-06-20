# D3.js
## Hello World
index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>D3js Hello World</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
    <script src="main.js"></script>
</body>
</html>
```

main.js
```
d3.select("body").append("p").text(() =>  "Hello World");
```
## 参考リンク
- [D3 Data-Driven Documents](https://d3js.org/)
- [D3js gallery](https://observablehq.com/@d3/gallery)
- [earth: d3jsが使われているproject](https://github.com/cambecc/earth)
