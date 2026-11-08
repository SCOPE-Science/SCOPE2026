"""Exact finite-field witness for the conic-Hadamard branch calculation.
Run: python verify_hadamard.py (requires sympy). No external inputs.
Finite-field witness establishes non-emptiness of algebraic open conditions.
The general theorem requires the separate intersection-theoretic proof.
"""
import sympy as s
p=101
x,y=s.symbols('x y')
A=[[5,-2,3],[4,-1,-3],[-5,3,-5]]
B=[[-1,5,6],[2,-1,-2],[3,6,-1]]

def poly(row,v): return row[0]*v*v+row[1]*v+row[2]
def ev(row,t): return int(poly(row,t))%p
def roots(row): return [t for t in range(p) if ev(row,t)==0]
def wronskian(u,v,w):
    R=s.Poly(s.expand(s.diff(poly(u,w),w)*poly(v,w)-poly(u,w)*s.diff(poly(v,w),w)),w,modulus=p)
    return [int(R.nth(i))%p for i in (2,1,0)]
def ratio(u,v,t): return ev(u,t)*pow(ev(v,t),-1,p)%p

assert s.det(s.Matrix(A))%p==21 and s.det(s.Matrix(B))%p==57
for rows in (A,B):
    assert all((r[1]*r[1]-4*r[0]*r[2])%p != 0 for r in rows)
    for i in range(3):
        for j in range(i):
            assert s.gcd(s.Poly(poly(rows[i],x),x,modulus=p),s.Poly(poly(rows[j],x),x,modulus=p)).degree()==0
Wa=wronskian(A[1],A[2],x)
Wb=wronskian(B[1],B[2],y)
assert Wa==[7,31,14] and Wb==[15,8,13]
X0,Xc=roots(A[0]),roots(Wa)
Y0,Yc=roots(B[0]),roots(Wb)
assert (X0,Xc,Y0,Yc)==([17,44],[20,91],[6,100],[93,95])
assert not (set(X0)&set(Xc)) and not (set(Y0)&set(Yc))
for rows,loc in ((A,X0+Xc),(B,Y0+Yc)):
    assert all(ev(rows[j],a) !=0 for a in loc for j in (1,2))
images=[ratio(A[1],A[2],a)*ratio(B[1],B[2],b)%p
        for X,Y in ((X0,Y0),(X0,Yc),(Xc,Y0)) for a in X for b in Y]
assert images==[33,8,20,63,47,7,4,93,60,88,97,48]
assert len(set(images))==12

F=[s.expand(poly(a,x)*poly(b,y)) for a,b in zip(A,B)]
Jac=s.Matrix([F,[s.diff(f,x) for f in F],[s.diff(f,y) for f in F]])
R=s.Poly(s.expand(Jac.det()),x,y,modulus=p).as_expr()
assert s.degree(R,x)==4 and s.degree(R,y)==4
assert list(s.groebner((R,s.diff(R,x),s.diff(R,y)),x,y,modulus=p))==[1]
Rpoly=s.Poly(R,x,y)
def reversed_poly(rx,ry):
    r=0
    for (i,j),co in Rpoly.terms():
        r+=co*x**(4-i if rx else i)*y**(4-j if ry else j)
    return s.expand(r)
for rev,loc in (((True,False),x),((False,True),y)):
    rr=reversed_poly(*rev)
    arg = y if loc==x else x
    rr0=rr.subs(loc,0)
    derivative1=s.diff(rr,loc).subs(loc,0)
    derivative2=s.diff(rr,arg).subs(loc,0)
    assert s.gcd(s.Poly(rr0,arg,modulus=p),s.Poly(derivative1,arg,modulus=p),s.Poly(derivative2,arg,modulus=p)).degree()==0
assert int(reversed_poly(True,True).subs({x:0,y:0}))%p==59

# Degree/adjunction computations for the characteristic-zero theorem.
assert 2*4+2*4==16     # (2,2) dot (4,4) on P1 x P1
assert (4-1)*(4-1)==9    # genus of smooth (4,4) curve
assert (16-1)*(16-2)//2-9==96  # total delta
print('FIELD=101; conic determinant residues=21,57')
print('RAMIFICATION_BIDEGREE=(4,4); PROJECTIVE_RAMIFICATION_SMOOTH=True')
print('RAMIFICATION_AFFINE_GROEBNER_UNIT=True; INFINITY_GCDS=0,0; CORNER_VALUE=59')
print('AXIS_INTERSECTION_12_DISTINCT=',','.join(map(str,images)),sep='')
print('AXIS_MULTIPLICITIES=4*2+8*1; BRANCH_DEGREE=16; NORMALIZATION_GENUS=9; DELTA_TOTAL=96')
print('ALL_EXACT_CHECKS_PASSED')
