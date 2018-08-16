<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Web Filter Block Override</title>
    <style type="text/css">
        html, body { margin: 0; padding: 0; font-family: Verdana, Arial, sans-serif; font-size: 10pt; }
        h1, h2 { height: 82px; text-indent: -999em; margin: 0; padding: 0; margin: 0; }
        div { margin: 0; padding: 0; }
        div.header { background: url(http://www.aianaconda.com:8008/XX/YY/ZZ/CI/MGPGHGPGPFGHCDPFGGOGFGEH) 0 0 repeat-x; height: 82px; }
        div.header h1 { background: url(http://www.aianaconda.com:8008/XX/YY/ZZ/CI/MGPGHGPGPFGHCDPFGGHGFHBGCHEGPFHHGG) 0 0 no-repeat; }
        div.header h2 { background: url(http://www.aianaconda.com:8008/XX/YY/ZZ/CI/MGPGHGPGPFGHCDPFGGOGFGEH) 0 -82px no-repeat; width: 160px; float: right; }
        div.sidebar { width: 195px; height: 200px; float: left; }
        div.main { padding: 5px; margin-left: 195px; }
        div.buttons { margin-top: 30px; text-align: right; }
        h3 { margin: 36px 0; font-size: 16pt; }
        .blocked      h3 { color: #c00; }
        .authenticate h3 { color: #36c; }
        h2.fgd_icon { background: url(http://www.aianaconda.com:8008/XX/YY/ZZ/CI/MGPGHGPGPFGHCDPFGGOGFGEH) 0 -166px repeat-x; width: 90px; height: 92px; margin: 48px auto; }
        .blocked      h2.fgd_icon { background-position: 0 -166px; }
        .authenticate h2.fgd_icon { background-position: -89px -166px; }
        form { width: 300px; margin: 30px 0; }
        label { display: block; width: 300px; margin: 5px 0; line-height: 25px; }
        label input { width: 200px; border: 1px solid #7f9db9; height: 20px; float: right; }
    </style>
</head>
<body class="authenticate">
    <div class="header">
        <h2>Powered By Fortinet</h2>
        <h1>FortiGuard Web Filtering</h1>
    </div>
    <div class="sidebar">
        <h2 class="fgd_icon">authenticate</h2>
    </div>
    <div class="main">
<h3>Web Page Blocked!</h3>
<div class="notice">
    <p>You have tried to access a web page which is in violation of your internet usage policy.</p>
    <p>
        URL: www.aianaconda.com/uploadfiles/tf_1code/8-9__cifar%E5%8D%B7%E7%A7%AF.py<br />
        Category: Unrated
        <br/>Client IP: 10.2.131.133
        <br/>Server IP: 39.106.63.137
        <br/>User name: 
        <br/>Group name: 
    </p>
    <p> To have the rating of this web page re-evaluated <a href="http://url.fortinet.net/rate/submit.php?id=5B5B2B32271C6144342566323A62792D&cat=00&loc=http://www%2eaianaconda%2ecom%2fuploadfiles%2ftf%5f1code%2f8%2d9%5f%5fcifar%25E5%258D%25B7%25E7%25A7%25AF%2epy&ver=6">please click here</a>.</p>
</div>
<div>
   <form>
       <input type="button" value="Proceed" onclick="document.location.href='https://www.aianaconda.com:8010/warn?fblob=XU-ymIDNhdS0SRaiZNn5peqZpj-38bTXX5vkLfka4op58SYiAqw584DT-GGSycXYTS8.&uri=%2fuploadfiles%2ftf%5f1code%2f8%2d9%5f%5fcifar%25E5%258D%25B7%25E7%25A7%25AF%2epy'; return false;">&nbsp;
       <input type="button" value="Go Back" onclick='history.go(-1); return false'>
   </form>
</div>
    </div>
</body>
</html>
