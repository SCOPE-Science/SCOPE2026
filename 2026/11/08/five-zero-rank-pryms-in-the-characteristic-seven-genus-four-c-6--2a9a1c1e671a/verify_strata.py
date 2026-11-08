"""Exact modular elimination and sample stable-rank checks for a genus-four family.
Run: python verify_strata.py   (requires SymPy).
"""
import sympy as S
A,B,X=S.symbols('a b x')
p=7
m=lambda f:S.Poly(f,A,B,modulus=p)
u=A**3+6*A*B+3*B**2
v=3*A**2+3*A+6*B
Delta=A**2+3*A**3+3*B+B**2+4*A*B
BV=3*A*(A+1)
assert m(v.subs(B,BV)).is_zero
assert m(u.subs(B,BV)+A**2*(A+2)**2).is_zero
assert m(Delta.subs(B,BV)-2*A*(A+2)**3).is_zero
# The formal matrix is C_{ij} = coefficient of x^(7*i-j) in f^3.
f=S.Poly(X**10+X**7+A*X**4+B*X,X)**3
M=S.Matrix(4,4,lambda i,j:S.Poly(f,X).coeff_monomial(X**(7*(i+1)-(j+1))))
assert m(M.det()-3*B**2*u*v**2).is_zero
# On v=0, the rank-one 2x2 Cartier block has stable rank zero
# precisely when w^(7) v_vec = 0; the nontrivial factor is T.
T=2*A**3+(A+1)**5
assert m((A*BV**2+(A+1)**7)-(A+1)**2*T).is_zero
Q=S.Poly(T,A,modulus=p)
assert S.Poly(T-(A-2)*(A-3)*(A**3+3*A**2-1),A,modulus=p).is_zero
assert all((int((A**3+3*A**2-1).subs(A,t))%7)!=0 for t in range(7))
assert Q.degree()==5
assert S.gcd(Q,Q.diff()).degree()==0
assert S.gcd(Q,S.Poly(A*(A+1)*(A+2),A,modulus=p)).degree()==0
# Compare with smooth discriminant on the entire parabola.
assert S.gcd(Q,S.Poly(Delta.subs(B,BV),A,modulus=p)).degree()==0
# The scalar u vanishes on the v-parabola only at singular parameters.
assert S.gcd(S.Poly(u.subs(B,BV),A,modulus=p),Q).degree()==0

def rank7(Q):
    vals=[[int(x)%7 for x in row] for row in Q.tolist()]
    i=0
    for j in range(len(vals[0])):
        where=next((t for t in range(i,len(vals)) if vals[t][j]%7),None)
        if where is None: continue
        vals[where],vals[i]=vals[i],vals[where]
        inv=pow(vals[i][j],-1,7)
        vals[i]=[(z*inv)%7 for z in vals[i]]
        for t in range(len(vals)):
            if t==i: continue
            c=vals[t][j]
            vals[t]=[(w-c*z)%7 for w,z in zip(vals[t],vals[i])]
        i+=1
        if i==len(vals):break
    return i

def smooth(a,b):
    F=S.Poly(X**10+X**7+a*X**4+b*X,X,modulus=p)
    return S.gcd(F,F.diff()).degree()==0
counts={}
for a in range(p):
    for b in range(p):
        ok=(b*int(Delta.subs({A:a,B:b})))%7 !=0
        assert smooth(a,b)==ok
        if not ok:continue
        V=M.subs({A:a,B:b}).applyfunc(lambda z:int(z)%7)
        cr=rank7(V)
        stable=rank7((V**4).applyfunc(lambda z:int(z)%7))
        z=(stable,4-cr)
        counts[z]=counts.get(z,0)+1
        if int(v.subs({A:a,B:b}))%7==0:
            assert cr==2
            if int(T.subs(A,a))%7==0: assert stable==1
            else: assert stable==2
        elif int(u.subs({A:a,B:b}))%7==0:
            assert (stable,cr)==(3,3)
        else:
            assert (stable,cr)==(4,4)
assert counts[(1,2)]>=2 and counts[(2,2)]>=1 and counts[(3,1)]>=1 and counts[(4,0)]>=1
print('C7_RANK_STRATA_GF7_PASS',counts)
print('C7_EXACT_FIVE_GEOMETRIC_PRYM_RANK_ZERO_PARAMETERS_PASS')
