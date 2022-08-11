from pyprint import Printer

if __name__ == "__main__":
    p = Printer()
    printers = p.available_printers()
    selected_printer = int(input("Choose a printer:\n"+"\n".join([f"{n} {p}" for n, p in enumerate(printers)])+"\n"))
    p.set_default_printer(printers[selected_printer])
    p.print_file("template.pdf")
    input("press any key to exit")
