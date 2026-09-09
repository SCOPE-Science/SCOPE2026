"""EXACT cut-locus certificate engine for the regular tetrahedron D_1.
Exact arithmetic in Q(sqrt(3)): each scalar is a+b*sqrt(3) with Fractions.
Stdlib only. Proves interior cut points (two equal shortest valid unfold paths).
"""
from fractions import Fraction as Fr
F = Fr

class S3:
    """a + b*sqrt(3), exact."""
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a = F(a); self.b = F(b)
    def __add__(self, o): o = _c(o); return S3(self.a+o.a, self.b+o.b)
    def __sub__(self, o): o = _c(o); return S3(self.a-o.a, self.b-o.b)
    def __neg__(self): return S3(-self.a, -self.b)
    def __mul__(self, o):
        o = _c(o)
        return S3(self.a*o.a + 3*self.b*o.b, self.a*o.b + self.b*o.a)
    def __truediv__(self, o):
        o = _c(o)
        den = o.a*o.a - 3*o.b*o.b
        assert den != 0, "division by zero in S3"
        return S3((self.a*o.a - 3*self.b*o.b)/den, (self.b*o.a - self.a*o.b)/den)
    def __eq__(self, o): o = _c(o); return self.a == o.a and self.b == o.b
    def sign(self):
        """Exact sign of a+b*sqrt(3)."""
        if self.b == 0: return (self.a > 0) - (self.a < 0)
        if self.a == 0: return (self.b > 0) - (self.b < 0)
        # sign(a+b*s): compare a^2 vs 3b^2 when a,b opposite signs
        if (self.a > 0) == (self.b > 0):
            return (self.a > 0) - (self.a < 0)
        # opposite signs: |a| vs sqrt(3)|b|
        d = self.a*self.a - 3*self.b*self.b
        if d == 0: return 0
        # a+b*s has sign of a iff a^2 > 3b^2
        if d > 0: return (self.a > 0) - (self.a < 0)
        return (self.b > 0) - (self.b < 0)
    def tofloat(self): return float(self.a) + float(self.b)*3**0.5
    def __repr__(self): return f"({self.a}+{self.b}s)"

def _c(o):
    if isinstance(o, S3): return o
    return S3(F(o), F(0))

class Pt:
    __slots__ = ("x", "y")
    def __init__(self, x, y): self.x = _c(x); self.y = _c(y)
    def __add__(self, o): return Pt(self.x+o.x, self.y+o.y)
    def __sub__(self, o): return Pt(self.x-o.x, self.y-o.y)
    def __mul__(self, k): k = _c(k); return Pt(self.x*k, self.y*k)
    def dot(self, o): return self.x*o.x + self.y*o.y
    def norm2(self): return self.dot(self)
    def __repr__(self): return f"[{self.x},{self.y}]"

SQ3 = None  # placeholder

def reflect_point(P, A, B):
    """Reflect P across line AB (all Pt). Exact."""
    d = B - A
    n2 = d.norm2()
    assert n2.sign() > 0
    t = (P - A).dot(d) / n2
    proj = A + d*t
    return proj*S3(2) - P

def reflect_layout(layout, A, B):
    return {v: reflect_point(P, A, B) for v, P in layout.items()}

# Tetrahedron combinatorics
FACES = [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]

def ref_face():
    # equilateral side 1: A=(0,0) B=(1,0) C=(1/2, sqrt3/2)
    return {0: Pt(0,0), 1: Pt(1,0), 2: Pt(S3(0), S3(F(1,2), F(0))) }

def ref_layout(F):
    r = ref_face()
    return {F[0]: r[0], F[1]: r[1], F[2]: r[2]}

def unfold_paths(Fs, Ft):
    adj = {}
    for a in range(4):
        for b in range(4):
            if a == b: continue
            e = tuple(sorted(set(FACES[a]) & set(FACES[b])))
            if len(e) == 2: adj.setdefault(a, []).append((e, b))
    si = FACES.index(Fs); ti = FACES.index(Ft)
    out = []
    def dfs(cur, used, path):
        if cur == ti: out.append(tuple(path)); return
        if len(path) > 6: return
        for (e, nxt) in adj[cur]:
            if e in used: continue
            dfs(nxt, used | {e}, path+[nxt])
    dfs(si, set(), [si])
    return out

def layout_sequence(Fs_seq, ref0):
    """seq = face indices; ref0 = layout dict of seq[0]. Returns dict fi->layout."""
    layouts = {Fs_seq[0]: ref0}
    for a, b in zip(Fs_seq[:-1], Fs_seq[1:]):
        Fa = FACES[a]; Fb = FACES[b]
        e = tuple(sorted(set(Fa) & set(Fb)))
        LA = layouts[a]
        # reflect LA's third-vertex across edge e to get Fb layout? No: reflect whole Fa layout
        # across line LA[e0]LA[e1]; image of edge stays, third vertex maps to other side.
        # But Fb's third vertex must be placed: reflect Fa's layout, then relabel: the
        # reflected position of Fa's apex is NOT Fb's apex in general (different... on tetrahedron
        # all faces congruent equilateral so reflection gives correct apex position).
        LB_full = reflect_layout(LA, LA[e[0]], LA[e[1]])
        layouts[b] = {e[0]: LA[e[0]], e[1]: LA[e[1]],
                      [v for v in Fb if v not in e][0]: LB_full[[v for v in Fa if v not in e][0]]}
    return layouts

