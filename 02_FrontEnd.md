
[參考資訊](http://tsweb44.com/TS_Bootstrap4/i4.html)
[Carousel](https://andy6804tw.github.io/2018/01/14/bootstrap-carousel/)
[Codepen](https://codepen.io/pen/)

### Bootstrap

* 支援響應式網頁 (responsive website)➁ 的佼佼者</br>
*註：可根據你的瀏覽視窗的大小，比如說手機螢幕、筆電螢幕、桌電螢幕等等，來變換相對應的排版，使得使用者不論透過哪一種屏幕，都能夠有良好的閱讀效果跟使用者體驗。*

* 外掛好用網頁的元素，如訊息快閃(flash)、導覽列(navbar)、表單(form)、列表(list)、按鈕(button)，

* HTML 5 檔案中加入 url_for()，或是使用 `我是藍圖.url_for()`
* 因網路設計以封閉式為主，因此不採行內容傳遞網路資源 (Content Delivery Network, cdn) 將相關檔案進行下載。
* CSS 相關的資源放在 \<head> 標籤當中，而 JavaScript 相關的資源放在 \<body> 中。

### bootstrap 元件
```html
<head>
  <link rel="style" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
</head>
<body>
  <script src="{{ url_for('static', filename='js/bootstrap.bundle.min.js') }}"></script>
</body>
```

### 下拉式選單

```html


```

### Navbar 導覽列
```html
<body>
<nav class="navbar navbar-expand-sm bg-light navbar-light">
  <ul class="navbar-nav">
    <li class="nav-item">
      <a class="nav-link" href="#">Link 1</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Link 2</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Link 3</a>
    </li>
  </ul>
</nav>
</body>
```

```html
<div class="navbar-wrapper">
    <div class="container">
        <nav class="navbar navbar-inverse navbar-static-top">
          <div class="container">
            <div class="navbar-header">
              <a class="navbar-brand" href="#">功能導航</a>
            </div>
            <div id="navbar" class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li class="active"><a href="/welcome">首頁</a></li>
                <li class="dropdown">
                  <a class="dropdown-toggle" data-toggle="dropdown" href="#">帳號管理<span class="caret"></span></a>  
                  <ul class="dropdown-menu">
                    <li><a href="#">研發雲</a></li>
                    <li><a href="#">資料庫</a></li>
                    <li><a href="#">使用者清單</a></li>
                    <li class="divider"></li>
                    <li><a href="#">管理專區</a></li>
                  </ul>  
                </li>  
                <li><a href="/admin/bootstrap_Esun">資訊展示</a></li>
                <li><a href="/IndexCollect">資訊收集</a></li>
                <li><a href="/NetAutoRun">配置執行</a></li>
                <li><a href="/contact">聯絡我</a></li>
              </ul>
            </div>
          </div>
        </nav>
    </div>
</div>
```

