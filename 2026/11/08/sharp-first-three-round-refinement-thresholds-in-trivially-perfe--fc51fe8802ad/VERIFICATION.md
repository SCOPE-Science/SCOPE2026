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

Run `python3 check_tp_cutoff.py` with Python 3. The checker generates all unlabelled rooted forests through order nine using a recursive sorted-multiset representation, constructs ancestor-comparability graphs, and calculates strict partition refinements by two independent implementations. It checks every graph, not a sample. The full observed count histograms and PASS line are in `check_tp_cutoff_output.txt`. Exactness relies on the elementary rooted-forest representation and uniqueness proof in RESULT.md. It does not constitute independent third-party validation, and no claim about graph orders above the first thresholds follows from the census.