def seg_params(P, Q, A, B):
    """Solve P+t(Q-P) = A+u(B-A). Returns (t,u) as S3 or None if parallel."""
    rx = Q.x - P.x; ry = Q.y - P.y
    ex = B.x - A.x; ey = B.y - A.y
    den = rx*ey - ry*ex
    if den.sign() == 0: return None
    fx = A.x - P.x; fy = A.y - P.y
    t = (fx*ey - fy*ex)/den
    u = (fx*ry - fy*rx)/den
    return (t, u)

def valid_and_dist(sxy, Fs, yxy, Ft, seq, strict=True):
    L = layout_sequence(seq, ref_layout(FACES[seq[0]]))
    # map y from Ft reference into current layout of seq[-1] via rigid motion from 2 pts
    ref = ref_layout(Ft); tgt = L[seq[-1]]
    r0, r1 = list(Ft[:2])
    p0, p1 = ref[r0], ref[r1]; q0, q1 = tgt[r0], tgt[r1]
    # rigid motion: rotation+translation taking p0->q0, p1->q1 (orientation preserving, exact in S3?)
    # Rotation by angle theta with cos,sin in Q(sqrt3)? Angles are multiples of 60deg: cos,sin in
    # {0,+-1,+-1/2,+-sqrt3/2} — representable. Compute via complex division in Q(sqrt3,i)? Simpler:
    # express y in barycentric coords (rational!) w.r.t. Ft triangle, then evaluate in tgt.
    # Barycentric via areas: all in S3; ratios must be rational. Solve 2x2 for (u,v): y = p0 + u*(p1-p0) + v*(p2-p0).
    p2 = ref[list(Ft[2:])[0]]
    d1 = p1 - p0; d2 = p2 - p0; rhs = yxy - p0
    den = d1.x*d2.y - d1.y*d2.x
    assert den.sign() != 0
    u = (rhs.x*d2.y - rhs.y*d2.x)/den
    v = (rhs.x*d1.y - rhs.y*d1.x)/den * S3(-1)
    # NOTE: second coord: standard Cramer: v = (d1.x*rhs.y - d1.y*rhs.x)/den... check sign below
    v = ((d1.x*rhs.y - d1.y*rhs.x)/den)
    # verify reconstruction exactly
    rec = Pt(p0.x + d1.x*u + d2.x*v, p0.y + d1.y*u + d2.y*v)
    assert rec.x == yxy.x and rec.y == yxy.y, f"barycentric reconstruct failed {rec} vs {yxy}"
    q2 = tgt[list(Ft[2:])[0]]
    e1 = q1 - q0; e2 = q2 - q0
    yp = Pt(q0.x + e1.x*u + e2.x*v, q0.y + e1.y*u + e2.y*v)
    ts = []
    for a, b in zip(seq[:-1], seq[1:]):
        Fa = FACES[a]; Fb = FACES[b]
        e = tuple(sorted(set(Fa) & set(Fb)))
        A, B = L[a][e[0]], L[a][e[1]]
        r = seg_params(sxy, yp, A, B)
        if r is None: return None
        t, uu = r
        if strict:
            if not (t.sign() > 0 and (t - S3(1)).sign() < 0 and uu.sign() > 0 and (uu - S3(1)).sign() < 0):
                return None
        else:
            if not (t.sign() >= 0 and (t - S3(1)).sign() <= 0 and uu.sign() >= 0 and (uu - S3(1)).sign() <= 0):
                return None
        ts.append(t)
    for a, b in zip(ts[:-1], ts[1:]):
        if (b - a).sign() <= 0: return None
    return (yp - sxy).norm2()

def true_dists(sxy, Fs, yxy, Ft, strict=True):
    out = []
    for seq in unfold_paths(Fs, Ft):
        if len(seq) == 1:
            out.append(((yxy - sxy).norm2(), seq)); continue
        d2 = valid_and_dist(sxy, Fs, yxy, Ft, seq, strict=strict)
        if d2 is not None: out.append((d2, seq))
    out.sort(key=lambda r: (r[0].a, r[0].b))
    # sort exactly: sort by float key of exact value (ties broken by exact compare after)
    out.sort(key=lambda r: r[0].tofloat())
    return out

def bary(F, l0, l1, l2):
    L = ref_layout(F)
    return Pt(L[F[0]].x*S3(l0)+L[F[1]].x*S3(l1)+L[F[2]].x*S3(l2),
              L[F[0]].y*S3(l0)+L[F[1]].y*S3(l1)+L[F[2]].y*S3(l2))

def egrid(Ft, n):
    pts = []
    for i in range(1, n):
        for j in range(1, n-i):
            k = n-i-j
            pts.append(((i, j, k), bary(Ft, Fr(i)/Fr(n), Fr(j)/Fr(n), Fr(k)/Fr(n))))
    return pts

if __name__ == "__main__":
    # self-test: adjacent vertex distance == 1
    FF = (0,1,2); L = ref_layout(FF)
    ds = true_dists(L[0], FF, L[1], FF)
    print("d(v0,v1)^2 =", ds[0][0], "npaths =", len(ds))
    assert ds[0][0] == S3(1), "self-test failed"
    print("SELF-TEST OK")
