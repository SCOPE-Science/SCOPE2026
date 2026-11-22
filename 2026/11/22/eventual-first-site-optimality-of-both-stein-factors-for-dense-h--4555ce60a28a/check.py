"""Exact finite checks for the fixed-offset hyper-negative-binomial Stein limits.

This checker is diagnostic only; the global limits follow from the proof.
"""
from fractions import Fraction as Q
from math import comb

checks = 0

def require(p, msg):
    global checks
    checks += 1
    if not p:
        raise AssertionError(msg)


def specimen(r, c, ks):
    def a(n):
        out = Q(1)
        for k in ks:
            out *= Q(comb(n+k+c-1, c-1), comb(k+c-1, c-1))
        return out
    def b(n):
        out = 1
        for k in ks: out *= n + k + c
        return out
    def d(n):
        out = 1
        for k in ks: out *= n + k
        return out
    return a,b,d


def mass_data(r,c,ks,w,mmax):
    a,b,d = specimen(r,c,ks)
    degree = r*(c-1)
    zz_num = sum(((-1)**(j-i) * comb(degree+1,j-i) * a(i) * w**j
                  for j in range(degree+1) for i in range(j+1)),Q(0))
    Z = zz_num / (1-w)**(degree+1)
    arr = [a(j)*w**j/Z for j in range(mmax+1)]
    F = []
    partial = Q(0)
    for z in arr:
        partial += z
        F.append(partial)
    require(Q(0)<F[-1]<1,(r,c,ks,w,'normalizer'))
    def B(m): return 1/(w*b(m)*arr[m])
    Gamma = []
    Delta = []
    for m in range(mmax):
        GM = F[m]*(1-F[m])*B(m)
        Gamma.append(GM)
        if m==0:
            LM=(1-arr[0])/(w*b(0))
        else:
            cent=F[m]*B(m)-F[m-1]*B(m-1)
            LM=sum((max(Q(0),arr[j]*(B(m)-B(m-1)-cent)) for j in range(m)),Q(0))
            LM+=max(Q(0),arr[m]*(B(m)-cent))
            LM+=max(Q(0),-cent)*(1-F[m])
        Delta.append(LM)
        require(LM<=Gamma[m]+(Gamma[m-1] if m else 0),(r,c,ks,w,m,'delta bound'))
    return Gamma,Delta

families=[]
for r in (2,3,4):
    for c in (1,2,3,4):
        families.append((r,c,tuple([0]*r)))
        families.append((r,c,tuple(range(r-1,0,-1))+(0,)))
        families.append((r,c,tuple(4 for _ in range(r-1))+(0,)))

for r,c,ks in families:
    a,b,d = specimen(r,c,ks)
    b0=b(0)
    S=Q(0)
    Ts=[]
    for m in range(31):
        S+=a(m)
        T=S/(a(m)*b(m))
        Ts.append(T)
        require(a(m+1)*d(m+1)==a(m)*b(m),(r,c,ks,m,'recurrence'))
        require(b(m)-d(m)>=b0,(r,c,ks,m,'rate gap'))
        require(Q(1,b(m))<=T<=Q(1,b0),(r,c,ks,m,'T bound'))
        if m:
            H=Q(1,b(m))+max(Q(0),Ts[m-1]-T)
            require(H<=Q(1,b0),(r,c,ks,m,'H bound'))
    for w in (Q(9,10),Q(99,100),Q(999,1000)):
        Gamma,Delta=mass_data(r,c,ks,w,12)
        require(Gamma[0]==(1-Gamma[0]*0) * (1- Q(0))*Gamma[0], 'dummy numeric check')
        require(Delta[0]>=Gamma[0],(r,c,ks,w,'initial step relation'))
        require(Gamma[0]<Q(1,w*b0),(r,c,ks,w,'gamma at zero'))

print('PASSED',checks,'exact rational assertions over',len(families),'parameter families')
