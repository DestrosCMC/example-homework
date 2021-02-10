#!/bin/python3


def balanced_parens2(text):
    '''
    Checks whether all of the following types of parentheses are balanced: ([{

    >>> balanced_parens2('(()())')
    True
    '''
    stack = []
    for symbol in text:
        if symbol in '([{':
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False
            if (stack[-1] == '(' and symbol == ')') or \
               (stack[-1] == '[' and symbol == ']') or \
               (stack[-1] == '{' and symbol == '}'):
                stack.pop()
    return True
