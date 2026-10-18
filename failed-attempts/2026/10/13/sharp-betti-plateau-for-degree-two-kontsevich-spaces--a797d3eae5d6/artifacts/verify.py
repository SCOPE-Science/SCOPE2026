from math import floor

def conv(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return z

def poly(n):
    # (1-q^(n+1))/(1-q) times (1-q^n)(1-q^(n-1))/((1-q)(1-q^2));
    # exact long division of numerator by denominator.
    num=[1]
    for e in (n+1,n,n-1):
        f=[0]*(e+1); f[0]=1; f[e]=-1
        num=conv(num,f)
    den=conv([1,-2,1],[1,0,-1])
    out=[0]*(3*n-3)
    rem=num[:]
    for k in range(len(out)):
        out[k]=rem[k]
        if out[k]:
            for j,d in enumerate(den):
                if k+j<len(rem): rem[k+j]-=out[k]*d
    assert all(x==0 for x in rem[len(out):])
    return out

def c(j): return j//2+1 if j>=0 else 0

checks=0
for n in range(2,301):
    a=poly(n)
    assert len(a)==3*n-3
    assert a==a[::-1]
    M=max(a)
    assert M==floor(3*n*n/8)
    inds=[k for k,x in enumerate(a) if x==M]
    if n%2:
        want=[(3*n-5)//2,(3*n-3)//2]
    elif n%4==0:
        want=[(3*n-4)//2]
    else:
        want=[(3*n-6)//2,(3*n-4)//2,(3*n-2)//2]
    assert inds==want,(n,inds,want)
    lo,hi=inds[0],inds[-1]
    assert all(a[k]<a[k+1] for k in range(lo))
    assert all(a[k]>a[k+1] for k in range(hi,len(a)-1))
    d=[a[0]]+[a[k]-a[k-1] for k in range(1,len(a))]
    for k in range(min(2*n-1,len(d))):
        assert d[k]==c(k)-c(k-n+1)-c(k-n)-c(k-n-1)
    checks+=1
print('VERIFY_OK',checks)
