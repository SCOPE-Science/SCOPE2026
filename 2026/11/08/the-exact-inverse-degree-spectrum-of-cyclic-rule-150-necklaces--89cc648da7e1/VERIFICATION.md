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

Run `python3 verify_rule150_necklaces.py` using standard Python 3. The program constructs each labeled cyclic Rule 150 state transition, groups source and target configurations independently into rotation classes, and checks every output against both the exact degree formula and the independent Möbius–Burnside histogram.

The actual replay ended with:

`VERIFY_OK exhaustive_lengths=1..18 formula_censuses=3,6,..,60`

The exhaustive ranges are all ring lengths from \(1\) through \(18\). Arithmetic-only identity checks cover every multiple of three up to \(60\). These checks do not establish the unbounded theorem; the proof depends on the three-periodic kernel, the exact image parity constraints, and the stabilizer action on each four-element labeled fiber. All required code is included without nonstandard dependencies. No independent mathematical audit has been performed.
