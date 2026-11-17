"""Finite reproducibility checks for rectangular-block edge faults in bicliques.

Run with Python 3.9+; no external packages.
"""
from itertools import combinations
from math import comb

def faces(s, b, k, t):
    a = s + 1
    n = a + b
    u = s
    B = tuple(range(a,n))
    T = set(B[:t])
    out = set()
    for z in range(1 << n):
        verts = [i for i in range(n) if z & (1 << i)]
        if len(verts) < k:
            out.add(z);continue
        valid = True
        for I in combinations(verts,k):
            if all(i <= s for i in I) or all(i >= a for i in I):
                valid = False; break
            IA = [i for i in I if i <= s]
            IB = [i for i in I if i >= a]
            if IA and IB and all(i != u for i in IA) and all(j in T for j in IB):
                valid = False; break
        if valid:
            out.add(z)
    return out

def target(s,b,k,t):
    a=s+1;u=s
    stay=list(range(a))+list(range(a+t,a+b))
    z=set()
    for bits in range(1<<len(stay)):
        pick=[stay[i] for i in range(len(stay)) if bits>>i&1]
        if sum(v<a for v in pick)<k and sum(v>=a for v in pick)<k:
            z.add(sum(1<<v for v in pick))
    return z

def chi(f):
    return sum(((-1)**(z.bit_count()-1)) for z in f if z)

def gf2rank(vectors):
    piv={}
    for x in vectors:
        while x:
            bit=x.bit_length()-1
            if bit in piv:x^=piv[bit]
            else:
                piv[bit]=x;break
    return len(piv)

def betti(f):
    cells={}
    for z in f:
        if z:cells.setdefault(z.bit_count()-1,[]).append(z)
    ranks={}
    for d in sorted(cells):
        if d==0:ranks[d]=0;continue
        mapping={z:i for i,z in enumerate(cells[d-1])}
        col=[]
        for z in cells[d]:
            mask=0
            for i in range(z.bit_length()):
                if z>>i&1:
                    mask^=1<<mapping[z^(1<<i)]
            col.append(mask)
        ranks[d]=gf2rank(col)
    ans={d:len(v)-ranks[d]-ranks.get(d+1,0) for d,v in cells.items()}
    ans[0]=ans.get(0,0)-1
    return {d:r for d,r in ans.items() if r}

def one(s,b,k):
    n=s+1+b;u=s;B=tuple(range(s+1,n))
    prev=None
    for t in range(b+1):
        f=faces(s,b,k,t); g=target(s,b,k,t)
        assert g<=f
        if prev is not None:assert f<=prev
        prev=f
        # Every one of the t deleted-neighborhood vertices is foldable to u.
        current=f.copy()
        for v in B[:t]:
            bit=1<<v
            for z in current:
                if z&bit and not (z&(1<<u)):
                    assert (z|(1<<u)) in current, (s,b,k,t,v,z)
            current={z for z in current if not(z&bit)}
        assert current==g, (s,b,k,t,'fold-target')
        m=b-t
        if m==0:
            pred={k-2:comb(s,k-1)}
        elif m>=k:
            pred={2*k-3:comb(s,k-1)*comb(m-1,k-1)}
        else:pred={}
        pred={d:r for d,r in pred.items() if r}
        actual=betti(f)
        assert actual==pred, (s,b,k,t,actual,pred)
        expected_euler=1+sum((-1)**d*r for d,r in pred.items())
        assert chi(f)==expected_euler, (s,b,k,t,'Euler')
        print(f's={s} b={b} k={k} t={t} faces={len(f)} betti={actual} fold=PASS')

if __name__=='__main__':
    for p in ((3,5,4),(4,5,4),(4,6,4),(4,6,5)):
        one(*p)
    print('RECTANGULAR_BLOCK_FINITE_CHECK_PASS')
