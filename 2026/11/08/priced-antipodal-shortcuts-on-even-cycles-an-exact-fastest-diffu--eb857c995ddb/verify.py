"""Reproducible finite checks for a priced antipodal-cycle spectral-gap theorem.

Run: python3 verify.py
Only the Python standard library is needed. Numerical checks do not prove the
all-size theorem; the proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import sin, pi, cos, isclose
from random import Random

checks = 0

def require(condition, msg):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(msg)

def laplacian(m, rails, chords):
    n = 2*m
    A = [[0.0]*n for _ in range(n)]
    def edge(u,v,w):
        A[u][u] += float(w)
        A[v][v] += float(w)
        A[u][v] -= float(w)
        A[v][u] -= float(w)
    for j,w in enumerate(rails): edge(j,(j+1)%n,w)
    for j,w in enumerate(chords): edge(j,j+m,w)
    return A

def jacobi_eigenvalues(A):
    n = len(A)
    A = [row[:] for row in A]
    for _ in range(45*n*n):
        p,q = max(((i,j) for i in range(n) for j in range(i+1,n)),
                   key=lambda ij: abs(A[ij[0]][ij[1]]))
        v = A[p][q]
        if abs(v) < 3e-13:
            return sorted(A[i][i] for i in range(n))
        tau = (A[q][q]-A[p][p])/(2*v)
        t = (1 if tau >= 0 else -1)/(abs(tau)+(1+tau*tau)**0.5)
        cs = 1/(1+t*t)**0.5
        sn = t*cs
        ap,aq = A[p][p],A[q][q]
        A[p][p] = ap-t*v
        A[q][q] = aq+t*v
        A[p][q] = A[q][p] = 0.0
        for i in range(n):
            if i in (p,q): continue
            ip,iq=A[i][p],A[i][q]
            A[i][p]=A[p][i]=cs*ip-sn*iq
            A[i][q]=A[q][i]=sn*ip+cs*iq
    raise RuntimeError('Jacobi iteration did not converge')

def parameters(m,c,B):
    D=4*sin(pi/(2*m))**2
    A=4*sin(pi/m)**2
    cstar=4/D
    if c<cstar:
        a=2*B/(m*(4+c*(A-D)))
        b=B*(A-D)/(m*(4+c*(A-D)))
        gap=A*a
    elif c>cstar:
        a=B/(2*m);b=0.0;gap=D*a
    else:
        a=B/(2*m);b=0.0;gap=D*a
    return a,b,gap,cstar,D,A

# Exact checks in the six-vertex case; every edge coefficient and eigenvector is rational.
def exact_m3(c,B,b):
    a=(B-3*c*b)/6
    rails=[a]*6; chords=[b]*3
    def apply(v):
        r=[F(0)]*6
        for j,w in enumerate(rails):
            k=(j+1)%6; d=w*(v[j]-v[k]); r[j]+=d;r[k]-=d
        for j,w in enumerate(chords):
            k=j+3;d=w*(v[j]-v[k]);r[j]+=d;r[k]-=d
        return r
    modes=[([1,F(1,2),-F(1,2),-1,-F(1,2),F(1,2)],a+2*b),
           ([0,1,1,0,-1,-1],a+2*b),
           ([1,-F(1,2),-F(1,2),1,-F(1,2),-F(1,2)],3*a),
           ([0,1,-1,0,1,-1],3*a),
           ([1,-1,1,-1,1,-1],4*a+2*b)]
    for vector,value in modes:
        vector=list(map(F,vector))
        require(apply(vector)==[value*x for x in vector], 'exact m=3 eigenvector')
    require(6*a+3*c*b==B,'exact budget')
    return min(a+2*b,3*a)

require(exact_m3(F(2),F(30),F(5,2))==F(15,2),'subcritical m=3')
require(exact_m3(F(4),F(30),F(1))==F(5),'critical m=3')
require(exact_m3(F(5),F(30),F(0))==F(5),'supercritical m=3')

rng=Random(11273)
for m in range(3,13):
    for fraction in (0.15,0.7,0.999,1.001,2.0,7.0):
        _,_,_,star,_,_ = parameters(m,1.0,1.0)
        c=star*fraction
        B=0.5+m/4
        a,b,gap,_,D,A=parameters(m,c,B)
        require(a>0 and b>=0,'candidate positivity')
        require(isclose(2*m*a+m*c*b,B,rel_tol=1e-12,abs_tol=1e-12),'budget')
        require(isclose(min(D*a+2*b,A*a),gap,rel_tol=1e-11),'spectral formula')
        eig=jacobi_eigenvalues(laplacian(m,[a]*(2*m),[b]*m))
        require(abs(eig[1]-gap)<2e-9*(1+gap),'full symmetric eigencheck')
        for _ in range(3):
            w=[rng.random()+0.05 for _ in range(3*m)]
            norm=B/(sum(w[:2*m])+c*sum(w[2*m:]))
            rails=[t*norm for t in w[:2*m]]
            chords=[t*norm for t in w[2*m:]]
            eig=jacobi_eigenvalues(laplacian(m,rails,chords))
            mean_a=sum(rails)/(2*m); mean_b=sum(chords)/m
            ray=min(D*mean_a+2*mean_b,A*mean_a)
            require(eig[1]<=ray+2e-9*(1+ray),'two Fourier test-subspace bound')
            require(eig[1]<=gap+2e-9*(1+gap),'unrestricted candidate bound')

for m in (40,80,160,320,640):
    c=2.0;B=1.0
    a,b,gap,star,D,A=parameters(m,c,B)
    frac=m*c*b/B
    cycle=D*B/(2*m)
    require(star>c and b>0,'fixed-price regime')
    require(abs((b/a)*m*m-1.5*pi*pi)<100.0/m,'rung-ratio asymptotics')
    require(abs(frac*m*m-0.75*c*pi*pi)<150.0/m,'budget-fraction asymptotics')
    require(abs(gap/cycle-4)<100/m,'fourfold asymptotic gain')

print('VERIFY_OK', checks)
