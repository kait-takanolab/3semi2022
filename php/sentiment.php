<?php
$dsn='mysql:dbname=3semi2022;host=localhost;charset=utf8';
$user='root';
$password='';

try {
    $dbh=new PDO($dsn,$user,$password);
    print("DBに接続しました。<br>");
} catch(PDOException $e){
    print($e->getMessage());
    die();
}

?>

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
    $usermsg = $_GET["usermsg"];
    print("送信されたメッセージ:<br>");

    print($usermsg);
?>
</div>

</body>
</html>