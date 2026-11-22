"""Symbolic identities and exact arithmetic coefficient checks; uses SymPy."""
import sympy as sp
A,B,C,D,z,t,u,v=sp.symbols('A B C D z t u v')
P=lambda z:A+B*z+C*z*z
Q=A*C*t*t+B*(A+C)*t+(A-C)**2+B*B-D*D
identity=sp.expand((P(z)*P(1/z)-D*D-Q.subs(t,z+1/z))*z*z)
assert sp.simplify(identity)==0, identity
# For any two distinct desired real roots with nonzero sum: all four coefficients are nonzero.
bs=-(u+v)/2; ds=(u-v)/2
fact=sp.factor(Q.subs({A:1,B:bs,C:1,D:ds}))
assert sp.simplify(fact-(t-u)*(t-v))==0, fact
# Exceptional opposite-root construction with nonzero weights when |u| <=2.
fact2=sp.factor(Q.subs({A:1,B:2,C:-1,D:sp.sqrt(8-u*u)}))
assert sp.simplify(fact2 + (t-u)*(t+u))==0, fact2
# Exact rational/surd witnesses at the small orders, evaluated at every possible spectral t.
s5=sp.sqrt(5)
levels={3:[sp.Integer(2),sp.Integer(-1)],4:[sp.Integer(2),sp.Integer(0),sp.Integer(-2)],
        5:[sp.Integer(2),(s5-1)/2,-(s5+1)/2],6:[sp.Integer(2),sp.Integer(1),sp.Integer(-1),sp.Integer(-2)]}
count=0
for m,grid in levels.items():
    interior=[x for x in grid if x!=2 and x!=-2]
    for defect in range(4 if m in (3,4) else 5):
        roots= {0:(sp.Integer(3),sp.Integer(4)),1:(sp.Integer(2),sp.Integer(3)),
                2:(interior[0],sp.Integer(3)),3:(sp.Integer(2),interior[0])}
        if defect==4:roots[4]=(interior[0],interior[1])
        x,y=roots[defect]
        if sp.simplify(x+y)!=0:
            bs=-(x+y)/2;ds=(x-y)/2;a,c=1,1
        else:
            a,c=1,-1;bs=2;ds=sp.sqrt(8-x*x)
        assert all(sp.simplify(w)!=0 for w in (a,bs,c,ds))
        expr=sp.factor(Q.subs({A:a,B:bs,C:c,D:ds}))
        roots_set={str(sp.simplify(w)) for w in (x,y)}
        matched=[w for w in grid if sp.simplify(expr.subs(t,w))==0]
        packet=sum(1 if w in (2,-2) else 2 for w in matched)
        assert packet==defect, (m,defect,matched,expr)
        count+=1
print('PASS symbolic determinant, two-root constructions,',count,'exact small-order examples')
