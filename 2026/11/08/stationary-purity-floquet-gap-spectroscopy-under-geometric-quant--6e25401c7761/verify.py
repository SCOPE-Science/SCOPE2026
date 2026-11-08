"""Standalone finite arithmetic checks of stationary purity, inversion, and homometric obstruction.
This script uses only the Python standard library.
Run: python3 verify.py
"""
from fractions import Fraction as Q
from itertools import combinations
from math import cos, pi, isclose
import cmath

checks = 0

def test(statement, label):
    global checks
    assert statement, label
    checks += 1

def rational_purity(p, masses, phase_gap):
    z = p * p / (1-p)
    return sum((u*v*z/(z+phase_gap[i][j]) for i,u in enumerate(masses) for j,v in enumerate(masses)), Q(0))

def gauss(A, rhs):
    rows = [list(row)+[v] for row,v in zip(A,rhs)]
    n = len(rhs)
    for c in range(n):
        pivot = next(i for i in range(c,n) if rows[i][c])
        rows[c], rows[pivot] = rows[pivot], rows[c]
        fac = rows[c][c]
        rows[c] = [v/fac for v in rows[c]]
        for i in range(n):
            if i != c:
                fac = rows[i][c]
                rows[i] = [x-fac*y for x,y in zip(rows[i],rows[c])]
    return [row[-1] for row in rows]

masses = [Q(1,2),Q(1,3),Q(1,6)]
phase_gap = [[Q(0),Q(2),Q(4)],[Q(2),Q(0),Q(2)],[Q(4),Q(2),Q(0)]]
B2 = Q(4,9);B4=Q(1,6);B0=Q(7,18)
for i in range(1,150):
    p = Q(i,151)
    z = p*p/(1-p)
    fp = Q(8,9)/(z+2) + Q(2,3)/(z+4)
    P = rational_purity(p,masses,phase_gap)
    test(P == 1-fp, ('spectral decomposition',i))
    test(P == B0+B2*z/(z+2)+B4*z/(z+4), ('zero-gap mass',i))
    test(Q(0)<P<Q(1), ('purity domain',i))
    d1=B2*2/(z+2)**2+B4*4/(z+4)**2
    d2=-2*(B2*2/(z+2)**3+B4*4/(z+4)**3)
    test(d1>0 and d2<0, ('signed derivatives',i))
    # Independently compute density entries from the stationary recurrence.
    lambdas=[1+0j,1j,-1+0j]
    rho = [[complex((float(masses[a]*masses[b]))**0.5)*float(p)/(1-(1-float(p))*lambdas[a]/lambdas[b])
           for b in range(3)] for a in range(3)]
    tr2 = sum(abs(rho[a][b])**2 for a in range(3) for b in range(3))
    test(isclose(tr2,float(P),rel_tol=1e-12,abs_tol=1e-12),('density recurrence',i))

ps = [Q(1,5),Q(2,5),Q(3,5),Q(4,5)]
zs=[p*p/(1-p) for p in ps]
fs=[1-rational_purity(p,masses,phase_gap) for p in ps]
coeff=gauss([[f*z,f,-z,-Q(1)] for z,f in zip(zs,fs)],[-f*z*z for z,f in zip(zs,fs)])
test(coeff==[Q(6),Q(8),Q(14,9),Q(44,9)],'four-sample reconstruction')
D1,D0,N1,N0=coeff
c2=(N1*(-2)+N0)/(-4+D1)
c4=(N1*(-4)+N0)/(-8+D1)
test(c2==Q(8,9) and c4==Q(2,3),'residues')
test(c2/2==B2 and c4/4==B4,'spectral weights')

# A pair of classical homometric six-point configurations; strict phase diameter < pi.
A=(0,1,4,10,12,17)
B=(0,1,8,11,13,17)
da=sorted(b-a for a,b in combinations(A,2))
db=sorted(b-a for a,b in combinations(B,2))
test(da==db and len(set(da))==15, 'homometric distance equality')
test(tuple(sorted(17-x for x in A))!=B and A!=B, 'not related by translation/reflection')
for k in range(1,100):
    p=k/101
    z=p*p/(1-p)
    def purity(S):
        return (6+2*sum(z/(z+2*(1-cos(pi*(b-a)/18))) for a,b in combinations(S,2)))/36
    test(isclose(purity(A),purity(B),rel_tol=1e-13,abs_tol=1e-13),('purity blind spot',k))

print('PASS:',checks,'standalone arithmetic/numerical assertions')
