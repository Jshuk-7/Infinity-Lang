from config import *
from run_time_result import RTResult
from error import *
from context import Context
from symbol_table import SymbolTable
import infinity

import os
import math
from datetime import datetime

class Value:
    def __init__(self):
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None):
        self.context = context
        return self

    def added_to(self, other):
        return None, self.illegal_operation(other)

    def subbed_by(self, other):
        return None, self.illegal_operation(other)

    def multed_by(self, other):
        return None, self.illegal_operation(other)

    def dived_by(self, other):
        return None, self.illegal_operation(other)

    def powed_by(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_eq(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_ne(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_lt(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_gt(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_lte(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_gte(self, other):
        return None, self.illegal_operation(other)

    def anded_by(self, other):
        return None, self.illegal_operation(other)

    def ored_by(self, other):
        return None, self.illegal_operation(other)

    def notted(self, other):
        return None, self.illegal_operation(other)

    def execute(self, args):
        return RTResult().failure(self.illegal_operation())

    def copy(self):
        raise Exception('No copy method defined')

    def is_true(self):
        return False

    def illegal_operation(self, other=None):
        if not other: other = self
        return RTError(self.pos_start, other.pos_end, 'Illegal operation', self.context)

class Number(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def subbed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def dived_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RTError(
					other.pos_start,
					other.pos_end,
					'Division by zero results in undefined behavior',
					self.context
				)

            return Number(self.value / other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def powed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value**other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_eq(self, other):
        if isinstance(other, Number):
            return Number(int(self.value == other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_ne(self, other):
        if isinstance(other, Number):
            return Number(int(self.value != other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_lt(self, other):
        if isinstance(other, Number):
            return Number(int(self.value < other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_gt(self, other):
        if isinstance(other, Number):
            return Number(int(self.value > other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_lte(self, other):
        if isinstance(other, Number):
            return Number(int(self.value <= other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_gte(self, other):
        if isinstance(other, Number):
            return Number(int(self.value >= other.value)).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def anded_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value and other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def ored_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value or other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def notted(self):
        return Number(1 if self.value == 0 else 0).set_context(self.context), None

    def copy(self):
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def is_true(self):
        return self.value != 0

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

Number.null = Number(0)
Number.false = Number(0)
Number.true = Number(1)
Number.math_PI = Number(math.pi)

class String(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def added_to(self, other):
        if isinstance(other, String):
            return String(self.value + other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other):
        if isinstance(other, Number):
            return String(self.value * other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_eq(self, other):
        if isinstance(other, String):
            return Number(int(self.value == other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_ne(self, other):
        if isinstance(other, String):
            return Number(int(self.value != other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def is_true(self):
        return len(self.value) > 0

    def copy(self):
        copy = String(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'"{self.value}"'

class List(Value):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements

    def added_to(self, other):
        new_list = self.copy()
        new_list.elements.append(other)
        return new_list, None

    def subbed_by(self, other):
        if isinstance(other, Number):
            new_list = self.copy()
            try:
                new_list.elements.pop(other.value)
                return new_list, None
            except:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    f"\nSEGMENTATION FAULT:\nElement at index '{other.value}' is out of bounds",
                    self.context
                )
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other):
        if isinstance(other, List):
            new_list = self.copy()
            new_list.elements.extend(other.elements)
            return new_list, None
        else:
            return None, Value.illegal_operation(self, other)

    def dived_by(self, other):
        if isinstance(other, Number):
            try:
                return self.elements[other.value], None
            except:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    f"\nSEGMENTATION FAULT:\nElement at index '{other.value}' is out of bounds",
                    self.context
                )
        else:
            return None, Value.illegal_operation(self, other)

    def copy(self):
        copy = List(self.elements)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __str__(self):
        return ", ".join([str(x) for x in self.elements])

    def __repr__(self):
        return f'[{", ".join([repr(x) for x in self.elements])}]'

List.days_of_the_week = List([
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
])
List.months_of_the_year = List([
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
])

class BaseFunction(Value):
    def __init__(self, name):
        super().__init__()
        self.name = name or "<anonymous>"

    def generate_new_context(self):
        new_context = Context(self.name, self.context, self.pos_start)
        new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
        return new_context

    def check_args(self, arg_names, args):
        res = RTResult()

        if len(args) > len(arg_names):
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"'{repr(self)}', expected {len(arg_names)} argument(s), found {len(args)}, remove {len(args) - len(arg_names)} to match definition",
                self.context
            ))

        if len(args) < len(arg_names):
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"'{repr(self)}', expected {len(arg_names)} argument(s), found {len(args)}, add {len(arg_names) - len(args)} to match definition",
                self.context
            ))

        return res.success(None)

    def populate_args(self, arg_names, args, exec_ctx):
        for i in range(len(args)):
            arg_name = arg_names[i]
            arg_value = args[i]
            arg_value.set_context(exec_ctx)
            exec_ctx.symbol_table.set(arg_name, arg_value)

    def check_and_populate_args(self, arg_names, args, exec_ctx):
        res = RTResult()
        res.register(self.check_args(arg_names, args))
        if res.should_return(): return res
        self.populate_args(arg_names, args, exec_ctx)
        return res.success(None)

class Function(BaseFunction):
    def __init__(self, name, body_node, arg_names, should_auto_return):
        super().__init__(name)
        self.body_node = body_node
        self.arg_names = arg_names
        self.should_auto_return = should_auto_return

    def execute(self, args):
        res = RTResult()
        interpreter = infinity.Interpreter()
        exec_ctx = self.generate_new_context()

        res.register(
            self.check_and_populate_args(self.arg_names, args, exec_ctx))
        if res.should_return(): return res

        value = res.register(interpreter.visit(self.body_node, exec_ctx))
        if res.should_return() and res.func_return_value == None: return res

        ret_value = (value if self.should_auto_return else None) or res.func_return_value or Number.null
        return res.success(ret_value)

    def copy(self):
        copy = Function(self.name, self.body_node, self.arg_names,
                        self.should_auto_return)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<function {self.name}>"

class BuiltInFunction(BaseFunction):
    def __init__(self, name):
        super().__init__(name)

    def execute(self, args):
        res = RTResult()
        exec_ctx = self.generate_new_context()

        method_name = f'execute_{self.name}'
        method = getattr(self, method_name, self.no_visit_method)

        res.register(
            self.check_and_populate_args(method.arg_names, args, exec_ctx))
        if res.should_return(): return res

        return_value = res.register(method(exec_ctx))
        if res.should_return(): return res
        return res.success(return_value)

    def no_visit_method(self, node, context):
        raise Exception(f'No execute_{self.name} method defined')

    def copy(self):
        copy = BuiltInFunction(self.name)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<built-in function std::{self.name}>"

    #####################################

    def execute_println(self, exec_ctx):
        print(str(exec_ctx.symbol_table.get('value')))
        return RTResult().success(Number.null)
    execute_println.arg_names = ['value']

    def execute_println_ret(self, exec_ctx):
        return RTResult().success(
            String(str(exec_ctx.symbol_table.get('value'))))
    execute_println_ret.arg_names = ['value']

    def execute_input(self, exec_ctx):
        text = input()
        return RTResult().success(String(text))
    execute_input.arg_names = []

    def execute_input_int(self, exec_ctx):
        while True:
            text = input()
            try:
                number = int(text)
                break
            except ValueError:
                print(f"'{text}' must be of type integer")
        return RTResult().success(Number(number))
    execute_input_int.arg_names = []

    def execute_clear(self, exec_ctx):
        os.system('cls' if os.name == 'nt' else 'clear')
        return RTResult().success(Number.null)
    execute_clear.arg_names = []

    def execute_atoi(self, exec_ctx):
        string = exec_ctx.symbol_table.get('string')

        if not isinstance(string, String):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Expected string, found '{string.value}'"
            ))

        return RTResult().success(Number(ord(string.value)))
    execute_atoi.arg_names = ['string']

    def execute_itoa(self, exec_ctx):
        number = exec_ctx.symbol_table.get('number')

        if not isinstance(number, Number):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Expected int, found '{number.value}'"
            ))

        return RTResult().success(String(chr(number.value)))
    execute_itoa.arg_names = ['number']

    def execute_to_string(self, exec_ctx):
        value = exec_ctx.symbol_table.get("value")

        if isinstance(value, List):
            string_from_list = ''

            for element in value.elements:
                if not isinstance(element, List):
                    string_from_list += str(element.value)
                else: # if element is a list then loop through each element and add it to string
                    for list_value in element.elements:
                        string_from_list += str(list_value.value)

            return RTResult().success(String(string_from_list))
        elif isinstance(value, BuiltInFunction):
            return RTResult().success(String(repr(value)))
        elif isinstance(value, BaseFunction):
            return RTResult().success(String(repr(value)))
        else:
            return RTResult().success(String(str(value.value)))
    execute_to_string.arg_names = ['value']

    def execute_to_int(self, exec_ctx):
        value = exec_ctx.symbol_table.get("value")
        return RTResult().success(Number(int(value.value)))
    execute_to_int.arg_names = ['value']

    def execute_string_to_list(self, exec_ctx):
        string = exec_ctx.symbol_table.get('string')
        elements = []

        if not isinstance(string, String):
            if not isinstance(string, List):
                return RTResult().failure(RTError(
                    self.pos_start, self.pos_end,
                    f"Expected string, found '{string.value}'",
                    exec_ctx
                ))
            else:
                return RTResult().failure(RTError(
                    self.pos_start, self.pos_end,
                    f"Expected string, found '{string.elements}'",
                    exec_ctx
                ))

        for char in string.value:
            elements.append(char)
        return RTResult().success(List(elements))
    execute_string_to_list.arg_names = ['string']

    def execute_list_to_string(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get('list')
        elements = []

        if not isinstance(list_, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Expected list, found '{list_.value}'",
                exec_ctx
            ))

        res = ''

        for element in list_.elements:
            if isinstance(element, List):
                for list_value in element:
                    res += str(list_value.value)
            else:
                res += str(element.value)

        return RTResult().success(String(res))
    execute_list_to_string.arg_names = ['list']

    def execute_is_instance(self, exec_ctx):
        type_string = exec_ctx.symbol_table.get('type')

        if not isinstance(type_string, String):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Expected string found '{type_string.value}'" if not isinstance(type_string, List) else f"Expected string found, '{type_string.elements}'",
                exec_ctx
            ))

        if type_string.value == "":
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Expected 'std::int', 'std::string', 'std::list', or 'std::fn'. '' is not a type.",
                exec_ctx
            ))
        elif type_string.value == "std::int":
            is_number = isinstance(exec_ctx.symbol_table.get('value'), Number)
            return RTResult().success(Number.true if is_number else Number.false)
        elif type_string.value == "std::string":
            is_string = isinstance(exec_ctx.symbol_table.get('value'), String)
            return RTResult().success(Number.true if is_string else Number.false)
        elif type_string.value == "std::list":
            is_list = isinstance(exec_ctx.symbol_table.get('value'), List)
            return RTResult().success(Number.true if is_list else Number.false)
        elif type_string.value == "std::fn":
            is_fn = isinstance(exec_ctx.symbol_table.get('value'), BaseFunction)
            return RTResult().success(Number.true if is_fn else Number.false)
        else:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Expected 'std::int', 'std::string', 'std::list', or 'std::fn'. Type '{type_string.value}' does not exist in the language.",
                exec_ctx
            ))
    execute_is_instance.arg_names = ['type', 'value']

    def execute_int_new(self, exec_ctx):
        value = exec_ctx.symbol_table.get('value')

        if not isinstance(value, Number):
            if not isinstance(value, List):
                return RTResult().failure(
                    RTError(value.pos_start, value.pos_end, f"Expected int, found '{value.value}'", exec_ctx)
                )
            else:
                return RTResult().failure(
                    RTError(value.pos_start, value.pos_end, f"Expected int, found '{value.elements}'", exec_ctx)
                )

        return RTResult().success(Number(value.value))
    execute_int_new.arg_names = ['value']

    def execute_string_new(self, exec_ctx):
        value = exec_ctx.symbol_table.get('value')

        if not isinstance(value, String):
            if not isinstance(value, List):
                return RTResult().failure(
                    RTError(value.pos_start, value.pos_end, f"Expected string, found '{value.value}'", exec_ctx)
                )
            else:
                return RTResult().failure(
                    RTError(value.pos_start, value.pos_end, f"Expected string, found '{value.elements}'", exec_ctx)
                )

        return RTResult().success(String(value.value))
    execute_string_new.arg_names = ['value']

    def execute_list_new(self, exec_ctx):
        value = exec_ctx.symbol_table.get('value')

        if not isinstance(value, List):
            return RTResult().failure(
                RTError(value.pos_start, value.pos_end, f"Expected list, found '{value.value}'", exec_ctx)
            )

        return RTResult().success(List(value.elements))
    execute_list_new.arg_names = ['value']

    def execute_push_back(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get('list')
        value = exec_ctx.symbol_table.get('value')

        if not isinstance(list_, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, "First argument must be of type list", exec_ctx)
            )

        list_.elements.append(value)
        return RTResult().success(Number.null)
    execute_push_back.arg_names = ['list', 'value']

    def execute_pop_back(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get('list')

        if not isinstance(list_, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, f"Expected list, found '{list_.value}'", exec_ctx)
            )

        popped_value = list_.elements.pop(len(list_.elements) - 1)

        if not isinstance(popped_value, List):
            return RTResult().success(popped_value)
        else:
            return RTResult().success(popped_value.elements)
    execute_pop_back.arg_names = ['list']

    def execute_pop_at(self, exec_ctx):
        list_, index = self.make_list_and_index(exec_ctx)

        try:
            popped_value = list_.elements.pop(index.value)
        except:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"\nSEGMENTATION FAULT:\nElement at index '{index.value}' is out of bounds",
                exec_ctx)
            )

        return RTResult().success(popped_value)
    execute_pop_at.arg_names = ["list", "index"]

    def execute_push_front(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get('list')
        value = exec_ctx.symbol_table.get('value')

        if not isinstance(list_, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, "First argument must be of type list", exec_ctx)
            )

        list_.elements.insert(0, value)
        return RTResult().success(Number.null)
    execute_push_front.arg_names = ['list', 'value']

    def execute_pop_front(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get('list')

        if not isinstance(list_, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, f"Expected list, found '{list_.value}'", exec_ctx)
            )

        popped_value = list_.elements.pop(0)

        if not isinstance(popped_value, List):
            return RTResult().success(popped_value)
        else:
            return RTResult().success(List(popped_value.elements))
    execute_pop_front.arg_names = ['list']

    def execute_extend(self, exec_ctx):
        listA = exec_ctx.symbol_table.get("listA")
        listB = exec_ctx.symbol_table.get("listB")

        if not isinstance(listA, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, "First argument must be of type list", exec_ctx)
            )

        if not isinstance(listB, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, "Second argument must be of type list", exec_ctx)
            )

        listA.elements.extend(listB.elements)
        return RTResult().success(Number.null)
    execute_extend.arg_names = ["listA", "listB"]

    def execute_insert(self, exec_ctx):
        list_, index = self.make_list_and_index(exec_ctx)

        new_value = exec_ctx.symbol_table.get("value")

        if not isinstance(new_value, type(list_.elements[0])):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, "Lists can only be updated with the same type they hold", exec_ctx)
            )

        elements: list = list_.elements
        elements.insert(index.value, new_value)

        if not isinstance(elements[index.value], List):
            return RTResult().success(elements[index.value])
        else:
            return RTResult().success(elements[index.elements])
    execute_insert.arg_names = ["list", "index", "value"]

    def execute_update(self, exec_ctx):
        list_, index = self.make_list_and_index(exec_ctx)

        new_value = exec_ctx.symbol_table.get("value")

        if not isinstance(new_value, type(list_.elements[0])):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, "Lists can only be updated with the same type they hold", exec_ctx)
            )

        elements: list = list_.elements
        elements[index.value] = new_value

        return RTResult().success(elements[index.value])
    execute_update.arg_names = ["list", "index", "value"]

    def execute_sort(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get('list')

        if not isinstance(list_, List):
            return RTResult().failure(RTError(self.pos_start, self.pos_end, f"Cannot sort '{list_.value}', must be a list"))

        list_.elements.sort(key=lambda x: x.value)

        return RTResult().success(List(list_.elements))
    execute_sort.arg_names = ['list']

    def execute_sort_reverse(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get('list')

        if not isinstance(list_, List):
            return RTResult().failure(RTError(self.pos_start, self.pos_end, f"Cannot sort '{list_.value}', must be a list"))

        list_.elements.sort(key=lambda x: x.value, reverse=True)

        return RTResult().success(List(list_.elements))
    execute_sort_reverse.arg_names = ['list']

    def execute_list_clear(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")

        if not isinstance(list_, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, "First argument must be of type list", exec_ctx)
            )

        list_.elements.clear()

        return RTResult().success(Number.null)
    execute_list_clear.arg_names = ['list']

    def make_list_and_index(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        index = exec_ctx.symbol_table.get("index")

        if not isinstance(list_, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, "First argument must be of type list", exec_ctx)
            )

        if not isinstance(index, Number):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, "Second argument must be of type int", exec_ctx)
            )

        return list_, index

    def execute_len(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")

        if not isinstance(list_, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, "Argument must be of type list", exec_ctx)
            )

        return RTResult().success(Number(len(list_.elements)))
    execute_len.arg_names = ["list"]

    def execute_nth(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")

        if not isinstance(list_, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, "Argument must be of type list", exec_ctx)
            )

        elements = list_.elements
        return_value = elements[len(elements) - 1]

        if isinstance(return_value, Number):
            return RTResult().success(Number(return_value))
        if isinstance(return_value, String):
            return RTResult().success(String(return_value))
        if isinstance(return_value, List):
            return RTResult().success(List(return_value.elements))

    execute_nth.arg_names = ["list"]

    def execute_now(self, exec_ctx):
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        return RTResult().success(String(current_time))
    execute_now.arg_names = []

    def execute_value_copy(self, exec_ctx):
        value = exec_ctx.symbol_table.get('value')
        if not isinstance(value, BaseFunction):
            if isinstance(value, Number):
                return RTResult().success(Number(value.value))
            if isinstance(value, String):
                return RTResult().success(String(value.value))
            if isinstance(value, List):
                return RTResult().success(List(value.elements))
        else:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Cannot copy '{value}'"
            ))
    execute_value_copy.arg_names = ['value']

    def execute_runtime_error(self, exec_ctx):
        error_message = exec_ctx.symbol_table.get('error_message')

        if not isinstance(error_message, String):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be of type string",
                exec_ctx
            ))

        return RTResult().failure(RTError(
            error_message.pos_start, error_message.pos_end,
            error_message.value,
            exec_ctx
        ))
    execute_runtime_error.arg_names = ['error_message']

    def execute_version(self, exec_ctx):
        print(infinity.version())
        return RTResult().success(Number.null)
    execute_version.arg_names = []

    def execute_run(self, exec_ctx):
        fn = exec_ctx.symbol_table.get("fn")

        if not isinstance(fn, String):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Argument must be of type string",
                exec_ctx
			))

        fn: str = fn.value

        if not fn.endswith(EXTERN_FILE_EXTENSION):
            return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				f"The Infinity interpreter can only accept files that end in {EXTERN_FILE_EXTENSION}",
				exec_ctx
			))

        try:
            with open(fn, "r") as f:
                script = f.read()
        except Exception as e:
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end, f"Failed to load script \"{fn}\"\n" + str(e),
                exec_ctx
			))

        _, error = infinity.run(fn, script)

        if error:
            return RTResult().failure(
                RTError(
                    self.pos_start, self.pos_end,
                    f"Failed to finish executing script \"{fn}\"\n" +
                    error.as_string(), exec_ctx
				))

        return RTResult().success(Number.null)
    execute_run.arg_names = ["fn"]

    def execute_exit(self, exec_ctx):
        exit_code: Number = exec_ctx.symbol_table.get('exit_code')

        if not isinstance(exit_code, Number):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Cannot exit with '{exit_code.value}', must be an int",
                exec_ctx
            ))

        print(f"process exited with code: {exit_code.value}")

        os._exit(exit_code.value)
    execute_exit.arg_names = ['exit_code']

