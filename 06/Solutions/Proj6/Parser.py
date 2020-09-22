import collections
from HackAssembler import *

class Parser():
    def __init__(self, filename):
        self.labels = dict()
        free_mem = iter(range(16, GIVEN_SYMBOLS['SCREEN']-1))
        self.variables = collections.defaultdict(free_mem.__next__)

        with open(filename) as f:
            self.lines = self.cleaning(f)

    def cleaning(self, file):
        lines = []
        for line in file:
            clean_line = line.split("//")[0].strip() ### cleaning comments
            if clean_line.startswith("("):  # label declaration
                label_name = clean_line[1:-1]
                self.labels[label_name] = len(lines)  # line number
            elif clean_line:
                lines.append(clean_line)
            else:  # Skip whitespace/comment line
                pass
        return lines

    def assemble_line(self, line): # Assemble cleaned lines, in A instr and C instr
        if line.startswith("@"):
            return AInstruction(line, parser=self)
        else:
            return CInstruction(line)

    def assemble_binary(self):
        return map(self.assemble_line, self.lines)

        ####Symbols
    def resolve_symbol(self, symbol):
        if symbol in self.labels:
            return self.labels[symbol]
        if symbol in GIVEN_SYMBOLS:
            return GIVEN_SYMBOLS[symbol]
        else:
            return self.variables[symbol]  # autoincrement default dictionary
