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

The all-size stability identity and the fixed-point and random asymptotic laws are established by symbolic arguments in RESULT.md. `verify.py` provides finite corroboration via two separate state-update implementations: (a) unordered six-petal-type aggregation with exact multinomial/orientation weights, and (b) direct simultaneous updates of all labelled vertices. The agreement is checked for all three-color labelled states through five petals, and all weighted states through ten petals. The exact equilibrium formula is checked against every one of these weighted censuses. The three sharpness witnesses are directly replayed, and appending three monochromatic petals is checked for further cases.

Run `python3 verify.py` in the same directory with Python 3 and no external dependencies. `verification_counts.txt` is the recorded standard output of that command. The finite verification is exhaustive for each of the specified sizes, but not for unbounded petal counts; the proof covers those counts. Historical priority and independent external review are not certified.
