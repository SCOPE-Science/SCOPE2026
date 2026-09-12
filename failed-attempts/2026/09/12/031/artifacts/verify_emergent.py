"""Stdlib-only verifier for the certified sharp-cutoff jump obstruction (lane-1104).
Recomputes exact shell counts R(N) by integer arithmetic and rigorous jump intervals.
Replay: python3 verify_emergent.py  ->  prints VERIFY_OK on success.
"""
import math, json
K = 40  # interval precision bits
PI_LO = 3.14159265358978
PI_HI = 3.14159265358980
assert PI_LO < math.pi < PI_HI
def R_exact(N):
    lo2 = (N-1)*(N-1); hi2 = N*N; R = 0
    for a in range(-N, N+1):
        hi = hi2 - a*a
        if hi < 0:
            continue
        bmax = math.isqrt(hi)
        lo = lo2 - a*a
        if lo < 0:
            R += 2*bmax + 1
        else:
            bmin = math.isqrt(lo) + 1
            if bmax >= bmin:
                R += 2*(bmax - bmin + 1)
    return R
def sqrt_iv(n):
    m = math.isqrt(n * (1 << (2*K)))
    return m / (1 << K), (m+1) / (1 << K)
def jump_iv(N, R):
    s_lo, s_hi = sqrt_iv(N)
    t_lo, t_hi = sqrt_iv((N-1)**3)
    A_lo, A_hi = N*s_lo, N*s_hi
    C_lo = (4*PI_LO/3)*(A_lo - t_hi)
    C_hi = (4*PI_HI/3)*(A_hi - t_lo)
    assert A_lo - t_hi > 0
    return R/s_hi - C_hi, R/s_lo - C_lo
# c0 = 1/(2*sqrt(2*pi)) rigorous interval
p2_lo, p2_hi = 2*PI_LO, 2*PI_HI
x_lo = math.isqrt(int(p2_lo*(1 << (2*K))))/(1 << K)
x_hi = (math.isqrt(int(math.ceil(p2_hi*(1 << (2*K)))))+1)/(1 << K)
assert x_lo**2 <= p2_lo and x_hi**2 >= p2_hi
C0_LO, C0_HI = 1/(2*x_hi), 1/(2*x_lo)
print("c0 in [%.12f, %.12f]" % (C0_LO, C0_HI))
NS = [893, 894, 962, 1365, 2275, 2520, 2728, 2926]
rows = {}
ok = True
for N in NS:
    R = R_exact(N)
    jlo, jhi = jump_iv(N, R)
    clo, chi = (C0_LO*min(jlo,jhi), C0_HI*max(jlo,jhi)) if jlo>0 else (C0_LO*jlo, C0_HI*jhi)
    # C-scale jump interval (jumps all have fixed sign here)
    if jlo > 0:
        c_lo, c_hi = C0_LO*jlo, C0_HI*jhi
    else:
        c_lo, c_hi = C0_LO*jlo, C0_HI*jhi  # both negative; lower bound is C0_HI*jlo? fix:
        c_lo, c_hi = C0_HI*jlo, C0_LO*jhi
    rows[str(N)] = {"R": R, "S_jump": [jlo, jhi], "C_jump": [c_lo, c_hi]}
    print("N=%d R=%d S-jump=[%.6f,%.6f] C-jump=[%.6f,%.6f]" % (N, R, jlo, jhi, c_lo, c_hi))
    if min(abs(jlo), abs(jhi)) < 4.5 or min(abs(c_lo), abs(c_hi)) < 0.9:
        ok = False
json.dump(rows, open("output/artifacts/witness_jumps.json", "w"), indent=1)
print("VERIFY_OK" if ok else "VERIFY_FAIL")
