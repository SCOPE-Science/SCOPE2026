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

# Reproducibility and limits

The accompanying standalone `verify.py` has no dependencies outside the Python standard library. Run `python verify.py` from the directory containing the extracted files. It uses 200 exact-rational parameter checks for both logarithmic derivative identities, 19 exact-rational sharpness examples, and two rational feedback targets outside the physical interval. Its output was:

```
PASS: 219 independent exact-rational identity/equilibrium cases; 2 excluded-regime witnesses
```

The analytic proof in RESULT.md is the evidence for the infinite-time theorem: an exact derivative identity plus a compactness contradiction. Finite arithmetic checks are only reproducibility and transcription aids. Supplementary material at the external article site was not accessible, so an independent literature-priority audit is outstanding. The sharpness construction proves existence of an interior stationary point, not its dynamical attraction.
