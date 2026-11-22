"""Standalone independent finite verification of a sharp sparse-run exponent theorem."""
from fractions import Fraction
from itertools import combinations


def runs_by_period(word):
    n = len(word)
    output = set()
    for p in range(1, n // 2 + 1):
        i = 0
        while i + p < n:
            if word[i] != word[i+p]:
                i += 1
                continue
            s = i
            while i + p < n and word[i] == word[i+p]:
                i += 1
            e = i + p
            if e - s < 2*p:
                continue
            sub = word[s:e]
            if any(all(sub[j] == sub[j+q] for j in range(len(sub)-q))
                   for q in range(1,p)):
                continue
            output.add((s,e,p))
    return output


def runs_by_intervals(word):
    n = len(word)
    output = set()
    for s in range(n):
        for e in range(s+2,n+1):
            sub = word[s:e]
            for p in range(1,(e-s)//2+1):
                if any(sub[t] != sub[t+p] for t in range(e-s-p)):
                    continue
                if any(all(sub[t] == sub[t+q] for t in range(e-s-q))
                       for q in range(1,p)):
                    break
                if ((s == 0 or word[s-1] != word[s-1+p]) and
                    (e == n or word[e] != word[e-p])):
                    output.add((s,e,p))
                break
    return output


def total_exponent(run_set):
    return sum((Fraction(e-s,p) for s,e,p in run_set), Fraction(0))


def predicted(n):
    m = (n-1)//4
    return Fraction(n+3) - Fraction(1,m) - Fraction(2,m+1)


total=0
for n in range(3,31):
    best = Fraction(-1)
    witnesses = []
    for ones in combinations(range(n),3):
        w = ['0']*n
        for j in ones:
            w[j] = '1'
        r = runs_by_period(w)
        if n <= 12:
            assert r == runs_by_intervals(w), (n,ones,r,runs_by_intervals(w))
        exp = total_exponent(r)
        if exp > best:
            best=exp
            witnesses=[ones]
        elif exp==best:
            witnesses.append(ones)
        total += 1
    if n >= 13:
        assert best == predicted(n), (n,best,predicted(n),witnesses)
        m=(n-1)//4
        candidate=(m-1,2*m-1,3*m)
        assert candidate in witnesses, (n,candidate,witnesses)
    print('n=%d  maximum=%s  maximizers=%d  first=%s' %
          (n,str(best),len(witnesses),witnesses[0]))
print('VERIFIED_WORDS',total)
print('INDEPENDENT_INTERVAL_CHECK',sum(__import__('math').comb(n,3) for n in range(3,13)))
print('SHARP_FORMULA_CHECK n=13..30')
