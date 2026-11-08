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

# Reproducible computations and their limits

The accompanying `check_boolean_chains.py` is an independent straightforward enumeration and exact version-space recursion, not a symbolic formalization of the proof. Running `python3 check_boolean_chains.py` produces the marker `BOOLEAN_CHAIN_SHATTERING_PASS face_n=1..5 ldim_n=1..5 eulerian_n=1..9` when all assertions succeed.

The checker independently lists all \(n!\) permutations, forms the complete query-domain incidence matrix, enumerates **every** support of nonempty proper queries for \(1\le n\le5\), and checks all \(2^{|S|}\) possible traces. It compares shattering status with pairwise inclusion-comparability, and compares the enumerated face vector to the ordered-partition formula. A separate memoized mistake-tree recurrence tests the exact Littlestone dimension for the same finite values. Stirling-to-Eulerian \(h\)-vectors are checked for \(1\le n\le9\).

In particular, the exact face-vector data for \(n=1,2,3,4,5\) are respectively `[1]`, `[1,2]`, `[1,6,6]`, `[1,14,36,24]`, and `[1,30,150,240,120]`. These finite tests do not imply the all-integer theorem, which relies on the explicit extension and inductive online-rank proof in `RESULT.md`. An independent audit has not been performed.
