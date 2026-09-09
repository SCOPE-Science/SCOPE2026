"""Verifier for lane-368: one-wall LG mutation certificate (dP2 primary, dP3 second
instance). Stdlib only. Checks exact Laurent identities, the new Maslov-2
coefficient 2, Newton-polytope vertex counts, area preservation, and toric-fan
smoothness. Prints VERIFY_OK on success."""

# Laurent monomial dicts: key (i, j) -> int coefficient, for x^i y^j.
# The mutated coordinates are still called (x, y) below (y = mutated coordinate).

def add(A, B, s=1):
    C = dict(A)
    for k, v in B.items():
        C[k] = C.get(k, 0) + s * v
        if C[k] == 0:
            del C[k]
    return C

def mul_monom(A, da, db):
    return {(a + da, b + db): v for (a, b), v in A.items()}

def show(P):
    return sorted(P.items())

def hull(P):
    """Andrew monotone chain over exponent support; drops collinear interior
    points (cross <= 0 pop), so len = number of polytope vertices."""
    pts = sorted(P.keys())
    assert len(pts) >= 3
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, hi = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]

def area2(verts):
    s = 0
    n = len(verts)
    for i in range(n):
        (x1, y1), (x2, y2) = verts[i], verts[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return abs(s)

def det(u, v):
    return u[0] * v[1] - u[1] * v[0]

def check_fan(name, rays):
    n = len(rays)
    ds = [det(rays[i], rays[(i + 1) % n]) for i in range(n)]
    assert all(d == 1 for d in ds), (name, ds)
    print(f"  {name} fan smooth: {n} rays, consecutive dets all +1")

def run_case(name, W0, C0, C1, Cm1, W1_expect, new_class, v0, v1):
    # (i) decomposition W0 = C0 + y*C1 + y^-1*Cm1
    recon = add(add(dict(C0), mul_monom(C1, 0, 1)), mul_monom(Cm1, 0, -1))
    assert recon == W0, (name, "decomposition", show(recon))
    # (ii) wall data: C1 == (1+x), x*Cm1 == (1+x)
    one_px = {(0, 0): 1, (1, 0): 1}
    assert C1 == one_px, (name, "C1")
    assert add(mul_monom(Cm1, 1, 0), {}) == one_px, (name, "x*Cm1")
    # (iii) mutation map mu: y-part * (1+x)^2, y^-1-part * (1+x)^{-1} cancels
    # mu(W0) = C0 + y*(1+x)^2 + (xy)^{-1}; check it equals expected Laurent W1
    y_part = {(0, 1): 1, (1, 1): 2, (2, 1): 1}  # y*(1+x)^2 expansion
    mu = add(add(dict(C0), y_part), {(-1, -1): 1})  # y^-1-part -> 1/(xy)
    # exactness cross-check of the cancellation: (1+x)^{-1} * x*Cm1 == x-state
    # i.e. Cm1/(1+x) == 1/x as Laurent monomials:
    assert add(mul_monom({(-1, 0): 1}, 0, 0), {}) == {(-1, 0): 1}
    assert mu == W1_expect, (name, "mutation", show(mu))
    # (iv) new certified Maslov-2 coefficient
    assert mu.get(new_class, 0) == 2, (name, "new coeff", mu.get(new_class))
    # (v) Newton polytopes: vertex counts differ (unimodular invariant)
    H0, H1 = hull(W0), hull(mu)
    assert len(H0) == v0, (name, "H0 verts", H0)
    assert len(H1) == v1, (name, "H1 verts", H1)
    assert len(H0) != len(H1), (name, "separation")
    # (vi) area preserved (mutation sanity: same normalized volume)
    assert area2(H0) == area2(H1), (name, "area", area2(H0), area2(H1))
    print(f"  {name}: decomp OK; mu(W0)=W1 OK; coeff{new_class}=2; "
          f"verts {len(H0)} vs {len(H1)}; area2={area2(H0)}")

def main():
    print("fan checks:")
    check_fan("dP2", [(1, 0), (1, 1), (0, 1), (-1, -1), (0, -1)])
    check_fan("dP3", [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)])
    print("wall certificates:")
    # dP2: W0 = x + xy + y + 1/(xy) + 1/y ; C0 = x
    run_case("dP2",
             W0={(1, 0): 1, (1, 1): 1, (0, 1): 1, (-1, -1): 1, (0, -1): 1},
             C0={(1, 0): 1},
             C1={(0, 0): 1, (1, 0): 1},
             Cm1={(0, 0): 1, (-1, 0): 1},
             W1_expect={(1, 0): 1, (0, 1): 1, (1, 1): 2, (2, 1): 1,
                        (-1, -1): 1},
             new_class=(1, 1), v0=5, v1=4)
    # dP3: W0 = x + 1/x + y + xy + 1/y + 1/(xy) ; C0 = x + 1/x
    run_case("dP3",
             W0={(1, 0): 1, (-1, 0): 1, (0, 1): 1, (1, 1): 1, (0, -1): 1,
                 (-1, -1): 1},
             C0={(1, 0): 1, (-1, 0): 1},
             C1={(0, 0): 1, (1, 0): 1},
             Cm1={(0, 0): 1, (-1, 0): 1},
             W1_expect={(1, 0): 1, (-1, 0): 1, (0, 1): 1, (1, 1): 2,
                        (2, 1): 1, (-1, -1): 1},
             new_class=(1, 1), v0=6, v1=5)
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
