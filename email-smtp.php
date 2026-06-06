<?php
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';
require 'PHPMailer/src/Exception.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;


$MailSubject = 'Email From SBIHM & SCHOOL OF BUSINESS AND HOTEL MANAGEMENT Landing Page Section';

$sender_name    = $_POST["name"]; 
$reply_to_email = $_POST["email"];
$phone          = $_POST["phone"];

$MailHtmlMessage = '
    <p><strong>Name:</strong> ' . htmlspecialchars($sender_name) . '</p>
    <p><strong>Email:</strong> ' . htmlspecialchars($reply_to_email) . '</p>
    <p><strong>Phone:</strong> ' . htmlspecialchars($phone) . '</p>
';

// Send email
$mail = new PHPMailer(true);

try {
    $mail->isSMTP();	
    $mail->Host = "smtp.gmail.com";
    $mail->SMTPAuth = true;
    $mail->Username = "plandleadtest@gmail.com";
    $mail->Password = "pwas ggqt voph lxrq"; 
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port       = 587;

    $mail->setFrom('plandleadtest@gmail.com', 'SBIHM & SCHOOL OF BUSINESS AND HOTEL MANAGEMENT');
    $mail->addAddress('admissions.sbihm@gmail.com', 'SBIHM & SCHOOL OF BUSINESS AND HOTEL MANAGEMENT');
    $mail->addAddress('plandleadtest@gmail.com', 'SBIHM & SCHOOL OF BUSINESS AND HOTEL MANAGEMENT');
    $mail->addAddress('strategy@pland.in', 'SBIHM & SCHOOL OF BUSINESS AND HOTEL MANAGEMENT');
	
    $mail->isHTML(true);
    $mail->Subject = $MailSubject;
    $mail->Body    = $MailHtmlMessage;

    $mail->send();

    echo "<script type='text/javascript'>
            window.location.href = 'thankyou.html';
          </script>";
} catch (Exception $e) {
    echo 'Message could not be sent. Mailer Error: ' . $mail->ErrorInfo;
}
?>
