#!/usr/bin/env python3
"""Independent firing-pattern interval enumeration and coefficient checks."""
from collections import Counter
from itertools import product
from math import comb, factorial


def trace_poly(n):
    answer = Counter()
    for phases in product(range(3),repeat=n):
        fired = [phases.count(t) for t in range(3)]
        term = Counter({0:1})
        for phase in phases:
            offsets = []
            received = 0
            for t in range(3):
                offsets.append(received - n * (phase < t))
                received += fired[t]
            # Enforce chip nonnegativity and the three firing/waiting inequalities.
            lower = max([0]+[-offset for offset in offsets]+[n-1-offsets[phase]])
            upper = min(n-2-offsets[t] for t in range(3) if t!=phase)
            if lower > upper:
                term.clear()
                break
            newer=Counter()
            for E,v in term.items():
                for x in range(lower,upper+1):
                    newer[E+x]+=v
            term=newer
        answer.update(term)
    return answer


def theoretical_poly(n):
    result=Counter()
    for a in range(1,n-1):
        for b in range(1,n-a):
            c=n-a-b
            base=n*(n-1)-(a*b+a*c+b*c)
            scale=factorial(n)//(factorial(a)*factorial(b)*factorial(c))
            coef=Counter({base:scale})
            for count,width in ((a,c),(b,a),(c,b)):
                for _ in range(count):
                    follow=Counter()
                    for e,v in coef.items():
                        for k in range(width): follow[e+k]+=v
                    coef=follow
            result.update(coef)
    return result


def predicted_bottom(n):
    q,r=divmod(n,3)
    if r==0: return factorial(n)//factorial(q)**3
    if r==1: return 3*factorial(n)//(factorial(q+1)*factorial(q)**2)
    return 3*factorial(n)//(factorial(q+1)**2*factorial(q))


def main():
    for n in range(3,10):
        check=trace_poly(n)
        formula=theoretical_poly(n)
        L=n*(n-1)-n*n//3
        U=n*(n-2)
        assert check==formula,(n,check,formula)
        assert set(check)==set(range(L,U+1))
        assert check[L]==predicted_bottom(n)
        assert check[U]==3**n-3*2**n+3
        reflected=Counter({n*(2*n-3)-E:v for E,v in check.items()})
        assert not (set(check)&set(reflected))
        total=sum(check.values())+sum(reflected.values())
        assert total%3==0
        print(f"n={n}: phase_words={3**n} one_fire_states={sum(check.values())} total_primitive3={total} low_band=[{L},{U}] balanced_boundary={check[L]} central_boundary={check[U]} MATCH")
    print('PASS: independent trace poly and phase formula n=3..9; endpoint identities')

if __name__=='__main__':
    main()
