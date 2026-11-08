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
Run `python verify.py` from the extracted package directory with Python 3. The program uses integer arithmetic and heap-based shortest paths. It independently enumerates all triples \(1\le a<b<c\le120\) with joint gcd one, calculates the Frobenius number by Apéry residues, and compares equality against the asserted classification; it also tests the exact two-coin interval criterion for all admissible cases with \(2\le k\le2000\). These computations corroborate the proof but cannot replace Kneser's theorem or establish the claim beyond the finite checked ranges. The known three-generator upper bound is quoted and used from arXiv:2610.32219v1. External independent audit has not been performed.
