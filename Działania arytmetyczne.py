import random
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def random_numbers():
    """ Generates a random number in a given range

    :return: random values for 'a' and 'b'
    """
    min = -10
    max = 10

    a = random.randint(min, max)
    b = random.randint(min, max)

    while True:

        if a == 0:
            a = random.randint(min, max)
        elif b == 0:
            b = random.randint(min, max)
        else:
            break

    return a, b


def store_results(a, b, user_input, op_char, op_func, correct='yes'):
    """ Returns user's result as a string.
    If user's result is correct -> return whole equation string
    If not, -> return string with wrong equation followed by the correct one

    :param a: first value
    :param b: second value
    :param user_input: value provided by user
    :param op_char: opearation character
    :param op_func: operation funciont
    :param correct: yes or no value. Default: yes.
    :return: Returns user result as a string.
    """
    not_equal = chr(8800)
    if correct == 'yes':
        user_results = f"{a} {op_char} {b} = {user_input}"
    else:
        user_results = f"{a} {op_char} {b} {not_equal} {user_input} || {a} {op_char} {b} = {round(op_func(a, b),2)}"
    return user_results


def percentage(part, whole):
    """ Calculates a percentage of correct answers given by the user

    :param part: amount of correct answers
    :param whole: amount af all answers
    :return: Percentage value of correct answers
    """
    pct: float = 100 * int(part)/int(whole)
    pct = int(pct)
    return str(pct) + '%'


def stats(all_results):
    """ Calculates the amount of correct and wrong answers given by the user

    :param all_results: list of all answers provided by the user during the program duration
    :return: amount of correct and wrong answers together with the percentage of the correct values
    """

    correct_answers = []
    wrong_answers = []
    for answer in all_results:
        if '||' in answer:
            wrong_answers.append(answer)
        else:
            correct_answers.append(answer)
    correct_perc = percentage(len(correct_answers), len(all_results))
    return len(correct_answers), len(wrong_answers), correct_perc


def show_all_results(all_results):
    """ Prints the amount of correct and wrong answers followed by the percentage (avarage) for all correct ones

    :param all_results: list of all answers provided by the user during the program duration
    :return: None
    """

    correct_answers, wrong_answers, correct_perc = stats(all_results)
    print(f"\nStatystyka:\n"
          f"Poprawne odpowiedzi: {correct_answers}\n"
          f"Niepoprawnych odpowiedzi: {wrong_answers}\n"
          f"Średnia: {correct_perc} poprawnych odpowiedzi.\n")
    for result in all_results:
        print(result)


def check_user_input(user_value):
    """ Validates the value provided by the user. Expected value is an integer

    :param user_value: value of the equation provided by user
    :return: an integer value (validated)
    """

    while True:
        try:
            # Convert it into integer
            val = int(user_value)
            return val
        except ValueError:
            try:
                # Convert it into float
                val = float(user_value)
                return val
            except ValueError:
                new_result = input(f"Wpisałeś: {user_value} zaminast liczby. Spróbuj ponownie: ")
                user_value = new_result


def computing(a, b, op_char, op_func):
    """ Calculates 'a' and 'b' based on provided sing

    :param a: first value
    :param b: second value
    :param op_char: character sign. Possible values: + , - , * , /
    :param op_func: operational function e.g. operator.add
    :return: full user result, e.g. '10 - 3 = 7' as a str
    """

    user_value = input(f"Ile jest {a} {op_char} {b}? ")

    user_value_validated = check_user_input(user_value)

    if user_value_validated == op_func(a, b):
        print(f"Brawo, prawidłowy wynik to {round(op_func(a, b),2)}.")
        result = store_results(a, b, user_value_validated, op_char, op_func)
        return result

    else:
        print(f"Wynik: {user_value_validated} jest niepoprawny. Prawidłowy to: {round(op_func(a, b),2)}")

        result = store_results(a, b, user_value_validated, op_char, op_func, 'no')
        return result


def main():
    """ Main function

    :return: None
    """

    print("Witaj w grze! \n")
    op_char = input('Jakie działanie chcesz wykonać?\n'
                    '- Dodawanie:   +\n'
                    '- Odejmowanie: -\n'
                    '- Mnożenie:    *\n'
                    '- Dzielenie:   /\n')
    all_results = []

    while True:

        a, b = random_numbers()

        op_func = ops[op_char]

        result = computing(a, b, op_char, op_func)

        all_results.append(result)

        next_move = input("Jeszcze raz?\n")

        if next_move.lower() == 'q':
            show_all_results(all_results)
            break
        else:
            continue


if __name__ == '__main__':
    main()




