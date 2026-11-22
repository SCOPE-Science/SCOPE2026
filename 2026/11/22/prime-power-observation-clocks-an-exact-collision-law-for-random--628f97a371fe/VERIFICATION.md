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

The complete argument is in `RESULT.md`. It uses Frobenius, independent residue-class recurrences, a Vandermonde minor, onto bilateral difference recurrences, exact coefficient extraction and Poisson factorial moments. None of these infinite claims is inferred solely from a computation.

Reproducibility: run `python3 verify_cylinder.py` with a standard Python 3 interpreter. It checks 7,080 independent finite-field rank evaluations, full small-volume coefficient enumerations, and 20,000 random samples against an exact success probability. The tests confirm examples and arithmetic identities, not global mathematical certification.

No independent mathematical audit has been performed. In particular, historical priority beyond the inspected literature remains unresolved.
