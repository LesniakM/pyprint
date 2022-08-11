import win32api
import win32print


# Requires Adobe Reader or other pdf reader set as default.
class Printer:
    def __init__(self, default_printer=None):
        self.default_printer = default_printer

    @staticmethod
    def available_printers():
        return [printer[2] for printer in win32print.EnumPrinters(2)]

    def set_default_printer(self, printer_name: str) -> None:
        win32print.SetDefaultPrinter(printer_name)
        self.default_printer = printer_name

    @staticmethod
    def print_file(file):
        win32api.ShellExecute(0, "print", file, None, ".", 0)
