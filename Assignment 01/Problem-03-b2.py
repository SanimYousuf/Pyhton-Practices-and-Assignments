def info(**data):
    for key, value in data.items():
        print("{} is {}".format(key,value))


info(Name="Sayem", Address="Faridpur")
info(Name="Arfin", Address="Dhaka", Age=23, Phone="0145562552")