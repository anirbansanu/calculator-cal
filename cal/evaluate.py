from root_eval import eval_root
from with_in_brackets_evaluate import b_evaluate


def evaluate(string):
    eval_string = string
    root_sign = string.find("√")
    power_of_sign = string.find("^")
    if power_of_sign != -1:
        eval_string = string.replace("^", "**")
    if root_sign != -1:
        eval_string = eval_root(eval_string)
    if eval_string.find("(") or eval_string.find("{") or eval_string.find("["):
        eval_string = b_evaluate(eval_string)

    eval_string = eval(eval_string)
    return eval_string
