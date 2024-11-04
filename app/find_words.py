import time
from pathlib import Path

HERE = Path(__file__).parent

print(HERE)


def is_include(chars: str, string: str):
    if not chars:
        return True
    if chars[0] == "е":
        if not ("е" in string or "ё" in string):
            return False
        else:
            return is_include(chars[1:], string.replace(chars[0], "", 1))

    if chars[0] not in string:
        return False
    else:
        return is_include(chars[1:], string.replace(chars[0], "", 1))


def find_words(test, file):
    found_words = []
    test_len = len(test)
    start = time.time()
    count = 0
    for line in file:
        line = line.strip()
        if len(line) != test_len:
            continue
        if not is_include(test, line):
            continue
        found_words.append(line)
        count += 1

    return {"found_words": found_words, "spent time": time.time() - start, "count": count}


if __name__ == "__main__":
    with open(f"{HERE}/russian_nouns.txt", "r") as f:
        words = find_words("бада", f)

    # words = find_words("да", ["ад", "да"])
    print(words)
