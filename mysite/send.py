import smtplib
import ssl


def sendmail(useremail, message):
    senderemail = "yellowredpidemi@gmail.com"
    receiveremail = "djaliloua@gmail.com"
    port = 587
    pwd = "Hello2022@"
    message = f"You received message from: {useremail}\n\n {message}"
    # Create context
    context = ssl.create_default_context()
    server = smtplib.SMTP("smtp.gmail.com", port)
    server.starttls(context=context)
    server.login("yellowredpidemi@gmail.com", pwd)
    server.sendmail("yellowredpidemi@gmail.com", "djaliloua@gmail.com", message)
    print("Mail sent...")


if __name__ == "__main__":
    sendmail("houdayatoua@gmail.com", "hello")
