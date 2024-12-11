from textx import metamodel_from_file
class MorseInterpreter:
    def __init__(self):
        self.variables = {}

    def execute(self, model):
        for command in model.commands:
            self._interpret_command(self, command)

    def _interpret_command(self, command):
        break_loop = False
        continue_loop = False
        if command.__class__.__name__ == "AssignCommand":
            self.variables[command.var] = command.value
        elif command.__class__.__name__ == "ManipulateCommand":
            self.variables[command.var] += command.increment
        elif command.__class__.__name__ == "ConditionalBlock":
            if self._evaluate_condition(self, command.condition):
                self._interpret_commands(self, command.block.commands)
            elif command.elseCause:
                self._interpret_commands(self, command.elseClause.block.commands)
        elif command.__class__.__name__ == "DivisionCommand":
            operand1 = self._resolve_value(self, command.dividend)
            operand2 = self._resolve_value(self, command.divisor)
            if operand2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            self.variables[command.result] = operand1 / operand2
        elif command.__class__.__name__ == "ForBlock":
            start = self.variables.get(command.loopVar, 0)
            stop = self._resolve_value(self, command.loopStop)
            step = self._resolve_value(self, command.step) if command.step else 1

            if step == 0:
                raise ValueError("Step value cannot be zero.")

            self.variables[command.loopVar] = start
            while (start <= stop and step > 0) or (start >= stop and step < 0):
                if continue_loop:
                    continue_loop = False
                    start += step
                    self.variables[command.loopVar] = start
                    continue
                if break_loop:
                    break_loop = False
                    break

                self._interpret_command(self, command.block.commands)
                start += step
                self.variables[command.loopVar] = start
        elif command.__class__.__name__ == "IndexCommand":
            list_name = command.list
            search_value = self._resolve_value(self, command.search)
            result_var = command.resultIndex

            if list_name not in self.variables or not isinstance(self.variables[list_name], list):
                raise ValueError(f"variable '{list_name}' is not a list or does not exists.")
            
            try:
                index = self.variables[list_name].index(search_value)
            except ValueError:
                index = -1
            self.variables[result_var] = index
        elif command.__class__.__name__ == "LengthCommand":
            list_name = command.list
            result_length = command.resultLength

            if list_name not in self.variables or not isinstance(self.variables[list_name], list):
                raise ValueError(f"variable '{list_name}' is not a list or does not exists.")
            
            length = len(self.variables[list_name])
            self.variables[result_length] = length
        elif command.__class__.__name__ == "CreateListCommand":
            var_name = command.var
            list_length = command.listLength

            new_list = [None] * list_length

            self.variables[var_name] = new_list
        elif command.__class__.__name__ == "OpenListCommand":
            if list_name not in self.variables or not isinstance(self.variables[list_name], list):
                raise ValueError(f"Variable '{list_name}' is not a list or does not exist.")
            if index < 0 or index >= len(self.variables[list_name]):
                raise IndexError(f"Index {index} is out of bounds for list '{list_name}'.")
            element = self.variables[list_name][index]
            self.variables[command.valueAtIndex] = element
        elif command.__class__.__name__ == "PrintCommand":
            value = command.message
            if value in self.variables:
                print(self.variables[value])
            else:
                print(self._resolve_value(self, value))
        elif command.__class__.__name__ == "RemoveListCommand":
            list_name = command.list
            index = self._resolve_value(self, command.index)
            if list_name not in self.variables or not isinstance(self.variables[list_name], list):
                raise ValueError(f"Variable '{list_name}' is not a list or does not exist.")
            if index < 0 or index >= len(self.variables[list_name]):
                raise IndexError(f"Index {index} is out of bounds for list '{list_name}'.")
            element = self.variables[list_name][index]
            self.variables[list_name].remove(self.variables[list_name][index])
            self.variables[command.itemRemoved] = element
        elif command.__class__.__name__ == "SubtractionCommand":
            operand1 = self._resolve_value(self, command.minuend)
            operand2 = self._resolve_value(self, command.subtrahend)
            self.variables[command.difference] = operand1 - operand2
        elif command.__class__.__name__ == "AdditionCommand":
            operand1 = self._resolve_value(self, command.addend1)
            operand2 = self._resolve_value(self, command.addend2)
            self.variables[command.sum] = operand1 + operand2
        elif command.__class__.__name__ == "BreakCommand":
            break_loop = True
        elif command.__class__.__name__ == "ContinueCommand":
            continue_loop = True
        elif command.__class__.__name__ == "WhileBlock":
            while self._evaluate_condition(self, command.condition):
                if continue_loop:
                    continue_loop = False
                    continue
                if break_loop:
                    break_loop = False
                    break
                self._interpret_command(self,command.block.commands)
        elif command.__class__.__name__ == "MultiplyCommand":
            operand1 = self.resolve_value(command.multiplicand)
            operand2 = self.resolve_value(command.multipler)
            self.variables[command.product] = operand1 * operand2
        else:
            raise ValueError(f"Unknown command type: {command.__class__.__name__}")
        
    def _interpret_commands(self, commands):
        for command in commands:
            self._interpret_command(command)

    def _evaluate_condition(self, condition):
        var1 = self.variables.get(condition.var1, condition.var1)
        var2 = self.variables.get(condition.var2, condition.var2)
        operator = condition.operator

        if operator == '*':
            return var1 == var2
        elif operator == '--*':
            return var1 > var2
        elif operator == '*-**':
            return var1 < var2
        elif operator == '--':
            return var1 >= var2
        elif operator == '-*':
            return var1 != var2
        elif operator == '--*-':
            return var1 <= var2
        else:
            raise ValueError(f"Unknown operator {operator}")
    
    def _resolve_value(self, value):
        if isinstance(value, str):  # If it's a string (ID), check if it's in variables
            if value in self.variables:
                return self.variables[value]
            else:
                raise ValueError(f"Variable '{value}' not found.")
        return value  # If it's not a string, return the value directly (e.g., INT)
 


morseCode_mm = metamodel_from_file('MorseCODE.tx')
#morse_code_model = morseCode_mm.model_from_file('program1.morse')
#print(morse_code_model)
#interpreter = MorseInterpreter()
#interpreter.execute(morse_code_model)

try:
    # This will give the raw model in a structured form
    morse_code_model = morseCode_mm.model_from_file('program1.morse')
    print(f"Model successfully parsed: {morse_code_model}")
except Exception as e:
    print(f"Error parsing the file: {e}")
