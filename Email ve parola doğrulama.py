# Email ve parola doğrulama
email="email@12345.com"
password="deneme12345"
girilenEmail=input("email:")
girilenPassword=input("parola:")
isEmail=(email==girilenEmail.lower().strip())
isPassword=(password==girilenPassword.lower().strip())
print(f"Email doğru girildi mi?:{isEmail} ve parola doğru girildi mi?:{isPassword}")