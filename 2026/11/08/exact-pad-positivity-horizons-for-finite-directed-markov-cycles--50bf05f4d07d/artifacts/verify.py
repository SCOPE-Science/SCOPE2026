"""Exact-rational checks for Padé [2/2] positivity on directed cycles.

Run with: python artifacts/verify.py
Dependencies: Python 3 and SymPy.
The proof of the all-dimensional statements is mathematical, not enumeration.
"""
import sympy as sp

h, u = sp.symbols('h u', real=True)
F = {
    4: h**4 - 24*h**2 - 72*h - 72,
    5: 5*h**6 + 30*h**5 - 432*h**3 - 1584*h**2 - 2592*h - 1728,
    6: 3*h**7 + 26*h**6 + 60*h**5 - 120*h**4 - 1152*h**3 - 3456*h**2 - 5184*h - 3456,
    7: 7*h**10 + 105*h**9 + 630*h**8 + 1764*h**7 - 21168*h**5 - 95040*h**4 - 233280*h**3 - 352512*h**2 - 311040*h - 124416,
}
C = {4:3, 5:12, 6:1, 7:24}
root_intervals = {4:(6135720, 6135721), 5:(4314322, 4314323),
                  6:(3808010, 3808011), 7:(3611919, 3611920)}
checks = 0

def certify(condition, description):
    global checks
    assert bool(condition), description
    checks += 1

def poly_nonnegative_coefficients(expr):
    p=sp.Poly(sp.expand(expr),h)
    return all(coef>=0 for coef in p.all_coeffs())

def positive_on_zero_to_four(numerator):
    degree=sp.degree(numerator,h)
    transformed=sp.cancel((1+u)**degree * numerator.subs(h,4*u/(1+u)))
    p=sp.Poly(transformed,u)
    return all(c>=0 for c in p.all_coeffs()) and any(c>0 for c in p.all_coeffs())

def transition(n):
    P=sp.zeros(n)
    for i in range(n):P[i,(i+1)%n]=1
    Q=P-sp.eye(n)
    B=sp.eye(n)-h*Q/sp.Integer(2)+h**2*Q**2/sp.Integer(12)
    A=sp.eye(n)+h*Q/sp.Integer(2)+h**2*Q**2/sp.Integer(12)
    return P,Q,B,B.inv()*A

for n in range(2,8):
    P,Q,B,R=transition(n)
    certify(sp.simplify(R*sp.ones(n,1)-sp.ones(n,1)) == sp.zeros(n,1),f'row sums n={n}')
    certify(sp.simplify(R[0,:]*sp.ones(n,1)-sp.ones(1,1)) == sp.zeros(1,1),f'first row n={n}')
    for j in range(n):
        # By cyclic equivariance every row is a rotation of the first.
        certify(sp.simplify(R[0,j]-R[1,(j+1)%n])==0,f'circulant n={n},j={j}')
        num,den=sp.fraction(sp.factor(R[0,j]))
        certify(sp.Poly(sp.expand(den),h).eval(0)>0,f'denominator constant n={n},j={j}')
        certify(poly_nonnegative_coefficients(den),f'denominator coefficients n={n},j={j}')
        if n in (2,3):
            if n==3 and j==0:
                certify(sp.factor(num)==h**2-2*h+4,'n=3 discriminant-positive diagonal')
            else:
                certify(poly_nonnegative_coefficients(num),f'unconditional positive n={n},j={j}')
        elif j==1:
            certify(sp.factor(num + C[n]*h*F[n])==0,f'neighbor sign polynomial n={n}')
        elif n in (4,5):
            certify(poly_nonnegative_coefficients(num),f'all other entries positive n={n},j={j}')
        else:
            certify(positive_on_zero_to_four(num),f'positive on 0<h<=4 n={n},j={j}')
    if n>=4:
        poly=sp.Poly(F[n],h)
        coefs=[sp.sign(c) for c in poly.all_coeffs() if c]
        changes=sum(coefs[k]!=coefs[k+1] for k in range(len(coefs)-1))
        certify(changes==1,f'one Descartes sign variation n={n}')
        certify(F[n].subs(h,0)<0 and sp.LC(poly)>0,f'one positive root n={n}')
        lo,hi=root_intervals[n]
        certify(F[n].subs(h,sp.Rational(lo,10**6))<0,f'lower isolator n={n}')
        certify(F[n].subs(h,sp.Rational(hi,10**6))>0,f'upper isolator n={n}')
        if n in (6,7):
            certify(F[n].subs(h,4)>0,f'root before 4 n={n}')

# Verify the first negative Taylor coefficient, the small-step obstruction for n>=8.
z=sp.symbols('z')
r=(12+6*z+z*z)/(12-6*z+z*z)
certify(sp.expand(sp.series(r,z,0,8).removeO()).coeff(z,6)==0,'Padé sixth coefficient')
certify(sp.expand(sp.series(r,z,0,8).removeO()).coeff(z,7)==-sp.Rational(1,1728),'Padé seventh coefficient')

# Group-inverse coefficient for all cycle lengths; finite checks support the symbolic identity.
for n in range(2,16):
    P=sp.zeros(n)
    for i in range(n):P[i,(i+1)%n]=1
    X=sp.zeros(n)
    for j in range(n): X+=sp.Rational(2*j-n+1,2*n)*(P**j)
    E=sp.ones(n,n)/n
    certify((P-sp.eye(n))*X==sp.eye(n)-E,f'group inverse n={n}')
    certify(X*sp.ones(n,1)==sp.zeros(n,1),f'group inverse normalization n={n}')
    certify(X[0,1]==-sp.Rational(n-3,2*n),f'neighbor Laurent coefficient n={n}')

print(f'PASS: {checks} exact symbolic/rational assertions')
print('One-step positivity: n=2,3 every h>=0; n=4..7 exactly [0,H_n]')
for n in F:
    low,high=root_intervals[n]
    print(f'n={n}: unique H_n in ({low/1e6:.6f},{high/1e6:.6f})')
print('For n>=8 one entry is negative at all sufficiently small h>0.')
print('For every n>=4 one entry is negative at all sufficiently large h.')
