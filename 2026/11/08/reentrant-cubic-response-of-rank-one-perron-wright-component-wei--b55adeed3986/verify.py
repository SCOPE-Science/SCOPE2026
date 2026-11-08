"""Reproduce exact algebraic identities and finite checks for the rank-one Perron--Wright expansion.

Requires SymPy; run `python verify.py` after installing requirements.txt.
This is a finite/symbolic diagnostic, not an independent proof of the asymptotic theorem.
"""
from fractions import Fraction
from itertools import combinations, product
from sympy import symbols, Rational, series, log, expand, factor, simplify, diff

checks = 0

def check(statement, description):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(description)

z, e = symbols('z e')
A, B, G, D = symbols('A B G D', positive=True)
F1 = 1 + A*z + B*z*z/2 + G*z**3/6 + D*z**4/24
F2 = A + B*z + G*z*z/2 + D*z**3/6
T = expand(series(A*(F1/F2-z), z, 0, 4).removeO())
t1, t2, t3 = [simplify(T.coeff(z,j)) for j in (1,2,3)]
check(simplify(t1+B/A) == 0, 'critical derivative')
r1 = simplify(1/t1)
r2 = simplify(-t2*r1**2/t1)
r3 = simplify(-(2*t2*r1*r2+t3*r1**3)/t1)
for n, value in ((1, r1), (2, r2), (3, r3)):
    check(simplify(expand(series(T.subs(z,r1*e+r2*e**2+r3*e**3),e,0,4).removeO()).coeff(e,n)-(1 if n==1 else 0)) == 0, 'series inversion')
check(simplify(r1+A/B)==0, 'first inverse coefficient')
check(simplify(r2+A*(A*A*B+A*G-2*B**2)/(2*B**3))==0, 'second inverse coefficient')
inv = r1*e+r2*e**2+r3*e**3
radius = series(-log(1+e)-log(F2.subs(z, inv)/A),e,0,4).removeO().expand()
coefs = [factor(radius.coeff(e,j)) for j in (1,2,3)]
expected_c3 = A**2*(3*A*A*B+A*G-6*B*B)/(6*B**3)
check(simplify(coefs[0])==0, 'linear term is zero')
check(simplify(coefs[1]-A*A/(2*B))==0, 'quadratic term')
check(simplify(coefs[2]-expected_c3)==0, 'cubic term')
check(not coefs[2].has(D), 'fifth moment cancels')

# A two-type, mean-one, strictly positive family with a fixed high type at 21.
a=symbols('a', real=True)
wlo=Rational(20)/(20+a)
whi=a/(20+a)
xlo=1-a
xhi=Rational(21)
check(simplify(wlo+whi-1)==0, 'mass normalization')
check(simplify(wlo*xlo+whi*xhi-1)==0, 'mean normalization')
M = lambda j: simplify(wlo*xlo**j+whi*xhi**j)
alpha,beta,gamma=(M(j) for j in (2,3,4))
Q=13000*a**4-325210*a**3+509550*a*a-2860*a+1
check(simplify(3*alpha*alpha*beta+alpha*gamma-6*beta*beta+2*Q)==0, 'quartic sign factorization')
check(Q.subs(a,0)>0 and Q.subs(a,Rational(1,1000))<0 and Q.subs(a,Rational(1,100))>0, 'two sign crossings')
check(diff(Q,a,2).subs(a,Rational(1,2))==82470, 'convex region derivative')
check(diff(Q,a).subs(a,0)<0, 'initially decreasing')
check(diff(Q,a).subs(a,Rational(1,2))>0, 'increasing after minimum')
check(Q.subs(a,Rational(37,100000))>0 and Q.subs(a,Rational(38,100000))<0, 'first isolated root')
check(Q.subs(a,Rational(525,100000))<0 and Q.subs(a,Rational(527,100000))>0, 'second isolated root')
actual_m=[M(j).subs(a,Rational(1,200)) for j in (2,3,4)]
expected_m=[Rational(11,10),Rational(6599,2000),Rational(19835201,400000)]
check(actual_m==expected_m, 'exact positive type moments')
pos_c3=factor(expected_c3.subs({A:actual_m[0],B:actual_m[1],G:actual_m[2]}))
check(pos_c3==Rational(5826325450,862096019397), 'exact positive skew coefficient')
check(simplify(expected_c3.subs({A:1,B:1,G:1})+Rational(1,3))==0, 'homogeneous cubic coefficient')
check(pos_c3>0, 'positive versus negative skew')

# Exhaustive weighted-Cayley tree identity on 2-5 labelled vertices, for all two-valued type vectors.
values=(Fraction(199,200),Fraction(21,1))
mean2=Fraction(11,10)

def is_tree(n, edges):
    par=list(range(n))
    def root(v):
        while par[v]!=v:
            v=par[v]
        return v
    for i,j in edges:
        x,y=root(i),root(j)
        if x==y:return False
        par[x]=y
    return len({root(v) for v in range(n)})==1

for n in (2,3,4,5):
    edges=list(combinations(range(n),2))
    trees=[comb for comb in combinations(edges,n-1) if is_tree(n,comb)]
    for typs in product(values,repeat=n):
        left=sum((__import__('math').prod(typs[i]*typs[j]/mean2 for i,j in tree) for tree in trees),Fraction(0))
        right=__import__('math').prod(typs)*(sum(typs)**(n-2))/(mean2**(n-1))
        check(left==right,'weighted Cayley/Pruefer identity')

# The scalar homogeneous case is also exact, not just an expansion:
# C_t/C_1=t^(k+r-1) exp[-k(t-1)] and rho(t)=exp(t-1)/t.
import math
for k in (10,51,300):
    for r in (0,1,3):
        for t in (0.9,0.99,1.01,1.1):
            logratio=(k+r-1)*math.log(t)-k*(t-1)
            logrho=(t-1)-math.log(t)
            check(abs(logratio - (-k*logrho+(r-1)*math.log(t)))<1e-10, 'homogeneous gauge exactness')

print(f'PASS: {checks} exact algebraic/rational and finite diagnostic checks')
print(f'two-type positive example c3={pos_c3}; approx {float(pos_c3):.12g}')
print('The source uniform asymptotic and novelty are not certified by this script.')
