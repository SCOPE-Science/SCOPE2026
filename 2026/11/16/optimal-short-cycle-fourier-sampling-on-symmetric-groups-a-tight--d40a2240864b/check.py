"""Reproducible finite tests for short-permutation standard-Fourier sampling.
No numerical test is used as a proof of the all-n formulas.
Requires numpy (only Python stdlib is otherwise used).
"""
from fractions import Fraction as F
from itertools import combinations, permutations
import numpy as np

def spectrum(n,f,t):
    l0=F((f-1)**2,n-1)
    lv=F(f*(n-f),(n-1)*(n-2))
    lu=F(n-f-2*t,(n-1)*(n-2))
    lw=(F(n+f+2*t-2,2)-l0-(n-1)*lv)/F(n*(n-3),2)
    return np.array([float(q) for q in (l0,lv,lw,lu)])

def perm_class(n,shape):
    # Entire symmetric group is enumerated for n <= 6 only.
    for p in permutations(range(n)):
        vis=set(); lengths=[]
        for i in range(n):
            if i not in vis:
                j=i;k=0
                while j not in vis:
                    vis.add(j);j=p[j];k+=1
                lengths.append(k)
        if tuple(sorted((k for k in lengths if k>1),reverse=True))==shape:
            yield p

def matrix_for(n,shape):
    ps=list(perm_class(n,shape))
    P=np.eye(n)-np.ones((n,n))/n
    cols=[]
    for p in ps:
        X=np.zeros((n,n))
        for j,i in enumerate(p):X[i,j]=1.
        cols.append((X-P*0-np.ones((n,n))/n).reshape(-1))
    C=np.stack(cols)
    return C.T@C/len(C),len(C)

classes=[('id',(),lambda n:(n,0)),('T',(2,),lambda n:(n-2,1)),('C3',(3,),lambda n:(n-3,0)),('D22',(2,2),lambda n:(n-4,2)),('C4',(4,),lambda n:(n-4,0))]
for n in (4,5,6):
    mats={}
    for name,shape,ft in classes:
        M,k=matrix_for(n,shape)
        f,t=ft(n)
        expected=spectrum(n,f,t)
        eig=np.linalg.eigvalsh(M)
        positive=sorted([*([expected[0]]),*([expected[1]]*(n-1)),*([expected[2]]*(n*(n-3)//2)),*([expected[3]]*((n-1)*(n-2)//2))])
        actual=sorted(eig)[-len(positive):]
        assert np.max(np.abs(np.array(actual)-np.array(positive)))<1e-9,(n,name,actual,positive)
        mats[name]=M
    if n==4: weights={'T':.5,'C4':.5}; target=1.
    elif n==5:weights={'id':F(1,13),'D22':F(36,143),'C4':F(96,143)}; target=F(11,8)
    else:weights={'D22':F(5,19),'C4':F(14,19)};target=F(19,7)
    S=sum(float(w)*mats[key] for key,w in weights.items())
    ev=np.linalg.eigvalsh(S);nonzero=ev[-(n-1)**2:]
    assert min(nonzero)>1e-9
    assert abs(max(nonzero)/min(nonzero)-float(target))<1e-9,(n,nonzero,target)
    print(f'n={n} verified all 5 exact class formula predictions, best witness ratio={target}')
for n in range(7,101):
    x=F(2*n-7,n*n-3*n+1); y=1-x
    lo=x*spectrum(n,n-4,2)+y*spectrum(n,n-4,0)
    val=float(F((n-5)**2*(n-2)*(n*n-3*n+1),4*(n*n-5*n+8)))
    assert abs(max(lo)/min(lo)-val)<1e-9
print('SHORT_PERMUTATION_FOURIER_OPTIMUM_CHECK_PASS')
