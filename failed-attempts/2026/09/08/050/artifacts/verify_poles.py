"""Rigorous pole-gap certificate. Exact rational (Fraction) arithmetic only.
For each pool graph: F(u)=sum (-1)^k c_k u^k factored over Z (factorizations
proved by expansion check in-script); smallest positive root u* isolated in a
rational interval [lo,hi] with uniqueness proof (monotonicity / linear factors);
R=u*/(1-u*) interval via monotonicity; tau=1/R interval.
Winner W8star maximizes R (minimizes tau=phi). Runner-up TRI family tau=2.
Replay: python3 verify_poles.py  (exits nonzero on any failure)
"""
from fractions import Fraction
import json, os
ART = os.path.dirname(os.path.abspath(__file__)) + '/'
cl = json.load(open(ART+'cliques.json'))

def F(c, u):
    s = Fraction(0); p = Fraction(1)
    for k in range(len(c)):
        s += Fraction(((-1)**k)*c[k])*p; p *= u
    return s

def check_factor(c, factors):
    # factors: list of coeff-lists (ascending) over Z; product must equal F coeffs
    acc = [Fraction(1)]
    for f in factors:
        nxt = [Fraction(0)]*(len(acc)+len(f)-1)
        for i,a in enumerate(acc):
            for j,b in enumerate(f):
                nxt[i+j] += a*Fraction(b)
        acc = nxt
    while len(acc) > 1 and acc[-1] == 0: acc.pop()
    cc = list(c)
    while len(cc) > 1 and cc[-1] == 0: cc.pop()
    assert len(acc) == len(cc), (len(acc), len(cc))
    for i in range(len(cc)):
        assert acc[i] == Fraction(((-1)**i)*cc[i]), (i, acc[i], cc[i])

res = {}
# ---- W8star: F = -(u-1)^5 (u^2-3u+1)
c = cl['W8star']['clique_counts']
check_factor(c, [[1,-5,10,-10,5,-1],[1,-3,1]])
# uniqueness: q(u)=u^2-3u+1 strictly decreasing on [0,2/5] (q'=2u-3<0); q(1/3)=1/9>0>q(2/5)=-1/25 -> unique root in (1/3,2/5); q<0 on [2/5,1] so unique positive root != 1. sqrt5 sandwich -> (0.381965,0.38197).
assert F(c,Fraction(1,3)) == Fraction(32,2187) and F(c,Fraction(2,5)) == Fraction(-243,78125)
uW = (Fraction(381965,1000000), Fraction(38197,100000))
assert Fraction(1,3) < uW[0] and uW[1] < Fraction(2,5)
# sandwich check: q(lo)<0<q(hi)?? q decreasing, root in interval iff q(lo)>0>q(hi)
q = lambda u: u*u-3*u+1
assert q(uW[0]) > 0 > q(uW[1]), (q(uW[0]), q(uW[1]))
R = lambda u: u/(1-u)
RW = (R(uW[0]), R(uW[1]))
assert RW[0] > Fraction(1,2)  # gap above runner-up R=1/2
res['W8star'] = {'u_star': [str(uW[0]), str(uW[1])], 'R': [str(RW[0]), str(RW[1])],
  'tau': [str(1/RW[1]), str(1/RW[0])], 'exact': 'tau=phi=(1+sqrt5)/2, R=1/phi'}
print('W8star R in (%s, %s) tau in (%s, %s)' % (float(RW[0]), float(RW[1]), float(1/RW[1]), float(1/RW[0])))

# ---- TRI family: F = s*(u-1)^k*(3u-1), u*=1/3 exact
import itertools
for name, k, sgn in [('G07tri',4,-1),('G08tri',5,1),('G09tri',6,-1)]:
    c = cl[name]['clique_counts']
    facs = [[sgn]] + [[-1,1]]*k + [[-1,3]]
    # careful: leading sign fold into first factor
    check_factor(c, [[sgn]] + [[-1,1]]*k + [[-1,3]])
    assert F(c, Fraction(1,3)) == 0
    res[name] = {'u_star': ['1/3','1/3'], 'R': ['1/2','1/2'], 'tau': ['2','2'], 'exact': 'tau=2'}
    print(name, 'tau=2 exact')

