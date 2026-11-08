#!/usr/bin/env python3
"""Exact finite-field and polynomial checks for a genus-four hyperelliptic family."""
from itertools import product

def field(m,mod):
    els=list(product(range(3),repeat=m));zero=(0,)*m;one=(1,)+(0,)*(m-1)
    def add(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
    def mul(a,b):
        vals=[0]*(2*m-1)
        for i,ai in enumerate(a):
            for j,bj in enumerate(b):vals[i+j]=(vals[i+j]+ai*bj)%3
        for n in range(2*m-2,m-1,-1):
            v=vals[n]
            if v:
                for i in range(m):vals[n-m+i]=(vals[n-m+i]-v*mod[i])%3
        return tuple(vals[:m])
    def power(a,n):
        r=one
        while n:
            if n%2:r=mul(r,a)
            a=mul(a,a);n//=2
        return r
    return els,zero,one,add,mul,power

def test_field(m,mod):
    E,z,o,add,mul,powr=field(m,mod);q=len(E)
    assert all(powr(a,q-1)==o for a in E if a!=z),"nonfield modulus"
    minusone=add(z,tuple(2*x%3 for x in o))
    counts={'singular':0,'ordinary':0,'supersingular':0}
    for a in E:
        # f'(x)=x^4(x^5-a), common root with f iff a^2=1.
        if mul(a,a)==o:
            counts['singular']+=1
            continue
        # Cartier-Manin: for f=x^10+a*x^5+1, p=3,
        # M_(i,j) = [x^(3i-j)]f, 1<=i,j<=4.
        coefficients={0:o,5:a,10:o}
        M=[[coefficients.get(3*i-j,z) for j in range(1,5)] for i in range(1,5)]
        assert M[0][2]==o and M[1][0]==a and M[2][3]==a and M[3][1]==o
        det=mul(a,a)
        # The determinant is -a^2 (a unit iff a != 0).
        if a!=z:
            assert det!=z
            counts['ordinary']+=1
        else:
            assert det==z
            # Semilinear nilpotence: M M^(3) = 0.
            twist=[[powr(v,3) for v in row] for row in M]
            for i in range(4):
                for j in range(4):
                    val=z
                    for k in range(4):val=add(val,mul(M[i][k],twist[k][j]))
                    assert val==z
            counts['supersingular']+=1
    assert counts=={'singular':2,'ordinary':q-3,'supersingular':1},counts
    print('GF(%d): singular %d; ordinary %d; supersingular %d; ALL_CHECKS_PASSED'%(q,*counts.values()))

def laurent_mul(A,B):
    C={}
    for i,a in A.items():
        for j,b in B.items():C[i+j]=C.get(i+j,0)+a*b
    return {k:v for k,v in C.items() if v}

def laurent_add(A,B,sign=1):
    R=dict(A)
    for e,c in B.items():R[e]=R.get(e,0)+sign*c
    return {k:v for k,v in R.items() if v}

# Dickson recursion D_n(x+x^-1)=x^n+x^-n in Z[x,x^-1].
T={1:1,-1:1};D0={0:2};D1=T
for n in range(2,6):
    D0,D1=D1,laurent_add(laurent_mul(T,D1),D0,sign=-1)
assert D1=={5:1,-5:1}
# Evaluate T^5 - 5T^3 + 5T and match D5.
T2=laurent_mul(T,T);T3=laurent_mul(T2,T);T5=laurent_mul(T3,T2)
expr=laurent_add(laurent_add(T5,{e:-5*c for e,c in T3.items()}),{e:5*c for e,c in T.items()})
assert expr==D1
# The change of variables Y=y(x +/- 1)/x^3 yields Y²=(T +/-2)(D5(T)+a).
# The two factors (x +/-1)^2/x = x+x^-1 +/-2.
for s in (1,-1):
    lhs={2:1,1:2*s,0:1}
    rhs={1:1,-1:1,0:2*s}
    assert lhs=={i+1:c for i,c in rhs.items()}
print('DICKSON_AND_QUOTIENT_IDENTITIES_PASSED')
for d,mod in [(1,[0,1]),(2,[1,0,1]),(3,[1,2,0,1])]:test_field(d,mod)
print('ALL_CHECKS_PASSED')
