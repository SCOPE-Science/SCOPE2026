---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The mathematical proof uses the explicit hypotheses of Tuffley's sphere and degree-two theorems, free finite cyclic rotation, ordinary integral cyclic group cohomology, and a two-row Cartan–Leray cohomology spectral sequence.

The general nonzero-transgression step was checked symbolically: the only differential capable of eliminating infinitely many even-degree classes of \(H^*(BC_p;\mathbb Z)\) is \(d_{2q}\), which must be nonzero for a finite-dimensional quotient; modulo prime \(p\), nonzero is invertible. The degree-two inclusion gives the exact naturality equation; a putative homotopy equivalence multiplies the base generator by a unit and cover orientation by a sign, yielding the displayed signed-power obstruction. Universal coefficients determine the homology.

The accompanying exact arithmetic verifier was executed on its actual packaged source, with stdout compared byte-for-byte to `verification/expected_output.txt`. These finite cases are checks of arithmetic only and do not constitute a proof of any infinite topological claim. No independent external audit, machine-checked proof, or exhaustive literature uniqueness certification is represented.
