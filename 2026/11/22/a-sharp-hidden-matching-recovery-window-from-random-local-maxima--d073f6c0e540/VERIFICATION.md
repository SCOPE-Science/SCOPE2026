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

The included standalone `verify.py` uses only Python 3's standard library. Run `python verify.py`. It constructs all perfect matchings on two, four and six labelled vertices and exhausts every priority permutation, checking the exact distribution of singleton and two-peak observations. It also verifies finite inclusion-exclusion formulas and basic minimax bounds in exact rational arithmetic. The recorded run completed with `PASS: 416 finite exact checks`.

The critical Poisson and minimax recovery limits are justified by factorial moments, a uniform posterior argument, and the stated variance bound, rather than by numerical experiments. The exercise is not an independent audit or an external proof certificate.
