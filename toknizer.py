import re


def tokenize(text):

    scanner = re.Scanner([
        (r"[0-9]+", lambda scanner, token:("NUM", token)),
        (r"[a-z_]+", lambda scanner, token:("NAME", token)),
        (r"[+\-*/]+", lambda scanner, token:("OP", token)),
        (r"[:=]+", lambda scanner, token:("ASSIGN", token)),
        (r"\s+", None),
    ])
    results, remainder = scanner.scan(text)
    print(results)


tokenize("spam = x + 34 * 567")


