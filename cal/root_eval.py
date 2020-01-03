from with_in_brackets_evaluate import b_evaluate


def calsval(string, pos, end):
    val = ""
    for i in range(pos + 1, end):
        if string[i] == "-" or string[i] == "+" or string[i] == "/" or string[i] == "*":
            break
        else:
            val = val + string[i]
    return val


def eval_root(string):
    root_value_pos = string.find("√")
    if root_value_pos != -1:
        pos = root_value_pos
        if string[pos+1] == "(":
            endpos = string.find(")")
            eval_string = str(string[pos + 1:endpos + 1])
            s2 = b_evaluate(eval_string)
            pos = endpos
        elif string[pos+1] == "{":
            endpos = string.find("}")
            eval_string = str(string[pos + 1:endpos + 1])
            s2 = b_evaluate(eval_string)
            pos = endpos
        elif string[pos+1] == "[":
            endpos = string.find("]")
            eval_string = str(string[pos + 1:endpos + 1])
            s2 = b_evaluate(eval_string)
            pos = endpos
        elif string[pos] == "√":
            s2 = calsval(string, pos, len(string))
            eval_string = s2
        root_value = int(s2) ** 0.5
        #print("root_value : ", root_value)
        replace_string = string.replace("√"+eval_string, str(root_value))
        return replace_string
    return string

def check_calroot_value():
    string = "√100"
    string = eval_root(string)

    print("this is the actual string : ", string)

