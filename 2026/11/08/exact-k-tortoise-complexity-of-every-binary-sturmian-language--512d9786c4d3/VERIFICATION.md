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

# Reproducible checks and proof responsibilities

Run `python3 verify_tortoise_sturmian.py` with standard Python 3. No dependencies beyond the standard library. Its method enumerates the \(n+1\) rotation cells for each tested irrational slope, generates their distinct factors, applies the first-one-moving tortoise transformation literally, and compares the resulting number of images against the claimed exact formula. A separate orbit-prefix generator reconstructs the factor language for the initial lengths without using the rotation-cell sampling procedure.

Observed successful outputs:

```text
PASS: 11200 (slope,length,iteration) exact language checks
PASS: 320 independent orbit-language comparisons; 25550 rotation cells
Limits: finitely many quadratic slopes/lengths/iterations; proof establishes infinite claim.
```

The universal proof relies on four mathematical assertions given explicitly in `RESULT.md`: mechanical rotation partition, the \(01\)/\(10\) transposition at each interior cut, the transposed one's rank \(\lceil j\alpha\rceil\), and the largest-cut/rightmost-surviving-digit no-nonlocal-collision argument. The finite enumeration is not an exhaustive search over all irrational slopes or all lengths. It uses 64-digit Decimal samples and is not a formal arithmetic proof. No independent audit has been carried out.
