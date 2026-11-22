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
# Verification record

The finite verifier `verify.py` was executed from the actual packaged bytes. It checks prime-field Paley intersection sizes for five odd primes congruent to three modulo four; direct modular square statuses against the valuation/Legendre criterion at 1399 positive exponents per prime; finite-index pair densities at multiple precisions and shifts; and direct Mersenne pair samples at several lengths and shifts.

It produces `verify_output.txt`. The approximate finite-block comparisons are consistency checks with explicit finite tolerances and are not proofs of the infinite limits. The infinite theorem is established by the analytic shell partition, a finite-field character-sum identity, a recursive valuation case split, and residue-class counting. Source comparison is bounded and not a proof of uniqueness; independent audit is not performed.
