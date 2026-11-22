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

Checks made from the included `verify.py` using Python standard library alone. The script checks 10,000 exponent pairs by independently iterating the explicit state transition; 192 prime-power triples by calculating the first Fibonacci zero modulo the integer directly (without invoking the exponent formulas for the rank), including the exact destination fixed point; and ten finite lattice inclusion-exclusion identities. At four logarithmic sample cutoffs it also compares empirical distributions and means with the claimed asymptotic values. These are consistency checks, not a proof of the formula for infinitely many exponents or the limit theorem. The source rank identities and the lattice-point estimates, together with the analytic argument in `RESULT.md`, establish those claims. No independent audit has been performed.
