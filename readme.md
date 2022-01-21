# Python LL(1) Parsing Table Generator (Tugas 1)


## Input file format
`input`
```
NON TERMINAL SYMBOLS (divided by ,)
TERMINAL SYMBOLS (divided by ,)
STARTING SYMBOL
TOTAL AMOUNT OF PRODUCTION RULE (N)
PRODUCTION RULE 1
.
.
.
PRODUCTION RULE N
```

Production Rule Format
```
NON TERMINAL SYMBOL => PRODUCT
```

or

```
NON TERMINAL SYMBOL => PRODUCT 1 | ... | PRODUCT N
```

Example

```
E,E',T,T',F
id,+,*,(,)
E
5
E=>TE'
E'=>+TE'|Є
T=>FT'
T'=>*FT'|Є
F=>(E)|id
```

# Python Predictive Parser (Tugas 2)

## Input file format
### `input_token`
```
TOTAL NUMBER OF TOKENS (N)
TOKEN 1
.
.
TOKEN N
```

Example
```
2
id + id * id $
id + * id id $
```

### `output_table` (from Tugas 1)
```
ROW
COL
NON TERMINAL SYMBOL 1
TERMINAL SYMBOL 1 | PRODUCTION RULE
.
.
TERMINAL SYMBOL COL | PRODUCTION RULE
NON TERMINAL SYMBOL 2
.
.
.
NON TERMINAL SYMBOL ROW
```

Example

```
5
6
E
(|E   => TE'     
id|E   => TE'     
+|ERROR          
*|ERROR          
)|ERROR          
$|ERROR          
E'
+|E'  => +TE'    
$|E'  => Є       
)|E'  => Є       
id|ERROR          
*|ERROR          
(|ERROR          
T
(|T   => FT'     
id|T   => FT'     
+|ERROR          
*|ERROR          
)|ERROR          
$|ERROR          
T'
*|T'  => *FT'    
$|T'  => Є       
+|T'  => Є       
)|T'  => Є       
id|ERROR          
(|ERROR          
F
(|F   => (E)     
id|F   => id      
+|ERROR          
*|ERROR          
)|ERROR          
$|ERROR          
```