#! BUILTIN FUNCTION DEFINITIONS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

BuiltInFunction.println         = BuiltInFunction("println")
BuiltInFunction.println_ret     = BuiltInFunction("println_ret")
BuiltInFunction.input           = BuiltInFunction("input")
BuiltInFunction.input_int       = BuiltInFunction("input_int")
BuiltInFunction.clear           = BuiltInFunction("clear")
BuiltInFunction.atoi            = BuiltInFunction("atoi")
BuiltInFunction.itoa            = BuiltInFunction("itoa")
BuiltInFunction.to_int          = BuiltInFunction("to_int")
BuiltInFunction.to_string       = BuiltInFunction("to_string")
BuiltInFunction.string_to_list  = BuiltInFunction("string_to_list")
BuiltInFunction.list_to_string  = BuiltInFunction("list_to_string")
BuiltInFunction.is_instance     = BuiltInFunction("is_instance")
BuiltInFunction.int_new         = BuiltInFunction("int_new")
BuiltInFunction.string_new      = BuiltInFunction("string_new")
BuiltInFunction.list_new        = BuiltInFunction("list_new")
BuiltInFunction.push_back       = BuiltInFunction("push_back")
BuiltInFunction.pop_back        = BuiltInFunction("pop_back")
BuiltInFunction.pop_at          = BuiltInFunction("pop_at")
BuiltInFunction.push_front      = BuiltInFunction("push_front")
BuiltInFunction.pop_front       = BuiltInFunction("pop_front")
BuiltInFunction.extend          = BuiltInFunction("extend")
BuiltInFunction.insert          = BuiltInFunction("insert")
BuiltInFunction.update          = BuiltInFunction("update")
BuiltInFunction.sort            = BuiltInFunction("sort")
BuiltInFunction.sort_reverse    = BuiltInFunction("sort_reverse")
BuiltInFunction.list_clear      = BuiltInFunction("list_clear")
BuiltInFunction.len             = BuiltInFunction("len")
BuiltInFunction.nth             = BuiltInFunction("nth")
BuiltInFunction.now             = BuiltInFunction("now")
BuiltInFunction.value_copy      = BuiltInFunction("value_copy")
BuiltInFunction.runtime_error   = BuiltInFunction("runtime_error")
BuiltInFunction.version         = BuiltInFunction("version")
BuiltInFunction.run             = BuiltInFunction("run")
BuiltInFunction.exit            = BuiltInFunction("exit")


