import sympy as s,itertools
w,x,y,z=s.symbols('w x y z'); v=(w,x,y,z)
Q=w*w+w*x+x*x+y*z
G=w**3+w*w*z+w*x*x+w*x*y+w*y*z+w*z*z+x**3+x*x*y+x*y*y+x*y*z
P=[t for t in itertools.product((0,1),repeat=4) if any(t) and int(Q.subs(dict(zip(v,t))))%2==0]
assert len(P)==5
assert all(int(G.subs(dict(zip(v,t))))%2==0 for t in P)
Jq=[s.diff(Q,t) for t in v];Jg=[s.diff(G,t) for t in v]; minors=[s.expand(Jq[i]*Jg[j]-Jq[j]*Jg[i]) for i in range(4) for j in range(i+1,4)]
for i in range(4):
 unknowns=[v[j] for j in range(4) if j!=i]
 B=s.groebner([h.subs(v[i],1) for h in [Q,G]+minors],*unknowns,modulus=2)
 print('chart',i,'Groebner',list(map(str,B.polys)))
 assert len(B.polys)==1 and B.polys[0].total_degree()==0
print('VERIFIED: Q has 5 points, G vanishes, geometric smoothness all charts')
