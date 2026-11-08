#!/usr/bin/env python3
"""Exact small-matrix checks and independent high-precision exponential tests."""
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import factorial

checks=0

def check(value, message):
    global checks
    checks += 1
    if not value:
        raise AssertionError(message)

def zero(n, value=F(0)):
    return [[value for _ in range(n)] for _ in range(n)]

def mm(A,B):
    n=len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def add(A,B):
    return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]

def scal(A,x):
    return [[x*a for a in row] for row in A]

def G(n,i):
    A=zero(n);A[i][i]=-1;A[i][i+1]=1;return A

def comm(A,B):
    return add(mm(A,B),scal(mm(B,A),-1))

def magnus(n,h,weights=None):
    if weights is None: weights=[F(1)]*(n-1)
    generators=[scal(G(n,i),h*weights[i]) for i in range(n-1)]
    O=zero(n)
    for a in generators: O=add(O,a)
    for earlier in range(n-2, -1, -1):
        for later in range(earlier-1,-1,-1):
            O=add(O,scal(comm(generators[earlier],generators[later]),F(1,2)))
    return O

for h in [F(0),F(1,10),F(1,2),F(2),F(4),F(6)]:
    O=magnus(4,h)
    expected=[[ -h, h+h*h/2, -h*h/2, F(0)],
              [F(0),-h,h+h*h/2,-h*h/2],
              [F(0),F(0),-h,h],
              [F(0),F(0),F(0),F(0)]]
    check(O==expected,'Magnus matrix and chronological commutator sign')
    for row in O:check(sum(row)==0,'row-conservation of logarithm')

# Exact cubic Taylor coefficient of exp(O(h)) for arbitrary reverse cascades.
# Writing O(h)=h A+h^2 B, the third coefficient is (AB+BA)/2+A^3/6.
for n in range(4,10):
    for seed in range(1,7):
        weights=[F((i+seed)%7+1, (i+2)%4+1) for i in range(n-1)]
        A=zero(n);B=zero(n)
        generators=[scal(G(n,i),weights[i]) for i in range(n-1)]
        for g in generators:A=add(A,g)
        for earlier in range(n-2,-1,-1):
            for later in range(earlier-1,-1,-1):
                B=add(B,scal(comm(generators[earlier],generators[later]),F(1,2)))
        coeff3=add(scal(add(mm(A,B),mm(B,A)),F(1,2)),scal(mm(mm(A,A),A),F(1,6)))
        check(coeff3[0][3] == -F(1,3)*weights[0]*weights[1]*weights[2], 'universal cubic obstruction')
        check(B[0][3]==0 and (mm(A,A))[0][3]==0,'no lower-order 1-to-4 paths')

with localcontext() as ctx:
    ctx.prec=85
    d=lambda x:Decimal(str(x))
    def edec(h):return h.exp()
    def defect(h):
        p=1+h+h*h/2+h*h*h/2+h**4/8
        return 1-p/edec(h)
    def deriv(h):return (-h).exp()*h*h*(h*h-8)/8
    # Unique zero beyond sqrt(8), proved analytically in text.
    l=d('4');r=d('8')
    for it in range(350):
        mid=(l+r)/2
        if defect(mid)<0:l=mid
        else:r=mid
        check(l<r,'root enclosure')
    root=(l+r)/2
    check(abs(root-d('5.20228372790060182518'))<d('1e-19'),'root decimal')
    check(abs(defect(root))<d('1e-75'),'root residual')
    check(defect(d('0.1'))<0 and defect(d('1'))<0 and defect(d('3'))<0 and defect(d('5'))<0,'negative region')
    check(defect(d('5.3'))>0 and defect(d('10'))>0,'positive region')
    check(deriv(d('1'))<0 and deriv(d('2.82'))<0 and deriv(d('3'))>0,'minimum derivative signs')
    check(abs(defect(d('8').sqrt())-d('-0.6042561893264855'))<d('0.0000000000000001'),'defect minimum')
    for h in [d('0.0001'),d('0.01'),d('0.1'),d('0.5'),d('1'),d('2'),d('4'),d('5.3'),d('6'),d('10')]:
        # Completely independent matrix exponential using convergent Taylor series.
        Of=magnus(4,F(str(h)))
        O=[[Decimal(v.numerator)/Decimal(v.denominator) for v in row] for row in Of]
        I=[[Decimal(int(i==j)) for j in range(4)] for i in range(4)]
        result=[row.copy() for row in I]
        term=[row.copy() for row in I]
        for k in range(1,600):
            term=mm(term,O)
            term=scal(term,Decimal(1)/k)
            result=add(result,term)
            if max(abs(v) for row in term for v in row)<d('1e-76'):break
        else: raise AssertionError('Taylor series did not converge')
        a=h+h*h/2
        e=(-h).exp()
        formulas=[[e,a*e,(h**3/2+h**4/8)*e,defect(h)],
                  [d('0'),e,a*e,1-(1+a)*e],
                  [d('0'),d('0'),e,1-e],
                  [d('0'),d('0'),d('0'),d('1')]]
        for i in range(4):
            check(abs(sum(result[i])-1)<d('1e-65'),'exp preserves row sums')
            for j in range(4):
                check(abs(result[i][j]-formulas[i][j])<d('1e-65'), 'independent exponential matches all entries')
        check(result[0][3]<0 if h<root else result[0][3]>0,'expected sign')
    # Three-state boundary family: no negative full-step transition.
    for h in [d('0.01'),d('0.1'),d('1'),d('3'),d('8'),d('25')]:
        a=h+h*h/2;e=(-h).exp()
        check(1-(1+a)*e>0,'three-state reversed cascade positive')

print('VERIFICATION_PASS',checks,'assertions; sharp_root=',root,'; max_violation=',defect(d('8').sqrt()))
