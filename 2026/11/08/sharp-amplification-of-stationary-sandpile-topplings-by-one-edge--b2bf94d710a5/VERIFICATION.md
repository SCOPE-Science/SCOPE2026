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

Run `python verify_extremal.py` and `python verify_formula.py` with both files in one directory; no third-party packages are required. The first independently solves the grounded Laplacian rational linear systems for all source-leaf-rooted labeled trees and every missing edge with \(1\le N\le5\), exactly 20,796 edge augmentations. The second tests the exact rooted-descendant formula for all 7,035 possible source-to-nonroot insertions and checks the discrete maximizing distance for \(1\le N\le499\). Both completed with all assertions passing before packaging.

The proof covers every integer \(N\ge1\); numerical or finite enumeration does not certify the unbounded range. No independent scientific audit has been performed.
