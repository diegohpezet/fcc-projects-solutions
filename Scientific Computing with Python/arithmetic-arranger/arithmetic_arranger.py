import re

class MathOperation:
    def __init__(self, n1, n2, sign, show_results = False):
        self.n1 = n1
        self.n2 = n2
        self.sign = sign
        if show_results:
            self.result = int(self.n1) + int(self.n2) if self.sign == '+' else int(self.n1) - int(self.n2)
        else:
            self.result = ''

    def __str__(self):
        # Operation width is equal to longest string + 2
        condition = len(str(self.n1)) >= len(str(self.n2))
        width = len(str(self.n1)) + 2 if condition else len(str(self.n2)) + 2
        
        line = f'{"-" * width}'
        
        operation_string = f"{str(self.n1).rjust(width)}\n{self.sign}{str(self.n2).rjust(width-1)}\n{line}"
        
        if self.result:
            operation_string += f'\n{str(self.result).rjust(width)}'
        
        return operation_string
    
def parse_operation_string(string: str):
    # Define a regular expression pattern to capture digits and non-digits
    pattern = r'(\d+|\D)'
    
    # Use re.split to split the string based on the pattern
    parts = [part.strip() for part in re.split(pattern,string) if part.strip()]

    return MathOperation(int(parts[0]), int(parts[2]), parts[1])

def arithmetic_arranger(array_of_operations, show_results = False):
    list_of_operations = []
    
    if len(array_of_operations) > 5:
        return "Error: Too many problems."
    
    for operation in array_of_operations:
        if "*" in operation or "/" in operation:
            return "Error: Operator must be '+' or '-'."
        
        pattern = r'(\d+|\D)'
        splitted_operation = [part.strip() for part in re.split(pattern,operation) if part.strip()]

        for element in splitted_operation:
            if len(element) > 4:
                return "Error: Numbers cannot be more than four digits."
            
            if element not in ['+','-'] and not(element.isdigit()):
                return "Error: Numbers must only contain digits."
        
        this_operation = MathOperation(splitted_operation[0], splitted_operation[2], splitted_operation[1], show_results)

        list_of_operations.append(this_operation)

    # Split each multiline string into lines
    lines_array = [str(operation).split('\n') for operation in list_of_operations]

    # Transpose the lines to pair corresponding lines
    transposed_lines = list(zip(*lines_array))

    # Concatenate the lines with 4 spaces between them
    result = "\n".join("    ".join(line) for line in transposed_lines)

    return result