
import colorama

print(colorama.Fore.BLUE + 'This text is blue' + colorama.Style.RESET_ALL)
print(colorama.Back.RED + "This text is red-highlighted" + colorama.Style.RESET_ALL)
print(colorama.Style.BRIGHT + "This text is bold!" + colorama.Style.RESET_ALL)
raise SystemExit(0)

print('This text is still blue')
