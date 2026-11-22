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

# Verification record

The theorem is proved by coloring-to-edge-set reconstruction and a fixed edge-cover augmentation injection. The computer test uses two different enumerations: (1) direct evaluation of \(L(X)\) and \(U(X)\) over vertex subsets, and (2) edge-cover enumeration with path parity checks. The maximal-ambiguity gap is checked for every observed pair in the finite suite.

Command: `python3 checker.py`.

Observed result: `VERIFY_OK graphs=226 label_tests=109278`.

The finite suite includes every labeled simple forest on two through five vertices having no isolated vertices, and 24 sampled labeled spanning trees at each of six and seven vertices. The argument in `RESULT.md`, not the tests, is the proof for unbounded forest order. Independent audit: not performed.
