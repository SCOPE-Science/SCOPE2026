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

In Smith coordinates the right factor has form D_{k-a}H after the coordinate change, because Ann(pi^a)=pi^{k-a}R including levels 0 and k. The middle product Y=D_a S D_{k-a} is supported only on a_i<a_j. At any h its entries are covered by the rows a_i<h and columns a_j>h. Splitting into those two blocks factors YH through a free module of rank n-n_h, proving the upper bound without confusing image generators with reduction rank or minors. For an independent sharpness argument, sort the levels and write m=max n_h. Pair row i with column i+m for 1<=i<=n-m; a_{i+m}>a_i since no equal-level block has m+1 entries. Put ones at any t of these pairs in S and take H=I. The resulting t separated entries are nonzero powers of pi, and their image is a direct sum of t nonzero cyclic modules, each contributing one residue-field generator by Nakayama. This realizes every t including zero for the original A by reversing the coordinate changes. Balanced multiplicities give the global optimum n-ceil(n/(k+1)), also for n=1 and fields, and yield the k>=n-1 criterion at n>=2.

## originality

PASS

The field boundary is covered, including the fixed-rank bound by ordinary subspace arguments. The checked statements do not cover the arbitrary-length, fixed-Smith-level generator capacity. The radical filtration changes the support to strict inequalities over k+1 levels; the optimized bound detects capacity above half rank, already at n=3, k=2, where reduction to the residue field loses the witness.

## value

PASS

The zero-product sandwich is an established object and the generator count is its natural image-size invariant over a local ring. The exact formula sees the full Smith profile, explains the field/nonfield change, and detects precisely when an image can have n-1 generators. The witness and bound make the result useful without assuming a particular residue field or equal characteristic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
