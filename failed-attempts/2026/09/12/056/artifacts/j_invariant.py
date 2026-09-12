import cmath
pts=[cmath.exp(1j*cmath.pi/3),cmath.exp(-1j*cmath.pi/3),cmath.exp(2j*cmath.pi/3),cmath.exp(-2j*cmath.pi/3)]
a,b,c,d=pts
lam=(a-c)*(b-d)/((a-d)*(b-c))
print("lambda =", lam)
j=256*(1-lam+lam**2)**3/(lam**2*(1-lam)**2)
print("j =", j)
# cross ratio may permute; j invariant under S3, so any ordering same
import itertools
for perm in itertools.permutations(pts):
    a,b,c,d=perm
    lam=(a-c)*(b-d)/((a-d)*(b-c))
    j=256*(1-lam+lam**2)**3/(lam**2*(1-lam)**2)
    print([round((p.real,p.imag).__class__ and 0,2) for p in perm], complex(round(j.real,6),round(j.imag,6)))
    break
# exact: compute with sympy
import sympy as sp
w=sp.exp(2*sp.I*sp.pi/3)
rts=[sp.exp(sp.I*sp.pi/3),sp.exp(-sp.I*sp.pi/3),sp.exp(2*sp.I*sp.pi/3),sp.exp(-2*sp.I*sp.pi/3)]
a,b,c,d=rts
lam=sp.simplify((a-c)*(b-d)/((a-d)*(b-c)))
print("exact lambda =", sp.simplify(lam))
j=sp.simplify(256*(1-lam+lam**2)**3/(lam**2*(1-lam)**2))
print("exact j =", j)
