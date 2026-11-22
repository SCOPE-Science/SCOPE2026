from fractions import Fraction as F
from itertools import product
from math import prod

def shared_cherries(pp,qq):
    n=len(pp)+1
    def get(x):
        leaves={i for i in range(2,n+1) if i not in x}
        return {(i,j) for i in leaves for j in leaves if i<j and x[i-2]==x[j-2]}
    return len(get(pp)&get(qq))

def model_exact(n,r):
    r=F(r)
    out=F(0)
    for i in range(2,n):
        for j in range(i+1,n+1):
            a,b=i-1,j-1
            t=r*r/b+r*(1-r)/(a*b)+(1-r)/(b*b)
            u=prod([r*(1-F(1,k-1))+(1-r)*(1-F(1,k-1))**2 for k in range(i+1,j)],start=F(1))
            v=prod([r*(1-F(2,k-1))+(1-r)*(1-F(2,k-1))**2 for k in range(j+1,n+1)],start=F(1))
            out+=t*u*v
    return out

def enumerate_exact(n,r):
    histories=list(product(*[range(1,j) for j in range(2,n+1)]))
    m=F(0)
    for p in histories:
        for q in histories:
            pr=F(1)
            for j in range(2,n+1):
                a,b=p[j-2],q[j-2]; d=j-1
                pr*=r*(F(int(a==b),d))+(1-r)*F(1,d*d)
            m+=pr*shared_cherries(p,q)
    return m

def asymptotic_float(n,r):
    # O(n^2) exact summation with precomputed backwards v product and running u
    vp=[1.]*(n+2)
    for j in range(n-1,1,-1):
        d=j; fac=r*(1-2/d)+(1-r)*(1-2/d)**2
        vp[j]=vp[j+1]*fac
    total=0.
    for i in range(2,n):
        u=1.
        a=i-1
        for j in range(i+1,n+1):
            b=j-1
            t=r*r/b+r*(1-r)/(a*b)+(1-r)/b**2
            total+=t*u*vp[j]
            if j<n:
                d=j; u*=r*(1-1/d)+(1-r)*(1-1/d)**2
    return total

if __name__=='__main__':
    checks=0
    for n in range(3,7):
        for r in (F(0),F(1,4),F(1,2),F(1)):
            v=enumerate_exact(n,r); w=model_exact(n,r)
            assert v==w, (n,r,v,w)
            checks+=1
    for n in range(3,20):
        assert model_exact(n,F(0))==sum((n-i)*(i-1)**2 for i in range(2,n))/F((n-1)**2*(n-2)**2),n
        assert model_exact(n,F(1))==F(n,6), n
        checks+=2
    for r in (0.2,0.5,0.9,1.):
        n=1500; val=asymptotic_float(n,r)/n
        tgt=r*r/((3-r)*(5-2*r))
        assert abs(val-tgt)<0.002, (r,val,tgt)
        checks+=1
    for L in (0.,0.5,2.):
        n=2500; val=asymptotic_float(n,L/n**0.5)
        tgt=1/12+L**2/15
        assert abs(val-tgt)<0.07,(L,val,tgt)
        checks+=1
    print('PASS',checks,'grouped exact and asymptotic assertions')
    for L in (0,0.5,2):
        n=2500; print('critical',L,asymptotic_float(n,L/n**0.5),1/12+L*L/15)

def model_mismatch(n,r):
    r=F(r)
    out=F(0)
    for i in range(2,n):
        for j in range(i+1,n+1):
            a,b=i-1,j-1
            t=F(a-1,a)*(1-r)**2/F(b*b)
            u=prod([r*(1-F(1,k-1))+(1-r)*(1-F(1,k-1))**2 for k in range(i+1,j)],start=F(1))
            v=prod([r*(1-F(2,k-1))+(1-r)*(1-F(2,k-1))**2 for k in range(j+1,n+1)],start=F(1))
            out+=t*u*v
    return out

def enumerate_mismatch(n,r):
    histories=list(product(*[range(1,j) for j in range(2,n+1)]))
    ans=F(0)
    for p in histories:
        leaves_p={i for i in range(2,n+1) if i not in p}
        ch_p={(i,j) for i in leaves_p for j in leaves_p if i<j and p[i-2]==p[j-2]}
        for q in histories:
            pr=F(1)
            for j in range(2,n+1):
                a,b=p[j-2],q[j-2]; d=j-1
                pr*=r*(F(int(a==b),d))+(1-r)*F(1,d*d)
            leaves_q={i for i in range(2,n+1) if i not in q}
            ch_q={(i,j) for i in leaves_q for j in leaves_q if i<j and q[i-2]==q[j-2]}
            ans+=pr*sum(p[i-2]!=q[i-2] for i,j in ch_p & ch_q)
    return ans

def mismatch_float(n,r):
    vp=[1.]*(n+2)
    for j in range(n-1,1,-1):
        d=j; vp[j]=vp[j+1]*(r*(1-2/d)+(1-r)*(1-2/d)**2)
    total=0.
    for i in range(2,n):
        u=1.; a=i-1
        for j in range(i+1,n+1):
            b=j-1
            total+=(1-1/a)*(1-r)**2/b**2*u*vp[j]
            if j<n:
                d=j; u*=r*(1-1/d)+(1-r)*(1-1/d)**2
    return total

if __name__=='__main__':
    check=0
    for n in range(3,7):
        for r in (F(0),F(1,4),F(1,2),F(1)):
            assert model_mismatch(n,r)==enumerate_mismatch(n,r)
            check+=1
    for r in (0.,.25,.5,.8,1.):
        target=(1-r)**2/((3-r)*(4-2*r))
        got=mismatch_float(2200,r)
        print('mismatch',r,got,target)
        assert abs(got-target)<0.002
        check+=1
    print('PASS',check,'extra mismatch checks')
