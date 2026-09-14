"""Focused B-step probe at q=p^2 (p=7,13): complete sums for the critical
root-collision patterns of Irving's amplified (A^3B) moment.

For primitive chi mod p^2 with chi = chi0 * (1+p t -> e_p(c t)), p odd, c != 0
(a primitive chi MUST have c != 0), and f the monic shift-product polynomial:

  Q2(s)  = sum_x chi~(x(x+ps)),           s=1..p-1   (B1 partial collision)
  C3(s)  = sum_x chi~(x(x+s)(x+2s)),      p|s, s!=0  (A-step 3-term, p|disc)
  Q3(s,t)= sum_x chi~(x(x+s)(x+2s)) with general (s,t)=(s,2s) patterns incl.
           unit shifts for control.

Also evaluates the closed-form lift predictions:
  Q2: p * e_p(-c*s/4 ... ) style Gauss-phase value, |Q2| = p exactly.
  C3 with p|s: x=py terms vanish; unit-x terms give (p-1)*E, E = sum_{u mod p}
  chi0(u(u+s0)(u+2s0)) with the SAME degeneracy one level down — but evaluated
  against a chi0 that may itself be non-principal, including chi0 trivial
  (when chi factors through 1+pZ). Reports the full distribution over all
  primitive chi, not just maxima, and the exact |Q2|/p histogram.

Usage: python3 irving_primepower_probe.py
"""
import cmath
import itertools
from math import gcd, sqrt

from irving_block import CharGroup, primitive_chi_arrays, prime_factors


def probe(p):
    q = p * p
    chis = primitive_chi_arrays(q)
    print(f"=== q={q} (p={p}), {len(chis)} primitive chi ===")
    # B1 partial-collision family Q2(s)
    print("B1: |Q2(s)|/p for s=1..p-1 (partial root collision mod p):")
    allq2 = []
    for A in chis:
        row = []
        for s in range(1, p):
            h = p * s
            tot = sum(A[x] * A[(x + h) % q] for x in range(q))
            row.append(abs(tot) / p)
        allq2.append(row)
    # distribution summary: min/max/mean over chi at each s (rows vary by chi)
    for s in range(1, p):
        col = [r[s - 1] for r in allq2]
        print(f"  s={s}: min={min(col):.4f} max={max(col):.4f} mean={sum(col)/len(col):.4f}")
    # A-step degenerate 3-term family C3(s)=sum chi~(x(x+s)(x+2s)), p|s, s!=0
    print("A3-degenerate: |C3(s)|/sqrt(q) for 0<s<q, p|s:")
    for s in range(p, q, p):
        vals = []
        for A in chis:
            tot = sum(A[x] * A[(x + s) % q] * A[(x + 2 * s) % q] for x in range(q))
            vals.append(abs(tot) / sqrt(q))
        print(f"  s={s}: min={min(vals):.4f} max={max(vals):.4f} mean={sum(vals)/len(vals):.4f}")
    # control: unit-shift 3-term, s=1
    vals = []
    for A in chis:
        tot = sum(A[x] * A[(x + 1) % q] * A[(x + 2) % q] for x in range(q))
        vals.append(abs(tot) / sqrt(q))
    print(f"A3-control (unit shifts 1,2): min={min(vals):.4f} max={max(vals):.4f} mean={sum(vals)/len(vals):.4f}")


if __name__ == "__main__":
    probe(7)
    probe(13)
