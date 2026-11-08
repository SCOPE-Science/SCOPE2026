#!/usr/bin/env python3
"""Independent finite-field checks for four-by-four strict upper triangular Lie brackets.

Uses literal matrix multiplication for brackets and Gaussian elimination for
adjoint ranks. It does not use the counting reductions in the proof.
"""
from itertools import product
from collections import Counter
from random import Random

POSITIONS = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

def arithmetic(q):
    if q == 4:
        return lambda x,y:x^y, lambda x,y:((1 if (x&1 and y&1) else 0) ^ (2 if bool(x&1 and y&2)^bool(x&2 and y&1) else 0) ^ (3 if (x&2 and y&2) else 0))
    return lambda x,y:(x+y)%q, lambda x,y:(x*y)%q

def negate(x,q):
    return x if q == 4 else (-x)%q

def bracket(a,b,q,add,mul):
    A = [[0]*4 for _ in range(4)]
    B = [[0]*4 for _ in range(4)]
    for (i,j),x,y in zip(POSITIONS,a,b):
        A[i][j]=x
        B[i][j]=y
    C = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            left=right=0
            for k in range(4):
                left=add(left,mul(A[i][k],B[k][j]))
                right=add(right,mul(B[i][k],A[k][j]))
            C[i][j]=add(left,negate(right,q))
    assert all(C[i][j]==0 for i in range(4) for j in range(4) if (i,j) not in ((0,2),(1,3),(0,3)))
    return C[0][2],C[1][3],C[0][3]

def predicted(q,u,v,w):
    if u or v: return q**7*(q*q-1)
    if w: return 2*q**7*(q*q-1)
    return 2*q**9+q**8-2*q**7

def inv(a,q,mul):
    for t in range(1,q):
        if mul(a,t)==1:return t
    raise AssertionError('no inverse')

def rank(a,q,add,mul):
    a = [row[:] for row in a];r=0
    if not a:return 0
    for c in range(len(a[0])):
        piv=next((i for i in range(r,len(a)) if a[i][c]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        v=inv(a[r][c],q,mul)
        a[r]=[mul(v,x) for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                f=a[i][c]; a[i]=[add(x,negate(mul(f,y),q)) for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a): break
    return r

def adjoint_rank(a,q,add,mul):
    bas=[]
    for j in range(6):
        e=[0]*6;e[j]=1
        bas.append(bracket(a,e,q,add,mul))
    return rank([[bas[j][i] for j in range(6)] for i in range(3)],q,add,mul)

def main():
    for q in (2,3):
        add,mul=arithmetic(q)
        E=list(product(range(q),repeat=6)); ctr=Counter()
        for a in E:
            for b in E:
                ctr[bracket(a,b,q,add,mul)]+=1
        assert len(ctr)==q**3
        assert sum(ctr.values())==q**12
        for (u,v,w),n in ctr.items():
            assert n==predicted(q,u,v,w),(q,(u,v,w),n,predicted(q,u,v,w))
        ar=Counter(adjoint_rank(a,q,add,mul) for a in E)
        expected={0:q,1:q*(q*q-1),2:q**3*(q*q+q-2),3:q**3*(q-1)*(q*q-1)}
        assert ar==expected,(q,ar,expected)
        assert sum(q**(6-r)*cnt for r,cnt in ar.items())==predicted(q,0,0,0)
        print(f'EXHAUSTIVE q={q} inputs={q**12} targets={q**3} adjoint_elements={q**6} PASS')
    rng=Random(9462101)
    for q in (4,5):
        add,mul=arithmetic(q)
        for _ in range(50000):
            a=tuple(rng.randrange(q) for i in range(6))
            b=tuple(rng.randrange(q) for i in range(6))
            u,v,w=bracket(a,b,q,add,mul)
            # Correctness of multiplication via the structural coordinate identity.
            aa,bb,cc,dd,ee,ff=a
            AA,BB,CC,DD,EE,FF=b
            uu=add(mul(aa,DD),negate(mul(dd,AA),q))
            vv=add(mul(dd,FF),negate(mul(ff,DD),q))
            ww=add(add(mul(aa,EE),negate(mul(ee,AA),q)),add(mul(bb,FF),negate(mul(ff,BB),q)))
            assert (u,v,w)==(uu,vv,ww)
        E=product(range(q),repeat=6)
        ar=Counter(adjoint_rank(a,q,add,mul) for a in E)
        expected={0:q,1:q*(q*q-1),2:q**3*(q*q+q-2),3:q**3*(q-1)*(q*q-1)}
        assert ar==expected,(q,ar,expected)
        assert sum(q**(6-r)*cnt for r,cnt in ar.items())==predicted(q,0,0,0)
        # Independently sum predicted mass over all possible targets.
        assert sum(predicted(q,u,v,w) for u,v,w in product(range(q),repeat=3))==q**12
        print(f'ADJOINT_AND_MATRIX_SAMPLE q={q} samples=50000 adjoint_elements={q**6} MASS_PASS')
    print('UT4_BRACKET_ALL_CHECKS_PASS')
if __name__=='__main__':main()
