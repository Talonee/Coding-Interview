# Python fxn cheatsheets
These are useful python codes and functions I've compiled throughout my journey of practicing with the language.

# Misc

### Swap two variable in one line
`a, b = b, a`

### Single command range
`if a < b <= c:`

### No decimal division
`x//y`

### Base manipulation
`bin(n)[2:]` - convert to binary

`n.bit_length()` - count binary length (110010 -> 6)

`int(n,x)` - convert string n to base x

`bin(n), oct(n), hex(n)` - convert integer n to respective base, include [2:] to extract

### For-else
`for i in s: ... else:` - the else (`finally:`) clause executes after loop completion; will not executes if for loop encounters a `break`

### Extended Iterable Unpacking
`a, *b, c = range(5)`

`a >>> 0` and `c >>> 4` and `b >>> [1, 2, 3]`

# Strings

### Formatted string literals (f-strings)
`[[fill]align][sign][pad][width][,][.precision][type]` - str.format()

`f"{}"` - f-strings; can contain `[var][operations:^<>8 (pad)/.2f (round)/xoe (num notation)][fxn][objects]`

- create multiline by escaping a \; require f in front of each line.

### Regular expression
`import re` - learn more in **Resources** 

# List

### Combine lists
`[*l1, *l2]` or `l1 + l2`

### List Iteration/Slicing
`list[start:stop:increment]`