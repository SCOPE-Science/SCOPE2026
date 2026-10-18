#!/usr/bin/env python3
import sympy as sp

S,Q,E,I,A,R=sp.symbols("S Q E I A R", positive=True)
beta,theta,u1,u2,u3=sp.symbols("beta theta u1 u2 u3", positive=True)
mu,muI,sigma,rho,gI,gA,lam=sp.symbols("mu muI sigma rho gI gA lam", positive=True)
Recruit,A1,A2,B1,B2,B3=sp.symbols("Recruit A1 A2 B1 B2 B3", positive=True)
l1,l2,l3,l4,l5,l6=sp.symbols("l1 l2 l3 l4 l5 l6")

N=S+Q+E+I+A+R
U=u1*I+u2*A
V=I+theta*A
F=beta*sp.exp(-U/N)*S*V/N

fS=-F-u3*S+lam*Q+Recruit-mu*S
fQ=u3*S-lam*Q-mu*Q
fE=F-sigma*E-mu*E
fI=sigma*rho*E-gI*I-muI*I-mu*I
fA=sigma*(1-rho)*E-gA*A-mu*A
fR=gI*I+gA*A-mu*R
H=A1*I+A2*A+B1*u1**2/2+B2*u2**2/2+B3*u3**2/2+l1*fS+l2*fQ+l3*fE+l4*fI+l5*fA+l6*fR

FS=sp.diff(F,S); FQ=sp.diff(F,Q); FE=sp.diff(F,E); FI=sp.diff(F,I); FA=sp.diff(F,A); FR=sp.diff(F,R)
assert sp.simplify(FS-F*(1/S-1/N+U/N**2))==0
assert sp.simplify(FQ-F*(-1/N+U/N**2))==0
assert sp.simplify(FE-FQ)==0
assert sp.simplify(FR-FQ)==0
assert sp.simplify(FI-F*(1/V-(u1+1)/N+U/N**2))==0
assert sp.simplify(FA-F*(theta/V-(u2+1)/N+U/N**2))==0

correct=[
 (l1-l3)*FS+(l1-l2)*u3+mu*l1,
 (l1-l3)*FQ+(l2-l1)*lam+mu*l2,
 (l1-l3)*FE+(l3-l5)*sigma+(l5-l4)*sigma*rho+mu*l3,
 -A1+(l1-l3)*FI+(l4-l6)*gI+(muI+mu)*l4,
 -A2+(l1-l3)*FA+(l5-l6)*gA+mu*l5,
 (l1-l3)*FR+mu*l6,
]
for state,rhs in zip((S,Q,E,I,A,R),correct):
    assert sp.simplify(-sp.diff(H,state)-rhs)==0

# Printed recovered equation omits a generically nonzero incidence derivative.
printed_l6=mu*l6
assert sp.simplify(correct[5]-printed_l6-(l1-l3)*FR)==0
# Printed susceptible u3 coefficient is wrong.
assert sp.diff(correct[0],u3)==l1-l2
# Correct exposed non-incidence rho coupling carries sigma.
noninc_l3=sp.simplify(correct[2]-(l1-l3)*FE-mu*l3)
assert sp.simplify(noninc_l3-((l3-l5)*sigma+(l5-l4)*sigma*rho))==0

# Exact interior witness for omitted recovered-costate term.
w={S:1,Q:1,E:1,I:1,A:1,R:1,beta:1,theta:1,u1:sp.Rational(1,2),u2:sp.Rational(1,2),l1:1,l3:3}
omitted=sp.simplify(((l1-l3)*FR).subs(w))
assert omitted != 0
assert sp.simplify(omitted-5*sp.exp(-sp.Rational(1,6))/54)==0

print("VERIFY_OK")
print("F_R_witness", omitted)
print("u3_coefficient_correct", l1-l2)
print("exposed_rho_term", sigma*rho*(l5-l4))
