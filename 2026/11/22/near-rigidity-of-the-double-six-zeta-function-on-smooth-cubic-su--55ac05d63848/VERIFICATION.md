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

# Reproducible mathematical checks

Run `python3 verify.py certificate.csv` with a standard Python 3 interpreter. The verifier enumerates all 51,840 elements of the E6 Weyl group on the 27 exceptional classes and the complete 25-class conjugacy partition. It independently reconstructs 36 unordered double-sixes by (a) testing the 296,010 candidate six-line subsets for pairwise skewness and complementary incidence, and (b) acting on the standard double-six with the Weyl group. It checks the agreement of the two constructions and recomputes the table in `certificate.csv` from first principles.

The checker verifies that the double-six spectra comprise 24 distinct classes among 25 Weyl classes; the sole duplicate has double-six spectrum `1^2,2^3,4^7` and the two different line spectra `1^5,2^1,4^5` and `1^1,2^3,4^5`. The invariant Picard ranks and traces are verified by exact rational row reduction on the seven-dimensional integer Picard matrices. The result was repeated with different Python hash seeds and the stored certificate agreed byte-for-byte.

The calculations are exhaustive **within the proven 27-line geometric universe**. They do not independently verify the classical theorem that every smooth cubic surface has this configuration, or independently construct every finite-field Frobenius type; those inputs are cited published results. The output is a self-reviewed proof and finite certificate, not an independent audit.
