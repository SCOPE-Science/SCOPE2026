"""Bounded recovery test for lane-1004 twisted inhomogeneous target.

Target: max(||q*sqrt2-1/4||, ||q*sqrt3-1/9||) >= (1/800) q^{-1/2} for all q>=1.
Test A: extended float scan to Q=2e7, track joint min and single-coordinate bests.
Test B: high-precision (mpmath 80 digits) recheck of joint near-misses and the
        single-coordinate hits, ruling out floating-point artifacts.
Writes results JSON to stdout and to results_recovery.json next to this script.
"""
import json, math, time
import numpy as np

S2 = math.sqrt(2); S3 = math.sqrt(3); G1 = 0.25; G2 = 1/9; C = 1/800

def scan(Q, chunk=1_000_000):
    best = 1e9; bq = -1
    best1 = 1e9; bq1 = -1
    best2 = 1e9; bq2 = -1
    nviol = 0
    for start in range(1, Q + 1, chunk):
        end = min(start + chunk - 1, Q)
        q = np.arange(start, end + 1, dtype=np.float64)
        x1 = q * S2 - G1; x2 = q * S3 - G2
        r1 = np.abs(x1 - np.round(x1)); r2 = np.abs(x2 - np.round(x2))
        m = np.maximum(r1, r2)
        v = m * np.sqrt(q)
        i = int(np.argmin(v))
        if v[i] < best:
            best = float(v[i]); bq = int(q[i])
        v1 = r1 * np.sqrt(q); i1 = int(np.argmin(v1))
        if v1[i1] < best1:
            best1 = float(v1[i1]); bq1 = int(q[i1])
        v2 = r2 * np.sqrt(q); i2 = int(np.argmin(v2))
        if v2[i2] < best2:
            best2 = float(v2[i2]); bq2 = int(q[i2])
        nviol += int(np.sum(v < C))
    return dict(Q=Q, joint_min=best, joint_arg=bq,
                coord1_min=best1, coord1_arg=bq1,
                coord2_min=best2, coord2_arg=bq2, violations=nviol)

t0 = time.time()
resA = scan(20_000_000)
resA["seconds"] = time.time() - t0

# Test B: high-precision recheck
import mpmath
mpmath.mp.dps = 80
s2 = mpmath.sqrt(2); s3 = mpmath.sqrt(3)
def hp(q):
    e1 = abs(q * s2 - mpmath.mpf(1) / 4 - mpmath.nint(q * s2 - mpmath.mpf(1) / 4))
    e2 = abs(q * s3 - mpmath.mpf(1) / 9 - mpmath.nint(q * s3 - mpmath.mpf(1) / 9))
    return e1, e2
resB = {}
for q in [resA["joint_arg"], resA["coord1_arg"], resA["coord2_arg"], 3, 3465, 102, 537]:
    e1, e2 = hp(q)
    m = max(e1, e2)
    resB[str(q)] = dict(
        e1=str(e1), e2=str(e2),
        joint_scaled=str(m * mpmath.sqrt(q)),
        coord1_scaled=str(e1 * mpmath.sqrt(q)),
        coord2_scaled=str(e2 * mpmath.sqrt(q)),
        beats_single_c1=bool(e1 * mpmath.sqrt(q) < mpmath.mpf(C)),
        beats_single_c2=bool(e2 * mpmath.sqrt(q) < mpmath.mpf(C)),
        beats_joint=bool(m * mpmath.sqrt(q) < mpmath.mpf(C)))
out = dict(testA_extended_scan=resA, testB_high_precision=resB,
           threshold_C=str(mpmath.mpf(C)))
with open("results_recovery.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
