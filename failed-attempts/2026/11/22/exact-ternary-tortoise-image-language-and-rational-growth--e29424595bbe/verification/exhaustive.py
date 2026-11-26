"""Exact finite cross-check of the two independently specified word maps and target-language test."""
from itertools import product

def stack_tortoise(word):
    stack, output = [], []
    for letter in word:
        while stack and stack[-1] <= letter:
            output.append(stack.pop())
        stack.append(letter)
    output.extend(reversed(stack))
    return tuple(output)

def recursive_tortoise(word):
    if not word:
        return ()
    maximum = max(word)
    blocks = []
    block = []
    for value in word:
        if value == maximum:
            blocks.append(tuple(block))
            block = []
        else:
            block.append(value)
    blocks.append(tuple(block))
    out = list(recursive_tortoise(blocks[0]))
    for j in range(1, len(blocks)):
        out += list(recursive_tortoise(blocks[j]))
        out += [maximum]
    return tuple(out)

def binary_image(word):
    return not word or all(x == 0 for x in word) or word[-1] == 1

def ternary_image(word):
    if 2 not in word:
        return binary_image(word)
    pieces=[]; block=[]
    for letter in word:
        if letter == 2:
            pieces.append(tuple(block));block=[]
        else:
            block.append(letter)
    return not block and all(binary_image(p) for p in pieces[1:])

expected = [1, 3, 6, 14, 35, 91, 242, 653, 1780, 4888]
for n in range(10):
    outputs=set()
    for word in product(range(3),repeat=n):
        a=stack_tortoise(word)
        assert a == recursive_tortoise(word), (word,a,recursive_tortoise(word))
        outputs.add(a)
    assert len(outputs) == expected[n], (n,len(outputs))
    for word in product(range(3),repeat=n):
        assert (word in outputs) == ternary_image(word), (n,word)
    print(f'length={n}, image_count={len(outputs)}, test=PASS')
print('all finite exhaustive cross-checks passed')
