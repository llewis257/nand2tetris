import collections
import Parser

PREDEFINED_MEM = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
}

DEST = {
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111",
}

JUMP = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}

COMP = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "M": "1110000",
    "!D": "0001101",
    "!A": "0110001",
    "!M": "1110001",
    "-D": "0001111",
    "-A": "0110011",
    "-M": "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101",
}



class Code:
    def __init__(self, pline):
        free_addresses = iter(range(16, PREDEFINED_MEM['SCREEN']-1))
        variables = collections.defaultdict(free_addresses.__next__)
        labels = dict()
        self.pline = pline
           
    def A_instruction(self, pline):
        line2dec = pline.strip("@") #keeping the decimals
        if line2dec.isdigit():
            dec2bin = '{0:015b}'.format(int(line2dec)) #changing the decimal to  binary
        else:
            dec2bin = '{0:015b}'.format(int(PREDEFINED_MEM[line2dec]))  ###finding equivalent digit when a instruction is a predefined variable
        A_str = "".join('0'+ dec2bin)#changing that decimal's binary to A instruction binary
        return A_str
    def C_instruction(self, pline):
        dest, comp, jump = "","",""
        if "=" in pline:
            part1 = pline.split("=")
            dest = part1[0]
            if ";" in part1[1]:
                part2 = part1[1].split(";")
                jump = part2[1]
                comp = part2[0]
            else:
                comp=part1[1]

        elif ";" in pline:
            part3 = pline.split(";")
            jump= part3[1]
            comp = part3[0]
        C_instr = ''.join("1110"+COMP[comp]+DEST[dest]+JUMP[jump])
        return C_instr

    def symlabels(self, pline):
        label_name= pline
        self.labels[label_name]= Parser.i

    def a_instr_labels(self, pline):
        if pline in PREDEFINED_MEM:    ##################if the label is a predefined memory space
            self.A_instruction(PREDEFINED_MEM[pline]) 
        elif pline in self.labels:     ###################if label has been declared earlier
            self.A_instruction(self.labels[pline])
        else:                          ###################else allocate next free memory
            self.A_instruction(self.variables[pline])