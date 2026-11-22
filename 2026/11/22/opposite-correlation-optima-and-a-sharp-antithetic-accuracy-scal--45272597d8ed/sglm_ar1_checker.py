"""Independent exact-rational covariance checks for an AR(1)-oracle SGLM oscillator."""
from fractions import Fraction as F

def linear(A,b):
    m=[list(map(F,row))+[F(y)] for row,y in zip(A,b)]
    n=len(b)
    for j in range(n):
        k=next(k for k in range(j,n) if m[k][j]);m[k],m[j]=m[j],m[k]
        q=m[j][j];m[j]=[x/q for x in m[j]]
        for k in range(n):
            if k!=j:
                q=m[k][j]
                m[k]=[x-q*y for x,y in zip(m[k],m[j])]
    return [row[-1] for row in m]

def covariance(k,h,sig2,rho):
    r=1-k*h
    # A is the transition matrix for (Z, oracle error, thermal noise).
    # t = sqrt(h/2) is irrational in general; use rescaled thermal state u=t*chi.
    t2=h/2
    A=[[r,-h,1],[F(0),rho,F(0)],[F(0),F(0),F(0)]]
    Q=[[t2,F(0),t2],[F(0),sig2*(1-rho*rho),F(0)],[t2,F(0),t2]]
    # rescaled third coordinate u=t*chi; innovation u appears both as Z and u.
    M=[]; b=[]
    for i in range(3):
        for j in range(3):
            M.append([F(int(i==a and j==b))-A[i][a]*A[j][b] for a in range(3) for b in range(3)])
            b.append(Q[i][j])
    x=linear(M,b)
    P=[x[3*i:3*i+3] for i in range(3)]
    # Long-run variance is first diagonal of (I-A)^-1 Q (I-A')^-1.
    # first row v of (I-A)^-1 solved as (I-A)' v = e_0.
    v=linear([[F(int(i==j))-A[j][i] for j in range(3)] for i in range(3)], [F(1),F(0),F(0)])
    lrv=sum(v[i]*Q[i][j]*v[j] for i in range(3) for j in range(3))
    return P,lrv

def formula(k,h,sig2,rho):
    r=1-k*h
    return (1/k+h*h*sig2/(1-r*r)*(1+r*rho)/(1-r*rho),F(2)/(k*k*h)+sig2/(k*k)*(1+rho)/(1-rho))

checks=0
for k in [F(1,2),F(1),F(2),F(5,3)]:
    for a in [F(1,5),F(1,2),F(1),F(3,2),F(19,10)]:
        h=a/k
        for sig2 in [F(1,7),F(1),F(7,3)]:
            for rho in [F(-99,100),F(-3,4),F(-1,2),F(0),F(1,3),F(2,3),F(99,100)]:
                P,L=covariance(k,h,sig2,rho)
                V,L0=formula(k,h,sig2,rho)
                assert P[0][0]==V and L==L0
                r=1-k*h
                assert P[1][1]==sig2 and P[0][1]==-h*rho*sig2/(1-r*rho)
                assert P[0][2]==h/2 and P[1][2]==0
                assert V>1/k and L>0
                checks+=6
assert formula(F(1),F(3,2),F(1),F(1,2)) == (F(14,5),F(13,3))
assert formula(F(1),F(3,2),F(1),F(-1,2)) == (F(6),F(5,3))
checks+=2
# Exact small-step criterion check on 1/h integer sequences, rho=-1+c*h.
for k in [F(1,2),F(1),F(2)]:
    for c in [F(0),F(1,4),F(1),F(4)]:
        if c == 0: continue # rho=-1 not allowed; asymptotics handled analytically.
        for n in [16,32,64,128,256]:
            h=F(1,n)
            rho=-1+c*h
            if not (-1<rho<1):continue
            V,L=formula(k,h,F(1),rho)
            asym=F(k+c,4*k)
            assert abs((V-1/k)/h**2-asym) <= F(1,3)
            checks+=1
print(f"VERIFY_OK {checks} assertions, exact rational Lyapunov and Green-Kubo comparisons")
