def arithmetic_arranger(problems, display=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_width = max(len(operand1), len(operand2))
        width = max_width + 2  

        first_line += operand1.rjust(width) + "    "
        second_line += operator + operand2.rjust(max_width + 1) + "    "
        dash_line += "-" * width + "    "

        if display:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                 answer = str(int(operand1) - int(operand2))
            answer_line += answer.rjust(width) + "    "

    arranged_problems += first_line.rstrip() + "\n"
    arranged_problems += second_line.rstrip() + "\n"
    arranged_problems += dash_line.rstrip() + "\n"

    if display:
        arranged_problems += answer_line.rstrip() + "\n"

    return arranged_problems.rstrip()

problems1 = ["32 + 698", "3801 + 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems1, True))

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

problems2 = ["44 - 7", "102 - 5600", "9999 - 9999", "716 - 27"]
print(arithmetic_arranger(problems2, True))

