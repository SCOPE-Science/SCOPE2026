"""PG(2,13) incidence model + blocking-set verifier (stdlib+numpy)."""
import numpy as np

q = 13
# Points: 0..168 affine (x,y) -> x*13+y ; 169..181 direction points ; 182 = (1,0,0)
NPTS = 183
def paff(x, y): return (x % q) * 13 + (y % q)
def pinf_slope(s): return 169 + (s % q)   # point (1,s,0)
P_INF_X = 182                              # point (1,0,0)... note (1,s,0) covers all b!=0? no:
# homogeneous points with z=0: (a,b,0), normalized: (1,s,0) for s in F13 and (0,1,0).
# So 169+s = (1,s,0), and 182 = (0,1,0).
P_INF_Y = 182

def build_lines():
    lines = []
    lindex = {}
    for a in range(q):
        for b in range(q):
            for c in range(q):
                if a == b == c == 0:
                    continue
                if a != 0:
                    t = (1, (b * pow(a, -1, q)) % q, (c * pow(a, -1, q)) % q)
                elif b != 0:
                    t = (0, 1, (c * pow(b, -1, q)) % q)
                else:
                    t = (0, 0, 1)
                if t not in lindex:
                    lindex[t] = len(lines)
                    lines.append(t)
    return lines

LINES = build_lines()
NL = len(LINES)
assert NL == 183, NL

def build_incidence():
    INC = np.zeros((NL, NPTS), dtype=np.bool_)
    la = np.array([t[0] for t in LINES])[:, None]
    lb = np.array([t[1] for t in LINES])[:, None]
    lc = np.array([t[2] for t in LINES])[:, None]
    xs = np.arange(q)[None, :]
    # affine: for each x, y = -(ax+c)/b if b!=0 else check ax+c==0 -> all y
    for i in range(NL):
        a, b, c = LINES[i]
        if b % q != 0:
            binv = pow(b, -1, q)
            for x in range(q):
                y = (-(a * x + c) * binv) % q
                INC[i, paff(x, y)] = True
        else:
            if a % q != 0:
                x0 = (-c * pow(a, -1, q)) % q
                for y in range(q):
                    INC[i, paff(x0, y)] = True
            else:
                # c != 0, line at infinity z=0: contains all 14 inf points
                pass
        # infinity points: (1,s,0): a + b s == 0 ; (0,1,0): b == 0
        if b % q != 0:
            s0 = (-a * pow(b, -1, q)) % q
            INC[i, pinf_slope(s0)] = True
        else:
            if a % q == 0:
                for s in range(q):
                    INC[i, pinf_slope(s)] = True
                INC[i, P_INF_Y] = True
            else:
                INC[i, P_INF_Y] = True
    return INC

INC = build_incidence()
assert INC.sum(axis=1).min() == 14 and INC.sum(axis=1).max() == 14
assert INC.sum(axis=0).min() == 14 and INC.sum(axis=0).max() == 14
print("PG(2,13) model OK: 183 pts, 183 lines, 14 pts/line", flush=True)

def check_blocking(S):
    """S: set/list of point ids. Returns (is_blocking, nunblocked, unblocked_lines)."""
    m = INC[:, list(S)].sum(axis=1)
    unb = np.nonzero(m == 0)[0]
    return (len(unb) == 0, len(unb), unb)

def check_minimal(S):
    """Every point lies on a tangent (line meeting S exactly once)."""
    S = list(S)
    m = INC[:, S].sum(axis=1)
    tang = INC[:, S] & (m == 1)[:, None]
    has = tang.sum(axis=0) > 0
    return bool(has.all()), [S[j] for j in np.nonzero(~has)[0]]

def check_nontrivial(S):
    """No full line contained in S."""
    m = INC[:, list(S)].sum(axis=1)
    return bool((m < 14).all())

def line_sizes(S):
    m = INC[:, list(S)].sum(axis=1)
    return m

def certify(S):
    S = list(S)
    blk, n, _ = check_blocking(S)
    mn, missing = check_minimal(S)
    ntr = check_nontrivial(S)
    return {"blocking": blk, "unblocked": n, "minimal": mn,
            "missing_tangent": missing, "nontrivial": ntr, "size": len(S)}
