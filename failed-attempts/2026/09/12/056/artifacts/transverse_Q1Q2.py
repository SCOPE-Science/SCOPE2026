import sympy as sp
x0,x1,x2,x3=sp.symbols('x0 x1 x2 x3')
F1=x0*x3-x1*x2
F2=x0**2+x1**2+x2**2+x3**2-x0*x3-x1*x2
d1=[sp.diff(F1,v) for v in (x0,x1,x2,x3)]
d2=[sp.diff(F2,v) for v in (x0,x1,x2,x3)]
import itertools
minors=[d1[i]*d2[j]-d1[j]*d2[i] for i,j in itertools.combinations(range(4),2)]
G=sp.groebner([F1,F2]+minors+[x0-1],x0,x1,x2,x3,order='lex')
print("chart x0=1:", G.polys)
for ch,eq in [(1,'x1-1'),(2,'x2-1'),(3,'x3-1')]:
    v=(x0,x1,x2,x3)
    G=sp.groebner([F1,F2]+minors+[v[ch]-1],*v,order='grlex')
    const=any(p.is_number for p in G.polys)
    print(f"chart x{ch}=1: len {len(G.polys)}, const present: {const}")
