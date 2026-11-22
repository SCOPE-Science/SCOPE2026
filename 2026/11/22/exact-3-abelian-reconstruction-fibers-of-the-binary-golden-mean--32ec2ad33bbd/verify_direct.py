"""Independent direct 3-Abelian spectrum enumeration in the binary Fibonacci language.

Run: python3 verify_direct.py
Only Python 3 standard library is needed.
"""
from collections import defaultdict
from math import comb


def fibonacci_words(n):
    pool = ['']
    for _ in range(n):
        pool = [s + '0' for s in pool] + [s + '1' for s in pool if not s.endswith('1')]
    return pool


def profile(w):
    return tuple(
        sum(w[i:i+k] == ''.join(format(j, '0%db' % k))
            for i in range(len(w)-k+1))
        for k in (1,2,3) for j in range(1<<k))


def parameters(w):
    n = len(w)
    m = w.count('1')
    if m == 0:
        return ('zero', n)
    runs = w.split('1')
    u, v = min(2, len(runs[0])), min(2, len(runs[-1]))
    c = sum(len(x) >= 2 for x in runs[1:-1])
    h = sum(max(0,len(x)-2) for x in runs)
    return m,c,u,v,h


def formula_size(param):
    if param[0] == 'zero': return 1
    m,c,u,v,h = param
    r = c + (u==2) + (v==2)
    if not r: return comb(m-1,c) if not h else 0
    return comb(m-1,c)*comb(h+r-1,r-1)


def c_formula(n):
    if n==0: return 1
    if n==1: return 2
    if n%2:
        k=(n-1)//2
        return 3*k*k-k+3
    k=n//2
    return 3*k*k-4*k+4


def s_formula(n):
    if n >= 7: return 2*n+7 if n%2 else 2*n+6
    return [1,2,3,5,8,13,17][n]

for n in range(0,24):
    groups=defaultdict(list)
    for w in fibonacci_words(n):
        groups[profile(w)].append(w)
    counts=len(groups)
    singletons=sum(len(x)==1 for x in groups.values())
    assert counts == c_formula(n), (n,counts,c_formula(n))
    assert singletons == s_formula(n), (n,singletons,s_formula(n))
    byparam=defaultdict(list)
    for words in groups.values():
        for w in words:
            par=parameters(w)
            assert formula_size(par) == len(words), (n,w,par,len(words))
            byparam[par].append(w)
    assert len(byparam) == len(groups), (n,'param collisions')
    assert sorted(map(len,byparam.values())) == sorted(map(len,groups.values()))
    assert sum(map(len,groups.values())) == len(fibonacci_words(n))
    if n in (0,3,6,9,12,15,18,21,23):
        print(f'n={n} words={sum(map(len,groups.values()))} classes={counts} singletons={singletons}')
print('VERIFY_DIRECT_OK')
