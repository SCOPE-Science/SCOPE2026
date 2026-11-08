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

# Reproducibility

Using Python 3 with the SymPy package installed, execute `python verify_moments.py` in the extracted directory. The expected diagnostic is `PASSED 612 exact independent pair updates and moment identities` followed by `CHECK_LIMITS 6/7 3/7 26/7`.

The script checks symbolic stationary generator balances and normalized fourth-order ratios, then evaluates five exact identities on 117 seeded rational configurations with \(N\) between 2 and 10 and three additional exact balance equations for nine finite sizes. The all-\(N\) proof is the algebraic generator calculation and the analytic moment/stationarity argument in `RESULT.md`; a finite computation is not presented as a substitute for that proof. There was no independent scientific audit or independent publication-priority certification.
