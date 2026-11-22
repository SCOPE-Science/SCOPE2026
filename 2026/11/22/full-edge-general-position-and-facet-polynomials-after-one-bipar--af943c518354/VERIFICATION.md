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

# Verification procedures and limits

Build and run `direct_checker.cpp` with `g++ -O3 -std=c++17 direct_checker.cpp -o checker && ./checker`. The program derives the geodesic triples from graph distances and independently enumerates all subsets in five graph instances. It compares complete coefficient dictionaries for all-edge-set and facet polynomials with separately calculated closed-form coefficients. Its bounded check includes the twenty-four-edge graph and emits `DIRECT_CERTIFICATE_OK` only after exact matches.

Run `python3 check_formula.py` to compute coefficient distributions by integer binomial arithmetic for five direct cases plus a larger rectangular graph. These tests are independent corroboration of the formulas on finite instances, not a formal proof of the infinite family. The proof in `RESULT.md` supplies the all-parameter argument through the complete three-edge geodesic characterization and the exact facet cases.

No independent audit or external certification is asserted.
