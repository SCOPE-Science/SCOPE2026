"""Finite-field checks for the spin-factor square-map fiber census.

Runs exhaustive tests for several prime fields and F_9; no symbolic/computational
check is used as a replacement for the general proof.
"""
from collections import Counter
from itertools import product
import json

class Field:
    def __init__(self, q):
        assert q in (3, 5, 7, 9, 11)
        self.q = q
        self.p = 3 if q == 9 else q
        self.elements = tuple(range(q))
        self.one = 1
        self.zero = 0
    def add(self, x, y):
        if self.q == 9:
            return ((x % 3 + y % 3) % 3) + 3 * ((x // 3 + y // 3) % 3)
        return (x + y) % self.p
    def neg(self, x):
        return self.sub(0, x)
    def sub(self, x, y):
        if self.q == 9:
            return ((x % 3 - y % 3) % 3) + 3 * ((x // 3 - y // 3) % 3)
        return (x - y) % self.p
    def mul(self, x, y):
        if self.q == 9:
            a,b,c,d = x%3,x//3,y%3,y//3
            return ((a*c-b*d)%3)+3*((a*d+b*c)%3)
        return (x*y) % self.p
    def pow(self, x, n):
        r=1
        while n:
            if n & 1: r = self.mul(r, x)
            x = self.mul(x, x)
            n //= 2
        return r
    def inv(self, x):
        assert x
        return self.pow(x, self.q-2)

def census(q, diag):
    F=Field(q); d=len(diag); E=F.elements
    assert all(x for x in diag)
    two=F.add(1,1)
    four=F.mul(two,two)
    invfour=F.inv(four)
    H={F.mul(t,t) for t in E if t}
    h=len(H)
    nonsquares=set(E)-H-{0}
    def Q(v):
        s=0
        for a,x in zip(diag,v):
            s=F.add(s,F.mul(a,F.mul(x,x)))
        return s
    outputs=Counter(); norms=Counter()
    for v in product(E,repeat=d):
        s=Q(v)
        norms[s]+=1
        for a in E:
            b=F.add(F.mul(a,a),s)
            w=tuple(F.mul(two,F.mul(a,x)) for x in v)
            outputs[(b,w)]+=1
    T0=norms[0]
    Ts=norms[next(iter(H))]
    Tn=norms[next(iter(nonsquares))]
    assert all(norms[t]==Ts for t in H)
    assert all(norms[t]==Tn for t in nonsquares)
    epsilon=1 if F.pow(F.mul(F.pow(F.neg(1),d//2),_mul_all(F,diag)),h)==1 else -1
    if d%2 == 0:
        eT0=q**(d-1)+(q-1)*epsilon*q**(d//2-1)
        eTs=eTn=q**(d-1)-epsilon*q**(d//2-1)
        sign=1
        qpow=d//2-1
    else:
        eT0=q**(d-1)
        eTs=q**(d-1)+epsilon*q**((d-1)//2)
        eTn=q**(d-1)-epsilon*q**((d-1)//2)
        sign=-1
        qpow=(d-1)//2
    assert (T0,Ts,Tn)==(eT0,eTs,eTn),(q,diag,(T0,Ts,Tn),(eT0,eTs,eTn))
    image_formula=q+(T0-1)*h+Tn*h*h+Ts*h*(h+1)//2
    image_compact=q-h+(3*q**(d-1)*h*(h+1))//2+sign*epsilon*(h*(h-1)//2)*q**qpow
    assert len(outputs)==image_formula==image_compact,(q,diag,len(outputs),image_formula,image_compact)
    # Critically: all targets, including missing targets, must obey the fiber formula.
    for w in product(E,repeat=d):
        s=Q(w)
        for b in E:
            if any(w):
                predicted=2*sum(F.add(F.sub(F.mul(t,t),F.mul(b,t)),F.mul(s,invfour))==0 for t in H)
            else:
                predicted=norms[b]+(2 if b in H else 0)
            actual=outputs.get((b,w),0)
            assert predicted==actual,(q,diag,b,w,predicted,actual)
    roots=Counter(outputs.values())
    total_2=(T0-1)*h+Tn*h*h+Ts*h
    total_4=Ts*h*(h-1)//2
    nonzero_vector_2=sum(1 for (b,w),count in outputs.items() if any(w) and count==2)
    nonzero_vector_4=sum(1 for (b,w),count in outputs.items() if any(w) and count==4)
    assert (total_2,total_4)==(nonzero_vector_2,nonzero_vector_4)
    assert sum(roots[m]*m for m in roots)==q**(d+1)
    return dict(field=q, dimension=d, diagonal=list(diag), norm_counts=[T0,Ts,Tn],
                image_size=len(outputs), image_formula=image_formula,
                full_root_profile={str(k):v for k,v in sorted(roots.items())},
                nonzero_vector_two_root_targets=total_2,
                nonzero_vector_four_root_targets=total_4)

def _mul_all(F,xs):
    z=1
    for x in xs:z=F.mul(z,x)
    return z

if __name__=='__main__':
    rows=[]
    for q in (3,5,7,9,11):
        F=Field(q)
        H={F.mul(a,a) for a in F.elements if a}
        ns=next(a for a in F.elements if a and a not in H)
        for d in (2,3,4):
            for diag in ((1,)*d, (1,)*(d-1)+(ns,)):
                rows.append(census(q,diag))
    result={'status':'passed','method':'exhaustive all input and output elements (not a general proof)',
            'cases':len(rows),'records':rows}
    print(json.dumps(result,sort_keys=True,indent=2))
