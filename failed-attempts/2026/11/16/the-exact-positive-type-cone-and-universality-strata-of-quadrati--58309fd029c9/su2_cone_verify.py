"""Exact checks for SU(2) character-modulated Abel kernels.
Dependency: SymPy. Run: python su2_cone_verify.py
"""
import sympy as S
r,s,t=S.symbols('r s t', real=True)
H0=1+2*r*s+3*r**2*t
H1=1+(1+3*r**2)*s/(2*r)+(1+2*r**2)*t
Hinf=1+(r+1/r)*s+(1+r**2+r**-2)*t
b=lambda n:(n+1)*r**n
# Clebsch-Gordan: chi_1 chi_j=chi_(j+1)+chi_(j-1); chi_2 chi_j=chi_(j+2)+chi_j+chi_(j-2), omitting negative labels.
def from_fusion(n):
    c=b(n)
    c+=s*sum(b(j) for j in range(n+3) if j+1==n or (j>=1 and j-1==n))
    c+=t*sum(b(j) for j in range(n+3) if j+2==n or (j>=1 and j==n) or (j>=2 and j-2==n))
    return S.expand(c)
assert S.simplify(from_fusion(0)-H0)==0
for n in range(1,31):
    pred=b(n)*(Hinf+S.Rational(2,n+1)*(H1-Hinf))
    assert S.simplify(from_fusion(n)-pred)==0,n
vertices=[]
for i,j in [(0,1),(1,2),(0,2)]:
    h=[H0,H1,Hinf]
    sol=S.solve([h[i],h[j]],[s,t]);vertices.append(sol)
    assert all(S.simplify(x.subs(sol))==0 for x in [h[i],h[j]])
    print('facet pair',i,j,{str(k):S.factor(v) for k,v in sol.items()},'third',S.factor(h[3-i-j].subs(sol)))
# first two feasibility for all 0<r<1, third excluded
assert S.simplify(Hinf.subs(vertices[0])-(1-r**2)/r**4)==0
assert S.simplify(H0.subs(vertices[1])-(1-r**2)/(1+3*r**2+r**4))==0
assert S.simplify(H1.subs(vertices[2])-(r**2-1)/(2*r**2*(r**2+2)))==0
# constant kernel at H1=Hinf=0
v=vertices[1]
u=S.symbols('u')
poly=1+s*(2*u)+t*(4*u*u-1)
assert S.simplify(poly.subs(v)-(1-2*r*u+r*r)**2/(1+3*r*r+r**4))==0
# sum_{n>=0} (n+1)r^n U_n(u)=(1-r**2)/(1-2ru+r^2)^2 by generating function
# particular generic rational point and their positivity strata
for rv in [S.Rational(1,2),S.Rational(2,3),S.Rational(3,4)]:
    vals=[{k:z.subs(r,rv) for k,z in sol.items()} for sol in vertices]
    assert S.factor(Hinf.subs(vals[0]).subs(r,rv))>0
    assert S.factor(H0.subs(vals[1]).subs(r,rv))>0
    assert S.factor(H1.subs(vals[2]).subs(r,rv))<0
print('CHECK_OK fusion_degree=30 vertex_pairs=3 exact_factorization=1 rational_tests=9')
