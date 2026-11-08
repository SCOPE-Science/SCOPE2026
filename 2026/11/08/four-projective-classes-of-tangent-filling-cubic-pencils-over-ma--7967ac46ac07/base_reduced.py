import runpy,sympy as s
D=runpy.run_path('/mnt/data/research14_tf_pencils_20261103/public/enumerate_tf_pencils.py')
x,y,z=s.symbols('x y z');v=(x,y,z)
for p,n in D['orbits']:
 F=[]
 for c in p[:2]:F.append(s.expand(sum(int(D['TF'][c][i])*s.prod(v[j]**e[j] for j in range(3)) for i,e in enumerate(D['EXPS']))))
 f,g=F
 grads=[[s.diff(k,u) for u in v] for k in F]
 minors=[grads[0][i]*grads[1][j]-grads[1][i]*grads[0][j] for i in range(3) for j in range(i+1,3)]
 ok=[]
 for i in range(3):
  eqs=[s.expand(h.subs({v[i]:1})) for h in [f,g]+minors]
  B=s.groebner(eqs,*[u for j,u in enumerate(v) if j!=i],modulus=3)
  ok.append(any(u.as_expr()==1 for u in B.polys))
 print(p,'reduced',ok)
