from sympy import Matrix, Rational, symbols, Poly, simplify, factor, pi, I, sqrt
U=Rational(1,4); V=Rational(1,2); P=Rational(1); rU=12;rV=13;c=5;gamma=8;kappa=1;delta=Rational(1,2);muU=1;muV=7;D=Rational(1,4)
assert rU*P-c-gamma*(U+V)-muU==0
assert rV*P-gamma*(U+V)-muV==0
assert c*U-(kappa*(U+V)+delta)*P==0
q,w,z=symbols('q w z',real=True)
M=Matrix([[-gamma*U-D*q,-gamma*U,rU*U],[-gamma*V,-gamma*V-D*q,rV*V+2*w*D*V*q],[c-kappa*P,-kappa*P,-kappa*(U+V)-delta-D*q]])
coefs=M.charpoly(z).all_coeffs()
A,B,C=coefs[1:]
Aex=(3*q+29)/4; Bex=(3*q*q+4*q*w+58*q+32)/16; Cex=(q**3+4*q*q*w+29*q*q+160*q*w+32*q+320)/64
H=factor(A*B-C); Hex=(4*q**3+4*q*q*w+116*q*q-22*q*w+873*q+304)/32
for f,g in [(A,Aex),(B,Bex),(C,Cex),(H,Hex)]: assert simplify(f-g)==0
w1=Rational(1297,18);w2=Rational(1477,6)
assert simplify(H.subs({q:1,w:w1}))==0
assert simplify(H.subs({q:4,w:w2}))==0
assert simplify(H.subs({q:1,w:73}))<0
assert simplify(H.subs({q:4,w:247}))<0
assert simplify(H.subs({q:4,w:w1}))>0
assert simplify(H.subs({q:1,w:w2}))<0
assert simplify(H.subs({q:0,w:100000}))>0
B1=simplify(B.subs({q:1,w:w1}));B2=simplify(B.subs({q:4,w:w2}))
assert B1==Rational(3431,144); assert B2==Rational(797,3)
print('All exact identities, physical equilibrium, Hopf thresholds, mode regimes PASS')
print('M(q,w) =',M)
print('A,B,C,H =',Aex,Bex,Cex,Hex)
print('First Hopf w=',w1,'frequency square=',B1)
print('Second Hopf w=',w2,'frequency square=',B2)
for j,ww in [(0,0),(1,0),(1,73),(2,73),(2,247),(3,10000)]:
 qv=j*j; Mv=M.subs({q:qv,w:ww}); vals=[complex(v) for v in Mv.eigenvals(multiple=True)]
 print('mode',j,'w=',ww,'Re eigenvalues', [round(v.real,6) for v in vals], 'Im eigenvalues',[round(v.imag,6) for v in vals])
