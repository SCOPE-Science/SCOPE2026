"""Independent finite checks for pentagonal iid Kaczmarz sampling.

Analytic arguments in RESULT.md, not finite tests, certify global optimality.
Standard-library only: python3 verify_pentagonal.py.
"""
import math
import itertools
import random
from fractions import Fraction

N = 5
c = math.cos(math.pi / 5)
d = math.cos(2 * math.pi / 5)
a = -math.log(c * c)
b = -math.log(d * d)
assert b > 3*a > 0
CHECKS = 0

def check(condition, message="check failed"):
    global CHECKS
    assert condition, message
    CHECKS += 1

def close(x, y, tol=5e-12):
    check(abs(x-y) < tol * max(1, abs(x), abs(y)), (x,y))

def rate(p):
    return 2 * sum(p[i]*p[j]*(a if min((j-i)%5,(i-j)%5)==1 else b)
                   for i in range(5) for j in range(i+1,5))

expected=2*b*b/(4*b-a)
x=(2*b-a)/(4*b-a)
y=b/(4*b-a)
check(abs(x+2*y-1)<1e-12)
for middle in range(5):
    p=[0.0]*5
    p[middle]=x
    p[(middle+2)%5]=y
    p[(middle-2)%5]=y
    close(rate(p), expected)
    close(sum(p), 1)
    check(sum(v>1e-14 for v in p)==3)
    z=sum(p[j]*complex(math.cos(2*j*math.pi/5),math.sin(2*j*math.pi/5)) for j in range(5))
    close(abs(z), (2*b-a-2*b*c)/(4*b-a))
    check(0.5*(1+abs(z))>0.5)

# Check each three-element subset is one of the two abstract support patterns.
kind_count={"A":0,"B":0}
for subset in itertools.combinations(range(5),3):
    near=sum(1 for i,j in itertools.combinations(subset,2) if (j-i)%5 in (1,4))
    check(near in (1,2))
    kind_count["A" if near==1 else "B"]+=1
check(kind_count=={"A":5,"B":5})

# Exact combinatorial signs in the four-coordinate perturbation.
for first in range(5):
    v=[0]*5
    for t,sign in enumerate((1,-1,1,-1)):
        v[(first+t)%5]=sign
    an=sum(v[i]*v[j] for i in range(5) for j in range(i+1,5)
           if (j-i)%5 in (1,4))
    bn=sum(v[i]*v[j] for i in range(5) for j in range(i+1,5)
           if (j-i)%5 in (2,3))
    check((an,bn)==(-3,1))
    check(a*an+b*bn>0)

# Exact arithmetic identity: x+y+z=1 and the optimizer rational expression
# with formal, strictly positive parameters chosen from a generic rational grid.
for ar,br in itertools.product((Fraction(1,7),Fraction(2,9),Fraction(3,8)),
                                (Fraction(2),Fraction(3),Fraction(5))):
    X=(2*br-ar)/(4*br-ar)
    Y=br/(4*br-ar)
    assert br>3*ar
    check(X+2*Y==1)
    check(2*br*X*(2*Y)+2*ar*Y*Y==2*br*br/(4*br-ar))
    check(2*br*br/(4*br-ar)-br/2==ar*br/(2*(4*br-ar)))

# Independent dense random simplex and edge/face sampling: not an exhaustive
# numerical proof; supports the explicit analytic global certificate.
rng=random.Random(20261115)
for t in range(10000):
    raw=[rng.expovariate(1) for _ in range(5)]
    p=[v/sum(raw) for v in raw]
    check(rate(p)<=expected+2e-12)
for sub in itertools.chain.from_iterable(itertools.combinations(range(5),k)
                                      for k in (1,2,3,4)):
    for rep in range(25):
        raw=[rng.expovariate(1) for _ in sub]
        p=[0.0]*5
        for i,w in zip(sub,raw):
            p[i]=w/sum(raw)
        check(rate(p)<=expected+2e-12)

# Simulated products only check the rate formula for two distributions;
# sample length is finite and not a proof of the almost-sure limit.
for p in ([.2]*5,[x if i==0 else y if i in (2,3) else 0 for i in range(5)]):
    samples=rng.choices(range(5),weights=p,k=100000)
    empirical=-(sum(math.log(math.cos((samples[t]-samples[t-1])*math.pi/5)**2)
                 for t in range(1,len(samples)))/(len(samples)-1))
    check(abs(empirical-rate(p))<0.04)

close(expected,1.2298462771237793)
close(expected-b/2, a*b/(2*(4*b-a)))
close(rate([.2]*5), 2*(a+b)/5)
print('VERIFY_OK',CHECKS,'assertions')
print('a',repr(a),'b',repr(b),'opt_rate',repr(expected),'p_center',repr(x),'p_leaf',repr(y))
