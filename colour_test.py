from colorama import fore, style
#Kirjuta programm, mis küsib kasutajalt tema lemmikvärvi ja väljastab selle põhjal tema temperamendi.

#punane --> energiline
#roosa --> romantik
#roheline --> rahulik
#sinine --> keskendunud
# muud --> imeline ükssarvik

colour = input("Sisesta oma lemmikvärv:").lower()

# if colour == "punane":
#     print("Sa oled energiline inimene!")
# elif colour =="roosa":
#     print("Sa oled romantik!")
# elif colour == "roheline":
#     print("Sa oled rahulik inimene!")
# elif colour == "sinine":
#     print("Sa oled keskendunud inimene!")
# else:
#     print("Sa oled imeline ükssarvik!")

match colour:
    case "punane":
        print(fore.Red + "Sa oled energiline inimene!"+ style.RESET_ALL)
    case "roosa":
        print(fore.Pink + "Sa oled romantik!" + style.RESET_ALL)
    case "roheline":
        print(fore.Green + "Sa oled rahulik inimene!" + style.RESET_ALL)
    case "sinine":
        print(fore.Blue + "Sa oled keskendunud inimene!" + style.RESET_ALL)
    case _:
        print(fore.Cyan + "Sa oled imeline ükssarvik!" + style.RESET_ALL)
         