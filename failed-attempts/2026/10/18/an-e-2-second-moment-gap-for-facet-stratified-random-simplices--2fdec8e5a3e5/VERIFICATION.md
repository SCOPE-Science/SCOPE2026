---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Affine barycentric columns have a zero at their own facet index and are Dirichlet(1,…,1) on the remaining n-1 entries. The normalized oriented volume is the determinant. The mean determinant follows from multilinearity and the spectrum of (J-I)/(n-1). For the square, independence allows replacing the random rank-one column outer products by their means in the squarefree coefficient only. Scaling by n(n-1), the summed moment matrix has diagonal 2(T-t_i) and off-diagonal T-t_i-t_j. A rank-two update of TI gives nT^(n-2)(T²-∑t_i²): in the 2×2 reduction the diagonal is (n,0) and the off-diagonals are (T²-∑t_i²)/T and -n/T. Only T^n contributes to the required squarefree coefficient, giving n n!, even at n=2. The interior moment comes from n! det((I+J)/(n(n+1))); the exact ratio tends to e², and its square root tends to e. Squaring the signed determinant expansion gives precisely the derangement sum by the 2:1 ratio of repeated-entry to distinct-entry moments. The n=2 transposition and n=3 positive derangement terms give the stated signs; at n=4 and n=5 both parities occur and adding disjoint transpositions extends to all higher n. Permutation matrices are limit points with positive-probability relative neighborhoods of constant sign. The variance follows from the two moments, not from any claim about the unsigned first moment.

## originality

FAIL

A distinct same-date Resultary theorem explicitly states the exact shape-independent opposite-facet moment with the identical law for every nontrivial dimension. Its scope is bigger on boundary sampling. The interior e² ratio and signed derangement expansion are direct implications using known iid covariance and the entry second moments; n=2 is deterministic. This establishes material equivalent coverage, not which same-day work appeared first. The other signed statistics are elementary consequences of the same model, not a surviving distinct main result.

## value

FAIL

The second-moment constant would be useful for comparing sampling designs, but the constant is already exactly covered for the nontrivial cases. The e² limit and derangement sum respectively apply an iid-moment substitution and expand the same determinant; the signed auxiliary statistics do not provide a substantially different invariant or new comparison that merits credit as a standalone remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
