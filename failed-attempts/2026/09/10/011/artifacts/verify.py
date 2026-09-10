"""EMERGENT FINDING certificate (exact integer arithmetic, stdlib only).

Theorem (certified expected-dimension non-obstruction, degree <= 2000):
Let D = 28H - 2E4 - 5E3 on X_K and B = dH - m4E4 - m3E3 (nonneg integers).
If D.B = 28d - 42m4 - 140m3 < 0 and d <= 2000, then
  edim T_d(-m4E4-m3E3) = max(dimT_d - cond4(m4) - cond3(m3), 0) = 0.
That is, dimT_d - cond4(m4) - cond3(m3) <= 0.

Definitions (Bauer et al. Sec 4):
  dimT_d = #{(a,b,c) in N^3 : 4a+6b+14c = d}  (monomials in Phi4,Phi6,Phi14)
  cond_n(m) = #{(i,j) in N^2 : 2i+n*j <= m-1} (m>=1), cond_n(0)=0.
Exhaustiveness argument:
  Lemma (general monotonicity): cond_n(m+1) >= cond_n(m) for all m >= 0 and
  every n, since {(i,j): 2i+n*j <= m-1} subset {(i,j): 2i+n*j <= m}.
  For fixed (d,m4), raw edim is nonincreasing in m3 by the Lemma,
  so it suffices to check the smallest m3 with D.B<0 (all larger m3 give
  raw edim <= that value, including the unbounded tail).
  For fixed d, m4 ranges over all values admitting any m3>=0 with D.B<0,
  plus a tail: we loop m4 = 0..M4MAX(d) where M4MAX is chosen so that
  cond4(M4MAX) >= dimT_d (exact values); for m4 >= M4MAX, edim_raw <=
  dimT_d - cond4(m4) <= 0 regardless of m3. Tail validity is verified
  explicitly (monotonicity of cond4 checked on the fly).
"""
def dimT(d):
    n = 0
    for a in range(d // 4 + 1):
        rem = d - 4 * a
        for b in range(rem // 6 + 1):
            if (rem - 6 * b) % 14 == 0:
                n += 1
    return n

def cond(n_, m):
    if m <= 0:
        return 0
    c = 0
    j = 0
    while n_ * j <= m - 1:
        c += (m - 1 - n_ * j) // 2 + 1
        j += 1
    return c

def monot_cond(n_, mlo, mhi):
    prev = cond(n_, mlo)
    for m in range(mlo + 1, mhi + 1):
        v = cond(n_, m)
        assert v >= prev, (n_, m)
        prev = v

DMAX = 2000
DBAIL = []
for d in range(0, DMAX + 1):
    dt = dimT(d)
    # tail bound: smallest M with cond4(M) >= dt
    M = 0
    while cond(4, M) < dt:
        M += 1
    M4MAX = M  # for m4 >= M4MAX, edim_raw <= dt - cond4 <= 0 for every m3
    # all m4 that can pair with some m3>=0 to give D.B<0 lie below 28d/42+1 <= M4MAX?
    # No: loop m4 over 0..max(ceil range, M4MAX) to be safe. Actually suffices
    # 0..M4MAX since beyond that edim_raw<=0 already. But must also cover m4
    # with D.B<0 below M4MAX: all m4 <= M4MAX are looped. Complete.
    for m4 in range(0, M4MAX + 1):
        need = 28 * d - 42 * m4
        m3min = 0 if need < 0 else need // 140 + 1
        e = dt - cond(4, m4) - cond(3, m3min)
        assert 28 * d - 42 * m4 - 140 * m3min < 0
        if e > 0:
            DBAIL.append((d, m4, m3min, e))
    # spot-check monotonicity witnesses used (m3min boundary logic)
print("DMAX:", DMAX)
print("counterexamples (must be []):", DBAIL[:10], "count =", len(DBAIL))
assert len(DBAIL) == 0
# General monotonicity lemma: cond_n(m) = #{(i,j) in N^2 : 2i+n*j <= m-1},
# so {(i,j): 2i+n*j <= m-1} subset {(i,j): 2i+n*j <= m}, hence
# cond_n(m+1) >= cond_n(m) for every m >= 0 and every n. This covers the
# unbounded-m3/m4 tails. Defense-in-depth explicit checks over used ranges:
monot_cond(4, 0, 500)
monot_cond(3, 0, 1200)
print("cond monotonicity OK over used ranges")
# D-orthogonal census (exact, complete): D.B==0 <=> 28d=42m4+140m3 <=>
# 2d=3m4+10m3, so d<=2000 forces 3m4+10m3<=4000, i.e. m4<=1333, m3<=400.
# Looping m4=0..1334, m3=0..400 therefore visits EVERY D.B=0 class with d<=2000.
print("=== D.B==0, B^2<0, edim>0 classes with d<=2000 (informative) ===")
cnt = 0
shown = 0
worst = None
for m4 in range(0, 1335):
    # d from D.B=0: 28d = 42m4+140m3 -> d=(3m4+10m3)/2, need 3m4+10m3 even
    for m3 in range(0, 401):
        s = 3 * m4 + 10 * m3
        if s % 2 or (m4 == 0 and m3 == 0):
            continue
        d = s // 2
        if d > DMAX:
            continue
        B2 = d * d - 21 * m4 * m4 - 28 * m3 * m3
        e = dimT(d) - cond(4, m4) - cond(3, m3)
        if B2 < 0 and e > 0:
            cnt += 1
            if shown < 15:
                print(f"d={d} m4={m4} m3={m3} B2={B2} edim={e}")
                shown += 1
print("D-orthogonal negative edim>0 count:", cnt)
print("VERIFY_EMERGENT_OK")
