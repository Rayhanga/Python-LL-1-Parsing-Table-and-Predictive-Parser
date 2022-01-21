# Tugas Teknik Kompilasi

## Input file format

### Tugas 1

`input1.txt`
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

### Tugas 2

