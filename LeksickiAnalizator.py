# ne koristiti regexe!
# TODO: implementiraj zagrade!
def isoperator(word, line_counter):
    if word == "+":
        print('OP_PLUS', line_counter, word)
        return True
    if word == "-":
        print('OP_MINUS', line_counter, word)
        return True
    if word == "*":
        print('OP_PUTA', line_counter, word)
        return True
    if word == "/":
        print('OP_DIJELI', line_counter, word)
        return True
    if word == "=":
        print('OP_PRIDRUZI', line_counter, word)
    if word == "(":
        print('L_ZAGRADA', line_counter, word)
        return True
    if word == ")":
        print('D_ZAGRADA', line_counter, word)
        return True
    return False


def isvariable(word):
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


def isconst(word):
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
            if isvariable(variable_or_const):
                print('IDN', line_counter, variable_or_const)
            elif isconst(variable_or_const):
                print('BROJ', line_counter, variable_or_const)
            isoperator(character, line_counter)
            variable_or_const = ""

    if variable_or_const != "":
        if isvariable(variable_or_const):
            print('IDN', line_counter, variable_or_const)
        elif isconst(variable_or_const):
            print('BROJ', line_counter, variable_or_const)



def check_long_words(word, line_counter):
    if word == "za":
        print('KR_ZA', line_counter, word)
    elif word == "az":
        print('KR_AZ', line_counter, word)
    elif word == "od":
        print('KR_OD', line_counter, word)
    elif word == "do":
        print('KR_DO', line_counter, word)

    # can be either a variable, a constant or an expression
    else:
        if isvariable(word):
            print('IDN', line_counter, word)
            return
        elif isconst(word):
            print('BROJ', line_counter, word)
            return
        else:
            check_expression(word, line_counter)


def main():
    line_counter = 0
    while True:
        try:
            user_input = input("")
            if not user_input:
                continue
            words = user_input.split()
            line_counter += 1
            for word in words:
                if word.startswith("//"):
                    break
                elif len(word) > 1:
                    check_long_words(word, line_counter)
                else:
                    if isconst(word):
                        print('BROJ', line_counter, word)
                    elif isvariable(word):
                        print('IDN', line_counter, word)
                    else: isoperator(word, line_counter)
        except EOFError:
            break


if __name__ == "__main__":
    main()
