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
# Reproducible checks

Run `python3 verify.py` with the standard Python 3 library. Expected terminal line:

`VERTEX_DISPERSION_EXACT_OK 33867 posets; chain checks 18; boundary check PASS`

This computes the exact ideals and maximal antichains for every increasing-label DAG presentation on at most six elements, compares complete ordered-pair squared Hamming-distance sums and individual coordinate counts, checks the exact gap and strictness classification, and checks explicit all-chain formulas for dimensions three through twenty. It also directly computes the failure of covariance positive-semidefinite ordering in the three-element chain using the vector \((1,0,-1)\).

This finite check does not establish the theorem for arbitrary dimensions. The analytic proof's load-bearing steps are the binary-pair counting identity, maximal-element deletion injection, and equality analysis. All are reconstructed in `RESULT.md`. Primary-source priority comparisons remain provisional; independent audit is not performed.
