# Longest Balanced Substring

Write a function that takes in a string made up of parentheses (`(` and `)`). The function should return an integer representing the length of the longest balanced substring with regards to parentheses.

A string is said to be balanced if it has as many opening parentheses as it has closing parentheses and if no parenthesis is unmatched. Note that an opening parenthesis can't match a closing parenthesis that comes before it, and similarly, a closing parenthesis can't match an opening parenthesis that comes after it.

## Sample Input

```plaintext
string = "(()))("
```

## Sample Output

```plaintext
4 // The longest balanced substring is "(())".
```

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the length of the input string.
