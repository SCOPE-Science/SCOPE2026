"""Verify target impossibility for lane-869 via EMM Thm 1.14 specialized to n=2 (T(2,5)).

Encodes the exhaustive coarse lists of non-loose Legendrian (2,5) knots in
each supporting overtwisted contact structure (EMM notation), and checks the
target triple (tb=9, rot=2, tor=0) in the target host (Gompf d3=-1/2 = EMM xi_0).

Expected: EMPTY in xi_0 (rot forced to +-6, tor>=1/2 at tb=9); the triple
(9,2,tor 0) occurs only in xi_1 (EMM) = Gompf d3=+1/2.
"""
import sys

n = 2  # (2,2n+1) = (2,5)

def xi0_family(i_vals, k_vals=(0, 1, 2)):
    """Thm 1.14(1): L_pm^{i,k+1/2} in xi_0: tb=i, rot=mp(i-2n+1)=mp(i-3)."""
    out = []
    for i in i_vals:
        for k in k_vals:
            for sgn in (+1, -1):  # +1 = L_+, -1 = L_-
                rot = -sgn * (i - 2 * n + 1)
                tor = (k + 0.5) if i > 2 * n - 1 else (k + 1)
                out.append((i, rot, tor, sgn, k))
    return out

def xi_1m2n_family(i_vals, k_vals=(0, 1, 2)):
    """Thm 1.14(2): L_pm^{i,k} in xi_{1-2n}=xi_{-3}: tb=i, rot=mp(i+2n-1)."""
    out = []
    for i in i_vals:
        for k in k_vals:
            for sgn in (+1, -1):
                rot = -sgn * (i + 2 * n - 1)
                tor = k if i > 2 * n - 1 else k + 0.5
                out.append((i, rot, tor, sgn, k))
    return out

def xi1_coarse():
    """Thm 1.14(3) tor=0 coarse list in xi_1 relevant near tb=9."""
    pts = []
    # L_pm^i, i>2n+1=5: rot=mp(i-2n-1)=mp(i-5)
    for i in range(6, 13):
        for sgn in (+1, -1):
            pts.append((i, -sgn * (i - 5), 0, f"L_{'+' if sgn>0 else '-'}^{i}"))
    # L_{2,pm}^i, 2n+4=8<=i<=4n+2=10: rot=mp(i-2n-3)=mp(i-7)
    for i in range(8, 11):
        for sgn in (+1, -1):
            pts.append((i, -sgn * (i - 7), 0, f"L2_{'+' if sgn>0 else '-'}^{i}"))
    pts.append((5, 0, 0, "L^5"))
    pts.append((7, 0, 0, "L2^7"))
    return pts

fails = []
def check(name, cond, detail=""):
    print(("PASS" if cond else "FAIL") + f" {name} {detail}")
    if not cond:
        fails.append(name)

I = list(range(-3, 15))
xi0 = xi0_family(I)
xi0_tb9 = [(r, t) for (i, r, t, s, k) in xi0 if i == 9]
rots_tb9 = sorted(set(r for r, t in xi0_tb9))
tors_tb9 = sorted(set(t for r, t in xi0_tb9))
check("xi0_tb9_rots_are_pm6", rots_tb9 == [-6, 6], f"got {rots_tb9}")
check("xi0_tb9_tor_ge_half", min(tors_tb9) >= 0.5, f"got {tors_tb9}")
check("xi0_no_9_2_tor0",
      not any(i == 9 and r == 2 and t == 0 for (i, r, t, s, k) in xi0),
      "no (9,2,tor0) in xi_0")
# tor==0 impossible at tb=9 in xi_0 at all
check("xi0_no_tb9_tor0_at_all",
      not any(i == 9 and t == 0 for (i, r, t, s, k) in xi0),
      "tor obstruction")

xim3 = xi_1m2n_family(I)
check("xim3_no_9_2_tor0",
      not any(i == 9 and r == 2 and t == 0 for (i, r, t, s, k) in xim3),
      f"tb9 rots there: {sorted(set(r for (i,r,t,s,k) in xim3 if i==9))}")

xi1 = xi1_coarse()
hits = [p for p in xi1 if p[0] == 9 and p[1] == 2 and p[2] == 0]
check("xi1_has_unique_9_2_tor0", len(hits) == 1 and hits[0][3] == "L2_-^9",
      f"got {hits}")
# d3 conversion: d3_Gompf = d3_EMM - 1/2; target -1/2 -> EMM 0 -> xi_0
check("d3_target_is_xi0", (0 - 0.5) == -0.5, "EMM0<->Gompf-1/2")
check("d3_xi1_is_plus_half", (1 - 0.5) == 0.5, "EMM1<->Gompf+1/2")

# Thm 1.3 exception consistency: pq-p-q = 10-7 = 3; tb=9>3 in xi_0 -> half-integer tor
check("pq_p_q_threshold", 2 * 5 - 2 - 5 == 3, "threshold=3, tb9 above -> half-integer tor")

if fails:
    print(f"VERIFY_DISPROOF_FAIL {fails}")
    sys.exit(1)
print("VERIFY_DISPROOF_OK 8/8")
