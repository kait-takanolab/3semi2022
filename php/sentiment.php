<?php
$dsn='mysql:dbname=3semi2022;host=localhost;charset=utf8';
$user='root';
$password='';

try {
    $dbh=new PDO($dsn,$user,$password);
    print("DBに接続しました。<br>");

    $dbh->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    
    # INSERT INTO sentiment (id,sentence,posinega,score) 
    # VALUES (1, '私は犬が好きです。', 1, 0.95);

    # プリペアドステートメント
    $sql="insert into sentiment (sentence,posinega,score)" . 
         " values (:sentence, :posinega, :score);";
    
    $stmt=$dbh->prepare($sql);
    #$stmt->bindValue(':id', "2", PDO::PARAM_INT);
    $stmt->bindValue(':sentence',  $_GET["usermsg"], PDO::PARAM_STR);
    $stmt->bindValue(':posinega', 1, PDO::PARAM_INT);
    $stmt->bindValue(':score', 0.98, PDO::PARAM_STR);
    $stmt->execute();
    echo '登録しました。';

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