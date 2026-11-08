"""Finite-period inverse-resolution cross-checks (Python 3, standard library only).
This program checks finite instances. The uniform theorem is established analytically.
"""
from fractions import Fraction as Q


def tent(x):
    return 2*x if x <= Q(1,2) else 2-2*x


def fixed_by_inverse_words(k):
    # An independently generated set via all inverse-branch affine compositions.
    funcs = [(Q(1), Q(0))]
    for _ in range(k):
        funcs = [(a/2, b/2) for a,b in funcs] + [(-a/2,Q(1)-b/2) for a,b in funcs]
    return {b/(1-a) for a,b in funcs}


def fixed_grid(k):
    m = 2**k
    return ({Q(2*j,m+1) for j in range(m//2+1)} |
            {Q(2*j,m-1) for j in range(m//2)})


def deformed(x, n, delta):
    a = Q(2,2**n+1)
    if x <= a/2:
        return (2+delta)*x
    if x <= a:
        return (2-delta)*x + delta*a
    return tent(x)


def inverse_left(y, n, delta):
    a=Q(2,2**n+1)
    y1=(2+delta)*a/2
    if y <= y1: return y/(2+delta)
    if y <= 2*a: return (y-delta*a)/(2-delta)
    return y/2


def inverse_word_fixed_float(word,n,delta):
    x=0.4
    d=float(delta)
    a=2/(2**n+1)
    for _ in range(75):
        y=x
        # word maps in left-to-right function-composition order.
        for b in word[::-1]:
            if b:
                y=1-y/2
            elif y <= (2+d)*a/2:
                y=y/(2+d)
            elif y <= 2*a:
                y=(y-d*a)/(2-d)
            else:
                y=y/2
        x=y
    return x


def main():
    enumerated=0
    maximal=0
    inverse=0
    for n in range(2,12):
        P={Q(0),Q(1),Q(1,2)}
        for k in range(1,n+1):
            first=fixed_by_inverse_words(k)
            assert first==fixed_grid(k), (k,len(first),len(fixed_grid(k)))
            assert len(first)==2**k
            P |= first
            enumerated+=1
        sorted_p=sorted(P)
        gaps=[(sorted_p[i+1]-sorted_p[i],sorted_p[i],sorted_p[i+1]) for i in range(len(sorted_p)-1)]
        mx=max(gaps)
        assert mx==(Q(2,2**n+1),Q(0),Q(2,2**n+1)), (n,mx)
        maximal+=1
        delta=Q(1,3)
        for p in P:
            assert deformed(p,n,delta)==tent(p)
        a=Q(2,2**n+1)
        assert deformed(a/2,n,delta)-tent(a/2)==delta/(2**n+1)
        # Independently check exact low-period orbit positions using inverse words.
        if n<=7:
            for k in range(1,n+1):
                vals=[]
                for w in range(1<<k):
                    bits=[(w>>i)&1 for i in range(k)]
                    vals.append(inverse_word_fixed_float(bits,n,delta))
                expected=sorted(float(t) for t in fixed_by_inverse_words(k))
                assert len(vals)==len(expected)
                assert max(abs(a-b) for a,b in zip(sorted(vals),expected))<2e-12,(n,k)
                inverse+=1
    print('VERIFY_OK rational_grid_equalities=%d sharp_gap_cases=%d deformed_inverse_spectra=%d' % (enumerated,maximal,inverse))

if __name__=='__main__': main()
