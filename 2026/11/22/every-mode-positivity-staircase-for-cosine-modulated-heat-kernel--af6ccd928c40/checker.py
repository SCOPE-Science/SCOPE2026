"""Numerical regression checks for the finite-cycle heat modulation staircase.
No assertion substitutes for the analytic proof in RESULT.md.
"""
import math

def lf(n,N,t):
    h=2*math.pi/N
    c=math.cos(n*h); s=math.sin(n*h)
    u=2*t*(1-math.cos(h)); v=2*t*math.sin(h)
    x=v*s
    return -u*c+abs(x)+math.log1p(math.exp(-2*abs(x)))-math.log(2)

def diff(n,N,t): return lf(n,N,t)-lf(n+1,N,t)

def root(n,N):
    low,hi=1e-9,1.
    assert diff(n,N,low)<0,(N,n)
    while diff(n,N,hi)<=0:
       hi*=2
       assert hi <1e9,(N,n)
    for _ in range(100):
       mid=(low+hi)/2
       if diff(n,N,mid)>0: hi=mid
       else: low=mid
    return (low+hi)/2

assertions=0
for N in range(3,201):
 M=N//2; J=N//4+1
 roots={n:root(n,N) for n in range(J,M)}
 r=[roots[n] for n in range(M-1,J-1,-1)]
 assert all(r[i]<r[i+1] for i in range(len(r)-1)),(N,r);assertions+=1
 probe=[1e-6,0.05,0.25,1.,2.,10.]+r
 for t in probe:
    values=[lf(n,N,t) for n in range(M+1)]
    mx=max(range(M+1),key=lambda n:values[n]); assert (J <= mx<=M) or (N%4==0 and mx==J-1 and abs(values[J]-values[J-1])<2e-12),(N,t,mx,J,M);assertions+=1
    for n in range(J,M):
       if abs(t-roots[n])>1e-6:
        assert (diff(n,N,t)>0)==(t>roots[n]),(N,n,t); assertions+=1
    # All tested levels have a discrete maximizer that is either the expected phase or its tied neighbor.
    exp=M-sum(t>roots[n] for n in roots)
    assert mx in (exp, exp-1) or (N%4==0 and mx==J-1 and abs(values[J]-values[J-1])<2e-12), (N,t,mx,exp);assertions+=1
print('CHECKS PASSED',assertions,'N=3..200')
for N in (6,7,8,9,10,11,12,16,24):
 J=N//4+1;M=N//2
 print(N,'J,M',J,M,'critical times',[(j,round(root(j,N),7)) for j in range(M-1,J-1,-1)])

# Independent direct cyclic-DFT check of the sharp matrix threshold.
for N in range(3,26):
    h=2*math.pi/N
    for t in (0.07,0.3,0.8,2.0):
        a=[math.exp(-2*t*(1-math.cos(k*h))) for k in range(N)]
        H=[sum(a[k]*math.cos(k*h*x) for k in range(N))/N for x in range(N)]
        f=[(a[(k-1)%N]+a[(k+1)%N])/(2*a[k]) for k in range(N)]
        beta=-1/max(f)
        for bb in (beta, beta+0.05, beta-0.05):
            eig=[sum(H[x]*(1+bb*math.cos(h*x))*math.cos(k*h*x) for x in range(N)) for k in range(N)]
            pred=[a[k]*(1+bb*f[k]) for k in range(N)]
            assert max(abs(eig[k]-pred[k]) for k in range(N))<3e-12,(N,t,bb)
            if bb==beta:
                assert min(eig)>=-1e-12
                assert min(abs(w) for w in eig)<1e-10
            elif bb>beta:
                assert min(eig)>0
            else:
                assert min(eig)<-1e-13
            assertions+=N+2
print('TOTAL CHECKS PASSED', assertions)
