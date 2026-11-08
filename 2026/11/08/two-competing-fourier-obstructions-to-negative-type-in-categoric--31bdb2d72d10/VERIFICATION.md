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

# Reproducibility checks

Run `python check.py` under Python 3 (standard library only) to construct the finite categorical-product graph by breadth-first search, verify the explicit path-distance case split, and compare every character sum directly to the claimed Fourier eigenvalue. The program checks 28 full distance/character-spectrum configurations and five endpoint critical-eigenspace multiplicities. The expected successful prefix is `CATEGORICAL_FOURIER_DISTANCE_PASS 28 parameter-exponent cases`; it then prints five `CRITICAL` entries. The exact all-dimensions statement is established by the proof in RESULT.md rather than by these finite cases. The asymptotic constant follows from symbolic expansions in RESULT.md; it has not been numerically certified at all dimensions. No independent mathematical audit was performed.
