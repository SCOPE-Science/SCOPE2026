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

# Reproducible checks

Run the standalone `verify.py` using Python 3. No external packages or data files are required. The program independently builds each semigroup using ordinary coin-closure dynamic programming up to a safe bound derived from the two smallest coprime generators. The gap-interval formula is not used in that DP routine. It then checks the claimed expression over 5,000 integer pairs, exact branch polynomial evaluations over 43,554 cases, and cyclic-period comparisons for all moduli 2 through 120; a signature characterization is also checked for each modulus.

`checks.txt` contains the actual exact-arithmetic output from this implementation. This verifies finite cases only. The infinite assertion and sharp period depend on the explicit gap and signature arguments in `RESULT.md`, not on extrapolation. No independent mathematical audit has been performed.
