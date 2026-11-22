"""Independent left/right-context enumeration and random adversarial tests.
No external packages; execute: python check_contexts.py
"""
from itertools import product
from random import Random


def maws_by_contexts(s, alphabet):
    # A minimal absence a u b has both a u and u b present, but a u b absent.
    output = {a for a in alphabet if a not in s}
    substr = {s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)}
    substr.add('')
    for u in substr:
        for a in alphabet:
            if a+u not in substr:
                continue
            for b in alphabet:
                x = a+u+b
                if u+b in substr and x not in substr:
                    output.add(x)
    return output


def root(s):
    for p in range(1, len(s)+1):
        if len(s)%p == 0 and all(s[i]==s[i%p] for i in range(len(s))):
            return s[:p]
    raise RuntimeError('no root')


def test_one(s, alphabet, n):
    r=root(s); d=len(r); assert n >= max(1,2*d-2)
    # Compute periodic forbidden words directly from an independent long circular sample.
    cyc=r*4
    pfs={cyc[i:i+k] for i in range(d) for k in range(1, d+2)}
    pfs.add('')
    permanent={a for a in alphabet if a not in pfs}
    for midlen in range(d):
        for i in range(d):
            mid=cyc[i:i+midlen]
            for a in alphabet:
                for b in alphabet:
                    x=a+mid+b
                    if x not in pfs and x[:-1] in pfs and x[1:] in pfs:
                        permanent.add(x)
    periodic=r*((n+d+1)//d+3)
    boundary=periodic[d-1:n+1]
    actual=maws_by_contexts(periodic[:n], alphabet)
    assert actual==permanent|{boundary}, (s, n, actual^(permanent|{boundary}))
    return len(actual)


def main():
    total=0
    for q, maxlen in [(2,7),(3,4),(4,3)]:
        alphabet='0123'[:q]
        for p in range(1,maxlen+1):
            for chars in product(alphabet,repeat=p):
                s=''.join(chars)
                if root(s) != s: continue
                for n in range(max(1,2*p-2),3*p+3):
                    test_one(s,alphabet,n)
                    total+=1
    rng=Random(20261117)
    for i in range(500):
        q=rng.choice((2,3,4))
        alphabet='0123'[:q]
        length=rng.randint(1,12)
        s=''.join(rng.choice(alphabet) for _ in range(length))
        d=len(root(s)); n=rng.randint(max(1,2*d-2),max(1,5*d))
        test_one(s,alphabet,n)
        total+=1
    print('PASS independent context checks:',total,'cases')

if __name__ == '__main__':
    main()
