"""Reproduce exact two-by-three martingale Sinkhorn half-step identities."""
import math
from fractions import Fraction
from random import Random
import sympy as sp

A,B,T=sp.symbols('a b t', positive=True)
F=(1-B)/(B*(1-A*A))*(A*A*T+sp.sqrt(A*A*T*T+4*(1-A*A)))
root=2*(1-B)/sp.sqrt(B*B-A*A)
rho=A*A*(1-B)/(B*(B-A*A))
L=A*(1-B)/(B*(1-A))
sroot=2*B/sp.sqrt(B*B-A*A)
assert sp.simplify((1-A*A)*sroot*sroot-2*A*A*root*sroot-A*A*root*root-4)==0
assert sp.simplify((1-B)/B*sroot-root)==0
assert sp.simplify((1-B)/B*(A*A*(sroot+root)/(sroot-A*A*(sroot+root)))-rho)==0
assert sp.simplify(1-rho-(B*B-A*A)/(B*(B-A*A)))==0
assert sp.simplify(1-L-(B-A)/(B*(1-A)))==0

rng=Random(20261104)
count=0
for _ in range(350):
    denominator=rng.randint(6,50)
    na=rng.randint(1,denominator-2)
    nb=rng.randint(na+1,denominator-1)
    a,b=float(Fraction(na,denominator)),float(Fraction(nb,denominator))
    t=float(Fraction(rng.randint(1,200),rng.randint(1,20)))
    # projection onto row mass plus martingale constraint
    s=(a*a*t+math.sqrt(a*a*t*t+4*(1-a*a)))/(1-a*a)
    z=(a*t+math.sqrt(a*a*t*t+4*(1-a*a)))/(2*(1-a))
    weights=(1/z,t,z)
    q=[w/sum(weights) for w in weights]
    assert abs(sum(q)-1)<1e-12
    assert abs(q[2]-q[0]-a)<1e-12
    q0=q[1]
    # projection onto prescribed terminal marginal: endpoint/middle multipliers
    t_next=t*((1-b)/q0)/((b/2)/((1-q0)/2))
    mapped=(1-b)/b*s
    assert abs(t_next-mapped)<2e-10*max(1,mapped)
    assert 0<rho.subs({A:a,B:b})<1
    assert 0<L.subs({A:a,B:b})<1
    # random exact check for conditional row: one-step update and q relation
    assert abs(q0-t/(s+t))<1e-12
    count+=1

for a,b in ((0.2,0.6),(0.4,0.7),(0.55,0.8),(0.8,0.9),(0.4,0.4005)):
    c=(1-b)/b
    t=2*(1-b)/b  # dual potentials zero initially
    star=2*(1-b)/math.sqrt(b*b-a*a)
    r=a*a*(1-b)/(b*(b-a*a))
    def entropy(t):
        s=(a*a*t+math.sqrt(a*a*t*t+4*(1-a*a)))/(1-a*a)
        q=t/(s+t)
        p=[(b-a)/2,1-b,(b+a)/2]
        x=[(1-q-a)/2,q,(1-q+a)/2]
        return sum(pp*math.log(pp/xx) for pp,xx in zip(p,x))
    errors=[]
    for k in range(12):
        errors.append(entropy(t))
        t=c*(a*a*t+math.sqrt(a*a*t*t+4*(1-a*a)))/(1-a*a)
    assert t < star + 1e-12 and t > 0
    print('sample',a,b,'rate',r,'dual fixed',star,'first KL',errors[0], 'last KL',errors[-1])
print('EXACT SYMBOLIC and',count,'independent one-step tests passed')

# Endpoint degeneration: the exact boundary has no geometric convergence.
for a in (0.2,0.5,0.8):
    t=2*(1-a)/a
    N=100000
    for j in range(N):
        t=(1-a)/(a*(1-a*a))*(a*a*t+math.sqrt(a*a*t*t+4*(1-a*a)))
    s=(a*a*t+math.sqrt(a*a*t*t+4*(1-a*a)))/(1-a*a)
    q0=t/(t+s)
    qm=(1-q0-a)/2
    qp=qm+a
    KL=(1-a)*math.log((1-a)/q0)+a*math.log(a/qp)
    C= a*(1-a)/4
    assert abs(t/math.sqrt(N)/(2*math.sqrt(1-a)/a)-1)<0.005
    assert abs(N*qm/C-1)<0.005
    assert abs(N*KL/C-1)<0.005
    print('boundary',a,'sqrt-growth',t/math.sqrt(N),'k*qminus',N*qm,'k*KL',N*KL)
print('BOUNDARY and EXACT HALF-STEP identities passed')

# Independent complete 2-by-3 iterative KL projections, without using s(t).
for a,b in ((0.4,0.7),(0.5,0.5),(0.2,0.6)):
    nu=(b/2,1-b,b/2)
    matrix=[[v/2 for v in nu] for _ in range(2)]
    t=2*(1-b)/b
    for cycle in range(20):
        current=[]
        for i,target in enumerate((-a,a)):
            ws=matrix[i]
            def avg(h):
                vals=[ws[j]*math.exp(h*(j-1)) for j in range(3)]
                return (vals[2]-vals[0])/sum(vals)
            lo,hi=-30.,30.
            for _ in range(85):
                m=(lo+hi)/2
                if avg(m)<target: lo=m
                else: hi=m
            h=(lo+hi)/2
            v=[ws[j]*math.exp(h*(j-1)) for j in range(3)]
            current.append([q/(2*sum(v)) for q in v])
        q0=2*current[1][1]
        st=(a*a*t+math.sqrt(a*a*t*t+4*(1-a*a)))/(1-a*a)
        expected_q0=t/(t+st)
        assert abs(q0-expected_q0)<1e-12
        col=[current[0][j]+current[1][j] for j in range(3)]
        matrix=[[current[i][j]*nu[j]/col[j] for j in range(3)] for i in range(2)]
        assert all(abs(sum(matrix[i][j] for i in range(2))-nu[j])<1e-12 for j in range(3))
        t=(1-b)/b*st
print('COMPLETE DIRECT-MATRIX KL PROJECTIONS passed')
