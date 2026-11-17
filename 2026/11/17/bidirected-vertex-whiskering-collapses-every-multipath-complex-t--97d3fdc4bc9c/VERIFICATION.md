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

# Reproducibility and proof limits

Run `python3 verify.py` with Python 3 and the standard library. It prints a JSON report. The saved `verification_output.json` is the observed successful output. The script independently enumerates legal faces of 24 concrete bidirectionally whiskered digraphs and, for tractable cases, compares with independent subset enumeration. It checks all free-face pairs of the proposed descending-core/descending-face collapse, the entire surviving face set, its Euler characteristic, and pair counting. Observed: 24 cases, 34,838 augmented faces, and 15,622 elementary collapse pairs; all tests passed.

The finite checks do not establish the assertion for untested vertex counts or all possible core digraphs. That follows from the general fixed-core fiber argument and the explicit free-coface order in `RESULT.md`. The automorphism action is proved by naturality of the pendant-only inclusion and join orientation, not inferred from tests. Bibliographic comparisons are best-knowledge only; independent mathematical audit is not performed.
