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

# Computational verification
Run `python verify.py` from the same directory. The program directly constructs isotropic projective vectors, nonzero rank-one nilpotents, and every additive character on the five-dimensional quotient for \(q=5\). It independently compares the direct complex Fourier sum with the integer root-count eigenvalue, and checks exact inclusion-exclusion multiplicities. Expected output includes `ISOTROPIC_VERONESE_FOURIER_CENSUS_PASS`. This finite check is not a proof in arbitrary field order; the proof is in `RESULT.md`. No independent audit has been performed.
