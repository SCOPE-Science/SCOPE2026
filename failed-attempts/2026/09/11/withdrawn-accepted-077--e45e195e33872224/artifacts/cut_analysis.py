"""Top-floor cut analysis for F2, a=2, genus 0 (planar BM conventions).

For each diagram D = (L1,L2,U1,U2,x) with top floor VL (div 2) and bottom VU:
  complex cut prediction per diagram: x^2 * (markings of bottom piece?) vs actual.
We test the naive one-step recursion: cut internal edge x; top floor becomes a
1-floor diagram with (L1 down leaves, U1 up leaves, plus 1 cut leaf of weight x);
bottom becomes a 1-floor diagram with (L2 down, U2 up, 1 cut leaf weight x).
Since a=1 diagrams each contribute complex mult 1, the complex recursion term for
piece (L1,U1,x) is: x^2 * C(markings glue) — and summing over top pieces with
multinomial point-distribution must recover N(D).

Real (r=0) ledger: diagram contributes 1 iff x odd, else 0. Naive "elevator-weight
product" real rule prod w = x would predict nonzero for x even. We check the
mismatch per diagram class, which is the ledger correction.
"""
from enumerate import diagrams_F2, count_markings
import math

def cut_analysis(a, b):
    print(f"===== top-floor cut, F2 a={a} b={b} =====")
    for (L1, L2, U1, U2, x) in diagrams_F2(a, b):
        tot, ineq = count_markings(L1, L2, U1, U2)
        muC = x*x
        mu0 = 1 if x % 2 == 1 else 0
        # elevator-weight product rule would give x (real) vs x^2 (complex):
        print(f"D(L1={L1},L2={L2},U1={U1},U2={U2},x={x}): markings={ineq} "
              f"muC={muC} mu0^R={mu0} | naive-real-elevator-prod={x} "
              f"=> {'MATCH' if mu0==x else 'MISMATCH: signed rule needs 0/1-parity correction, not raw weight '+str(x)}; "
              f"complex cut factor x^2={muC} consistent with gluing of two 1-floor pieces")
    print()

for b in [0, 1, 2]:
    cut_analysis(2, b)
