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

## Reproduction
Run `python3 category_certificate.py` to inspect all 81 three-symbol population patterns, and `python3 direct_validation.py` to compare the closed labelled-state population law against direct full-configuration trajectories for n=2,...,9. Both programs use only the Python standard library. Their exact recorded outputs are `category_output.txt` and `direct_output.txt`. The symbolic category classification proves the all-size bound; direct enumeration alone would not.

## Boundaries
For n=2 all 16 configurations are fixed; for n=7 the depth-three population first becomes positive (2520); for n=8 the first primitive-four population is 2520. The category proof covers all larger n with no truncation. Historical comparison includes an early preprint abstract which could not be obtained as complete text. Independent audit is not performed.
