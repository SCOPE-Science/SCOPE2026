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

Run `python deletion_checker.py` using Python 3. SciPy and NumPy are optional for the independent low-dimensional convex-hull checks; when present, the recorded check performs 11 such hull comparisons. The exact-distance and combinatorial-volume tests require only the Python standard library.

The checker constructs every surviving signed-root vertex for 256 pairs \(2\le p,q\le17\) and tests the squared-distance formula and first-order projection inequality using exact rational numbers. It evaluates the integer volume sums, their positivity, and the \(p=2\) special identities. Its optional convex-hull computation independently compares the exact normalized original and removed volumes for 11 pairs with total vertex count at most nine. In the stated environment the result was:

`BICLIQUE_SIGNED_ROOT_DELETION_PASS exact_profiles=256 independent_hulls=11 threshold=pq-2(p+q)`

The finite checks are not an exhaustive verification of every dimension. The theorem for all \(p,q\ge2\) depends on the analytic slice-and-projection proof and on the simplex mixed-volume identity. Historical priority and independent validation have not been established.
