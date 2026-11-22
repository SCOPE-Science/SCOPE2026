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

Two runnable Python 3 standard-library programs, `check_primary.py` and `check_scalar.py`, construct the Tutte eight-cage from duads and synthemes and exhaust all \(2^{15}\) states on each incidence shore. Both were executed successfully, using `python3 check_primary.py` and `python3 check_scalar.py`, respectively. They assert all 32,768 instances of the polynomial map identity on each shore, enumerate 2,386 phase labels, independently reproduce the nine paired fiber classes, and compute all orbit-basin populations. Their exact outputs are embedded as `primary_results.json` and `scalar_results.json`.

The Cartesian-product factorization proves that these finite shore enumerations account for all \(2^{30}\) labelled initial states without naively visiting a billion full configurations. The computed complete basin weight identity equals 1,073,741,824, and the first-periodic-entry histogram sums to the same total. The sharpness witness is the state with duad mask 106 and syntheme mask zero, which first reaches a fixed state at update four.

No theorem about arbitrary graphs is inferred from this finite computation. The proof applies to exactly this graph and the specified threshold-two synchronous rule. A separate external mathematical assessment has not been performed.
