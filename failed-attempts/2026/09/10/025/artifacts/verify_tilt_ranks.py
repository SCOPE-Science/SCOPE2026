"""Verify tilt-shadow margins and symbol-rank obstruction counts (stdlib only).

Part A: for tilt t (deg), e=(cos t, sin t, 0); max over K_- samples of nu.e.
Part B: per-frequency row counts: 3 div-free rows + available frame rows;
  fixed weight -> <=1 frame row per xi (rank<=4 generically, <=3 on e1-axis);
  tilted window |t|<=tmax adds only cone |a|<=tan(tmax)|b| + e3 axis, one tilt each.
Part C: e3-axis full rank 6 from multi-tilt frame rows (replay of lane computation).
"""
import math

def max_shadow(tilt_deg, n=4000):
    t = math.radians(tilt_deg); e = (math.cos(t), math.sin(t))
    worst = -1e9
    for i in range(n):
        th = 2 * math.pi * i / n
        x1, x2 = math.cos(th), math.sin(th)
        if x1 <= -0.5:
            worst = max(worst, x1 * e[0] + x2 * e[1])
    return worst

def frame_row(xi, e, q, tau=10.0):
    A = [xi[i] / 2 + q[i] for i in range(3)]
    B = [xi[i] / 2 - q[i] for i in range(3)]
    z1 = [tau * e[i] + 1j * A[i] for i in range(3)]
    z2 = [-tau * e[i] + 1j * B[i] for i in range(3)]
    assert abs(sum(v * v for v in z1)) < 1e-9
    assert abs(sum(v * v for v in z2)) < 1e-9
    return [z1[0]*z2[0], z1[1]*z2[1], z1[2]*z2[2],
            z1[0]*z2[1]+z1[1]*z2[0], z1[0]*z2[2]+z1[2]*z2[0], z1[1]*z2[2]+z1[2]*z2[1]]

def crank(M):
    M = [list(r) for r in M]; m = len(M); n = len(M[0]); r = 0
    for c in range(n):
        p = max(range(r, m), key=lambda i: abs(M[i][c]))
        if abs(M[p][c]) < 1e-9:
            continue
        M[r], M[p] = M[p], M[r]
        M[r] = [v / M[r][c] for v in M[r]]
        for i in range(m):
            if i != r and abs(M[i][c]) > 1e-12:
                M[i] = [a - b * M[i][c] for a, b in zip(M[i], M[r])]
        r += 1
        if r == m:
            break
    return r

print("== Part A: shadow margins ==")
for deg in [0, 5, 10, 15, 30, 45, 90]:
    print(f"tilt={deg}: max_K_- nu.e = {max_shadow(deg):.3f}")
assert max_shadow(0) < -0.49 and max_shadow(30) < 0 and max_shadow(45) > 0
print("SHADOW_OK")

print("== Part B/C: ranks ==")
# fixed weight, generic xi perp e1: 3 div + 1 frame
xi = [0, 0, 2.0]; e = [1, 0, 0]; tau = 10.0
R = math.sqrt(tau**2 - 1.0)
rows = [[xi[0],0,0,xi[1],xi[2],0],[0,xi[1],0,xi[0],0,xi[2]],[0,0,xi[2],0,xi[0],xi[1]]]
rows.append(frame_row(xi, e, [0, R, 0]))
assert crank(rows) <= 4, crank(rows)
print(f"fixed-weight generic xi={xi}: rank={crank(rows)} <= 4 OK")
# e1-axis: no frames
xi = [3.0, 0, 0]
rows = [[xi[0],0,0,xi[1],xi[2],0],[0,xi[1],0,xi[0],0,xi[2]],[0,0,xi[2],0,xi[0],xi[1]]]
assert crank(rows) == 3
print(f"e1-axis xi={xi}: rank={crank(rows)} == 3 OK")
# e3-axis multi-tilt: full rank 6
xi = [0, 0, 2.0]
rows = [[xi[0],0,0,xi[1],xi[2],0],[0,xi[1],0,xi[0],0,xi[2]],[0,0,xi[2],0,xi[0],xi[1]]]
nxi = 2.0; Rt = math.sqrt(tau**2 - nxi**2 / 4)
for deg in [-10, -5, 0, 5, 10]:
    t = math.radians(deg); ee = [math.cos(t), math.sin(t), 0.0]
    cr = [ee[(i+1)%3]*xi[(i+2)%3]-ee[(i+2)%3]*xi[(i+1)%3] for i in range(3)]
    nc = math.sqrt(sum(v*v for v in cr)); nn = [v/nc for v in cr]
    rows.append(frame_row(xi, ee, [Rt*v for v in nn]))
r = crank(rows)
assert r == 6, r
print(f"e3-axis multi-tilt: rank={r} == 6 OK")
print("RANK-COUNTS_OK")
