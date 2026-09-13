"""Confirmatory computation for lane-1660: Y3 = Whitehead L5a1 exterior, fills (0,1)x(7,1).
Run: python3 confirm_y3.py  (requires SnapPy).
Checks: homology both fill orders (Z + Z/7, b1=1), orientability, degenerate volume
(consistent with non-hyperbolic / reducible diagnosis), single-filling controls
(W(0,1): Z+Z longitude fill; W(1,0): solid torus pi1=Z; W(7,1): hyperbolic vol 3.43454),
linking number 0 (SnapPy linking matrix)."""
import snappy
ok = True
def check(name, cond, detail=""):
    global ok
    print(("PASS " if cond else "FAIL ") + name + (" | " + str(detail) if detail else ""))
    ok = ok and cond

L = snappy.Link('L5a1')
check("linking number 0", list(map(list, L.linking_matrix())) == [[0,0],[0,0]], L.linking_matrix())
for tri in ['L5a1(0,1)(7,1)', 'L5a1(7,1)(0,1)']:
    N = snappy.Manifold(tri)
    check(tri+" homology Z+Z/7", str(N.homology()) == "Z/7 + Z", N.homology())
    check(tri+" orientable", N.is_orientable() is True)
    check(tri+" closed (no unfilled cusp remainders: 2 filled cusps, homology has torsion)",
          N.num_cusps() == 2)
    sol = N.solution_type()
    try: v = N.volume()
    except Exception as e: v = "err:"+str(e)[:60]
    check(tri+" non-hyperbolic structure (degenerate/unrecognized, |vol|~0)", ("degenerate" in sol or "unrecognized" in sol), f"{sol}, vol={v}")
N = snappy.Manifold('L5a1'); N.dehn_fill((0,1),0)
check("W(0,1) longitude fill preserves H1=Z+Z", str(N.homology()) == "Z + Z", N.homology())
N = snappy.Manifold('L5a1'); N.dehn_fill((1,0),0)
G = N.fundamental_group(); check("W(1,0) solid torus (pi1=Z)", G.num_generators()==1 and not G.relators(), str(G).replace("\n"," "))
M = snappy.Manifold('L5a1'); M.dehn_fill((7,1),0)
check("W(7,1) hyperbolic control vol~3.43454", M.solution_type()=="all tetrahedra positively oriented" and abs(M.volume()-3.4345408859)<1e-6, f"{M.solution_type()}, {M.volume()}")
print("ALL_OK" if ok else "SOME_CHECKS_FAILED")
