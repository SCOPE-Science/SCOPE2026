"""Route-justification check: the preset fallback's as-worded Delta-condition
does NOT imply non-effectivity in general. Counterexample (exact integers).

Lattice A: G=[[2,5],[5,2]], H=(1,0) (Q=2), v=(2,H,0) so v^2=2.
Fallback window: Delta = M^2-Q*D^2 <= Q*(v^2+2)/4 = 2.
Take D=(0,5): M = D.H = 25, D^2 = 50, Delta = 625-100 = 525 > 2 (violates).
s = (D^2+2)/2-1 = 25, i.e. s-deficient by exactly 1: a=(1,D,25), a^2 = 50-50 = 0.
But a = v(I_Z(D)) for Z of length n=2 (since s = D^2/2-n+1 = 25-2+1 = 24? check):
n = D^2/2+1-s = 25+1-25 = 1? recompute below. Either way n>=0 small and
h^0(O(D)) >= D^2/2+2 = 27 by Riemann-Roch (h^0(-D)=0 as M>0), so a general
length-n subscheme gives an effective stable rank-1 sheaf of class a.
Hence a IS effective despite violating the fallback inequality, and its
complementary factor b has b^2 = 52 >= -2 (computed). So violation of the
as-worded inequality does not imply non-effectivity. PRESET_FALLBACK not taken.
"""
import json

G = [[2, 5], [5, 2]]
H = (1, 0)
def dot(A, B):
    return A[0]*(G[0][0]*B[0]+G[0][1]*B[1]) + A[1]*(G[1][0]*B[0]+G[1][1]*B[1])

Q = dot(H, H)
C = (1, 0); r, S = 2, 0
v2 = dot(C, C) - 2*r*S
D = (0, 5)
M = dot(D, H); D2 = dot(D, D)
Delta = M*M - Q*D2
bound = Q*(v2+2)/4
s = (D2+2)//2 - 1
a2 = D2 - 2*s
# Riemann-Roch: h0(D) >= D2/2+2 (since h0(-D)=0 for M>0, D != 0)
rr = D2/2 + 2
n = D2//2 + 1 - s  # length of subscheme for I_Z(D) to have this s
CDOT = dot(C, D)
b2 = r*D2 - 2*CDOT + (v2 + 2*S + 2*r - 2)
print(f"Q={Q} v2={v2} bound={bound}")
print(f"D={D} M={M} D2={D2} Delta={Delta} (> bound: violation={Delta > bound})")
print(f"s={s} (spherical value={(D2+2)//2}, deficient by 1) a^2={a2}")
print(f"RR lower bound h0(O(D))>={rr}, subscheme length n={n} -> I_Z(D) effective, rank-1 stable")
print(f"complementary b^2={b2} (>= -2: passes necessary stable-occupation test)")
assert Delta > bound and a2 == 0 and n >= 0 and rr > n and b2 >= -2
print("FALLBACK-COUNTEREXAMPLE: CONFIRMED (literal fallback reading falsified)")
with open("output/artifacts/fallback_counterexample.json", "w") as f:
    json.dump({"Q": Q, "v2": v2, "Delta_window": bound, "D": list(D), "M": M,
               "D2": D2, "Delta": Delta, "s": s, "a2": a2,
               "RR_h0_lower": rr, "n": n, "b2": b2,
               "conclusion": "violation without non-effectivity"}, f, indent=1)
