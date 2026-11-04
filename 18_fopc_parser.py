"""
DSA03 – Natural Language Processing
Program 18: Simple parser for basic First-Order Predicate Calculus (FOPC).

Supported illustrative forms:
  human(socrates)
  loves(john, mary)
  forall x: human(x) -> mortal(x)
  exists y: student(y) & studies(y)

This program tokenizes and validates the structure; it does not prove
logical statements or implement a complete FOPC theorem prover.
"""
import re

TOKEN_PATTERN = r"forall|exists|[A-Za-z_][A-Za-z0-9_]*|->|[(),:&|]"

def tokenize(expression):
    tokens = re.findall(TOKEN_PATTERN, expression)
    compact = re.sub(r"\s+", "", expression)
    if "".join(tokens) != compact:
        raise ValueError("Expression contains unsupported characters or syntax.")
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected=None):
        token = self.peek()
        if token is None or (expected is not None and token != expected):
            raise ValueError(f"Expected {expected!r}, found {token!r}")
        self.pos += 1
        return token

    def expression(self):
        if self.peek() in {"forall", "exists"}:
            quantifier = self.consume()
            variable = self.consume()
            self.consume(":")
            body = self.expression()
            return (quantifier, variable, body)

        left = self.atom()
        if self.peek() in {"->", "&", "|"}:
            operator = self.consume()
            right = self.expression()
            return (operator, left, right)
        return left

    def atom(self):
        predicate = self.consume()
        if not re.fullmatch(r"[A-Za-z_]\w*", predicate):
            raise ValueError("Expected predicate or term.")
        self.consume("(")
        terms = [self.consume()]
        while self.peek() == ",":
            self.consume(",")
            terms.append(self.consume())
        self.consume(")")
        return ("PREDICATE", predicate, terms)

def parse_fopc(expression):
    tokens = tokenize(expression)
    parser = Parser(tokens)
    tree = parser.expression()
    if parser.peek() is not None:
        raise ValueError(f"Unexpected token: {parser.peek()}")
    return tree

if __name__ == "__main__":
    examples = [
        "human(socrates)",
        "loves(john, mary)",
        "forall x: human(x) -> mortal(x)",
        "exists y: student(y) & studies(y)",
    ]
    for item in examples:
        try:
            print("\nExpression:", item)
            print("Parsed structure:", parse_fopc(item))
        except ValueError as error:
            print("Invalid expression:", error)
