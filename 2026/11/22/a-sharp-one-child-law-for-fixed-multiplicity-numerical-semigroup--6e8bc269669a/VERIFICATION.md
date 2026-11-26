---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For fixed m and g≥m+1, F≥g>m; the only possible effective generators are the primitive nonzero Apéry representatives w_i=mx_i+i. They are primitive exactly when no nontrivial Kunz inequality with their residue on the right is an equality: a decomposition of w_i cannot use a positive multiple of m, and reducing each summand to its least representative must leave no added multiples of m. If there are no children, the largest representative w_r=F+m is decomposable. If there are at least two, two distinct representatives in (F,F+m] force a coordinate difference in {−1,0,1}. Each resulting equality is an affine hyperplane whose normal is independent of the all-ones genus equation: in a Kunz equality the result index differs from the two summand indices and has opposite sign, even when the summands have the same index. Two independent equations leave at most O_m(g^(m−3)) integer points by choosing the nonpivot coordinates in [1,g]. A proportional relative box about the balanced slice point gives Ω_m(g^(m−2)) strictly feasible vectors with max x_i<2 min x_i, and all positive compositions give the matching upper bound for N_m. For m≥4 use a proportional box on x₁=x₂ at the indicated positive profile; x_d (d=m−1≥3) has coefficient one in the remaining sum equation, so there is no congruence obstruction. The two tied maxima w₁,w₂ differ by one and are both primitive and effective. For m=3 the explicit even- and odd-genus pairs differ by one and two in Apéry value, also both effective for sufficiently large genus. Hence T_m, and therefore B_m, have the matching lower order for all sufficiently large g. At m=2 the unique semigroup has generators 2,2g+1 and F=2g−1, giving exactly one child when g≥2. A separate bounded tree enumeration, starting at the empty gap set with F=−1 and recursively adding each indecomposable present integer greater than F and ≤F+m+1 (m first positive nongap), gave the genus-14 profiles by degree for m=3: [0,4,1,0], m=4: [5,11,6,1,0], and m=5: [13,15,10,4,1,0]. Those are checks, not evidence for asymptotic extrapolation.

## originality

PASS

The main contribution is the sharp error order for one child and the matching multiple-child count for every fixed multiplicity, not the total count, maximal embedding dimension, or the small-m cases. Earlier indexed m=4 results are quantitatively stronger in that single multiplicity, and the primary m=3 theorem directly covers the exceptional child cases there. None of the checked statements furnishes the joint all-fixed-m law, including a matching lower bound for every sufficiently large genus.

## value

PASS

It identifies the typical branching degree in a standard semigroup tree and gives the sharp exceptional probability across all fixed multiplicities, stronger in interpretation than a qualitative leaf/internal comparison. The multiple-child lower bound separates the phenomenon from merely counting degenerate Kunz boundary points and explains why maximal embedding dimension is insufficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
