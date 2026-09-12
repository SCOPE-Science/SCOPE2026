import sympy as sp
x0,x1,x2=sp.symbols('x0 x1 x2')
F1 = x0 - x1*x2
F2 = x0**2+x1**2+x2**2+1 - x0 - x1*x2
G = x0**4+x1**4+x2**4+1
d1=[sp.diff(F1,v) for v in (x0,x1,x2)]
d2=[sp.diff(F2,v) for v in (x0,x1,x2)]
dg=[sp.diff(G,v) for v in (x0,x1,x2)]
n=0
for k in range(4):
    s=sp.exp(sp.I*sp.pi/4+k*sp.I*sp.pi/2)
    A=sp.simplify(s**2)
    disc=sp.simplify(4*s**2-4*(A+1)**2)
    sq=sp.sqrt(disc)
    for sgn in [1,-1]:
        tv=sp.simplify((2*s+sgn*sq)/(2*(A+1)))
        pt={x0:sp.simplify(s*tv),x1:sp.simplify(s),x2:sp.simplify(tv)}
        assert sp.simplify(F1.subs(pt))==0 and sp.simplify(F2.subs(pt))==0 and sp.simplify(G.subs(pt))==0
        r1=[sp.simplify(e.subs(pt)) for e in d1]
        r2=[sp.simplify(e.subs(pt)) for e in d2]
        rg=[sp.simplify(e.subs(pt)) for e in dg]
        M=sp.Matrix([r1,r2,rg]); rk=M.rank()
        B=sp.Matrix([[r1[0],r2[0]],[r1[1],r2[1]]])
        assert B.det()!=0, f"degenerate 2x2 at k={k}"
        ab=B.LUsolve(sp.Matrix([rg[0],rg[1]]))
        res=sp.simplify(ab[0]*r1[2]+ab[1]*r2[2]-rg[2])
        assert rk==2 and res==0
        assert not (sp.simplify(ab[0])==0 and sp.simplify(ab[1])==0)
        n+=1
        print(f"pt {n}: rank=2 residual=0 coeffs=({sp.simplify(ab[0])},{sp.simplify(ab[1])})")
print(f"ALL {n} POINTS OK")
