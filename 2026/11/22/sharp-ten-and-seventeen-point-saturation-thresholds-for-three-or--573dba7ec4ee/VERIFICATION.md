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

The standalone `checker.py` reconstructs the three strict linear orders and their exact directed successor relations from each two-order witness. It evaluates all reference-edge pair types independently from relational membership, verifies each full Cartesian profile set and its marginal frequencies, and tests explicit extensions through one hundred vertices. The final run returned `VERIFY_OK thresholds=10,17 extension_sizes=10..100,17..100, exhaustive_path_counts=[6, 24]`.

The infinite family of larger models is justified by the append-at-end argument in `RESULT.md`; the program samples the finite initial segment of that construction only. The two lower bounds are elementary theorems based on the exact number of edges of a finite spanning successor path, not assertions drawn from enumeration. Both original witnesses and the executable source are included in the same scientific package. Independent auditing and historical-priority certification have not been performed.
