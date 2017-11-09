import json, string, sys

#white_space = ["\t","\n"," "]

def trim_from_newline(line):
    if line [-1] == "\n":
        line = line[:-1]
    for index, char in enumerate(line[::-1]):
        if char not in string.whitespace:
            return line[:len(line) - index] + "\n"
    return ""
        

def golf_conversion(ifi, ofi):
    for line in ifi.readlines():
        first_index, line_length = 0, len(line)
        while first_index < line_length and line[first_index] in string.whitespace:
            first_index += 1
        if first_index != line_length
            if line[first_index] == "#":
                ofi.write(trim_from_newline(first_index:])) 
            else:
                break
        
                
        for char in line:
            

def main():
    if sys.argv > 2:
        with open(sys.argv[1], "r") as ifi, open(sys.argv[2], "w") as ofi:
            golf_conversion(ifi, ofi)
    elif sys.argv > 1:
        with open(sys.argv[1], "r") as ifi:
            golf_conversion(ifi, sys.stdout)
    else:
        golf_conversion(sys.stdin, sys.stdout)
        

if __name__ == "__main__":
    main()