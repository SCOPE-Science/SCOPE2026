"""Checks for a sharp rare-cooperator boundary fixed-point classification.
Run: python3 verify.py. Standard library only. Finite tests supplement the proof.
"""
from fractions import Fraction as Q
from math import log, isfinite

p0,p1,p2=Q(4,5),Q(1,2),Q(1,10)
q0,q1,q2=Q(1,5),Q(2,5),Q(9,10)
S0,S1,P0,P1=Q(1),Q(0),Q(37,57),Q(1)
R0,T0,R1,T1=Q(5),Q(3),Q(3),Q(4)
w,beta=Q(1,5),Q(40)
assert p0>p1>p2>0 and 0<q0<q1<q2<1
assert R0>T0 and S0>P0 and R1<T1 and S1<P1
assert 0<w<1 and beta>0

a=2*w*(p1+q1); b=1-w
u=q1/(p1+q1); v=q2/(p2+q2)
h=S0-S1; d=S1-P1-(P0-P1)*v
K=beta*h*a*b*(v-u)
assert (a,b,u,v,h,d)==(Q(9,25),Q(4,5),Q(4,9),Q(9,10),Q(1),Q(-13,19))
assert K==Q(656,125)
assert 4*a*(a+b)==Q(1044,625)
assert beta>4*(a+b)/(h*b*(v-u))==Q(522,41)

def c(r):return (a*u+b*r*v)/(a+b*r)
r=Q(1,2)
assert c(r)==Q(13,19) and d+h*c(r)==0
Fprime_mid=1/(r*(1-r))-K/(a+b*r)**2
assert Fprime_mid==-Q(1836,361)<0
# Exact at the middle branch: auxiliary environment unstable; cooperator growth neutral.
lam_env=-(a+b*r)*r*(1-r)*Fprime_mid
assert lam_env==Q(459,475)>0 and b*(2*r-1)==0

# Numeric bisection: auxiliary check of the exact three-branch theorem.
Af,Bf,uf,vf,hf,df,betaf=map(float,(a,b,u,v,h,d,beta))
def cf(r):return (Af*uf+Bf*r*vf)/(Af+Bf*r)
def F(r):return log(r/(1-r))-betaf*(df+hf*cf(r))
def bisect(l,r):
    fl,fr=F(l),F(r)
    assert fl*fr<0
    for _ in range(125):
        m=(l+r)/2;fm=F(m)
        if fm==0:return m
        if fl*fm<=0:r=m;fr=fm
        else:l=m;fl=fm
    return (l+r)/2
rlo=bisect(1e-10,.01)
rhi=bisect(.7,1-1e-10)
assert 0<rlo<.5<rhi<1
assert abs(F(rlo))<1e-8 and abs(F(rhi))<1e-8
for rr, expected_env_sign,expected_inv_sign in [(rlo,-1,-1),(.5,1,0),(rhi,-1,1)]:
    l_env=-(Af+Bf*rr)+Bf*betaf*hf*rr*(1-rr)*(vf-cf(rr))
    l_inv=Bf*(2*rr-1)
    assert isfinite(l_env) and isfinite(l_inv)
    assert (l_env>0)-(l_env<0)==expected_env_sign
    assert (l_inv>0)-(l_inv<0)==expected_inv_sign
print('Exact rational identities: PASS')
print('Three solution branches and stability signs: PASS')
print('Auxiliary numerical roots: %.12g, %.12g, %.12g'%(rlo,.5,rhi))
