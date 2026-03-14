# Стара система
class OldPrinter:
    def old_print(self, text):
        return f"OLD PRINT: {text}"

# Новий інтерфейс
class Printer:
    def print_text(self, text):
        pass

# Adapter
class PrinterAdapter(Printer):
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print_text(self, text):
        return self.old_printer.old_print(text)

# Демонстрація
old = OldPrinter()
adapter = PrinterAdapter(old)

print(adapter.print_text("Hello World"))
