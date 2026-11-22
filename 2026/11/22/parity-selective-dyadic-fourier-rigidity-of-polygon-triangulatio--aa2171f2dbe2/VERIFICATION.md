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

# Verification and reproducibility

Use Python 3.9 or later to run `python3 check.py`. The self-contained script uses only the Python standard library and exact integer arithmetic. One calculation enumerates geometric triangulations and ear masks before an integer Walsh–Hadamard transform; the independent calculation uses the prescribed-ear inclusion–exclusion formula and subset zeta transform. It asserts agreement for every frequency in each order from five to eleven (4,064 character comparisons), checks the global valuations and parity residues at every character through eighteen vertices, and prints a `PASS` record on success.

The infinite proof is the prescribed-ear Catalan bijection, expansion of signed ear indicators, and the digit-sum valuation argument. No finite certificate alone can validate the universal quantifier. Scientific limitations include lack of a complete even-polygon nullity classification and potential unindexed prior identities. Independent audit has not yet been performed.
