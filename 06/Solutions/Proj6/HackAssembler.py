import collections
from SymbolTab import *
from Parser import *

##### A instruction lines
class AInstruction():
    def __init__(self, code, parser):
        target = code[1:]
        try:
            self.address = int(target)
        except ValueError:
            self.address = parser.resolve_symbol(target)

    def __str__(self):
        return "0{:0>15b}".format(self.address)

##### C instruction lines
class CInstruction():
    def __init__(self, code):
        self.dest, rest = code.split("=") if "=" in code else ("", code)
        self.comp, self.jump = rest.split(";") if ";" in rest else (rest, "")

    def __str__(self):
        return "111{}{}{}".format(COMPARE[self.comp], DESTINATION[self.dest],
                                  JUMP[self.jump])

### Main function (getting the file to assemble, calling the "assembler" function, save the result.)
if __name__ == "__main__":
    file_to_assemble = input()
    binary_ops = Parser(file_to_assemble+".asm").assemble_binary()
    assembled_file = open(file_to_assemble+".hack", "a+")
    for op in binary_ops:
        assembled_file.write(str(op)+"\n")
    assembled_file.close()