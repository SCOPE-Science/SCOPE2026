---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Melman Theorem 3.1 gives the two positive roots of x²−Ax+|a|²=0 with x=|z|^(2n), A=|b|²−2Re a, admissibility A≥2|a|. Writing A=2|a|coshη and sqrt(A²−4|a|²)=2|a|sinhη yields x±=|a|exp(±η). Taking 2n-th roots establishes the radii, their product |a|^(1/n) and logarithmic separation η/n=asinh(sqrtΔ/(2|a|))/n. The primary theorem supplies the nth-root angular solutions and n double zeros at Δ=0. The Taylor expansions give square-root opening for fixed a≠0. No incorrect algebra, domain extension or quantifier issue found; C PASS.

## originality

FAIL

FAIL by direct implication from the already-published complete root classification in Melman 2026 Theorem 3.1. Viète gives x+x−=|a|² and hence the radius product immediately; a positive reciprocal pair can always be written x±=|a|e^(±η), and elementary arcosh/asinh plus Taylor expansion give the exact gap and square-root splitting. Even if Melman uses different vocabulary and does not print the same normal form, the whole claim follows mechanically from its stronger explicit-zeros theorem. Finding no matching words in index searches cannot rescue covered corollaries.

## value

FAIL

FAIL independently: once the original source explicitly determines all zeros by one quadratic and lists the double-zero threshold, the proposed invariant product, log symmetry and square-root discriminant law require only Viète and first-order Taylor expansion. Their specific formulations add no motivated unresolved invariant/classification, structural lemma, independent boundary obstruction or nontrivial dynamical information beyond the known exact root formula. As a pedagogical reparameterization they are correct, but do not clear the common scientific value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
