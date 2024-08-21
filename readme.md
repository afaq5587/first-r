# preference of operator in python.


1. **Parentheses `()`**
   - Expressions within parentheses are evaluated first.

2. **Exponentiation `**`**
   - The exponentiation operator has right-to-left associativity. For example, `2 ** 3 ** 2` is evaluated as `2 ** (3 ** 2)`.

3. **Unary plus and minus `+x`, `-x`, and bitwise NOT `~x`**
   - These operators have a higher precedence than binary arithmetic operations.

4. **Multiplication `*`, Division `/`, Floor Division `//`, and Modulus `%`**
   - These operators have left-to-right associativity.

5. **Addition `+` and Subtraction `-`**
   - These also have left-to-right associativity.

6. **Bitwise Shift Operators `<<`, `>>`**
   - These operators are used to shift bits and have a higher precedence than comparison operators.

7. **Bitwise AND `&`**
   - This operator performs a bitwise AND operation.

8. **Bitwise XOR `^`**
   - This operator performs a bitwise XOR operation.

9. **Bitwise OR `|`**
   - This operator performs a bitwise OR operation.

10. **Comparison Operators**
    - These include equality `==`, inequality `!=`, greater than `>`, greater than or equal to `>=`, less than `<`, and less than or equal to `<=`.

11. **Identity Operators `is`, `is not`**
    - Used to compare object identities.

12. **Membership Operators `in`, `not in`**
    - Used to check membership in sequences like lists, tuples, and strings.

13. **Logical NOT `not`**
    - This operator has higher precedence than logical AND and OR.

14. **Logical AND `and`**
    - This operator is evaluated before logical OR.

15. **Logical OR `or`**
    - This operator has the lowest precedence among logical operators.

16. **Conditional Expressions (Ternary Operator) `x if condition else y`**
    - This is used to select one of two expressions based on a condition.

17. **Assignment Operators `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `^=`, `|=`, `<<=`, `>>=`**
    - These operators have the lowest precedence and are used to assign values to variables.

## Example

To see operator precedence in action, consider the following expression:

```python
result = 3 + 4 * 2 ** (1 + 1)

