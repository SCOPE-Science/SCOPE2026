"""Corrected split-point trace-free Petri block check for lane-899.

F0 = A(+)B on a general genus-7 curve: A deg 8, h0=3 (W^2_8, chi=2, h1=1);
B deg 6, h0=2 (W^1_6, chi=0, h1=2). Verifies the corrected block table from
WORKLOG Step 7: no block has domain > target, so counting does NOT force a
kernel (retracts the mispaired 6->4 claim). Injectivity of the cross-maps is
NOT established here -- recorded as open. Stdlib only.
"""
import sys

FAILS = []


def check(name, cond, detail=""):
    print(("PASS" if cond else "FAIL"), name, detail)
    if not cond:
        FAILS.append(name)


G = 7
# line-bundle data
h0A, chiA = 3, 8 - G + 1
h1A = h0A - chiA
h0B, chiB = 2, 6 - G + 1
h1B = h0B - chiB
check("h1A==1", h1A == 1, f"h0A={h0A} chiA={chiA}")
check("h1B==2", h1B == 2, f"h0B={h0B} chiB={chiB}")
# H0(KA*), H0(KB*) dims via duality = h1A, h1B
# KAB* = K x A x B*: deg 12+8-6=14, chi=8, h1=h0(BA*) with deg(BA*)=-2 -> 0
h_KAB = (12 + 8 - 6) - G + 1
check("h0(KAB*)==8", h_KAB == 8, "h1=0 since deg(BA*)=-2 general")
# KBA* = K x B x A*: deg 12+6-8=10, chi=4, h1=h0(AB*) with deg(AB*)=2 -> 0
h_KBA = (12 + 6 - 8) - G + 1
check("h0(KBA*)==4", h_KBA == 4, "h1=0 since deg(AB*)=2 general")
blocks = {
    "A x KA* -> H0(K)": (h0A * h1A, G),
    "B x KB* -> H0(K)": (h0B * h1B, G),
    "A x KB* -> H0(KAB*)": (h0A * h1B, h_KAB),
    "B x KA* -> H0(KBA*)": (h0B * h1A, h_KBA),
}
dom = sum(d for d, _ in blocks.values())
tgt = G + h_KAB + h_KBA
check("domain==15", dom == 15, f"dom={dom}")
check("target==19", tgt == 19, f"tgt={tgt}")
forced = [(k, d, t) for k, (d, t) in blocks.items() if d > t]
for k, (d, t) in blocks.items():
    print("INFO block", k, "domain", d, "target", t)
check("no forced kernel by counting", len(forced) == 0, str(forced))
print("INFO diagonal blocks injective by Gieseker-Petri (C general => Petri);")
print("INFO cross-map injectivity OPEN (not established by counting).")
print("----")
if FAILS:
    print("PETRI_BLOCKS_FAIL", FAILS)
    sys.exit(1)
print("PETRI_BLOCKS_OK")
