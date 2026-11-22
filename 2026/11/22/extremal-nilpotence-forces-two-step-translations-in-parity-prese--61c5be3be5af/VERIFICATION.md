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

# Reproducibility and verification

The accompanying Python 3 standard-library file `verify.py` independently enumerates every parity-preserving increasing partial injection that preserves alternating-fence adjacency in both directions, for every chain size \(3\le n\le10\). It computes least zero powers from actual partial-map iterates and compares all observed maximal-index maps, rank spectra and finite monoid orders to the closed forms. Run `python verify.py` from this package; the success marker is `FENCE_EXTREMAL_NILPOTENCE_VERIFIED n=3..10`.

These finite enumerations are not a proof for arbitrary \(n\); the all-size proof is the orbit monotonicity, parity-class exhaustion, adjacent-gap rigidity and inclusion-exclusion argument in RESULT.md. Only the largest nilpotency index is enumerated. No independent mathematical audit was performed.
