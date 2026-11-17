"""Independent integer run-enumeration and polynomial certificate for wheel-majority cycles.

R_m records (number of ones, adjacent-one edges) on a cyclic word with no
isolated ones. A split into two skip-two components applies to even rim sizes.
No graph-update simulation is used here.
"""
from collections import Counter
from math import comb


def polynomial(m):
    assert m>=2
    out=Counter({(0,0):1,(m,m):1})
    for k in range(1,m//3+1):
        for j in range(2*k,m-k+1):
            numerator=m*comb(j-k-1,k-1)*comb(m-j-1,k-1)
            assert numerator%k==0
            out[(j,j-k)]+=numerator//k
    return out


def census(n):
    assert n>=3
    if n%2:
        counts=polynomial(n)
    else:
        p=polynomial(n//2)
        counts=Counter()
        for (j,e),v in p.items():
            for (k,f),w in p.items():
                counts[(j+k,e+f)]+=v*w
    hub_flips=sum(num for (ones,edges),num in counts.items() if 2*ones>n and 2*edges<n)
    return 2,hub_flips+(2 if n%2==0 else 0),hub_flips


def direct_cyclic_words(m):
    counts=Counter()
    for b in range(1<<m):
        word=[(b>>i)&1 for i in range(m)]
        if any(word[i] and not(word[(i-1)%m] or word[(i+1)%m]) for i in range(m)):
            continue
        counts[(sum(word),sum(word[i]*word[(i+1)%m] for i in range(m)))]+=1
    return counts


def main():
    for m in range(2,14):
        assert polynomial(m)==direct_cyclic_words(m),m
    print('direct_cyclic_word_polynomial_checks=12 (lengths 2..13)')
    expected={3:3,4:2,5:5,6:11,7:21,8:34,9:66,10:77,11:220,12:227,
              13:715,14:835,15:2318,16:2978,17:7463}
    for n in range(3,61):
        fixed,cycles,flips=census(n)
        assert fixed==2
        if n in expected:assert cycles==expected[n],(n,cycles)
        if n<=18 or n in (20,24,30,40,50,60):
            print(f"n={n:02d} fixed={fixed} primitive_two_cycles={cycles} hub_flip={flips}")
    print('formula_cases=58 (rim lengths 3..60)')

if __name__=='__main__':
    main()