#! GLOBAL LANGUAGE CONSTANTS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

global_symbol_table = SymbolTable()
global_symbol_table.set("NULL", Number.null)
global_symbol_table.set("false", Number.false)
global_symbol_table.set("true", Number.true)
global_symbol_table.set("std::math::PI", Number.math_PI)
global_symbol_table.set("std::time::DAYS", List.days_of_the_week)
global_symbol_table.set("std::time::MONTHS", List.months_of_the_year)


#! GLOBAL LANGUAGE FUNCTIONS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#! Standard Input and Output
global_symbol_table.set("std::println", BuiltInFunction.println)
global_symbol_table.set("std::println_ret", BuiltInFunction.println_ret)
global_symbol_table.set("std::input", BuiltInFunction.input)
global_symbol_table.set("std::input_int", BuiltInFunction.input_int)
global_symbol_table.set("std::clear", BuiltInFunction.clear)

#! Conversions
global_symbol_table.set("std::to_int", BuiltInFunction.to_int)
global_symbol_table.set("std::to_string", BuiltInFunction.to_string)
global_symbol_table.set("std::string_to_list", BuiltInFunction.string_to_list)
global_symbol_table.set("std::list_to_string", BuiltInFunction.list_to_string)
global_symbol_table.set("std::atoi", BuiltInFunction.atoi)
global_symbol_table.set("std::itoa", BuiltInFunction.itoa)

