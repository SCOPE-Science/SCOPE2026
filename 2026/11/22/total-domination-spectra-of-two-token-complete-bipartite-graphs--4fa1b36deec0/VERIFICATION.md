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

The attached `verify.py` is a standalone Python 3, standard-library-only exact arithmetic checker. Run `python3 verify.py` in the directory containing this file. The expected terminal line is `VERIFY_OK`.

It computes the all-set inclusion-exclusion polynomial independently from brute incidence-mask enumeration on the parameters shown in the results, computes the minimal-set star-forest recursion independently from a single-edge-deletion test, constructs and directly checks full two-token graph adjacency for all vertex subsets at four small parameter pairs, and checks the minimum-size and multiplicity formulas. All computations are finite and exhaust precisely their stated domains; the proof of the parameter-uniform theorem is in `RESULT.md`.

Self-review has been performed; independent audit has not been performed. No formal verification or independent historical-priority determination is claimed.
