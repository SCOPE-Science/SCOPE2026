"""Exact symbolic reproduction of the three-coordinate epoch law.

Requires Python 3 and SymPy. Execute: python artifacts/verify.py
"""
import itertools
from collections import Counter
import sympy as S

r = S.symbols('r', real=True)
H = (1-r)*S.eye(3)+r*S.ones(3)
U = []
for i in range(3):
    T = S.eye(3)
    for j in range(3):
        T[i,j] -= H[i,j]
    U.append(T)

def loss(seq):
    v = S.ones(3,1)
    for i in seq:
        v = U[i]*v
    return S.factor((v.T*H*v)[0]/2)

prefactor = (1-r)*(1+2*r)/2
expected = {
    'iii': 2*prefactor,
    'iij': prefactor*(2*r**2-r+1),
    'iji': prefactor*(2*r**4-r**3+r**2-r+1),
    'ijk': prefactor*r**2*(2*r**2-5*r+5),
}

def kind(seq):
    a,b,c=seq
    if a==b==c: return 'iii'
    if a==b or b==c: return 'iij'
    if a==c: return 'iji'
    return 'ijk'

cnt=Counter()
for seq in itertools.product(range(3),repeat=3):
    ty=kind(seq)
    cnt[ty]+=1
    assert S.cancel(loss(seq)-expected[ty])==0,(seq,ty)
assert cnt == {'iii':3,'iij':12,'iji':6,'ijk':6},cnt

base=expected['ijk']
assert S.simplify(expected['iii']-base-(1-r)**2*(1+2*r)**2*(r**2-2*r+2)/2)==0
assert S.simplify(expected['iij']-base-(1-r)**4*(1+2*r)**2/2)==0
assert S.simplify(expected['iji']-base-(1-r)**2*(1+2*r)**2*(1-2*r)/2)==0
assert S.simplify(expected['iij']-expected['iji']-r**2*(1-r)**2*(1+2*r)**2/2)==0
mean=S.expand(sum(cnt[k]*expected[k] for k in cnt)/27)
assert S.simplify(mean-base-(2-r)*(1-r)**2*(1+2*r)**2*(4-5*r)/18)==0
for rational in [S.Rational(-49,100),-S.Rational(1,4),S.Rational(0),S.Rational(1,5),S.Rational(1,2),S.Rational(3,5),S.Rational(4,5),S.Rational(9,10),S.Rational(99,100)]:
    values=[loss(seq).subs(r,rational) for seq in itertools.product(range(3),repeat=3)]
    cmp=[S.sign(v-base.subs(r,rational)) for v in values]
    if rational <= S.Rational(1,2):
        assert cmp.count(-1)==0
    else:
        assert cmp.count(-1)==6 and cmp.count(0)==6 and cmp.count(1)==15
    assert S.factor(sum(values)/27-mean.subs(r,rational))==0

# Minimality in one- and two-coordinate equicorrelation families.
H2=S.Matrix([[1,r],[r,1]])
T2=[]
for i in range(2):
    A=S.eye(2)
    for j in range(2): A[i,j]-=H2[i,j]
    T2.append(A)
def loss2(seq):
    v=S.ones(2,1)
    for i in seq: v=T2[i]*v
    return S.factor((v.T*H2*v)[0]/2)
assert all(S.factor(loss2(s)-r**2*(1-r**2)/2)==0 for s in [(0,1),(1,0)])
assert all(S.factor(loss2(s)-(1-r**2)/2)==0 for s in [(0,0),(1,1)])
assert S.simplify(loss2((0,0))-loss2((0,1))-(1-r**2)**2/2)==0

print('PASS: 27 exact symbolic objectives, four atom multiplicities, three difference factorizations, mean law, 9 rational parameter tests and 2D minimality.')
print('rho=3/5: permutation=',base.subs(r,S.Rational(3,5)), 'alternating repeat=',expected['iji'].subs(r,S.Rational(3,5)))
print('rho=9/10: mean minus permutation=',S.factor(mean-base).subs(r,S.Rational(9,10)))
