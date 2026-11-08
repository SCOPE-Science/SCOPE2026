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

The mathematical proof gives the characteristic-two all-field statement. Independently, run `python3 verify_tuples.py` from the folder containing the extracted package files. The checker enumerates finite-field polynomial coefficients, direct square-zero compositions and all pairwise commutators, comparing each checked total to the symbolic formula. All listed examples pass. Extension-field multiplication over \(\mathbb F_4\) uses the irreducible polynomial \(\xi^2+\xi+1\); this does not certify all extension fields. Output in `verification-output.txt` is a reproducibility aid, not independent mathematical validation. No independent audit has been performed.
