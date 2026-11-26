---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Write each nonzero value uniquely as a/2^s with a odd. The magnitude restriction gives bit length ≤s, the significand gives bit length ≤p, and the smallest tick forces s≤L=E+p−1. Conversely if b is the numerator bit length, exponent b−1−s≥−E yields a normal by left-padding to p bits; below that exponent the integer a·2^(L−s) is below 2^(p−1) and occupies a subnormal slot. Under doubling followed by reduction, for s>1 the residue modulo 2^(s−1) is odd and nonzero, so the exponent falls by one; for s=1 the image is zero. Both operations are exact: the product fits with exponent up through zero, and any subtraction of one from a product in [1,2) is exact by the binary representability of the difference (or Sterbenz's lemma with gradual underflow). Thus the lifetime is s, counted by the 2^(min(s,p)−1) odd numerators. Every eligible exponent s≤L−t occurs in the t-th image with its entire allowable numerator set because a/2^(s+t) is a preimage. Counting these bottom L−t exponent levels gives the support, while counting the bottom min(t,L) levels and normalizing gives the CDF. Both formulas meet at their stated endpoints, also when E=1 or p=1; the least positive tick always realizes L. The IEEE parameters, state counts and optional extra initial endpoint agree. A distinct integer-valuation and low-bit masking replay checked histogram, CDF and support in 57 formats (24,285 initial states), including full binary16.

## originality

PASS

Prior work already establishes finite-precision collapse, its bit-shift mechanism and degenerate limit, the Float32 state count, and a computed support trajectory/cutoff under tested precision conventions. The supported distinct result is the pair of exact transient censuses for arbitrary p and E, including their different transition indices and the equal-distinct-state first-hitting law.

## value

PASS

Finite-precision collapse is known, but it does not say how many distinct states remain reachable or how much original mass has already collapsed. The exact trajectories quantify these different questions at different clocks (E−1 and p), explain their order dependence on exponent depth versus precision, and give a practical reference for interpreting finite-precision experiments under the equal-state convention without enumerating binary32 or binary64.

The dated certificate retains the supplied scientific assessment, sources and limitations.