# ---- C4 family: F = s*(u-1)^m*(2u^2-4u+1); quad roots 1±sqrt2/2; small in (0.29289,0.292895)
r_lo, r_hi = Fraction(141421,100000), Fraction(141422,100000)
assert r_lo*r_lo < 2 < r_hi*r_hi
for name, m, sgn in [('G08c4',4,1),('G09c4',5,-1)]:
    c = cl[name]['clique_counts']
    check_factor(c, [[sgn]] + [[-1,1]]*m + [[1,-4,2]])
    uC = (1-r_hi/2, 1-r_lo/2)
    qq = lambda u: 2*u*u-4*u+1
    assert qq(Fraction(1,4)) > 0 > qq(Fraction(3,10))  # unique: decreasing on [0,3/10] (deriv 4u-4<0)
    assert qq(uC[0]) > 0 > qq(uC[1])
    RC = (R(uC[0]), R(uC[1]))
    res[name] = {'u_star': [str(uC[0]), str(uC[1])], 'R': [str(RC[0]), str(RC[1])],
      'tau': [str(1/RC[1]), str(1/RC[0])], 'exact': 'tau=1+sqrt2'}
    print(name, 'R in', float(RC[0]), float(RC[1]))

# ---- S3 (G08s3): F=-(u-1)^4 (u^3-3u^2+4u-1); cubic strictly increasing (deriv 3(u-1)^2+1>0); root in (0.317,0.318)
c = cl['G08s3']['clique_counts']
check_factor(c, [[-1]] + [[-1,1]]*4 + [[-1,4,-3,1]])
a, b = Fraction(317,1000), Fraction(318,1000)
assert F(c,a) > 0 > F(c,b)
RS = (R(a), R(b))
res['G08s3'] = {'u_star': [str(a), str(b)], 'R': [str(RS[0]), str(RS[1])],
  'tau': [str(1/RS[1]), str(1/RS[0])]}
print('G08s3 tau in', float(1/RS[1]), float(1/RS[0]))

# ---- S4 (G09s4): F=(u-1)^4 (u^4-4u^3+6u^2-5u+1); quartic strictly decreasing on [0,1] (deriv 4(u-1)^3-1<0); root in (0.275,0.276)
c = cl['G09s4']['clique_counts']
check_factor(c, [[1]] + [[-1,1]]*4 + [[1,-5,6,-4,1]])
a, b = Fraction(275,1000), Fraction(276,1000)
assert F(c,a) > 0 > F(c,b)
RS = (R(a), R(b))
res['G09s4'] = {'u_star': [str(a), str(b)], 'R': [str(RS[0]), str(RS[1])],
  'tau': [str(1/RS[1]), str(1/RS[0])]}
print('G09s4 tau in', float(1/RS[1]), float(1/RS[0]))

# ---- linear-factor graphs
for name, r in [('P08',Fraction(1,7)),('K35',Fraction(1,5)),('P09',Fraction(1,8))]:
    c = cl[name]['clique_counts']
    assert F(c, r) == 0
    Rr = R(r)
    res[name] = {'u_star': [str(r),str(r)], 'R': [str(Rr),str(Rr)], 'tau': [str(1/Rr),str(1/Rr)], 'exact': 'linear'}
    print(name, 'tau=', float(1/Rr))
# K35 full: (3u-1)(5u-1)
check_factor(cl['K35']['clique_counts'], [[1],[-1,3],[-1,5]])
# P08: (u-1)(7u-1)
check_factor(cl['P08']['clique_counts'], [[1],[-1,1],[-1,7]])
check_factor(cl['P09']['clique_counts'], [[1],[-1,1],[-1,8]])

# ---- C09: 9u^2-9u+1, roots (3±sqrt5)/6; small in ((3-2.23607)/6,(3-2.23606)/6)
c = cl['C09']['clique_counts']
check_factor(c, [[1], [1,-9,9]])
s_lo, s_hi = Fraction(223606,100000), Fraction(223607,100000)
assert s_lo*s_lo < 5 < s_hi*s_hi
u9 = ((3-s_hi)/6, (3-s_lo)/6)
qc = lambda u: 9*u*u-9*u+1
assert qc(Fraction(1,8)) > 0 > qc(Fraction(2,10))  # unique on [0,1/5]? deriv 18u-9<0 on [0,1/5] ✓ decreasing
assert qc(u9[0]) > 0 > qc(u9[1])
R9 = (R(u9[0]), R(u9[1]))
res['C09'] = {'u_star': [str(u9[0]), str(u9[1])], 'R': [str(R9[0]), str(R9[1])],
  'tau': [str(1/R9[1]), str(1/R9[0])]}
print('C09 tau in', float(1/R9[1]), float(1/R9[0]))

# ---- minimality: winner R lower bound exceeds every other R upper bound
RWlo = RW[0]
for name, d in res.items():
    if name == 'W8star': continue
    assert Fraction(d['R'][1]) < RWlo, (name, d['R'][1], str(RWlo))
print('MINIMALITY CERTIFIED: W8star R >= %s > all others' % RWlo)
json.dump(res, open(ART+'growth_table.json','w'), indent=1)
print('wrote growth_table.json')
