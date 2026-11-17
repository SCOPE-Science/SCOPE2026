"""Exact-rational consistency checks for symmetric three-species mutation/competition dynamics.
The continuous-time convergence proof is mathematical and does not rely on finite tests.
"""
from fractions import Fraction as F
from itertools import product

def field(x,c,m):
    S=sum(x)
    return tuple(z*(1-c*S+(c-1)*z)+m*(S-3*z) for z in x)

def P(r,c,m):
    return (c*c-1)*r*r+(c-1)*(2*m-1)*r+m*(1-3*m)

for cn in [F(1,3),F(1),F(5,4),F(2),F(7,2)]:
    for mn in [F(1,100),F(1,20),F(1,5),F(1,2)]:
        for xx in product([F(1,5),F(2,5),F(1),F(5,3)], repeat=3):
            x,y,z=xx; f=field(xx,cn,mn)
            assert f[0]-f[1]==(x-y)*(1-(x+y)-cn*z-3*mn)
            assert f[1]-f[2]==(y-z)*(1-(y+z)-cn*x-3*mn)
            assert sum(f)==sum(xx)-cn*sum(xx)**2+(cn-1)*sum(v*v for v in xx)
            assert f[0]==x*(1-x-cn*(y+z))+mn*(y+z-2*x)
        if cn>1 and mn < (cn-1)/(3*(1+2*cn)):
            r0=(1-3*mn)/(cn+2)
            assert r0>0 and P(F(0),cn,mn)>0 and P(r0,cn,mn)<0
            assert P(r0,cn,mn)==(1-3*mn)*(3*(2*cn+1)*mn-(cn-1))/(cn+2)**2
for cn in [F(1,2),F(1),F(2),F(7,3)]:
    for mn in [F(1,4),F(1,100)]:
        for r,z in product([F(1,10),F(1),F(7,3)],repeat=2):
            # Negative Bendixson-Dulac divergence of f/rz, g/rz.
            D=-(1+cn)/z-F(1)/r-mn/(r*r)-2*mn/(z*z)
            assert D<0
            # The two plane flow derivatives and equilibrium reduction.
            fr=r*(1-(1+cn)*r-cn*z)+mn*(z-r)
            gz=z*(1-z-2*cn*r)+2*mn*(r-z)
            assert fr==field((r,r,z),cn,mn)[0]
            assert gz==field((r,r,z),cn,mn)[2]
        for r in [F(1,10),F(2,9),F(3,10)]:
            z=1-(cn+1)*r-3*mn
            assert field((r,r,z),cn,mn)[0]==P(r,cn,mn)
            assert field((r,r,z),cn,mn)[2]==P(r,cn,mn)
print('MUTATION_SYMMETRY_EXACT_FRACTION_CHECKS_OK')
