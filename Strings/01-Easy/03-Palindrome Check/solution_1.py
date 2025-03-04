# Description:

"""
                                         Palindrome Check

Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.

## Sample Input:

```
string = "abcdcba"
```

## Sample Output:

```
true // it's written the same forward and backward
```

## Optimal Space & Time Complexity:

```
`O(n)` time | `O(1)` space - where `n` is the length of the input string.
```

"""

# =============================================================================================== #

# Solution


# O(n^2)time | O(n) space
def isPalindrome(string):
    reversed_string = ""
    for i in reversed(range(len(string))):
        reversed_string += string[i]
    return string == reversed_string


# Test Cases
print(isPalindrome("madam"))  # True
print(isPalindrome("hello"))  # False
print(isPalindrome("a"))  # True
print(isPalindrome(""))  # True
print(isPalindrome("Madam"))  # False

# =============================================================================================== #

# Big O:

"""

## Time and Space Complexity:

### Time Complexity:
The time complexity of the `isPalindrome` function is **O(n)**, where `n` is the length of the input string. Here's why:

1. **Reversing the string**: The `for` loop iterates over the string in reverse order, which takes **O(n)** time because
it processes each character once.
2. **String concatenation**: In Python, strings are immutable, so each concatenation (`reversed_string += string[i]`)
creates a new string. This operation takes **O(n)** time in total across all iterations.
3. **Comparison**: The final comparison `string == reversed_string` also takes **O(n)** time because it compares each
character of the two strings.

Thus, the overall time complexity is **O(n)**.

---

### Space Complexity:
The space complexity of the `isPalindrome` function is **O(n)**, where `n` is the length of the input string. Here's why:

1. **Reversed string storage**: The `reversed_string` variable stores a copy of the reversed input string, which requires
**O(n)** space.
2. **Auxiliary space**: The function uses a constant amount of additional space for variables like `i`, but this is negligible
compared to the space used by `reversed_string`.

Thus, the overall space complexity is **O(n)**.

---

### Optimized Approach:
You can optimize the function to use **O(1)** additional space by comparing characters directly without creating a reversed string. 

### Time Complexity: **O(n)** (same as before, but more efficient in practice due to fewer operations).  
### Space Complexity: **O(1)** (no additional space is used apart from a few variables).

"""

# Code Explanation:

"""

Here is an explanation of the given code in detail, along with an example test case to demonstrate its functionality.

---

### Code Analysis

#### Function Definition
```
def isPalindrome(string):
```
- This function, `isPalindrome`, takes a single argument, `string`, which is expected to be a string.

#### Reversing the String
```
    reversed_string = ""
    for i in reversed(range(len(string))):
        reversed_string += string[i]
```
- **`reversed(range(len(string)))`**: This generates a sequence of indices in reverse order, from the last index to the first.
  - For example, if `string = "abc"`, `range(len(string))` produces `[0, 1, 2]`, and `reversed(range(len(string)))`
  produces `[2, 1, 0]`.
- **Loop (`for i in ...`)**: The loop iterates over each index `i` in this reversed sequence.
- **String Construction**: During each iteration, `string[i]` (the character at the current index) is appended to `reversed_string`.
  - If `string = "abc"`, `reversed_string` builds up as follows:
    1. Initially, `reversed_string = ""`.
    2. Append `string[2]` (i.e., `'c'`): `reversed_string = "c"`.
    3. Append `string[1]` (i.e., `'b'`): `reversed_string = "cb"`.
    4. Append `string[0]` (i.e., `'a'`): `reversed_string = "cba"`.

#### Comparison
```
    return string == reversed_string
```
- The original string `string` is compared with `reversed_string`.
- If they are equal, the function returns `True`, indicating the string is a palindrome.
- If they are not equal, the function returns `False`, indicating the string is not a palindrome.

---

### Test Cases

1. **Test Case 1: Palindrome String**
   ```
   print(isPalindrome("madam"))  # Expected output: True
   ```
   - Original string: `"madam"`.
   - Reversed string: `"madam"`.
   - Both are equal → **True**.

2. **Test Case 2: Non-Palindrome String**
   ```
   print(isPalindrome("hello"))  # Expected output: False
   ```
   - Original string: `"hello"`.
   - Reversed string: `"olleh"`.
   - Both are not equal → **False**.

3. **Test Case 3: Single-Character String**
   ```
   print(isPalindrome("a"))  # Expected output: True
   ```
   - A single-character string is always a palindrome since reversing it produces the same string.

4. **Test Case 4: Empty String**
   ```
   print(isPalindrome(""))  # Expected output: True
   ```
   - An empty string is trivially a palindrome as reversing it has no effect.

5. **Test Case 5: Case Sensitivity**
   ```
   print(isPalindrome("Madam"))  # Expected output: False
   ```
   - Original string: `"Madam"`.
   - Reversed string: `"madaM"`.
   - Both are not equal due to case differences → **False**.

"""
