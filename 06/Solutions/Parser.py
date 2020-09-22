from Code import *
def parse(text):
    parsed = open('parsed.txt', 'a+')
    labels_dic = dict()
    i=0
    for line in text:
        raw_line=line.strip("\n")
        if raw_line.isspace():
            continue
        elif raw_line == "":
            continue
        elif "//" in raw_line:
            continue
        elif raw_line.startswith("("):
            label = ((raw_line.strip("(")).strip(")")).strip(" ")
        else:
            if "@" in raw_line:
                lab_instr = raw_line.strip("@")
                if not (lab_instr.isdigit()):
                    Code(lab_instr).a_instr_labels(lab_instr)
                print(raw_line)########################
                a_instr_parsed = Code(raw_line).A_instruction(raw_line)
                print(a_instr_parsed)###################################
                parsed.write(a_instr_parsed)
            elif raw_line.startswith("("):
                label = ((raw_line.strip("(")).strip(")")).strip(" ")
                label_parsed = Code(label).symlabels(label)
            else:
                print(raw_line)########################
                c_instr_parsed= Code(raw_line).C_instruction(raw_line)
                print(c_instr_parsed)####################################
                parsed.write(c_instr_parsed)
                
    i+=1
    parsed.close()