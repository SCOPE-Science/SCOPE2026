"""Independent six-representative Hessian check (requires SymPy)."""
import sympy as s
x,y,z,w=s.symbols('x y z w')
t=(1+s.sqrt(5))/2
F=4*(t*t*x*x-y*y)*(t*t*y*y-z*z)*(t*t*z*z-x*x)-(1+2*t)*(x*x+y*y+z*z-w*w)**2*w*w
reps=[
 ('infty_axis',(1,0,0,0),14),
 ('infty_cross',(1,t,t*t,0),34),
 ('sphere_axis',(1,0,0,1),18),
 ('sphere_cross',(1,t,t*t,2*t),38),
 ('outer_diagonal',(1,1,1,1),30),
 ('outer_cycle',(0,t-1,t,1),30),
]
vs=(x,y,z,w)
for name,point,power in reps:
    cc=[s.sympify(c) for c in point]
    assert s.simplify(F.subs(dict(zip(vs,cc))))==0
    assert all(s.simplify(s.diff(F,v).subs(dict(zip(vs,cc))))==0 for v in vs)
    i=next(i for i,c in enumerate(cc) if c!=0)
    other=[v for j,v in enumerate(vs) if j!=i]
    f=F.subs(vs[i],1)
    normalized={v:s.simplify(cc[j]/cc[i]) for j,v in enumerate(vs) if j!=i}
    d=s.simplify(s.hessian(f,other).subs(normalized).det())
    conjugate=d.xreplace({s.sqrt(5):-s.sqrt(5)})
    assert s.simplify(d*conjugate)==-2**power, (name,d)
print('BARTH_REPRESENTATIVE_CHECK_OK',len(reps))
