"""Exact polynomial certificates for the 28-bitangent construction.
Requires SymPy. No numerical or floating-point operations.
"""
import sympy as s
X,Y,Z,L,T=s.symbols('X Y Z L T')
F=X**4+Y**4+Z**4+L*(X**2*Y**2+X**2*Z**2+Y**2*Z**2)
R=(L+2)*(T**4+1)+2*L*T**2

def zero(expr):
    assert s.cancel(expr)==0,s.factor(expr)

# Four permanent diagonals.
zero(F.subs(X,-Y-Z)-(L+2)*(Y**2+Y*Z+Z**2)**2)

# Twelve coordinate-sparse lines; all powers of T are reduced modulo R.
rest=s.expand(F.subs(X,-T*Y))
sq=(Z**2+s.Rational(1,2)*L*(1+T**2)*Y**2)**2
zero(s.factor(rest-sq)-(2-L)*R*Y**4/s.Integer(4))

# Twelve all-nonzero additional lines, over the field with T^2=-1/(L+1).
rest=s.expand(F.subs(X,-T*(Y+Z)))
sq=(L+2)/(L+1)**2*(Y**2-(L-1)*Y*Z+Z**2)**2
num=s.together(rest-sq).as_numer_denom()[0]
red=s.Poly(num,T).rem(s.Poly((L+1)*T**2+1,T)).as_expr()
zero(red)

# Smoothness condition from Jacobian: solutions with two nonzero squares
# force L=+/-2; three nonzero squares force L=2 or L=-1.
J=s.Matrix([[2,L,L],[L,2,L],[L,L,2]])
zero(s.factor(J.det())-(2-L)**2*(2+2*L))

# For every nonsingular parameter the displayed 4+12+12 lines are distinct:
# R(0) = L+2, R(1)=4(L+1), R(-1)=4(L+1),
# R(T) at T^2=-1 is 4; and the all-nonzero family never has T^2=1.
zero(R.subs(T,0)-(L+2))
zero(R.subs(T,1)-4*(L+1))
zero(s.rem(R,T**2+1,T)-4)
print('VERIFY_SYMBOLIC_OK')
