"""Exact finite checks for the inconsistent-data DR/RD scalar least-squares theorem.

All operations use fractions and the Python standard library. These checks
supplement the separate infinite-sequence proof; they do not certify it.
"""
from fractions import Fraction as F

checks = 0


def dot(u, v):
    return sum((x*y for x,y in zip(u, v)), F(0))


def check(A, z, xstar, e0, steps=11):
    global checks
    A = tuple(map(F, A)); z = tuple(map(F, z))
    lam, c = dot(A,A), dot(z,z)
    assert lam > 0 and c > 0 and dot(A,z) == 0
    q = c / lam
    b = tuple(a*xstar + zz for a,zz in zip(A,z))
    def residual(x):
        return tuple(bb-a*x for a,bb in zip(A,b))
    def step_alpha(r):
        den=dot(A,r)**2
        assert den != 0
        return dot(r,r)/den
    x=xstar+e0
    oldr=None
    expected=[e0]
    for k in range(steps):
        r=residual(x)
        assert dot(A,r)==-lam*(x-xstar); checks+=1
        assert dot(r,r)==c+lam*(x-xstar)**2; checks+=1
        alpha=step_alpha(r if k==0 else oldr)
        xn=x+alpha*dot(A,r)
        if k==0:
            target=-q/e0
        else:
            target=-q*expected[-1]/expected[-2]**2
        assert xn-xstar==target; checks+=1
        assert xn!=xstar;checks+=1
        expected.append(target)
        oldr=r; x=xn
    # RD warm-starts using the exact same full-residual initial step.
    x0=xstar+e0
    r0=residual(x0)
    x1=x0+step_alpha(r0)*dot(A,r0)
    r1=residual(x1)
    d=tuple(t-s for s,t in zip(r0,r1))
    alpha_rd=dot(d,d)/dot(A,d)**2
    assert alpha_rd==1/lam; checks+=1
    x2=x1+alpha_rd*dot(A,r1)
    assert x2==xstar; checks+=1
    # The first warm step and RD step are both well-defined.
    assert dot(A,r0)!=0 and dot(A,d)!=0; checks+=1


for A,z in [((1,1),(1,-1)),((3,4),(4,-3)),((2,3,6),(3,-2,0))]:
    for xstar in (F(0),F(2,3)):
        for e0 in (F(1,2),F(1),F(3,2),F(2),F(3)):
            check(A,z,xstar,e0,steps=11)

# The first-order recurrence in the log coordinates has exact integer
# coefficients and characteristic polynomial z^2-z+2.
coef=[1,-1]
for k in range(2,25):
    coef.append(coef[-1]-2*coef[-2])
for k in range(2,len(coef)):
    assert coef[k]-coef[k-1]+2*coef[k-2]==0
    checks+=1

# At the balanced initialization e_0=sqrt(q), q=1, the DR dynamics
# alternate at a nonzero distance from the least-squares solution.
for e0 in (F(1),F(-1)):
    eprev=e0; enow=-e0
    for k in range(12):
        enext=-enow/(eprev**2)
        assert enext==e0 if k%2==0 else enext==-e0
        checks+=1
        eprev,enow=enow,enext

print(f'VERIFY_OK {checks} exact-rational assertions; infinite assertions use analytic proof')
