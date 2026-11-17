"""Literal gapped-pair counts versus exact low-run inverse formulas.

Use: python3 verify.py. No dependencies outside Python's standard library.
"""
from collections import Counter, defaultdict
from itertools import product


def deck(w):
    """One-letter counts and all length-two subsequences with separation >=2."""
    a = w.count('0')
    b = w.count('1')
    d = Counter(w[i]+w[j] for i in range(len(w)) for j in range(i+2, len(w)))
    return a,b,*(d.get(pair,0) for pair in ('00','01','10','11'))


def number_runs(w):
    return 1+sum(w[i] != w[i-1] for i in range(1,len(w)))


def r(A,B,p):
    """Number of factor pairs with 1<=u<A and 1<=v<B."""
    return sum(p%u==0 and 1<=p//u<B for u in range(1,A))


def fibre_formula(signature, run_count):
    A,B,g00,g01,g10,g11 = signature
    if run_count == 1:
        return 1
    if run_count == 2:
        return 2 if A==B==1 else 1
    if run_count == 3:
        return 1
    if run_count == 4:
        return r(A,B,g10+1) + r(A,B,g01+1)
    raise AssertionError("Unsupported run count")


def multiplication_table(A,B):
    return {u*v for u in range(1,A) for v in range(1,B)}


def tau(K):
    return sum(K%d==0 for d in range(1,K+1))


def test():
    words_checked=0
    classes_checked=0
    ambiguous=Counter()
    for n in range(1,19):
        observed=defaultdict(list)
        for chars in product('01',repeat=n):
            w=''.join(chars)
            t=number_runs(w)
            if t > 4:
                continue
            sig=deck(w)
            observed[(t,sig)].append(w)
            words_checked+=1
            A,B,g00,g01,g10,g11=sig
            r0=A-A*(A-1)//2+g00
            r1=B-B*(B-1)//2+g11
            assert r0+r1==t, (w,t,sig,r0,r1)
            assert g01+g10==A*B-(t-1), (w,t,sig)
        for (t,sig), words in observed.items():
            expected=fibre_formula(sig,t)
            assert len(words)==expected, (n,t,sig,words,expected)
            classes_checked+=1
            if len(words)>1:
                ambiguous[t]+=1
    for A in range(2,25):
        for B in range(2,25):
            P=multiplication_table(A,B)
            reflected={A*B-1-p for p in P}
            classes=len(P|reflected)
            assert classes==2*len(P)-len(P&reflected)
            assert sum(r(A,B,p)+r(A,B,A*B-1-p) for p in P|reflected)==2*(A-1)*(B-1)
    for K in range(1,121):
        A=B=K+1
        assert r(A,B,K)+r(A,B,A*B-1-K)==tau(K)
    assert ambiguous[3]==0 and ambiguous[2]==1
    print('VERIFY_OK words=%d profiles=%d ambiguity=%s multiplication_tables=%d divisor_examples=%d' % (
        words_checked, classes_checked, dict(ambiguous),23*23,120))


if __name__ == '__main__':
    test()
