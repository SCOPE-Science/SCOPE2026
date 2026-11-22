"""Independent forward enumeration of three reverse-complement symbol duplications."""
from itertools import product
from collections import Counter

def insert_complement(word, i):
    symbol = '1' if word[i] == '0' else '0'
    return word[:i+1] + symbol + word[i+1:]

def descendants(word, steps):
    reachable = {word}
    for _ in range(steps):
        reachable = {insert_complement(w, i) for w in reachable for i in range(len(w))}
    return reachable

def initial_run(word):
    return next((i for i in range(1, len(word)) if word[i] != word[0]), len(word))

def formula(n, r):
    return (n+2)*(n+1)*n//6 + r*(n+2)-r*(r-1)//2

def run():
    total = 0
    for n in range(1,11):
        counts = Counter()
        for symbols in product('01', repeat=n):
            word = ''.join(symbols)
            actual = len(descendants(word,3))
            predicted = formula(n,initial_run(word))
            assert actual == predicted, (word,actual,predicted)
            counts[actual] += 1
            total += 1
        assert len(counts) == n and sum(counts.values()) == 2**n
        assert counts[formula(n,n)] == 2
        for r in range(1,n):
            assert counts[formula(n,r)] == 2**(n-r)
    print(f'PASS forward {total} binary sources n=1..10')

if __name__=='__main__':run()
