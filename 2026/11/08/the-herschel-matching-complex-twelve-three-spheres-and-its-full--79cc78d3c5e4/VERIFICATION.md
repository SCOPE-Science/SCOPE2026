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

# Verification information

Execute `python3 herschel_matching_verify.py` using a standard Python 3 interpreter. The adjacent output file records a successful execution with the exact terminal marker `HERSCHEL_MATCHING_INTEGRAL_WEDGE_AND_CHARACTER_PASS`.

The proof-critical checks are (i) two complete face enumerations; (ii) disjointness and completeness of all 369 matched pairs; (iii) exhaustive acyclicity on 751 simplices and all 2,502 nonempty face-poset covers; (iv) the exact critical-cell dimension histogram; (v) the explicit full group action and signed Lefschetz character; and (vi) an independent edge-orbit character computation. Finite-field boundary ranks provide separate corroboration but are not treated as integral homotopy certificates.

This executable verification checks the specified finite graph only. It does not establish publication priority, a classification for other graphs, or independent external certification. No external audit has been performed.
