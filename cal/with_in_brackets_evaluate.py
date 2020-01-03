def rd1(string, pos):
    endpos = string.find(")")
    eval_string = string[pos + 1:endpos]
    old_string = str(string[pos:endpos + 1])
    result = str(eval(eval_string))
    replace_string = string.replace(old_string, result)
    return replace_string


def rd2(string, pos):
    first = string.find("(")
    if first != -1:
        string = rd1(string, first)
    endpos = string.find("}")
    eval_string = str(string[pos + 1:endpos])
    old_string = str(string[pos:endpos + 1])
    result = str(eval(eval_string))
    replace_string = string.replace(old_string, result)
    return replace_string


def rd3(string, pos):
    second = string.find("{")
    if second != -1:
        string = rd2(string, second)
        first = string.find("(")
        if first != -1:
            string = rd1(string, first)
    endpos = string.find("]")
    eval_string = str(string[pos + 1:endpos])
    old_string = str(string[pos:endpos + 1])
    result = str(eval(eval_string))
    replace_string = string.replace(old_string, result)
    return replace_string


def b_evaluate(string):
    for pos in range(len(string) - 1):
        if string[pos] == "[":
            string = rd3(string, pos)
            break
        elif string[pos] == "{":
            string = rd2(string, pos)
            break
        elif string[pos] == "(":
            string = rd1(string, pos)
            break

    result = str(eval(string))
    replace_string = string.replace(string, result)
    return replace_string


#string = "[2+{3+(1+2)-1}-2]"
#print(evaluate(string))
