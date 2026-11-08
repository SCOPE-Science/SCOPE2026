#!/usr/bin/env python3
"""Exact finite checks for the centers of Brandt power semigroups."""
from itertools import permutations, product


def group(nam):
    if nam == 'trivial':
        return [0], lambda a,b:0
    if nam.startswith('C'):
        k=int(nam[1:]); return list(range(k)), lambda a,b:(a+b)%k
    if nam == 'S3':
        els=list(permutations(range(3)))
        def mult(a,b):return tuple(a[b[t]] for t in range(3))
        return els,mult
    raise ValueError


def trial(n,gn,exhaustive=True):
    G,mul=group(gn)
    es=[None]+[(i,g,j) for i,j in product(range(n),repeat=2) for g in G]
    N=len(es); z=0
    table=[]
    ind={x:j for j,x in enumerate(es)}
    for a in es:
        row=[]
        for b in es:
            if a is None or b is None or a[2]!=b[0]:row.append(0)
            else:row.append(ind[(a[0],mul(a[1],b[1]),b[2])])
        table.append(row)
    # Conjugacy classes, computed by conjugates.
    one=next(g for g in G if all(mul(g,h)==h and mul(h,g)==h for h in G))
    inv={a:next(b for b in G if mul(a,b)==one and mul(b,a)==one) for a in G}
    classes=[];unseen=set(G)
    while unseen:
        a=next(iter(unseen)); cl={mul(mul(t,a),inv[t]) for t in G}
        unseen-=cl;classes.append(cl)
    predict={1}
    for mask in range(1,1<<len(classes)):
        H=set().union(*(cl for j,cl in enumerate(classes) if mask>>j&1))
        d=sum(1<<ind[(i,g,i)] for i in range(n) for g in H)
        predict.add(d);predict.add(d|1)
    assert len(predict)==2**(len(classes)+1)-1
    def cmask(A, idx, left=True):
        r=0
        while A:
            x=A&-A; a=x.bit_length()-1
            r|=1 << (table[a][idx] if left else table[idx][a]);A-=x
        return r
    checks=0
    for A in predict:
        for b in range(N):
            assert cmask(A,b)==cmask(A,b,False)
            checks+=1
    if exhaustive:
        actual=set()
        for A in range(1,1<<N):
            if all(cmask(A,b)==cmask(A,b,False) for b in range(N)):
                actual.add(A)
        assert actual==predict,(n,gn,predict^actual)
        checks+= (1<<N)-1
    # Validate exact layer-multiplication identities on all predicted centers.
    def multiply(A,B):
        r=0
        while A:
            x=A&-A;a=x.bit_length()-1
            tmp=B
            while tmp:
                y=tmp&-tmp;b=y.bit_length()-1
                r|=1<<table[a][b];tmp-=y
            A-=x
        return r
    normal_subgroups=sum(1 for mask in range(1,1<<len(classes))
                         if (lambda H: all(mul(a,b) in H for a in H for b in H))(
                             set().union(*(cl for j,cl in enumerate(classes) if mask>>j&1))))
    idempotents=sum(multiply(A,A)==A for A in predict)
    assert idempotents==1+(2 if n==1 else 1)*normal_subgroups
    for A in predict:
        for B in predict:
            assert multiply(A,B) in predict
            assert multiply(A,B)==multiply(B,A)
            checks+=1
    return (n,gn,N,len(classes),len(predict),normal_subgroups,idempotents,checks)

if __name__=='__main__':
    cases=[(1,'trivial'),(2,'trivial'),(3,'trivial'),(1,'C2'),(2,'C2'),(1,'C3'),(2,'C3'),(1,'S3')]
    outcomes=[trial(n,g) for n,g in cases]
    for out in outcomes:print('case=',out)
    print('VERIFY_OK cases=%d exact_assertions=%d'%(len(outcomes),sum(t[-1] for t in outcomes)))
