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
# Reproducible checks

Run `python3 verify.py` after extracting all files in this package to the same directory. No external mathematical software is required. The file `verify_output.txt` is the actual recorded output from running this executable against the four supplied shelling orders.

The script enumerates the disconnected three-vertex subsets by graph connectivity and compares them bijectively to the listed facets for sizes 17–20. Every prior-facet intersection is compared against an earlier ridge of each new facet, and all spanning facets are counted. For sizes 11–16 it enumerates the complete Alexander dual, constructs all boundary columns, performs binary elimination, and checks the resulting reduced homology and Euler characteristic. The void cases at sizes nine and ten are also checked.

Passing these finite tests is not extrapolated to all sizes: the published Theorem 1.4 of Chauhan–Shukla (arXiv:2603.23155v1) supplies the infinite theorem for sizes at least 21. The four positive boundary cases are the only new finite proof obligations. The lower-range ranks are supporting independent verifications of already published data, not newly claimed numerical discoveries.

This verification is a reproducible self-review, not independent mathematical auditing or external certification.
