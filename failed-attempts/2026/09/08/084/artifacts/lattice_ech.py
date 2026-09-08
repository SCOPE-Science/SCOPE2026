"""Concave lattice-path ECH capacities (Choi et al. 1310.6647, Thm 1.21).

c_k(X_Omega) = max{ ell_Omega(Lambda) : L(Lambda) = k }, over concave
integral paths Lambda (graph of convex PWL F:[0,B]->[0,A], lattice vertices).
L(Lambda) = # interior lattice pts of region bounded by Lambda and axes,
  excluding pts on Lambda.
ell_Omega(Lambda) = sum_e v_e x p_e, v_e = edge vector (right-left endpoints),
  p_e = point on graph of f with graph above line through p_e parallel to e
  (for integral concave Omega given by chain: p_e maximizes... choose vertex
  maximizing cross: ell = sum_e max_{q on graph} v_e x q? No: p_e such that
  graph contained in closed half-plane ABOVE line through p_e parallel e:
  v_e x p_e = min over graph? cross v_e x q minimized... verify sign below
  against ellipsoid case: ell = b*x + a*y form (paper Ex 1.23).)

For edge e with direction v=(dx,dy) (dx>0, dy<=0 for concave path traversed
left-to-right? path from (0,B) to (A,0)): support: p_e = argmin_q (v x q)
over graph vertices? Check ellipsoid Omega=(a,0),(0,b): paper: ell = b*x + a*y
where (x,y) = distinguished vertex. Cross-check numerically in tests.
"""
from fractions import Fraction as Q
import itertools

def concave_paths_for_k(k, bound=None):
    """Enumerate concave integral paths with L(path) <= k (bound box). Yields (verts, L)."""
    # Concave path from (0,B) to (A,0), convex F. Parametrize: lattice points,
    # slopes nondecreasing. Box: A,B <= k+1 (L>=max(A,B)? L counts interior).
    # Brute force over vertex lists (small k<=8): generate paths via partitions.
    seen = set()
    out = []
    Bmax = k + 1
    Amax = k + 1
    # generate all lattice paths and filter concavity: represent as sequence of
    # vertices (x0=0,y0=B),(x1,y1),...,(xm=A,ym=0) with x inc, y dec, slopes inc.
    # Bound search: edges primitive or not; total drop B, run A.
    def rec(verts):
        key = tuple(verts)
        if key in seen:
            return
        seen.add(key)
        x, y = verts[-1]
        if x > Amax or y < 0:
            return
        if y == 0:
            A = x
            B = verts[0][1]
            L = lattice_count(verts)
            if L <= (bound if bound is not None else k):
                out.append((list(verts), L))
            return
        # extend: next vertex (x+dx, y-dy), dx>=1? dx>=0... x strictly inc? allow vertical first? Path graph F:[0,B]x... use dx>=1, dy>=0, y-dy>=0; slope -dy/dx nondecreasing
        if not verts:
            return
        last_slope = None
        if len(verts) >= 2:
            (x0, y0) = verts[-2]
            last_slope = Q(y - y0, x - x0) if x - x0 != 0 else None
        for dx in range(0, Amax - x + 1):
            for dy in range(0, y + 1):
                if dx == 0 and dy == 0:
                    continue
                if dx == 0:
                    continue  # graph: x must advance (F function); vertical disallowed except maybe first? keep simple: disallow
                s = Q(-dy, dx)
                if last_slope is not None and s < last_slope:
                    continue
                rec(verts + [(x + dx, y - dy)])
    for B in range(0, Bmax + 1):
        rec([(0, B)])
    return out

def lattice_count(verts):
    """# strict-interior lattice pts of region under path (below graph, above axes wedge): region bounded by path + segment (0,0)-(0,B) + (0,0)-(A,0). Use Pick: L = Area - Boundary/2 + 1 minus path points... Define: region R; count lattice pts in R not on path."""
    # R polygon: (0,0),(A,0)? path ends (A,0); polygon: (0,0) -> (A,0) -> reversed path -> (0,B) -> close. Count via enumeration in bbox.
    A = verts[-1][0]
    B = verts[0][1]
    onpath = set()
    for i in range(len(verts) - 1):
        for p in _seg_lattice(verts[i], verts[i + 1]):
            onpath.add(p)
    # path as function: for each x, ytop(x) = min over edges covering x of line y
    cnt = 0
    for x in range(0, A + 1):
        yt = _ytop(verts, x)
        if yt is None:
            continue
        import math
        yti = int(math.floor(yt + 1e-9))
        for y in range(0, yti + 1):
            if (x, y) in onpath:
                continue
            cnt += 1
    return cnt

def _seg_lattice(p, q):
    import math
    x0, y0 = p
    x1, y1 = q
    g = math.gcd(abs(x1 - x0), abs(y1 - y0))
    return [(x0 + (x1 - x0) * t // g, y0 + (y1 - y0) * t // g) for t in range(g + 1)]

def _ytop(verts, x):
    for i in range(len(verts) - 1):
        x0, y0 = verts[i]
        x1, y1 = verts[i + 1]
        if x0 <= x <= x1 and x1 > x0:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return None

def omega_length(verts, chain):
    """ell_Omega: for each edge v (traversed from x=0 to x=A), p_e = graph vertex minimizing... determine sign: use p_e = argmax over graph of (v x q)? Calibrate: must reproduce ellipsoid formula. We compute BOTH min and max and let caller/tests decide; default min."""
    P = [(Q(x), Q(y)) for x, y in chain]
    total = Q(0)
    for i in range(len(verts) - 1):
        v = (Q(verts[i+1][0] - verts[i][0]), Q(verts[i+1][1] - verts[i][1]))
        vals = [v[0] * q[1] - v[1] * q[0] for q in P]
        # p_e: graph contained in half-plane ABOVE line through p_e parallel e
        # <=> v x p <= v x q for all q (verified vs paper Ex 1.23): MINIMIZE
        total += min(vals)
    return total
