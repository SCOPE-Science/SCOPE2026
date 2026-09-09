import sys; sys.path.insert(0,'output/artifacts')
import sympy as sp
from burau import alexander, perm
t=sp.Symbol('t')
w0=[1,1,1,-2,-1,-1,-1,-2]
def degdiff(d):
    p=sp.Poly(sp.expand(d*sp.Symbol('t')**8),sp.Symbol('t'))
    ds=[m[0] for m in p.monoms() if p.coeff_monomial(m)!=0]
    return (max(ds)-min(ds)) if ds else 0
print("base:", alexander(w0,3), "degdiff=", degdiff(alexander(w0,3)))
for site in range(9):
    for axis in (1,2):
        for sgn in (1,-1):
            w=w0[:site]+[sgn*axis,sgn*axis]+w0[site:]
            p=perm(w,3)
            # knot closure iff single cycle
            cyc=len(set(p))==3 and not any(p[i]==i for i in range(3)) and (p[p[p[0]]]==p[0])
            # proper single-cycle check
            v=0; seen=set()
            for _ in range(3): seen.add(v); v=p[v]
            knot = (len(seen)==3)
            try:
                d=sp.expand(alexander(w,3))
                dd=degdiff(d)
                print(f"site={site} axis={axis} sgn={sgn:+d} knot={knot} degdiff={dd} D={d} det={abs(complex(d.subs(t,-1)))}")
            except Exception as e:
                print(f"site={site} axis={axis} sgn={sgn:+d} knot={knot} ERROR {e}")
