"""Finite rational and numerical checks of complete-network entropy production lifting.
Run: python3 check_lift.py. Uses only the Python standard library.
"""
from fractions import Fraction as F
import math
import random

Q = ((0,1,20),(19,0,6),(1,4,0))
pi = (F(101,692),F(85,692),F(506,692))
trial = (F(9,100),F(7,100),F(84,100))

def rate(p):
    return sum((float(p[i])*Q[i][j]-float(p[j])*Q[j][i])*math.log(float(p[i])*Q[i][j]/(float(p[j])*Q[j][i])) for i in range(3) for j in range(i+1,3))

def log_bounds(x, terms=32):
    """Rigorous rational enclosures for log positive rational x."""
    x = F(x)
    assert x>0
    y=x; shift=0
    while y<F(1):
        y*=2;shift-=1
    while y>=2:
        y/=2;shift+=1
    def norm_bounds(z):
        s=F(0)
        for k in range(terms):
            s += 2*z**(2*k+1)/F(2*k+1)
        extra= 2*z**(2*terms+1)/F((2*terms+1)) / (1-z*z)
        return s, s+extra
    lo,hi=norm_bounds((y-1)/(y+1))
    two_lo,two_hi=norm_bounds(F(1,3))
    if shift>=0:
        return lo+shift*two_lo, hi+shift*two_hi
    return lo+shift*two_hi,hi+shift*two_lo

def ep_bounds(p):
    lo=hi=F(0)
    for i in range(3):
        for j in range(i+1,3):
            a=p[i]*Q[i][j]
            b=p[j]*Q[j][i]
            diff=a-b
            xlo,xhi=log_bounds(a/b)
            if diff>=0: lo+=diff*xlo;hi+=diff*xhi
            else: lo+=diff*xhi;hi+=diff*xlo
    return lo,hi

def epr_kn(p,n,c=F(1,1)):
    def rate_of(i,a,j,b):
        return F(Q[i][j],n) if i!=j else c/n
    v=0.
    N=3*n
    for z in range(N):
        for w in range(z+1,N):
            i,a=divmod(z,n);j,b=divmod(w,n)
            x=float(p[z]*rate_of(i,a,j,b))
            y=float(p[w]*rate_of(j,b,i,a))
            v+=(x-y)*math.log(x/y)
    return v

def decomp(p,n,c=F(1,1)):
    P=[sum(p[i*n:(i+1)*n]) for i in range(3)]
    m=[ [float(p[i*n+a]/P[i]) for a in range(n)] for i in range(3)]
    base=rate(P)
    correction=0.
    for i in range(3):
        outward=float(P[i]*(c+sum(Q[i][j] for j in range(3) if j!=i)))
        inward=float(c*P[i]+sum(P[j]*Q[j][i] for j in range(3) if j!=i))
        du=sum(y*math.log(n*y) for y in m[i])
        ud=sum(-math.log(n*y)/n for y in m[i])
        correction+=outward*du+inward*ud
    return base+correction,base,correction

def weighted_micro_rate(p,nu,c):
    n=len(nu[0]); total=0.0
    for z in range(3*n):
        for w in range(z+1,3*n):
            i,a=divmod(z,n);j,b=divmod(w,n)
            if i==j:
                x=float(p[z]*c[i]*nu[i][b]);y=float(p[w]*c[i]*nu[i][a])
            else:
                x=float(p[z]*Q[i][j]*nu[j][b]);y=float(p[w]*Q[j][i]*nu[i][a])
            total+=(x-y)*math.log(x/y)
    return total

def weighted_decomposition(p,nu,c):
    n=len(nu[0]); P=[sum(p[i*n:(i+1)*n]) for i in range(3)]
    val=rate(P)
    for i in range(3):
        mu=[float(p[i*n+a]/P[i]) for a in range(n)]
        u=[float(v) for v in nu[i]]
        forward=sum(a*math.log(a/b) for a,b in zip(mu,u))
        backward=sum(b*math.log(b/a) for a,b in zip(mu,u))
        out=float(P[i]*(c[i]+sum(Q[i][j] for j in range(3) if i!=j)))
        inc=float(P[i]*c[i]+sum(P[j]*Q[j][i] for j in range(3) if j!=i))
        val+=out*forward+inc*backward
    return val

def checks():
    assert sum(pi)==1 and sum(trial)==1
    for j in range(3):
        assert sum(pi[i]*Q[i][j] for i in range(3) if i!=j)==pi[j]*sum(Q[j][k] for k in range(3) if j!=k)
    lpi,upi=ep_bounds(pi)
    ltr,utr=ep_bounds(trial)
    assert ltr>0
    assert 50*lpi>59*utr
    print('EXACT rational certificate: 50 sigma(pi)>59 sigma(trial), with 32-term rigorous logarithmic bounds; margin lower:',float(50*lpi-59*utr))
    print('Stationary EPR',rate(pi),'Trial EPR',rate(trial),'ratio lower via trial',rate(pi)/rate(trial)-1)
    count=0
    rng=random.Random(14159)
    for n in (1,2,3,5,8):
        for c in (F(1,10),F(1),F(7)):
            unif=[pi[i]/n for i in range(3) for a in range(n)]
            assert abs(epr_kn(unif,n,c)-rate(pi))<1e-11
            for i in range(3):
                for a in range(n):
                    v=sum(unif[j*n+b]*F(Q[j][i],n) for j in range(3) if j!=i for b in range(n))
                    v+=sum(unif[i*n+b]*c/n for b in range(n) if b!=a)
                    out=unif[i*n+a]*(sum(Q[i][j] for j in range(3) if j!=i)+c*F(n-1,n))
                    assert v==out
                    count+=1
            for rep in range(8):
                draws=[F(rng.randint(1,100),1) for _ in range(3*n)]
                p=[x/sum(draws) for x in draws]
                exact_epr=epr_kn(p,n,c)
                dec,base,penalty=decomp(p,n,c)
                assert abs(exact_epr-dec)<3e-10*max(1,abs(exact_epr)),(n,c,rep,exact_epr,dec)
                assert penalty>=-1e-10 and exact_epr>=base-1e-9
                count+=1
    for n in (2,3,5,8):
        nu=[ [F((i+2)**(a+1), sum((i+2)**(b+1) for b in range(n))) for a in range(n)] for i in range(3)]
        c=(F(2),F(3,2),F(5,2))
        stationary=[pi[i]*nu[i][a] for i in range(3) for a in range(n)]
        assert abs(weighted_micro_rate(stationary,nu,c)-rate(pi))<1e-10
        for i in range(3):
            for a in range(n):
                incoming=sum(stationary[j*n+b]*Q[j][i]*nu[i][a] for j in range(3) if j!=i for b in range(n))
                incoming+=sum(stationary[i*n+b]*c[i]*nu[i][a] for b in range(n) if b!=a)
                outgoing=stationary[i*n+a]*(sum(Q[i][j] for j in range(3) if i!=j)+c[i]*(1-nu[i][a]))
                assert incoming==outgoing
                count+=1
        for rep in range(10):
            draws=[F(rng.randint(1,120)) for _ in range(3*n)]
            p=[x/sum(draws) for x in draws]
            direct=weighted_micro_rate(p,nu,c)
            reduced=weighted_decomposition(p,nu,c)
            assert abs(direct-reduced)<1e-9*max(1,abs(direct)),(n,rep,direct,reduced)
            count+=1
    print('PASSED stationarity, both symmetric and nonuniform weighted exact EPR decompositions and min-reduction witness:',count,'tests')

if __name__=='__main__':
    checks()
