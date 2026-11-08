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

# Verification

The included `verify_lie.py` contains two logically separate enumerators: `observed_classes` constructs each finite-period factor set and independently checks every rotation of each candidate, whereas `predicted_classes` constructs the exact families described in the theorem. It compares these *sets* and their cardinalities for every parameter-length configuration in the stated finite range, and includes seeded larger-alphabet tests.

Run with `python3 verify_lie.py`. A successful check reports 31,840 exhaustive cases for \(2\le q\le5\), all run lengths between one and four, and every length from one through twice the period; then 1,600 seeded cases for \(q=6,7\). The checker ran successfully on the embedded file before packaging. Finite checks alone cannot establish the all-length theorem; the proof in `RESULT.md` provides the universal argument.

The first-public guiding source is the 7 February 2021 arXiv version of Bell–Shallit (arXiv:2102.03821), which explicitly assigns primary subject 68R15. No external certificate, human review or independent scientific audit is claimed.
