<html>
<head><meta charset=UTF-8>
<style>
.msg {
    color: blue;
    font-size: 14pt;
}

</style>
</head>
<body>

<div class="msg">
<?php
    print("メッセージを入力してください。");
?>
</div>

<!-- HTMLフォーム -->
<form name="msgFrm" action="sentiment.php" method="GET">
    <input name="usermsg" type="text" size=64><br>
    <input name="myBtn" type="submit">
</form>
</body>
</html>