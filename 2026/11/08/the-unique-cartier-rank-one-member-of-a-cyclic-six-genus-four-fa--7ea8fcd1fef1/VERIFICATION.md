---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Squarefreeness of xQ(x³) in characteristic 11 is equivalent to bΔ≠0, yielding a genus-four smooth completion. The coefficients of f^5 at indices 11i−j have exactly the displayed three disjoint blocks. On b≠0 the first outer block vanishes only at (0,−2). For the other block v_2−3v_1=aL: a=0 again gives (0,−2); a=4 gives only b=−2, which is singular; otherwise substituting (1−3a)b=−a²+3a+4 gives the cleared powers of a−4, excluding any further simultaneous zero over the algebraic closure. At (0,−2), Δ=10 and P=5, so precisely the Frobenius-stable middle direction survives; Cartier rank and 11-rank are both one. Everywhere else the outer blocks contribute two, so the smooth P=0 locus has a-number two and the remaining locus has a-number one. `python3 /workspace/reviews/evidence/reproduce.py 1` used independent multinomial coefficient extraction, exact polynomial reductions, a squarefree gcd and modular minors on all 121 base-field pairs, obtaining 101 smooth parameters and counts 83,17,1. The finite enumeration is not the proof over the closure. The supplied scripts were inspected, not executed.

## originality

PASS

Supported for the explicit characteristic-11 positive-rank stratification over the algebraic closure, in particular the smooth divisor P=0 and its separate unique rank-one parameter. The family, Cartier coefficient rule, rank-zero exclusion, and method of computing matrices are prior, and the finite counts are supporting data rather than a new isomorphism classification.

## value

PASS

For an already studied cyclic genus-four family, the result identifies the full geometric jump divisor and one isolated more extreme Cartier type; the exceptional point also has exactly determined stable rank. Exact geometric membership, not merely enumeration of rational parameters, makes the result a useful classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
