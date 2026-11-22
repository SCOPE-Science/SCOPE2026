"""Direct graph check independent of the symbolic pair-space factorization.
Run: python3 verify_arborescences.py (standard Python, no dependencies).
"""
from itertools import product
from math import factorial

def allowed(w):
    return len(set(w))==3 and (w[0]==w[2] or w[1]==w[3] or w[0]==w[3])

def laplacian(q):
    words=[w for w in product(range(q), repeat=4) if allowed(w)]
    vertices=sorted({w[:3] for w in words}|{w[1:] for w in words})
    pos={v:i for i,v in enumerate(vertices)}
    out=[0]*len(vertices); inc=[0]*len(vertices)
    A=[[0]*len(vertices) for _ in vertices]
    for w in words:
        i,j=pos[w[:3]],pos[w[1:]]
        out[i]+=1;inc[j]+=1
        A[i][i]+=1;A[i][j]-=1
    assert out==inc
    assert len(words)==3*q*(q-1)*(q-2)
    assert len(vertices)==q*(q-1)**2
    assert sum(1 for i,v in enumerate(vertices) if v[0]==v[2] and out[i]==q-2)==q*(q-1)
    assert sum(1 for i,v in enumerate(vertices) if len(set(v))==3 and out[i]==2)==q*(q-1)*(q-2)
    return [row[1:] for row in A[1:]],out

def exact_det(A):
    B=[row[:] for row in A]; n=len(B); denom=1; sign=1
    for k in range(n-1):
        if B[k][k]==0:
            j=next((i for i in range(k+1,n) if B[i][k]),None)
            if j is None:return 0
            B[k],B[j]=B[j],B[k];sign=-sign
        pivot=B[k][k]
        for i in range(k+1,n):
            u=B[i][k]
            for j in range(k+1,n):
                val=B[i][j]*pivot-u*B[k][j]
                assert val%denom==0
                B[i][j]=val//denom
            B[i][k]=0
        denom=pivot
    return sign*B[-1][-1]

def modular_det(A,p):
    B=[list(map(lambda x:x%p,row)) for row in A]
    n=len(B); out=1
    for k in range(n):
        pivot=next((i for i in range(k,n) if B[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:
            B[k],B[pivot]=B[pivot],B[k];out=-out
        a=B[k][k];out=out*a%p; ai=pow(a,-1,p)
        for i in range(k+1,n):
            if B[i][k]:
                mult=B[i][k]*ai%p
                for j in range(k+1,n):B[i][j]=(B[i][j]-mult*B[k][j])%p
    return out%p

def predicted(q):
    ds=q*(q-3)//2;da=(q-1)*(q-2)//2
    e=q*(q-1)*(q-5)//3+q
    numerator=(7**e)*(6*(q-1))**ds*(2*(4*q-5))**da*(2*q*(q-2))**(q-1)
    assert numerator%(q*(q-1))==0
    return numerator//(q*(q-1))*factorial(q-3)**(q*(q-1))

for q in (3,4,5):
    A,degree=laplacian(q)
    expected=12 if q==3 else predicted(q)
    if q<=4:
        root=exact_det(A)
        count=root
        for d in degree:count*=factorial(d-1)
        assert count==expected
        print('q',q,'exact arborescence',root,'circles',count)
    else:
        for p in (1000000007,1000000009,998244353):
            t=modular_det(A,p)
            prod=1
            for d in degree:prod=prod*factorial(d-1)%p
            assert t*prod%p==expected%p
        print('q=5 three independent modular cofactor checks OK')
print('ARBORESCENCE_VERIFY_OK')
