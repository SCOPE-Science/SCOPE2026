"""Direct, dependency-free checks of exact circular square spectra."""
from itertools import product
from random import Random


def exact_factor_squares(gaps):
    w = ''.join('1' + '0'*(d-1) for d in gaps)
    n = len(w)
    double = w + w
    return {double[i:i+2*h]
            for i in range(n) for h in range(1,n//2+1)
            if double[i:i+h] == double[i+h:i+2*h]}


def predicted_squares(gaps):
    n = sum(gaps)
    result = {'0'*(2*k) for k in range(1,(max(gaps)-1)//2+1)}
    for j,d in enumerate(gaps):
        before,after = gaps[(j-1)%3], gaps[(j+1)%3]
        for i in range(max(0,d-after), min(d-1,before-1)+1):
            x = '0'*i+'1'+'0'*(d-i-1)
            if 2*len(x) <= n:
                result.add(x+x)
    return result


def closed_count(gaps):
    a,b,c = sorted(gaps)
    if a==b==c: mixed=a
    elif a==b: mixed=a+max(0,2*a-c)
    elif b==c: mixed=a+min(b,2*a)
    else: mixed=2*a+max(0,a+b-c)
    return (c-1)//2+mixed


def main():
    cases=0; roots=0
    for g in product(range(1,16),repeat=3):
        direct=exact_factor_squares(g)
        shapes=predicted_squares(g)
        assert direct==shapes,(g,'root classification',direct^shapes)
        assert len(direct)==closed_count(g),(g,'closed count')
        cases+=1;roots+=len(direct)
    print('EXHAUSTIVE_GAP_CUBES_PASS',cases, 'root_count',roots)
    rng=Random(482117)
    for j in range(240):
        g=tuple(rng.randint(1,260) for _ in range(3))
        # Independently compare literal membership and the exact structural list.
        assert exact_factor_squares(g)==predicted_squares(g),g
        assert len(exact_factor_squares(g))==closed_count(g)
    print('LONG_RANDOM_CASES_PASS',240,'max_gap',260)
    print('ALL_TESTS_PASS')

if __name__=='__main__': main()
