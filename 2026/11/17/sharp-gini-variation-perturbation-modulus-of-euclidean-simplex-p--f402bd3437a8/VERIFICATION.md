---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Simplex KKT gives P_r(x)_i=(x_i-tau)_+, and each nonempty support S of size k occurs on a strict open affine cell. Its Jacobian is mean-centering on S and zero outside, annihilating constants. Coarea shows its induced complete-pair Gini norm is maximized by a binary cut T. If a=|S∩T|, b=k-a, c=n-k and u=|T\S|, the output has values b/k, -a/k, 0 with exact dispersion ab(1+2c/k), and the input has (a+u)(b+c-u). Concavity of the denominator in u makes an endpoint optimal; monotonicity in the smaller active group gives a=1, b=k-1. The resulting support norm (k-1)(2n-k)/(k(n-1)) is attained by one-coordinate perturbations inside its strict cell. The forward difference -1+2n/[k(k+1)] proves the exact maximizing support inequalities and the asymptotic 2-2sqrt(2/n)+O(1/n). Fixed-input contraction is a separate 1-Lipschitz threshold map statement. Independently enumerated all 2..8 support subsets and proper binary cuts with exact fractions, recovering every claimed finite n norm.

## originality

PASS

PASS (bounded best-of-knowledge). Sparsemax is exactly Euclidean projection onto the unit simplex and its Jacobian has the same active-set mean-centering structure; Martins–Astudillo state those facts, not this pairwise Gini operator norm. The general active Jacobian and support formula are necessary prerequisites but do not imply the newly optimized Gini coefficient absent the cut counting argument. Material full texts and relevant primary sections checked; remaining historical-equivalence risks retained.

## value

PASS

Simplex projection is ubiquitous in optimization and sparse probability transformations. The contrast between fixed-input dispersion contraction and two-input expansion, the precise first dimension, the optimal active support near sqrt(2n) and the approach to factor 2 quantify a genuine and useful perturbation-stability gap in a natural seminorm. The all-dimensional classification is stronger than a routine KKT restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
