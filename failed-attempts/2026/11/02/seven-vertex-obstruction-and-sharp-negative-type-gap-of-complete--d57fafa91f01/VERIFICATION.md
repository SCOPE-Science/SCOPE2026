---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With q=2^p, the distance-power quadratic form on the zero-sum space is the orthogonal sum of clique contrasts (eigenvalue −1; absent for m=1), independent-set contrasts (−q), and the line (1/m on the clique, −1/n on the independent set). On the line the eigenvalue is [q(1−1/n)−1−1/m]/[1/m+1/n]; from q≥1 it is at least −1, so it gives the claimed exact gap with a witness even above the critical exponent. This also verifies the strictness and simple endpoint nullity, including the equidistant p=0 case and the star boundary. At p=1 the inequality reduces to n(m−1)≤2m. Checking n≤6−m for 1≤m≤4 proves the order-six statement, and the five admissible pairs at order seven leave exactly the stated three failures. Schoenberg centering gives the ranks from the same three modes. The proof's phrase ‘nonnegative type’ in the p=1 paragraph means 1-negative type here. The supplied rational checker is corroborative, not the proof for real exponents.

## originality

FAIL

Lou, Obata and Huang give the exact complete-split quadratic embedding constant (the negative of this normalized gap at p=1) in Example 3.4 of their 2022 paper. Since the only nonzero distances are 1 and 2, a positive affine transform of the compressed ordinary distance matrix gives every distance-power matrix. The published QEC therefore immediately fixes the entire all-p gap and the critical exponent, as well as the seven-vertex list. The regular-join block modes supply endpoint simplicity and rank. A distinct same-day indexed clique-core-book result also explicitly covers the critical exponent and ranks for m≥2; no within-day priority is assumed or needed for the failure.

## value

FAIL

An explicit phase boundary for a natural graph family is useful, but the purported gain here comes from an affine transformation of a published exact constant, a five-pair filter of its sign, and a rank calculation on the same join modes. The seven-vertex list adds no independent cutoff beyond the parameter inequality. There is no nonroutine surviving frozen component to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
