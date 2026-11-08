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

# Reproducibility and proof checks

The accompanying `verify.py` runs with a standard Python 3 interpreter; invoke `python3 verify.py` from the folder containing the package. It constructs the fixed point by nine substitution iterations and independently checks all 19,683 symbols against base-three digit parity. For all 512 positive antisquare orders and all 4,096 starts, it independently tests each word factor for exact bitwise complementation and compares that Boolean outcome with the claimed starting-position formula, giving 2,097,152 checks. It tests the derivative recurrence over 2,187 quotient values and the two primitive witnesses. Successful completion prints `VERIFY_OK`.

The proof of the infinite claim is entirely in `RESULT.md`: adjacency-residue obstruction for orders not divisible by three; substitution-based reduction and lift; exact quotiented block comparison; derivative recurrence and natural-density discrepancy. The finite checker is not an exhaustive verification of all infinite factors and does not certify bibliographic novelty or independent validation. The density limits are for fixed order as the start cutoff tends to infinity.
