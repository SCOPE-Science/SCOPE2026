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

Run `python3 verify.py` with standard Python 3. It performs exact set transitions on at most \(4\cdot256\) finite states, checks the decisive equality \(E_{11}=E_{17}\), verifies all six residue classes within the resulting period, checks the two exceptional masks, and independently enumerates all words of lengths \(3\) through \(15\). Equality of the full finite sets, plus determinism of the update, proves periodicity for every later length. Exhaustive word checks at bounded lengths are supplementary and not the justification for the infinite extension.
