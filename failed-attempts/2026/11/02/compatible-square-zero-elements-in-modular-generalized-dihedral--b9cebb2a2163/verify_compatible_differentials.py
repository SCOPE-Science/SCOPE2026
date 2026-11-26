#!/usr/bin/env python3
"""Reconstruct modular generalized dihedral multiplication and test compatible square-zero tuples.
Requires only Python's standard library; field arithmetic is implemented over GF(2) and GF(4).
"""
from collections import Counter
from itertools import product
from verify_group_ring import integer_digits, fmul, rank_field, orbit_degrees


def test_binary(orders, tuple_length=2):
    H=list(product(*[range(t) for t in orders])); h=len(H); n=2*h
    ix={v:i for i,v in enumerate(H)}
    inv=[ix[tuple((-u) % orders[k] for k,u in enumerate(v))] for v in H]
    idx=[]
    for i in range(n):
        hi,ei=i%h,i//h
        idx.append([ix[tuple((H[hi][k]+(1 if ei==0 else -1)*H[j%h][k])%orders[k] for k in range(len(orders)))] + h*((ei+j//h)&1) for j in range(n)])
    shifts=[[1<<idx[i][j] for j in range(n)] for i in range(n)]
    def prod(x,y):
        s=0
        while x:
            low=x&-x; i=low.bit_length()-1; x-=low
            t=y
            while t:
                b=t&-t;j=b.bit_length()-1;t-=b
                s^=shifts[i][j]
        return s
    def rank_left(x):
        piv={}
        for j in range(n):
            v=prod(x,1<<j)
            while v:
                i=v.bit_length()-1
                if i in piv:v^=piv[i]
                else:
                    piv[i]=v;break
        return len(piv)
    # Entire set of square-zero elements is constructed by taking the unique square root
    # of b*bar(b) in the odd-order abelian group ring; test each square in original algebra.
    xs=[]; ranks=[]
    for b in range(1<<h):
        y=0;t=b
        while t:
            bit=t&-t;j=bit.bit_length()-1;t-=bit;y|=1<<inv[j]
        z=prod(b,y)
        assert z < (1<<h)
        a=0;t=z
        while t:
            bit=t&-t;j=bit.bit_length()-1;t-=bit
            c=tuple((u*pow(2,-1,orders[k]))%orders[k] for k,u in enumerate(H[j]))
            a|=1<<ix[c]
        x=a+(b<<h)
        assert prod(x,x)==0
        xs.append(x);ranks.append(rank_left(x))
    assert len(set(xs))==1<<h
    d=orbit_degrees(orders,2);Q=[2**v for v in d]
    assert sum(d)*2==h-1
    def expectation(m):return (2**m)*__import__('math').prod(1+(u+1)*(u**m-1) for u in Q)
    pairhist=Counter(); neighbor=Counter(); total=0
    for i,x in enumerate(xs):
        for j,y in enumerate(xs):
            if prod(x,y)==prod(y,x):
                assert prod(x,y)==0,(orders,i,j)
                pairhist[(ranks[i],ranks[j])]+=1
                neighbor[i]+=1;total+=1
    assert total==expectation(2),(orders,total,expectation(2))
    # Independent symbolic coefficient extraction of the multivariate polynomial.
    pol={(0,0):1}
    for j in range(2):
        p={}
        for old,amt in pol.items():
            for t in range(2):
                key=list(old);key[j]+=t;key=tuple(key)
                p[key]=p.get(key,0)+amt
        pol=p
    for v in d:
        p={}
        factor={(0,0):1}
        for a in (0,1):
            for b in (0,1):
                if not (a or b):continue
                factor[(2*v*a,2*v*b)]=(2**v+1)*(2**v-1)**(a+b)
        for old,coef in pol.items():
            for (a,b),z in factor.items():
                key=(old[0]+a,old[1]+b)
                p[key]=p.get(key,0)+coef*z
        pol=p
    assert Counter(pol)==pairhist,(orders,len(pol),len(pairhist),set(pol.items())^set(pairhist.items()))
    # Three-way tuple census by common-neighborhood intersection (a truly direct check).
    triple=0
    if tuple_length>=3 and h<=5:
        for i,x in enumerate(xs):
            comp=[j for j,y in enumerate(xs) if prod(x,y)==0]
            for j in comp:
                y=xs[j]
                triple+=sum(prod(y,xs[k])==0 for k in comp)
        assert triple==expectation(3),(orders,triple,expectation(3))
    max_dim=1+sum(d)
    num_max=__import__('math').prod(v+1 for v in Q)
    # Checking global upper bound would require an independent subspace search;
    # these values are predictions of the proved blockwise classification.
    print(f'G=Dih({"x".join(map(str,orders))}), q=2: {len(xs)} square-zero elements, {total} compatible ordered pairs, {len(pairhist)} rank-vector types, tuples3={triple if tuple_length>=3 and h<=5 else "not enumerated"}, predicted maximal dimension={max_dim}, maximal spaces={num_max}, rank_hist={dict(sorted(pairhist.items()))}')


def test_quaternary_c3():
    # Exhaustive original 6-dimensional GF(4) group ring, no use of Wedderburn projections.
    h=3;n=6;q=4
    mult=[[((i%h+(-1 if i>=h else 1)*(j%h))%h)+h*((i//h+j//h)%2) for j in range(n)] for i in range(n)]
    def prod(x,y):
        out=[0]*n
        for i,a in enumerate(x):
            if a:
                for j,b in enumerate(y):
                    if b:out[mult[i][j]]^=fmul(a,b,4)
        return tuple(out)
    zero=(0,)*n; xs=[];ranks=[]
    for code in range(q**n):
        x=tuple(integer_digits(code,q,n))
        if prod(x,x)==zero:
            xs.append(x)
            columns=[]
            for j in range(n):
                t=[0]*n
                for i,v in enumerate(x):
                    if v:t[mult[i][j]]^=v
                columns.append(t)
            ranks.append(rank_field(columns,n,q))
    assert len(xs)==64
    hist=Counter();total=0
    for i,x in enumerate(xs):
        for j,y in enumerate(xs):
            if prod(x,y)==prod(y,x):
                assert prod(x,y)==zero
                hist[(ranks[i],ranks[j])]+=1;total+=1
    assert total==4**2*(1+5*(4**2-1))==1216
    expected=Counter()
    for s,t in product((0,1),(0,1)):
        for a,b in product((0,1),(0,1)):
            coef=3**(s+t)*(5*(3**(a+b)) if a+b else 1)
            expected[(s+2*a,t+2*b)]+=coef
    assert hist==expected,(hist,expected)
    print(f'G=Dih(3), q=4: {len(xs)} square-zero elements, {total} compatible ordered pairs, {len(hist)} rank-vector types, rank_hist={dict(sorted(hist.items()))}')

if __name__=='__main__':
    for H in [(3,),(5,),(7,),(3,3),(9,)]:test_binary(H,tuple_length=3)
    test_quaternary_c3()
    print('COMPATIBLE_GROUP_ALGEBRA_SQUAREZERO_OK 6_DIRECT_CONFIGURATIONS')
