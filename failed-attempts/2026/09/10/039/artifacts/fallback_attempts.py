"""Bounded PRESET_FALLBACK attempts (lane 598).

Fallback: D^{cc}(F_n) >= n/16 for ALL powers of 2 n>=16,
via logged disperser-plus-simulator lifting from DT bound.

F1: unique-collision counting sweep -- how far does the elementary
    deterministic bound reach?
F2: required-method check -- does IND_3 admit the disperser/simulator
    template the qualification demands? (reuses exact census constants)
F3: refutation search -- any concrete sublinear deterministic protocol
    shape at the first open slice (n=512)?
Stdlib only.
"""
import math

print("=== F1: unique-collision counting sweep ===")
# For each pair {i,j}: z with unique collision (i,j at hole 0, rest bijected
# to holes 1..n-1); lifted with x=0^N, y realizing z. Deterministic protocol
# needs distinct transcripts per pair: D >= ceil(log2(C(n+1,2))).
ok = []
for e in range(4, 14):
    n = 2 ** e
    pairs = (n + 1) * n // 2
    lb = math.ceil(math.log2(pairs))
    need = math.ceil(n / 16)
    holds = lb >= need
    ok.append((n, lb, need, holds))
    print(f"n={n:5d}: counting D>={lb:3d} vs need>={need:3d} "
          f"=> {'HOLDS' if holds else 'GAP'}")
print("F1 outcome: counting proves fallback only for n<=256; "
      "n>=512 needs a genuinely new linear lifting argument.")

print("=== F2: required-method (disperser/simulator) check ===")
# Qualification demands proof 'via a logged disperser-plus-simulator
# lifting argument'. Sufficient hypotheses and IND_3's exact constants
# (exhaustive 2x4 census, see probe_gadget.py / target_routes.py Route C):
print("IND_3: discrepancy(uniform)=0.25 (need exp-small in N) -> FAIL")
print("IND_3: max monochromatic-rectangle density=0.25 "
      "(need dispersing) -> FAIL")
print("IND_3: rank=2 (de Rezende needs >=12enk/NS = Omega(log^2 n)) -> FAIL")
print("IND_3: D(gadget)=1 (Iyer needs large constant) -> FAIL")
print("Deterministic covering lifts: GPW/log-discrepancy need log-size "
      "gadget; stifling gives PDT-size only; semi-structured is "
      "parity-restricted; Beame-Koroth needs near-linear Index size and "
      "marks constant size OPEN.")
print("F2 outcome: the exact method named by the success criterion is "
      "certified inapplicable to IND_3; constant-size deterministic "
      "lifting to standard CC is the documented open conjecture.")

print("=== F3: refutation search at first open slice n=512 ===")
n = 512
N = (n + 1) * int(math.log2(n))
print(f"n=512: N={(n + 1)}*9={N} query bits; counting forces D>=18; "
      f"refutation needs explicit deterministic protocol with cost<32.")
print("Candidate shapes: (a) birthday sampling is randomized, not "
      "deterministic; derandomizing to worst case needs s=Theta(n) reads "
      "=> Omega(n log n) >> 32. (b) Sending all pointers costs N=4617 "
      ">> 32. (c) No sparse-certificate structure: single-collision "
      "instances force reading Theta(n) pigeons in the worst case.")
print("F3 outcome: no concrete refuting protocol shape; refutation would "
      "itself be a research-level upper-bound construction.")
print("FALLBACK_BLOCKED")
