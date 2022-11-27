<?php
if ($_POST["message"]) {
    $msg = wordwrap($_POST["message"], 70);
    $header = "From: " . $_POST["email"] . "\r\n";
    $header.= "MIME-Version: 1.0\r\n";
    $header.= "Content-Type: text/html; charset=ISO-8859-1\r\n";
    $header.= "X-Priority: 1\r\n";
    if (mail("drpradhyum2016@outlook.com", $_POST["subject"], $msg, $header)) {
        echo "Success!";
    } else {
        echo "Failure :(";
    }
    // echo "Sender: ", $_POST["email"];
    // echo "Subject: ", $_POST["subject"];
    // echo "Content: ", $_POST["message"];
}
?>