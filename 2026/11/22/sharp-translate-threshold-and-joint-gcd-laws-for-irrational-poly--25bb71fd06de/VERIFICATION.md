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

# Verification notes

Run `python verify.py` using the Python standard library. The script has exact finite residue and local-valuation checks, observations at \(120000\) quadratic and \(60000\) cubic inputs, and an explicit quadratic finite-difference exclusion. It was executed successfully against the bundled source. The infinite law is proved by Weyl equidistribution plus Holdridge's published large-prime elimination; no finite run substitutes for the latter theorem. Independent validation is not performed.
