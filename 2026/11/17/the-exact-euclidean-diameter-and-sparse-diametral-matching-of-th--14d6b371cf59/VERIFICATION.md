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

Run `python3 artifacts/verify_diameter.py` from the extracted package root (Python standard library only). Expected output:

```
HARMONIC_DIAMETER_PASS exhaustive=[(2, 6, 1, 16), (3, 66, 3, 36), (4, 1200, 24, 68)] witnesses_n=2..100 random_pairs_n5=120000
```

The program enumerates every fine-harmonic-triple vertex (not every Minkowski generator) and every unordered vertex pair in orders 2, 3, and 4, verifying exact integer squared distances, maximum values, and all equality cases. It verifies explicit maximizing witnesses through order 100 and a reproducible seeded finite sample of pairs in order 5. No part of that finite sampling is asserted to be an exhaustive proof for higher dimensions. The all-dimensional argument is the strict rearrangement identity, the sharp coordinate perturbation bound with simultaneous equality, and the strict convexity of squared Euclidean distance in each endpoint.

The primary definition and vertex criterion were checked in the published preprint arXiv:2006.03078, particularly Definition 2.1 and Propositions 3.5–3.6. The precise published radial-shell theorem was compared for possible stronger coverage. This document does not claim independent verification.
