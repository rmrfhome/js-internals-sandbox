import re
import os

source_file = open("functions.js", "r")
lines = source_file.readlines()
function_declarations = filter(lambda line: re.search("^\s*function", line), lines)
function_names = map(lambda line: re.search("^\s*function\s+(\w+)", line).group(1), function_declarations)
commands = map(lambda line: f'node --print-bytecode --print-bytecode-filter={line} functions.js', function_names)
for command in commands:
    os.system(command)
#node --print-bytecode .\functions.js