---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A binary rotation class is represented once by starting at its unique 0^n arc; local bijections determine and are determined by the cyclic successor permutation. Independently enumerated successive n-bit windows by depth-first traversal with no repeated windows, closing at 0^n, without using selector-table enumeration. The counts at n=2,3,4,5 were 1,2,16,2048; the only negative pairs through n=4 and all exact covariances agree with the record. At n=5 the chosen pair has marginals 1/2,5/8, joint 11/32 and covariance 1/32. For the infinite family, each prescribed crossed selector enforces the occurrence of a unique 0v1 path; the two paths are disjoint for m=n−1≥4. Shortcutting preserves Euler circuits with the prescribed bonds, taking the new arcs as labeled. The affected intermediate outdegrees become one, so all BEST factorials remain one, with the unaffected 0^n start arc fixing rotation. The balanced Laplacian update for a→b→c is (e_a−e_b)(e_b−e_c)^T. The product P^m is uniform averaging, so the finite inverse on the zero-sum subspace and the determinant lemma give the stated probability matrix. Checked the all-order suffix/prefix table algebraically: for overlap length k=m−t, suffix integers of b1=2 are 0 at k=1 and 2 otherwise; of c1=5 are 1 for k≤2 and 5 otherwise; of b2=2^(m−1)+1 are 1 for k<m and b2 otherwise; of c2=3 are 1 at k=1 and 3 otherwise. The prefixes of a1=1 are 0 except at k=m, of b1 are 0 through m−2, then 1,2, of a2=2^(m−2) are 0 at k=1 and 2^(k−2) otherwise, and of b2 are 2^(k−1) except at k=m. Comparing these lists gives exactly the four signed overlap rows in the frozen proof, including m=4. Thus the determinant has off-diagonal entries 2^(1−m) and −1/4, giving covariance 2^(−m−1) with the displayed marginals and joint probability. This uniform calculation does not rely on extrapolation from the finite census.

## originality

PASS

The supported distinct content is the evaluated sign transition in binary order, with its small-order exclusion and uniform explicit witness. General Eulerian contraction/joint-factor machinery and the one-factor marginal framework are not novel. No inspected available statement supplies the same transition or a theorem from which the evaluated sign and first order are immediate.

## value

PASS

A uniform de Bruijn cycle couples binary local choices through the single-orbit condition. The exact first positive covariance disproves a natural nonpositive-pair pattern suggested by all smaller orders. The fixed kind of witness persists at every larger order, and the opposite signs in the cross terms explain the mechanism. That is more informative than the general determinant, a single computed order, or a numerical coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
