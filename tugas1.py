# Helper 
def tokenize(production, non_terminal, terminal):
  res = []
  products = production.split("|")
  for product in products:
    temp = []
    for i in range(len(product)):
      try:
        if product[i]+product[i+1] in non_terminal or product[i]+product[i+1] in terminal:
          temp += [product[i]+product[i+1]]
        elif product[i] in non_terminal or product[i] in terminal or product[i] == "Є":
          temp += product[i]
      except:
        if product[i] in non_terminal or product[i] in terminal or product[i] == "Є":
          temp += product[i]
    res += [temp]

  return res

def read_production_rule(production_rule, total_production_rule, input_file):
  def parse_text(txt):
    [key, value] = txt.split("=>")
    return key, value
  for _ in range(total_production_rule):
    key, value = parse_text(input_file.readline().replace("\n", ""))
    production_rule[key] = value.replace("\n", "")

# Core Functionalities
def First(symbol, production, non_terminal, terminal):
  res = []

  # Rule 1
  if symbol in terminal:
    res += [symbol]

  if symbol in production:
    token_group = tokenize(production[symbol], non_terminal, terminal)
    # Loop through product's tokens
    for tokens in token_group:
      # Rule  2
      if tokens[0] in terminal or tokens[0] == "Є":
        res += [tokens[0]]
      # Rule 3
      if tokens[0] in non_terminal:
        for i in range(len(tokens)):
          temp = First(tokens[0], production, non_terminal, terminal)
          res += temp
          if "Є" in temp:
            continue
          else:
            break 
  return res
 
def Follow(symbol, production, non_terminal, terminal, start_symbol):
  res = []
  
  # Rule 1
  if symbol == start_symbol[0]:
    res += ["$"]
  
  # Loop through all production rules
  for prod_symbol in production:
    token_group = tokenize(production[prod_symbol], non_terminal, terminal)
    for tokens in token_group:
      if symbol in tokens:
        index_of_symbol = tokens.index(symbol)
        
        # Rule 2
        if index_of_symbol < len(tokens) - 1:
          temp = First(tokens[index_of_symbol+1], production, non_terminal, terminal)
          if temp[0] != "Є":
            res += [x for x in temp if x != "Є"] 

          # Rule 3.2
          if "Є" in temp:
            res += [x for x in temp if x != "Є"]
            # if prod_symbol != symbol:
            # print(prod_symbol)
            res += Follow(prod_symbol, production, non_terminal, terminal, start_symbol)
        # Rule 3.1
        if index_of_symbol == len(tokens) - 1:
          if prod_symbol != symbol:
            res += Follow(prod_symbol, production, non_terminal, terminal, start_symbol)
      
  return list(set(res))

def LLTable(production, non_terminal, terminal, start_symbol):
  table = {}

  # Rule 1
  # Case: alpha = first token from a product
  for prod_symbol in production:
    table[prod_symbol] = {}
    products = tokenize(production[prod_symbol], non_terminal, terminal)

    for product in products:
      alpha = product[0]
      # Rule 1a
      for a in First(alpha, production, non_terminal, terminal):
        if a in terminal:
          rule = f"{prod_symbol:3} => {''.join(product):8}"
          table[prod_symbol][a] = rule
      # Rule 1b
      if "Є" in First(alpha, production, non_terminal, terminal) or len(First(alpha, production, non_terminal, terminal)) == 0:
        for b in Follow(prod_symbol, production, non_terminal, terminal, start_symbol):
          rule = f"{prod_symbol:3} => {''.join(product):8}"
          table[prod_symbol][b] = rule
      # Rule 1c
      if "Є" in First(alpha, production, non_terminal, terminal) and "$" in Follow(prod_symbol, production, non_terminal, terminal, start_symbol):
        rule = f"{prod_symbol:3} => {''.join(product):8}"
        table[prod_symbol]["$"] = rule

  # Rule 2
  for key in table:
    for term in terminal + ["$"]:
      try:
        table[key][term]
      except:
        table[key][term] = f"{'ERROR':15}"

  return table

# String formatting 
def format_list(arr, curly=False, spaces=10):
  if curly:
    return f"{'{ '+', '.join(arr)+' }':{spaces}}"
  else:
    return f"{'[ '+', '.join(arr)+' ]':{spaces}}"

def print_tokenized_production_table(production, non_terminal, terminal):
  print(f"\n{'==== Tokenized Production Rule ====':^35}")
  for prod in production:
    print(f"{prod:2} => {tokenize(production[prod], non_terminal, terminal)}")

def print_first_follow_table(production, non_terminal, terminal, start_symbol):
  print(f"\n{'==== First Follow Table ====':^35}")
  print(f"{'Production':15} {'First':10} {'Follow':10}")
  for prod in production:
    print(f"{prod:3} => {(production[prod]):8} {format_list(First(prod, production, non_terminal, terminal), True)} {format_list(Follow(prod, production, non_terminal, terminal, start_symbol), True)}")

def print_LL_table(table, terminal):
  print(f"\n{'==== LL(1) Parsing Table ====':^93}")
  header = f"{'':3}"
  for term in terminal + ["$"]:
    header += f"{term:15}"
  print(header)

  for key in table:
    row = f"{key:3}"
    for term in terminal + ["$"]:
      row += f"{table[key][term]:15}"
    print(row)

def output(output_file, table):
  output_file.write(f"{len(table)}\n")
  output_file.write(f"{len(table[next(iter(table))])}\n")
  for i, terminal in enumerate(table):
    output_file.write(f"{terminal}\n")
    for j, non_terminal in enumerate(table[terminal]):
      output_file.write(f"{non_terminal}|{table[terminal][non_terminal]}")
      if j < len(table[terminal])-1:
        output_file.write("\n")
    if i < len(table)-1:
      output_file.write("\n")

def main():
  print("TUGAS 1")
  with open("input1", encoding="utf-8") as input_file:
    non_terminal = [x.replace("\n", "") for x in input_file.readline().split(',') if x != ""]
    terminal = [x.replace("\n", "") for x in input_file.readline().split(',') if x != ""]
    start_symbol = [x.replace("\n", "") for x in input_file.readline().split(',') if x != ""]
    total_production_rule = int(input_file.readline())
    production_rule = {}
    read_production_rule(production_rule, total_production_rule, input_file)

  LL_1_table = LLTable(production_rule, non_terminal, terminal, start_symbol)
  print_tokenized_production_table(production_rule, non_terminal, terminal)
  print_first_follow_table(production_rule, non_terminal, terminal, start_symbol)
  print_LL_table(LL_1_table, terminal)

  with open("output1", "w", encoding="utf-8") as output_file:
    output(output_file, LL_1_table)

if __name__=="__main__":
  main()