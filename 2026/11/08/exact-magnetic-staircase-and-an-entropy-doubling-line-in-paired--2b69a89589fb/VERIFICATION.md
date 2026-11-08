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

Run `python3 verify.py` in this package directory. It exhaustively enumerates all labeled Ising configurations and compares the exact Hamiltonian against the analytical sector formula for 714 combinations: system sizes from one through six pairs, seven rational matched-bond ratios, and seventeen rational field ratios. The general proof does not require numerical enumeration. No independent external audit has been performed.