#! List Methods
global_symbol_table.set("std::list::push_back", BuiltInFunction.push_back)
global_symbol_table.set("std::list::pop_back", BuiltInFunction.pop_back)
global_symbol_table.set("std::list::pop_at", BuiltInFunction.pop_at)
global_symbol_table.set("std::list::push_front", BuiltInFunction.push_front)
global_symbol_table.set("std::list::pop_front", BuiltInFunction.pop_front)
global_symbol_table.set("std::list::extend", BuiltInFunction.extend)
global_symbol_table.set("std::list::insert", BuiltInFunction.insert)
global_symbol_table.set("std::list::update", BuiltInFunction.update)
# NOTE: sort and sort_reverse modify the given list
global_symbol_table.set("std::list::sort", BuiltInFunction.sort)
global_symbol_table.set("std::list::sort_reverse", BuiltInFunction.sort_reverse)
global_symbol_table.set("std::list::clear", BuiltInFunction.list_clear)
global_symbol_table.set("std::list::len", BuiltInFunction.len)
global_symbol_table.set("std::list::nth", BuiltInFunction.nth)

#! Misc
global_symbol_table.set("std::is_instance", BuiltInFunction.is_instance)
global_symbol_table.set("std::int::new", BuiltInFunction.int_new)
global_symbol_table.set("std::string::new", BuiltInFunction.string_new)
global_symbol_table.set("std::list::new", BuiltInFunction.list_new)
global_symbol_table.set("std::time::now", BuiltInFunction.now)
global_symbol_table.set("std::copy", BuiltInFunction.value_copy)
global_symbol_table.set("std::runtime_error", BuiltInFunction.runtime_error)
global_symbol_table.set("std::version", BuiltInFunction.version)
global_symbol_table.set("std::run", BuiltInFunction.run)
global_symbol_table.set("std::exit", BuiltInFunction.exit)