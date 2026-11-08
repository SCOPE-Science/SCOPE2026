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

The standalone `verify.py` reconstructs every unlabeled tree on up to eleven vertices by canonical leaf extension, evaluates isolated-cluster variance using exact rational arithmetic, and checks the minimizing tree and value at each order. It separately enumerates every retained-edge subset for all trees through seven vertices and checks the second-moment formula; an independent Prüfer-word generator lists all labeled trees through order seven and agrees with the isomorphism-class enumeration and minimum. It also verifies the double-star comparison for orders eleven through one hundred as a consistency check; the proof for all larger orders rests on the inequalities in RESULT.md, not on this loop.

Actual command: `python3 verify.py`. Expected terminal line: `VERIFY_OK 18909 exact assertions / checks`.

This is finite reproducible checking plus a symbolic proof for the unbounded part. Neither this check nor the proof record constitutes an independent audit.
