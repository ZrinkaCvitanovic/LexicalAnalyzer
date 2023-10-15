def is_operator(word, line_counter):
    if word == "+":
        print("OP_ADD", line_counter, word)
        return True
    if word == "-":
        print("OP_SUB", line_counter, word)
        return True
    if word == "*":
        print("OP_MULTIPLY", line_counter, word)
        return True
    if word == "/":
        print("OP_DIVIDE", line_counter, word)
        return True
    if word == "=":
        print("OP_ASSIGN", line_counter, word)
    if word == "(":
        print("LEFT_P", line_counter, word)
        return True
    if word == ")":
        print("RIGHT_P", line_counter, word)
        return True
    return False


def is_variable(word):
    if not word:
        return False
    if not word[0].isalpha():
        return False
    for char in word:
        if char.isalpha() or str(char).isdigit():
            continue
        else:
            return False
    return True


def is_const(word):
    if not word:
        return False
    for char in word:
        if not str(char).isdigit():
            return False
    return True


def check_expression(word, line_counter):
    variable_or_const = ""
    for character in word:
        if character.isalpha() or str(character).isdigit():
            variable_or_const += character
        else:
            if is_variable(variable_or_const):
                print("ID", line_counter, variable_or_const)
            elif is_const(variable_or_const):
                print("NUM", line_counter, variable_or_const)
            is_operator(character, line_counter)
            variable_or_const = ""

    if variable_or_const != "":
        if is_variable(variable_or_const):
            print("ID", line_counter, variable_or_const)
        elif is_const(variable_or_const):
            print("NUM", line_counter, variable_or_const)


def check_long_words(word, line_counter):
    if word == "for":
        print("KW_FOR", line_counter, word)
    elif word == "rof":
        print("KW_ROF", line_counter, word)
    elif word == "from":
        print("KW_FROM", line_counter, word)
    elif word == "to":
        print("KW_TO", line_counter, word)

    # can be either a variable, a constant or an expression
    else:
        if word[0].isdigit():
            const = ""
            counter = 0
            for char in word:
                if char.isdigit():
                    counter += 1
                    const += char
                else:
                    print("NUM", line_counter, const)
                    word = word[counter::]
                    break
        if is_variable(word):
            print("ID", line_counter, word)
            return
        elif is_const(word):
            print("NUM", line_counter, word)
            return
        else:
            check_expression(word, line_counter)


def main():
    line_counter = 0
    while True:
        try:
            user_input = input()
            if not user_input:
                line_counter += 1
                continue
            words = user_input.split()
            line_counter += 1
            for word in words:
                if word.startswith("//"):
                    break
                elif len(word) > 1:
                    check_long_words(word, line_counter)
                else:
                    if is_const(word):
                        print("NUM", line_counter, word)
                    elif is_variable(word):
                        print("ID", line_counter, word)
                    else:
                        is_operator(word, line_counter)
        except EOFError:
            break


if __name__ == "__main__":
    main()
