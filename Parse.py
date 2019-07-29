SQUARE = ["[", "]"]
ROUND = ["(", ")"]
CURLY = ["{", "}"]
FUNCTION = "@"

OPEN, CLOSE = "[({@", "])}@"


class CMDS:
    CMD = "cmd"
    IF = "if"
    FOR = "for"
    WHILE = "while"
    NOP = "nop"
    FUNCTION = "function"


class Token():
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __str__(self):
        return str(self.name) + " " + str(self.data)


def parse(prog):
    temp, parts, structures, escaped = "", [], [], False
    ast = []

    for char in prog:
        if escaped:
            escaped = not escaped
            continue

        if char == "\\":
            escaped = True
            continue

        if char in OPEN:
            if structures:
                temp += char

            if char == SQUARE[0]:
                structures.append(CMDS.IF)

            elif char == ROUND[0]:
                structures.append(CMDS.FOR)

            elif char == CURLY[0]:
                structures.append(CMDS.WHILE)

            elif char == FUNCTION[0]:
                structures.append(CMDS.FUNCTION)

        elif char in CLOSE:

            struct = structures.pop()

            if len(structures) == 0:
                parts.append(temp)
                temp = ""
                if struct == CMDS.IF:
                    if len(parts) == 0:
                        ast.append(CMDS.NOP)

                    elif len(parts) == 1:
                        ast.append(Token(struct, [parse(parts[0]),
                                                  CMDS.NOP]))

                    elif len(parts) == 2:
                        ast.append(Token(struct, [parse(parts[0]),
                                                  parse(parts[1])]))

                    else:
                        #raise SyntaxError("Too many if parts")
                        ast.append(CMDS.NOP)

                elif struct == CMDS.FOR:
                    if len(parts) == 0:
                        ast.append(CMDS.NOP)

                    elif len(parts) == 1:
                        ast.append(Token(struct, [Token(CMDS.CMD, "!"),
                                                  Token(CMDS.CMD, "¬"),
                                                  parse(parts[0])]))
                    elif len(parts) == 2:
                        ast.append(Token(struct, [parse(parts[0]),
                                                  Token(CMDS.CMD, "¬"),
                                                  parse(parts[1])]))
                    elif len(parts) == 3:
                        ast.append(Token(struct, [parse(parts[0]),
                                                  parse(parts[1]),
                                                  parse(parts[2])]))

                    else:
                        # raise SyntaxError("Too many for parts)
                        ast.append(CMDS.NOP)

                elif struct == CMDS.WHILE:
                    if len(parts) == 0:
                        ast.append(CMDS.NOP)

                    elif len(parts) == 1:
                        ast.append(Token(struct, [Token(CMDS.CMD, "1"),
                                                  Token(CMDS.CMD, "P"),
                                                  parse(parts[0])]))
                    elif len(parts) == 2:
                        ast.append(Token(struct, [parse(parts[0]),
                                                  Token(CMDS.CMD, "P"),
                                                  parse(parts[1])]))
                    elif len(parts) == 3:
                        ast.append(Token(struct, [parse(parts[0]),
                                                  parse(parts[1]),
                                                  parse(parts[2])]))

                    else:
                        # raise SyntaxError("Too many while parts)
                        ast.append(CMDS.NOP)

                elif struct == CMDS.FUNCTION:
                    if len(parts) == 0:
                        ast.append(CMDS.NOP)
                    if len(parts) == 1:
                        ast.append(Token(struct, ["anon", parse(parts[0])]))

                    elif len(parts) == 2:
                        ast.append(Token(struct, [[func(parts[0]),
                                                   parse(parts[1])]]))
                    else:
                        # raise SyntaxError("Too many function parts)
                        ast.append(CMDS.NOP)

            else:
                temp += char

        elif char == "|" and len(structures) == 1:
            parts.append(temp)
            temp = ""

        elif structures:
            temp += char
        else:
            ast.append(Token(CMDS.CMD, char))

    return ast


#while True:
x = input("...: ")
x = parse(x)

for item in x:
    print(item)
