import tugas1

def read_parsing_table(table, input_file):
  row = int(input_file.readline().replace("\n", ""))
  col = int(input_file.readline().replace("\n", ""))
  for _ in range(row):
    non_terminal = input_file.readline().replace("\n", "")
    table[non_terminal] = {}
    for _ in range(col):
      [terminal, value] = input_file.readline().replace("\n", "").split("|")
      table[non_terminal][terminal] = value

def get_symbols_from_parsing_table(table):
  non_terminal = list(table.keys())
  terminal = list(table[next(iter(table))].keys())
  
  return non_terminal, terminal

def raise_custom_error():
  global stack, output, token

  stack = []
  token = []
  output = "ERROR"
  print(f'{"".join(stack):20} {"".join(token):20} {output:20}')

def parse(parsing_table, token, stack, output, non_terminal, terminal):
  print(f'{"".join(stack):20} {"".join(token):20} {output:20}')
  # Rule 1
  if stack[-1] == token[0] == "$":
    return
  # Rule 2
  if stack[-1] == token[0] != "$":
    output = ""
    del token[0]
    del stack[-1]
    print(f'{"".join(stack):20} {"".join(token):20} {output:20}')
  # Rule 3
  if stack[-1] in terminal:
    if stack[-1] != token[0]:
      # # Python's Error Handler
      # raise Exception("Syntax Error")
      raise_custom_error()
      return
  # Rule 4
  if stack[-1] in non_terminal:
    product = parsing_table[stack[-1]][token[0]]
    output = product
    if product.strip() == "ERROR":
      # # Python's Error Handler
      # raise Exception("Parsing error")
      raise_custom_error()
      return
    del stack[-1]
    if "Є" not in product:
      temp = [symbol for symbol in tugas1.tokenize(product.split("=>")[-1], non_terminal, terminal)[0]]
      temp.reverse()
      stack += temp
  parse(parsing_table, token, stack, output, non_terminal, terminal)

def main():
  print("\nTUGAS 2")
  parsing_table = {}
  with open("output_table", encoding="utf-8") as table_file:
    read_parsing_table(parsing_table, table_file)
  
  with open("input_token", encoding="utf-8") as token_file:
    total_token = int(token_file.readline().replace("\n", ""))
    for _ in range(total_token):
      raw_token = token_file.readline().replace("\n", "")
      stack = ["$", next(iter(parsing_table))]
      non_terminal, terminal = get_symbols_from_parsing_table(parsing_table)
      token = tugas1.tokenize(raw_token, non_terminal, terminal)[0]
      output= ""
      print(f'\nToken: {raw_token}')
      print(f'{"Stack":20} {"Input":20} {"Output":20}')
      parse(parsing_table, token, stack, output, non_terminal, terminal)

if __name__ == "__main__":
  main()