---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The unit-cell Gram matrix is (4I+S+S^{-1})/6; the cyclic Green row b_j=√3[(-q)^j+(-q)^(n-j)]/(1-(-q)^n), q=2-√3, solves the inverse equations for n≥3. Exact integral J(a,b) of the absolute linear nodal interpolation gives Λ_n=ΣJ, with strict-only-knot convexity via sign disagreement of adjacent kernel evaluations. The cardinal L1 norm is 2, and periodization yields strict 1<Λ_n<2. Two nearest translates dominate the defect; after centering x=m+s the tails contribute O(q^(2m)), leaving explicit piecewise-linear overlap integrals. Evaluation gives distinct positive C_even≈1.6830464193 and C_odd≈0.7011506234. Reconstructed all parameter boundaries, including n=3,4,5. Independent exact rational and float checks at n=3..5 and larger n agree and scaled deficits approach distinct coefficients. Finite checks are corroboration, not proof of asymptotic error.

## originality

PASS

The entire finite knot norm formula, strict finite bound and sharp exponential RATE are published already (October 26 and November 2). These portions are not original. Those full inspected proofs expressly do not determine the two distinct leading parity coefficients or uniqueness of ALL norming output locations. The present refined overlap asymptotics and norming-location classification are non-implied surviving results, subject to possible older uncatalogued equivalent formulas.

## value

PASS

A sharp leading parity coefficient and strict norming-output classification resolve two natural gaps left explicitly open in already published exact finite-n periodic projection bounds: they quantify the size and sign geometry of the finite-size stability defect, a classical numerical-analysis invariant. This is substantially more than renaming the old norm formula; elementary finite fractions and generic exponential rates alone are not claimed as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
