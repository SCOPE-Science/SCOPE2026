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

# Verification procedure

Run `python3 verify.py` from this directory. The script uses only the Python standard library, enumerates all independent-bond states after every possible one-vertex deletion in the five- and seven-vertex graphs, and reconstructs exact expected outbreak polynomials using rational arithmetic. It checks the two-triangle analytic formulas, the factorization, representative strict inequalities and an exact six-decimal root bracket.

Checked execution: `PASS: 32 exact identities and rational inequalities; 412 exhaustive bond configurations across all vertex deletions`. The strict uniqueness of the crossover follows analytically from the transformed polynomial's single positive root, not merely from numerical bracketing. The general-size existence statement follows from the analytical small-transmission expansion and complete-transmission endpoint; the finite verifier does not range over every clique size.

No independent audit has been performed. Historical priority and applicability to general infectious-period SIR processes remain unverified.
