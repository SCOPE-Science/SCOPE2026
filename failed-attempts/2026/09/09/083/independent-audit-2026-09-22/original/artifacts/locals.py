#!/usr/bin/env python3
"""Local-solubility log at forced bad set S={inf,2,3,5,17} via the diagonal Q-point.
Stdlib only. Prints VERIFY_OK_LOCALS on success.
Logic: P0=(2,4,1) in U0(Q) satisfies F=0 exactly over Z (16-17=-1=(1)(-1)).
Hence for every place v, its image in X(Q_v) is a Q_v-point: for finite p this is
via Z_(p) integrality (coordinates in Z, equation holds over Z => holds in Z_p),
for inf via R. So X(Q_v)!=empty for all v in S (indeed all v), hence X(A_Q)!=empty.
This artifact independently re-checks: integrality, equation over Z, smoothness
(grad != 0 mod no confusion), and lists the per-place point (same coords).
"""
def F(x, y, z):
    return y*y - 17*z*z - (x*x - 3)*(x*x - 5)

def main():
    P0 = (2, 4, 1)
    x, y, z = P0
    assert F(x, y, z) == 0
    print(f"F{P0} = 0 over Z OK")
    # integrality => Z_p point for every p
    assert all(isinstance(c, int) for c in P0)
    print("coordinates integral => define Z_p-points for every finite p OK")
    # gradient nonzero over Q (hence smooth at P0 in every characteristic != dividing all minors;
    # smoothness over Q is what matters for X(Q)->X(Q_v) inclusion; record grad)
    dFdx = -4*x**3 + 16*x
    dFdy = 2*y
    dFdz = -34*z
    assert (dFdx, dFdy, dFdz) == (0, 8, -34) != (0, 0, 0)
    print(f"grad F(P0) = {(dFdx, dFdy, dFdz)} != 0 over Q: smooth Q-point OK")
    for v in ['inf', 2, 3, 5, 17]:
        if v == 'inf':
            # real check: 16-17+1=0 in R
            assert float(y*y - 17*z*z) == float((x*x-3)*(x*x-5))
            print(f"v=inf: P0 in X(R), real-topology verification OK")
        else:
            # p-adic check: equation mod p^k for k=1,2,3 (necessary shadow of Z_p solution;
            # sufficiency is the exact Z-equality, which implies Z_p equality)
            for k in (1, 2, 3):
                assert F(x, y, z) % (v**k) == 0
            print(f"v={v}: P0 mod {v}^k = 0 for k=1,2,3 (exact Z-equality => Z_{v} point) OK")
    print("X(Q_v) != empty for all v in S via diagonal P0 => X(A_Q) != empty (first conjunct TRUE)")
    print("VERIFY_OK_LOCALS")

if __name__ == '__main__':
    main()
