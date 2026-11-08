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

# Verification and limits

The accompanying Python standard-library program `verify_pitchfork_external.py` was run successfully and reported `PASS: 520 exact assertions; exhaustive event histories through n=7, Markov model through n=30`.

Its exhaustive branch enumerates all labeled histories of unordered coalescences for each size through seven, computes pitchfork count as exactly the number of size-two-lineage/size-one-lineage mergers, records singleton counts at each stage, and integrates out the independent exponential holding times using exact rational expectations. A separate weighted transition-state calculation handles sizes through thirty and compares all individual stagewise covariances to the proposed formula.

These are finite checks and do not certify the infinite assertion. That assertion relies on the explicitly proved factorial-moment recurrences, future-merger probabilities, finite rational identities, and polynomial telescoping sum in `RESULT.md`. The computation does not test other coalescent rate models, and no independent audit has been performed.
