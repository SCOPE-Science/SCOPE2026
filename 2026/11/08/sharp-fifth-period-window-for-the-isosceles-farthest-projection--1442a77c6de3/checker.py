"""Exact symbolic checks for the fifth-period isosceles farthest-projection classification.
Run with: python checker.py (requires SymPy). This complements, not substitutes for, the proof.
"""
import itertools
import sympy as S

h=S.symbols('h',positive=True)
u=S.symbols('u',positive=True)
A=S.Matrix([-1,0]); B=S.Matrix([1,0]); C=S.Matrix([0,h])
lines=[(A,B-A),(A,C-A),(B,C-B)]
M=[];c=[]
for p,d in lines:
    m=S.simplify(d*d.T/d.dot(d)); M.append(m);c.append(S.simplify(p-m*p))

def project(x,j): return M[j]*x+c[j]
def orbit_for_word(w):
    mat=S.eye(2);offset=S.zeros(2,1)
    for j in w[1:]+w[:1]:
        mat=M[j]*mat;offset=M[j]*offset+c[j]
    x=((S.eye(2)-mat).inv()*offset).applyfunc(S.factor)
    pts=[x]
    for j in w[1:]:pts.append(project(pts[-1],j).applyfunc(S.factor))
    assert all(S.simplify(z)==0 for z in project(pts[-1],w[0])-x)
    return pts, mat

def sqnorm(x):return x.dot(x)
def branch_gap(w,pts,i):
    j=w[(i+1)%len(w)];k=({0,1,2}-{w[i],j}).pop()
    return S.factor(sqnorm(pts[i]-project(pts[i],j))-sqnorm(pts[i]-project(pts[i],k)))

words=[w for w in itertools.product(range(3),repeat=5)
       if all(w[j]!=w[(j+1)%5] for j in range(5))
       and w==min(w[k:]+w[:k] for k in range(5))]
assert len(words)==6
Z=u**3+5*u**2+3*u+7
Q1=u**5+4*u**4+10*u**3+4*u**2+5*u-8
Q2=u**5-3*u**4-10*u**3-22*u**2-15*u-15
Q3=u**5-12*u**4-10*u**3-20*u**2-15*u-8
Q4=u**6-22*u**5-u**4-52*u**3-17*u**2-22*u-15
assert S.factor(Q2-Q3-(u*u-1)*(9*u*u+7))==0
assert Q3.subs(u,12)<0<Q3.subs(u,13)
assert Q4.subs(u,22)<0<Q4.subs(u,23)
assert Q3.subs(u,16)>0>Q4.subs(u,16)
# One positive root each, since coefficients have exactly one change of sign.
assert len([x for x in S.Poly(Q3,u).all_coeffs() if x!=0])==6
for q in [Q3,Q4]:
    v=[S.sign(x) for x in S.Poly(q,u).all_coeffs()];assert sum(a!=b for a,b in zip(v,v[1:]))==1

for w in words:
    pts,mat=orbit_for_word(w)
    if w in [(0,1,2,1,2),(0,2,1,2,1)]:
        sgn=1 if w[1]==1 else -1
        assert S.simplify(pts[0][0]-sgn*(h*h-1)**3/Z.subs(u,h*h))==0
        expected=[4*h*h*(h*h-1)**3/((h*h+1)*Z.subs(u,h*h)),
                  4*h*h*Q1.subs(u,h*h)/Z.subs(u,h*h)**2,
                  4*h*h*Q2.subs(u,h*h)/Z.subs(u,h*h)**2,
                  4*h*h*Q3.subs(u,h*h)/Z.subs(u,h*h)**2,
                  -4*h*h*Q4.subs(u,h*h)/((h*h+1)*Z.subs(u,h*h)**2)]
        for i,x in enumerate(expected): assert S.factor(branch_gap(w,pts,i)-x)==0,(w,i)
        assert S.factor(mat[0,0]+(h*h-1)**3/(h*h+1)**4)==0
    elif w in [(0,1,0,1,2),(0,2,0,2,1)]:
        assert S.factor(branch_gap(w,pts,1)+4*h*h*(h**8+h**6+2*h**4+h*h+3)/((h*h+1)*(h*h-h+2)**2*(h*h+h+2)**2))==0
    else:
        # Reflection pair has a necessary h<1 condition and a contradictory later test.
        early=0 if w==(0,1,0,2,1) else 3
        late=3 if w==(0,1,0,2,1) else 1
        assert S.factor(branch_gap(w,pts,early)+4*h**4*(h*h-1)/((h*h+1)*(h*h-h+2)*(h*h+h+2)))==0
        f=h**3-2*h*h+2*h-2;g=h**3+2*h*h+2*h+2
        assert S.factor(branch_gap(w,pts,late)-4*h*h*f*g/((h*h-h+2)**2*(h*h+h+2)**2))==0

# Independent exact-rational itinerary check for a diverse range of heights.
for hn in [S.Rational(1,2),S.Rational(9,10),S.Integer(1),S.Rational(3,2),
           S.Integer(3),S.Rational(7,2),S.Rational(18,5),S.Integer(4),
           S.Rational(47,10),S.Rational(24,5),S.Integer(5),S.Integer(8)]:
    expected=2 if Q3.subs(u,hn*hn)>0 and Q4.subs(u,hn*hn)<0 else 0
    count=0
    for w in words:
        pts,_=orbit_for_word(w)
        if all(branch_gap(w,pts,j).subs(h,hn)>0 for j in range(5)):count+=1
    assert count==expected,(hn,count,expected)
print('PASS: all six cyclic line words, 30 symbolic gap identities, root signs, multipliers and 12 exact-rational height censuses')
