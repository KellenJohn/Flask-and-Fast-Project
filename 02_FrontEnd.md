* 參考網站
  * [參考資訊](http://tsweb44.com/TS_Bootstrap4/i4.html)
  * [Carousel](https://andy6804tw.github.io/2018/01/14/bootstrap-carousel/)
  * [Free Carousel](https://freefrontend.com/bootstrap-carousels/)
  * [Codepen](https://codepen.io/pen/)
  * [html](http://tsweb44.com/TS_Bootstrap4/i18.html)

https://www.wfublog.com/2016/01/font-awesome-cheat-sheet.html

## HTML 基本範例

### 下拉式選單

```html
<select name"select_one>
<option value="1">選擇第一個選項</option>
<option value="2">選擇第二個選項</option>
<option value="3">選擇第三個選項</option>
</select>
```

### 表單選項按鈕 radio buttons

請選擇喜歡吃的水果
○ 蘋果
○ 香蕉

```html
<form>
請選擇喜歡吃的水果<br>
<input type="radio" name="Fruit" value="Apple"> 蘋果<br>
<input type="radio" name="Fruit" value="Bananas"> 香蕉<br>
</form>
```

### Navbar 導覽列

第二行：`<nav class="navbar navbar-expand-sm bg-light navbar-light">` <br>
利用 `<nav>` 標籤宣告導覽列的開頭。                                     <br>
並以 `class="navbar navbar-expand-sm bg-light navbar-light"` 為這個導覽列標註上了各種屬性，                          <br>
包括 "navbar"、"navbar-expand"(橫式導覽列)、"bg-light"(導覽列背景的顏色)、"navbar-light"(導覽列連結的字體顏色)➂。      <br>
更改屬性就可以很快速的更改導覽列的外觀： <br>

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
* `<ul class="navbar-nav">`
  * 利用<ul>無序列清單(unordered list)將導覽列裡面所有的項目放進這個標籤裡。
* <li class="nav-item">
  * 利用標籤<li>說明此為無序列清單中的項目(list item)，代表導覽列中的一個項目。
* `<a class="nav-link" href="#">Link 1</a>`
  * 利用標籤<a>表示這是一個連結，而連接會帶我們前往href指定的位置。



* 導覽列 - 下拉式選單
響應式網頁很重要的可折疊式導覽列(collapsibleNavbar)。
```html
<nav class="navbar navbar-expand-md bg-dark navbar-dark">

  <!-- 宣告一個可折疊的按鈕 -->
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>

  <!-- 導覽列 -->
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
    </ul>
  </div>
</nav>

```

* 導覽列 - 下拉式選單
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
                <li class="active">
                  <a href="/welcome">首頁</a>
                </li>
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

* Bootstrap：Grid System

能夠有效的利用版面，或是盡可能地隨心所欲創造出符合目標設計的排版 `<div class="container">`
Bootstrap 將網頁的版面分成 12 分，或說 12 欄(column)。
我們可以在這 12 欄當中任一個欄位書寫、擺放我們的資料，
從第 1 欄寫到第 2 欄，再從第 3 欄寫到第 6 欄，然後從第 7 欄一直寫到最後，愛怎麼分配就怎麼分配。
```html
<div class="container">
  <div class="row">
    <div class="col-2 bg-light border rounded border-dark">先從第 1 欄寫到第 2 欄</div>
    <div class="col-4 bg-light border rounded border-dark">再從第 3 欄寫到第 6 欄</div>
    <div class="col-6 bg-light border rounded border-dark">然後從第 7 欄一直寫到最後</div>
  </div>
  <div class="row">
    <div class="col bg-light border rounded border-dark">平均等分的第 1 塊</div>
    <div class="col bg-light border rounded border-dark">平均等分的第 2 塊</div>
    <div class="col bg-light border rounded border-dark">平均等分的第 3 塊</div>
  </div>
</div>
```

* 1.放入`<div class="row">`宣告一列的開始。
  在一列當中，我們可以按照自己喜愛的去分配 12 個欄位。  從第 1 欄寫到第 2 欄，總共是 2 個欄位，<br>
  所以用<div class="col-2">。  第 3 欄寫到第 6 欄總共用了 4 個欄位，  所以是<div class="col-4">，以此類推。<br>
  此外，若不在"col"後面特別宣告該欄總共需要橫跨幾個欄位，  那麼 Bootstrap 會自己計算並平均分配給所有沒有宣告數字的欄位。<br>

### Bootstrap：Jumbotron
因為網頁內容還很空虛的關係，讓我們擺一個大大的超大屏幕➃，一次把空間吃光光。

```html
<div class="jumbotron">
  <h1>Bootstrap Tutorial</h1>
  <p>Bootstrap is the most popular HTML, CSS...</p>
</div>
```

使用起來相當方便，用一個<div class="jumbotron">宣告我們將放入超大屏幕就行了！

