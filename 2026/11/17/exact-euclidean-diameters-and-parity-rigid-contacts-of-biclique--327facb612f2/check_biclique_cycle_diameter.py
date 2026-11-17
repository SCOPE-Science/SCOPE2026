#!/usr/bin/env python3
"""Exact reproducibility checks for a Euclidean cycle-space cube-projection theorem."""
from fractions import Fraction
from itertools import product


def upper(p,q):
    penalties=[]
    if p%2: penalties.append(Fraction(q,p))
    if q%2: penalties.append(Fraction(p,q))
    return Fraction(p*q)-max(penalties,default=Fraction(0))


def score(A):
    p=len(A);q=len(A[0])
    rows=[sum(row) for row in A]
    cols=[sum(A[i][j] for i in range(p)) for j in range(q)]
    total=sum(rows)
    return Fraction(p*q)-Fraction(sum(x*x for x in rows),q)-Fraction(sum(x*x for x in cols),p)+Fraction(total*total,p*q)


def transpose(A):
    return list(map(list,zip(*A)))


def witness(p,q):
    if not p%2 and not q%2:
        return [[1 if (i+j)%2==0 else -1 for j in range(q)] for i in range(p)]
    if p%2==0 and q%2:
        return transpose(witness(q,p))
    if p%2 and q%2==0:
        v=[1 if i<(p+1)//2 else -1 for i in range(p)]
        cols=[]
        for j in range(q//2):cols.extend((v,[-x for x in v]))
        return transpose(cols)
    if p>q:
        return transpose(witness(q,p))
    v=[1 if i<(p+1)//2 else -1 for i in range(p)]
    cols=[]
    for k in range(p):cols.append([v[(i-k)%p] for i in range(p)])
    for j in range((q-p)//2):cols.extend((v,[-x for x in v]))
    return transpose(cols)



def contact_criterion(A):
    p=len(A);q=len(A[0])
    rows=[sum(row) for row in A]
    cols=[sum(A[i][j] for i in range(p)) for j in range(q)]
    if p%2==0 and q%2==0:
        return all(x==0 for x in rows+cols)
    if p%2 and (q%2==0 or q>=p):
        return all(abs(x)==1 for x in cols) and len(set(rows))==1
    return all(abs(x)==1 for x in rows) and len(set(cols))==1

def exhaustive(p,q):
    target=upper(p,q)
    best=None; count=0
    for bits in product((-1,1),repeat=p*q):
        A=[bits[i*q:(i+1)*q] for i in range(p)]
        z=score(A)
        assert (z==target)==contact_criterion(A),(p,q,A,z,target)
        if best is None or z>best:
            best=z; count=1
        elif z==best:
            count+=1
    assert best==target,(p,q,best,target)
    return count


def run():
    trials=0
    for p in range(2,51):
        for q in range(2,51):
            A=witness(p,q)
            assert len(A)==p and all(len(row)==q for row in A)
            assert score(A)==upper(p,q),(p,q,score(A),upper(p,q))
            assert contact_criterion(A),(p,q,A)
            trials+=1
    exhaust=[]
    for p in range(2,6):
        for q in range(p,10):
            if p*q<=18:
                cnt=exhaustive(p,q)
                exhaust.append((p,q,cnt))
    assert upper(3,3)==Fraction(8)
    assert upper(3,5)==Fraction(40,3)
    print('BICLIQUE_CYCLE_DIAMETER_PASS witnesses=%d exhaustive_pairs=%d exhaustive=%s' % (trials,len(exhaust),exhaust))

if __name__=='__main__':run()
