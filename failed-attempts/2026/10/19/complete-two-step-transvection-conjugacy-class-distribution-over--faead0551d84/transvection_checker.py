"""Exact verification of two-transvection conjugacy-class counts over prime fields.
Run: python3 transvection_checker.py. No external libraries required.
"""
from itertools import product
from collections import Counter

def matmul(A,B,n,p):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%p for i in range(n) for j in range(n))

def rank(A,n,p):
    a=[list(A[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for j in range(n):
        z=next((i for i in range(r,n) if a[i][j]%p), None)
        if z is None: continue
        a[r],a[z]=a[z],a[r]
        t=pow(a[r][j],-1,p);a[r]=[(t*u)%p for u in a[r]]
        for k in range(r+1,n):
            t=a[k][j];a[k]=[(a[k][h]-t*a[r][h])%p for h in range(n)]
        r+=1
    return r

def transvections(n,p):
    ts=[]
    vectors=[x for x in product(range(p),repeat=n) if any(x)]
    for b in vectors:
        last=max(i for i in range(n) if b[i]);
        if b[last]!=1:continue
        for a in vectors:
            if sum(a[i]*b[i] for i in range(n))%p==0:
                ts.append(tuple((int(i==j)+b[i]*a[j])%p for i in range(n) for j in range(n)))
    assert len(set(ts))==len(ts)
    return ts

def label(M,n,p):
    D=tuple((M[i*n+j]-int(i==j))%p for i in range(n) for j in range(n))
    c=sum(D[i*n+i] for i in range(n))%p
    if c:
        assert rank(D,n,p)==2
        return ('c',c)
    D2=matmul(D,D,n,p)
    if any(D2):
        assert rank(D,n,p)==2 and rank(D2,n,p)==1
        return ('J3',)
    r=rank(D,n,p)
    assert r in (0,1,2)
    return ('J'+str(r),)

def expect(n,p):
    T=(p**n-1)*(p**(n-1)-1)//(p-1)
    d={('J0',):1, ('J1',):2*p**(n-1)-p-2,
       ('J3',):2*(p**(2*n-3)-p**(n-1)),
       ('J2',):((p**(n-1)-1)//(p-1)-1)*(p**(n-2)-p)}
    for c in range(1,p):d[('c',c)]=p**(2*n-3)
    assert sum(d.values())==T,(n,p,d,T)
    return T,d

def test(n,p,allpairs=False):
    arr=transvections(n,p)
    T,exp=expect(n,p)
    assert len(arr)==T
    base=arr[0]
    I=tuple(int(i==j) for i in range(n) for j in range(n))
    observed=Counter(label(matmul(base,b,n,p),n,p) for b in arr)
    assert observed==Counter({k:v for k,v in exp.items() if v}), (n,p,observed,exp)
    if allpairs:
        c=Counter(label(matmul(a,b,n,p),n,p) for a in arr for b in arr)
        assert c==Counter({k:v*T for k,v in exp.items() if v}), (n,p,c,exp)
    print('PASS',n,p,'transvections',T,'fixed-fiber',dict(observed),'allpairs',allpairs)

if __name__=='__main__':
    for n,p,allpairs in ((2,2,True),(2,3,True),(2,5,True),(3,2,True),(3,3,True),(3,5,False),(4,2,True),(4,3,False),(5,2,False)):
        test(n,p,allpairs)
    print('ALL_EXACT_CHECKS_PASSED 9')
