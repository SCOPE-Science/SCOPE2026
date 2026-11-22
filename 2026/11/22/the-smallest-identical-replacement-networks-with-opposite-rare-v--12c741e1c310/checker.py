"""Exact rational verification of the three-player, three-site volunteer-game witness."""
from fractions import Fraction as Q
from itertools import product

A = (Q(11,57),Q(11,57),Q(35,57))
B = (Q(26,57),Q(26,57),Q(5,57))
V=Q(1); K=Q(49,100)


def encounter(p):
    assert sum(p)==1 and all(t>0 for t in p)
    s2=sum(t*t for t in p)
    w0=sum(t*(1-t)**2 for t in p)
    w1=(1-w0)/2
    # independently enumerate all assignments of 3 labelled individuals to 3 sites
    W=[[Q(0) for _ in range(3)] for _ in range(3)]
    for sites in product(range(3),repeat=3):
        pr=p[sites[0]]*p[sites[1]]*p[sites[2]]
        for i in range(3):
            group=[j for j in range(3) if sites[j]==sites[i]]
            if len(group)==1:
                W[i][i]+=pr
            else:
                for j in group:
                    if j!=i:
                        W[i][j]+=pr/Q(len(group)-1)
    assert W==[[w0 if i==j else w1 for j in range(3)] for i in range(3)]
    return s2,w0,w1

s2a,w0a,w1a=encounter(A)
s2b,w0b,w1b=encounter(B)
assert s2a==Q(163,361) and s2b==Q(153,361)
assert w0a==w0b==Q(21164,61731)
assert w1a==w1b

# Fermi-free fitness-proportional birth-death Moran imitation with group-average payoffs:
# In a state with j volunteer cooperators, every cooperator gets 1-K;
# a defector receives the public benefit if and only if one cooperator occupies its site.
# j=1: cooperator meeting probability is s2; j=2: no cooperator probability w0.

def fixation(s2,w0,w):
    Fc=1-w+w*(V-K)
    Fd1=1-w+w*V*s2
    Fd2=1-w+w*V*(1-w0)
    assert all(x>0 for x in (Fc,Fd1,Fd2))
    R1=Fd1/Fc
    R2=Fd2/Fc
    return 1/(1+R1+R1*R2)

# For any w>0, sign(rho-1/3) == sign(L+Qcoef*w).
def coeffs(s2,w0):
    k=K/V;a=1-s2;b=w0
    return b+2*a-3*k, 2*k*k-a*(k+b)

La,Qa=coeffs(s2a,w0a)
Lb,Qb=coeffs(s2b,w0b)
assert La<0 and Qa>0 and La+Qa<0
assert Lb>0 and Qb>0
assert La==Q(-186457,6173100)
assert Lb==Q(155543,6173100)
assert Qa==Q(289772799,12380495000)
assert Qb==Q(37345691,111424455000)

for w in [Q(1,1000),Q(1,100),Q(1,10),Q(1,2),Q(1)]:
    rA=fixation(s2a,w0a,w)
    rB=fixation(s2b,w0b,w)
    assert rA<Q(1,3)<rB
    assert rA<rB

# General exact identity: with W self-loop probability equal,
# fixation odds are determined by the three-state birth-death walk.
for p,s2 in [(A,s2a),(B,s2b)]:
    for w in [Q(1,2),Q(1)]:
        Fc=1-w+w*(V-K)
        Fd=[None,1-w+w*s2,1-w+w*(1-w0a)]
        T=[]
        for j in [1,2]:
            denom=j*Fc+(3-j)*Fd[j]
            plus=Q(j)*Fc/denom*Q(3-j)*w1a
            minus=Q(3-j)*Fd[j]/denom*Q(j)*w1a
            T.append((plus,minus))
        rp=T[0][1]/T[0][0]; rq=T[1][1]/T[1][0]
        exact=1/(1+rp+rp*rq)
        assert exact==fixation(s2,w0a,w)

# Two sites suffice to uniquely recover a three-person common site law up to swapping:
# w0(q,1-q) = q(1-q); its quadratic roots are q and 1-q.
for q in [Q(i,20) for i in range(1,20)]:
    w0=q*(1-q)**2+(1-q)*q*q
    assert w0==q*(1-q) and w0==(1-q)*q

print('PASS: identical replacement matrices, distinct co-occupation, exact all-intensity reversed fixation')
print('A',A, 's2',s2a, 'w0',w0a, 'at w=1',fixation(s2a,w0a,Q(1)))
print('B',B, 's2',s2b, 'w0',w0b, 'at w=1',fixation(s2b,w0b,Q(1)))
print('L_A,Q_A,L_B,Q_B', La,Qa,Lb,Qb)
