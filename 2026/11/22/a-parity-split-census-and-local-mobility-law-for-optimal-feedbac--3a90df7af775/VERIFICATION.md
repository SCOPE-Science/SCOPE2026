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

The mathematical proof is given in RESULT.md. The following independent finite checks were actually executed with Python 3.

- `python3 verify_forest.py`: exhaustive union-find forest testing for every deletion set at the proposed minimum cardinality, for every \(3\le n\le12\). Exact counts by increasing circumference were `6,32,20,132,56,448,144,1360,352,3840`, agreeing with the column characterization.
- `python3 verify_mobility.py`: independent bit-mask graph construction and exhaustive slide-degree checks at odd circumferences \(3,5,7,9,11\). Edge totals were `6,20,84,288,880`; the degree histograms for the last three cases were `{2:14,3:28,4:14}`, `{3:36,4:72,5:36}`, `{4:88,5:176,6:88}`.

Both scripts completed with exit status zero and their stated success markers. These finite tests do not prove the infinite-family assertions. The proof of the all-length characterization, formulas, and local-move degree law is mathematical, not an extrapolation from the tests. No independent audit has been performed.
