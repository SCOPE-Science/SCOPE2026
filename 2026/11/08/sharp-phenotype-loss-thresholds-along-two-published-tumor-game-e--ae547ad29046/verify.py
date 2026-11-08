"""Exact-rational verification of three four-phenotype replicator scenario matrices.
Dependencies: Python 3.11+, sympy. Run: python verify.py
"""
import sympy as S
x=S.symbols('x0:4'); t=S.symbols('t'); lam=S.symbols('lam');
R=lambda rows:S.Matrix([[S.Rational(z) for z in row] for row in rows])
A0=R([['.90','.90','.95','.92'],['1.05','.85','.95','.92'],['1.02','1.00','.75','.92'],['1.03','1.04','1.00','.80']])
Ac=R([['.88','.85','.90','.88'],['1.10','.88','1.00','.90'],['1.05','1.05','.80','.92'],['1.00','1.02','.95','.78']])
Ab=R([['.92','.90','.95','.93'],['1.00','.85','.90','.90'],['.95','.95','.75','.90'],['1.05','1.05','1.00','.82']])
B=S.Matrix([[1,0,0],[0,1,0],[0,0,1],[-1,-1,-1]])
minors={
 'base':[-S.Rational(1,4),S.Rational(451,10000),-S.Rational(47263,4000000)],
 'acid':[-S.Rational(11,50),S.Rational(1447,40000),-S.Rational(32387,4000000)],
 'buffer':[-S.Rational(6,25),S.Rational(1167,40000),-S.Rational(911,160000)],
}
for k,M in [('base',A0),('acid',Ac),('buffer',Ab)]:
 H=B.T*(M+M.T)*B/2
 assert [H[:i,:i].det() for i in (1,2,3)]==minors[k]
 assert minors[k][0]<0 and minors[k][1]>0 and minors[k][2]<0
base=S.Matrix([120,360,252,655])/1387
assert A0*base==S.ones(4,1)*S.Rational(1274,1387)
scenarios=[
 ('acid',Ac,0,t**3-2*t**2+234*t-60,34*t**3-186*t**2+2173*t-13870,S.Matrix([0,-10*(2*t*t-t+24),2*(5*t*t-31*t-90),5*(4*t*t+48*t-91)])/(10*t*t+188*t-875)),
 ('buffer',Ab,2,41*t**3-712*t**2+3201*t-2520,31*t**3-1382*t*t+7871*t-13870,S.Matrix([(3*t*t+37*t+60),(7*t*t-138*t+180),0,-(7*t*t+83*t-275)])/(3*t*t-184*t+515)),
]
for tag,endpoint,absent,g,D,q in scenarios:
 M=A0+t*(endpoint-A0)
 zz=S.Matrix(x)
 # full equilibrium direct linear solve, compare symbolic expression for excluded coordinate
 equations=list(M*zz-lam*S.ones(4,1))+[sum(x)-1]
 sol=S.solve(equations, list(x)+[lam]); p=S.Matrix([S.factor(sol[z]) for z in x]);assert S.simplify((M*p)[0]-(M*p)[1])==0
 assert S.simplify(p[absent] - (20*g/D if tag=='acid' else g/D))==0
 # face is a valid normalized fixed point; invasion gap exact formula
 F=[i for i in range(4) if i!=absent]
 assert S.simplify(sum(q)-1)==0
 for i in F[1:]:assert S.simplify((M*q)[i]-(M*q)[F[0]])==0
 gap=S.factor((M*q)[absent]-(M*q)[F[0]])
 expected=g/(5*(10*t*t+188*t-875)) if tag=='acid' else -g/(100*(3*t*t-184*t+515))
 assert S.factor(gap-expected)==0
 roots=[float(S.re(r)) for r in S.nroots(g) if abs(float(S.im(r)))<1e-10 and 0<float(S.re(r))<1]
 assert len(roots)==1
 threshold=roots[0]
 if tag=='acid': assert .2569<threshold<.2570
 else:assert .9947<threshold<.9948
 for test in [S.Rational(0),S.Rational(1,10),S.Rational(1,4),S.Rational(1,2),S.Rational(9,10),S.Rational(99,100),S.Rational(999,1000),S.Rational(1)]:
  arr=[el.subs(t,test) for el in p]
  if float(test)<threshold:assert all(z>0 for z in arr)
  else:
   assert all(q[i].subs(t,test)>0 for i in F)
   assert gap.subs(t,test)<0
 # exact endpoints and invasion loss
 p_end=[S.simplify(v.subs(t,1)) for v in q]
 assert p_end[absent]==0
 assert sum(p_end)==1
 assert S.factor(gap.subs(t,1))==(-S.Rational(173,3385) if tag=='acid' else -S.Rational(1,3340))
 print(tag,'threshold',threshold,'endpoint',p_end,'invasion gap',gap.subs(t,1))
print('PASS: exact matrices, negative tangent Hessians, equilibria, endpoint margins, interpolation thresholds')
