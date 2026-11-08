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
# Verification and bounds

The included `VERIFIER.py` is a standalone, standard-library-only enumerator. Execute `python3 VERIFIER.py` from the folder containing it. For every \(3\le n\le6\) and \(1\le e<n\), it explicitly forms the \((2n+2)\)-by-\((2n+2)\) integer intersection matrix of all negative curves, enumerates every subset, and tests negative definiteness using exact-rational \(LDL\) pivots (not the proof's combinatorial threshold). It checks every coefficient of the proposed closed polynomial. It also checks the exchange symmetry and leading coefficient. `VERIFIER_OUTPUT.txt` contains the actual successful replay and the terminal line `ALL_CHECKS_PASSED`.

The uniform statement for all \(e\ge2\), \(n-e\ge2\) is proved by intersection inequalities and a Schur complement in `RESULT.md`. No finite experiment is asserted to prove the infinite statement. Source [3] could only be compared at abstract level; novelty assessment is therefore qualified by an explicit historical-priority risk. Independent mathematical validation has not been performed.
