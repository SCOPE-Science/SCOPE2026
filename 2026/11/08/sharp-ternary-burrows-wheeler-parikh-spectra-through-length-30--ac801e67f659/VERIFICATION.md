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

# Verification instructions

From the package root, compile `tools/checker.cpp` with a C++17 compiler and run it against `data/parikh_profiles.csv` for the three non-overlapping ranges \(13\)–\(28\), \(29\)–\(29\), and \(30\)–\(30\). Each range is complete for every word length it includes. Then execute `python3 tools/check_witness.py data/parikh_profiles.csv` to test all 115 CSV witnesses using direct cyclic rotations.

Observed exact checker summaries: length \(14\) has 4 sharp images in 1 type, length \(29\) has 8322 in 16 types, and length \(30\) has 1072 in 6 types. All 115 direct witnesses passed. An additional unpruned computation through length \(24\) agreed with the parity-pruned computation. These checks are exhaustive only for the declared finite range and do not constitute an independent mathematical audit.

The necessary parity lemma and the universal input-run lower bound come from the cited mathematical literature; they are assumptions only insofar as previously published results are used, not separately machine-proved here. No result about lengths above \(30\) is inferred.
