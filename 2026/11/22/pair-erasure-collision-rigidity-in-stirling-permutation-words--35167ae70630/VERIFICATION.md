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

# Verification

Run `python3 verify.py` with standard Python 3. The program generates each order \(n\in\{2,3,4,5,6,7\}\) from the unique order-one source by exhaustive largest-adjacent-pair insertion and constructs all erasure descendants directly. Its independent predicates test the three permitted label-interval geometries, equivalence-class convexity, pair-count products, exact rational mean, and three one-output words for each order.

On replay the program printed `VERIFY_OK`, with \(135135\) sources and \(2837835\) pair checks at order seven. Exhaustive finite enumeration independently validates only these finite cases, not the infinite theorem; the proof relies on a general induction through insertion and the exact count of destructive gaps. There is no external independent audit.
