---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Since t=s/(xy), nonzero target coordinates have equal positive v2 h. Substituting y=s-x and completing the square in Z/2^(k-h) proves a bijection to quadratic roots, each with exactly 2^h lifts. The parity of required roots is automatically enforced by the discriminant. Odd-square, even-square and zero-root counts give every fiber, plus sumset image sizes; Haar continuity from above gives limit 1/96. Independent complete convolution over all pairs and targets for k=1..8 reproduced image counts 1,2,4,12,24,72,216,792. Finite computation corroborates rather than proves for all k.

## originality

FAIL

FAIL: full primary November 8 theorem Exact pair-sum fibers and image density of the dyadic modular inverse hyperbola gives the same ordered r_k(s,t) at EVERY target via an explicitly parity-filtered square-root count, same nonzero valuation shells, same image density 1/96, identical k>=4 image-size formulas in parity-expanded form, and the known fourth moment. In submitted version the root parity is forced by the discrimination condition, hence the two pointwise formulas are mathematically equivalent. Earlier theorem covers k>=4; only easy small boundary k=1,2,3 is newly listed and cannot support substantive novelty.

## value

FAIL

FAIL incremental value: the natural entire pointwise representation spectrum and sumset-density problem is solved in the full prior theorem, which even includes energy. Listing three trivial smaller moduli and choosing a non-parity-filtered root notation provides no non-implied motivated invariant or substantive improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
