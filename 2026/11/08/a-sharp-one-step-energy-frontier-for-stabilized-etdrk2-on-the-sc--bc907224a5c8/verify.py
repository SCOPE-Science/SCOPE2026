"""Exact polynomial certificate for one-step scalar ETDRK2 energy descent.
Run: python3 verify.py. Standard-library only; no downloaded packages.
"""
from fractions import Fraction as Q
from math import comb, exp, sqrt
from random import Random

Z=(0,0,0)

def const(n):
    return {Z:Q(n)} if n else {}

def var(i):
    k=[0,0,0];k[i]=1
    return {tuple(k):Q(1)}

def add(a,b):
    out=a.copy()
    for e,c in b.items():out[e]=out.get(e,Q(0))+c
    return {e:c for e,c in out.items() if c}

def neg(a):return {e:-c for e,c in a.items()}

def sub(a,b):return add(a,neg(b))

def mul(a,b):
    out={}
    for e,c in a.items():
        for f,d in b.items():
            g=tuple(e[i]+f[i] for i in range(3))
            out[g]=out.get(g,Q(0))+c*d
    return {e:c for e,c in out.items() if c}

def powpol(a,n):
    out=const(1)
    for _ in range(n):out=mul(out,a)
    return out

one=const(1); two=const(2); three=const(3)
z=var(0);y=var(1);t=var(2)
q=mul(mul(t,y),sub(one,z))
# q= H(1-u^2), y=alpha*H, t=1/alpha,
# W=w/u for the upper comparison endpoint B=H.
inner=sub(add(three,add(mul(three,q),powpol(q,2))),const(0))
W=add(one,mul(q,add(one,mul(y,sub(add(one,t),mul(mul(t,z),inner))))))
N=sub(two,mul(z,add(one,powpol(W,2))))
# Divide N by (1-z) in the polynomial ring Q[z,y,t].
# P=(2-z(1+W^2))/(1-z); exact divisibility is asserted.
P={}
assert max(e[0] for e in N)<=9 and all(max(e[j] for e in N)<=8 for j in (1,2))
max_z=max(e[0] for e in N)
for j in range(9):
    for k in range(9):
        cumulative=Q(0)
        for i in range(max_z+1):
            cumulative+=N.get((i,j,k),Q(0))
            if i < max_z and cumulative:P[(i,j,k)]=cumulative
        assert cumulative==0,('nonzero remainder',j,k,cumulative)
P={e:c for e,c in P.items() if c}
assert mul(P,sub(one,z))==N, "incomplete polynomial quotient"
assert max(max(e) for e in P)<=8
assert len(P)==46, len(P)
# If P=sum_{ijk} b_ijk Binomial(8,i) z^i(1-z)^(8-i) ...,
# then b_ijk=sum_{a<=i,b<=j,c<=k} monomial_coeff[a,b,c]
# * C(i,a)/C(8,a)*C(j,b)/C(8,b)*C(k,c)/C(8,c).
minval=None;minindex=None
for i in range(9):
    for j in range(9):
        for k in range(9):
            s=sum((coeff*Q(comb(i,a),comb(8,a))*Q(comb(j,b),comb(8,b))
                   *Q(comb(k,c),comb(8,c))
                for (a,b,c),coeff in P.items() if a<=i and b<=j and c<=k),Q(0))
            if minval is None or s<minval:minval,minindex=s,(i,j,k)
assert minval==Q(1,8),(minval,minindex)
print('BERNSTEIN_CERTIFICATE_OK', 'monomials',len(P),'min',str(minval),'at',minindex)

# Further independent numerical checks for the original ETDRK2 recurrence.
def etd2(u,h,alpha):
    if alpha==0:
        H=h; B=h/2
    else:
        a=alpha*h; E=exp(-a)
        H=-__import__('math').expm1(-a)/alpha
        B=(a+E-1)/(alpha*alpha*h)
    g=lambda v:(alpha+1)*v-v*v*v
    v=u+H*u*(1-u*u)
    return v+B*(g(v)-g(u))

def energy(u):return (1-u*u)**2/4
r=Random(602)
for _ in range(20000):
    alpha=1+99*r.random()
    u=2*r.random()-1
    h=10**(-4+8*r.random())
    new=etd2(u,h,alpha)
    assert energy(new)<=energy(u)+2e-13,(alpha,u,h,new,energy(new)-energy(u))
# Sharp counterexample sequence for each tested alpha below 1.
for alpha in (0.,0.02,0.2,0.5,0.8,0.98,0.999):
    h=1e8/max(alpha,0.01)
    u=1-1e-6
    out=etd2(u,h,alpha)
    assert energy(out)>energy(u),(alpha,h,u,out)
print('VERIFY_OK')
