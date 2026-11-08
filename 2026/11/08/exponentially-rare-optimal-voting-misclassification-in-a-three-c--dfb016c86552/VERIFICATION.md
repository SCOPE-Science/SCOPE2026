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

Run `python3 check.py` in the extracted directory. The script uses only Python's standard library.

Its completed run produced: 60 winning and 59 losing certificate occurrences with identical incidence vectors; all 56 profiles with at most five voters checked; 3,575,656 class profiles at sizes 5–60 checked; 294,912 fully enumerated labeled coalitions at sizes 5 and 6 checked; and 300 seeded relabeling certificates checked. All assertions passed.

The complete proof of the infinite inequalities is in `RESULT.md`: upper classifier, exact symmetric lower bound, and the random-injection averaging of the balanced certificate. Finite computer tests are not offered as proof for untested sizes or for arbitrary real weights. The precise unrestricted leading coefficient is not claimed. The original source's earlier normalized weight-excess formula is credited, not independently re-certified here. Independent scientific assessment has not been performed.
