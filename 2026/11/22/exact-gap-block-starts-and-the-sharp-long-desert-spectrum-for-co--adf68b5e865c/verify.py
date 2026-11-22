from heapq import heappush, heappop

def ap(n):
    a=n*(n+1)//2; vs=[(n+1)*(n+2)//2,(n+2)*(n+3)//2]
    D=[10**30]*a;D[0]=0;hp=[(0,0)]
    while hp:
        z,r=heappop(hp)
        if D[r]!=z:continue
        for v in vs:
            z1=z+v;r1=(r+v)%a
            if z1<D[r1]:D[r1]=z1;heappush(hp,(z1,r1))
    return D

def predicted(n):
    a=n*(n+1)//2;b=(n+1)*(n+2)//2;c=(n+2)*(n+3)//2
    if n%2==0:d=n+1;A=n//2;B=A+1;C=A+2;H=A
    else:d=(n+1)//2;A=n;B=A+2;C=A+4;H=A+1
    assert a==d*A and b==d*B and c==d*C+1
    invB=pow(B,-1,A)
    values=[]; starts=[]
    for r in range(a):
        t,ell=divmod(r,d)
        j=((t-ell*C)*invB)%A
        w=j*b+ell*c
        assert (w-r)%a==0
        values.append(w)
    for r in range(a-1):
        k0=(values[r]-r)//a;k1=(values[r+1]-(r+1))//a
        if k1>k0:
            assert r%d<d-1 and ((values[r]-((r%d)*c))//b) in (0,1)
            assert k1-k0==H
            for h in range(k0,k1): starts.append(r+1+h*a)
    return values,sorted(starts),H

def actual_starts(D):
    a=len(D)
    # For every represented s=r+ka, s+1 absent, compare columns without materializing gaps
    starts=[]
    for r in range(a-1):
        k0=(D[r]-r)//a;k1=(D[r+1]-r-1)//a
        for h in range(k0,k1):starts.append(r+1+h*a)
    return sorted(starts)

def all_gaps(n,D):
    a=len(D);F=max(D)-a
    starts=[];end=[];last=False
    for s in range(1,F+1):
        gap=s<D[s%a]
        if gap and not last:starts.append(s)
        if not gap and last:end.append(s-1)
        last=gap
    if last:end.append(F)
    return list(zip(starts,end))

if __name__=='__main__':
    gc=0;full=0
    for n in range(3,121):
        D=ap(n);p,starts,H=predicted(n)
        assert p==D,(n,'aper')
        aa=actual_starts(D)
        assert starts==aa,(n,'starts')
        assert len(starts)==(n*n if n%2==0 else n*n-1),(n,'total',len(starts))
        gc+=len(starts)
        if n<=60:
            runs=all_gaps(n,D); full+=len(runs)
            assert [s for s,e in runs]==starts,(n,'full starts')
            u=n+1;a=n*(n+1)//2;c=(n+2)*(n+3)//2
            long=[(s,e) for s,e in runs if e-s+1>u]
            K=(n+1)//4
            expect=[(q*c+1,(q+1)*a-1) for q in range(K)]
            assert long==expect,(n,'long',long,expect)
            # Independently generate by direct membership DP, not only Apéry threshold.
            if n<=28:
                F=max(D)-a; V=[False]*(F+1);V[0]=True
                for x in range(1,F+1):
                    V[x]=any(x>=v and V[x-v] for v in [a,(n+1)*(n+2)//2,c])
                assert all(V[x]==(x>=D[x%a]) for x in range(F+1)),(n,'DP')
    print('VERIFY_OK n=3..120; Apéry entries and all starts checked:',gc,'; full runs n=3..60:',full,'; independent DP n=3..28')
