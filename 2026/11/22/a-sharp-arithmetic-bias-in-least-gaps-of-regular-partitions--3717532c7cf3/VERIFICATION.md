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

# Verification

Run `python verify.py` with Python 3 and no external dependencies. The script independently enumerates small regular partitions, computes restricted-partition counts using Euler's pentagonal recurrence, verifies the exact shifted survivor and point-mass formulas, then compares the analytic local and residue-class expansions to exact counts at a large finite argument. The output file `verification_output.txt` records the observed runs and ends with `VERIFY_OK`.

The 7,851 exact small-case comparisons test only the finite combinatorial identities. The 30 numerical comparisons corroborate convergence but neither prove the infinite asymptotic nor certify originality. The proof needs the published Rademacher/Hagis expansion, the explicitly stated uniform quotient remainder, and shifted Euler--Maclaurin summation. All mathematical limitations and prerequisite analytic results are specified in `RESULT.md`. No independent audit has been performed.
