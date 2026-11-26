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

In the principal-angle block, P-tQ has positive trace 1-t and nonpositive determinant -t(1-a), so its trace norm is the eigenvalue difference sqrt((1+t)^2-4ta), including a=0 or 1. For coinciding ranges in zero-angle blocks, the ambient dimension hypothesis supplies the requisite unused zero directions. After division by 1+t, samples measure sums of sqrt(1-qu) with q=4t/(1+t)^2 strictly increasing into (0,1). For two lists of length k, the cumulative difference H has variation at most 2k including its initial and final jumps from and to zero. If it has r sign changes, each alternation of nonzero signed integer values costs at least 2 variation, with at least 1 each to start and end. Thus r<=k-1 even if multiple jumps at one point skip zero. Integration by parts (or integrating sqrt(1-qa)-sqrt(1-q) against the atomic difference) gives orthogonality to g_j=(1-q_j u)^(-1/2), including endpoint atoms. The consecutive Wronskians are positive by the displayed Vandermonde factorization in q_j/(1-q_j u); the functions are smooth across the closed interval. Choosing r separation points and a nonzero combination of the first r+1 functions vanishing there gives exactly r simple zeros by the extended Chebyshev zero bound, so its product with H has one sign and nonzero integral unless the atomic difference is zero. The matched multiset determines the blocks and common zero multiplicity on a fixed ambient space. For m<k, a Chebyshev evaluation minor in the Jacobian is nonsingular everywhere on the strict ordered interior chamber; hence the fibers have positive dimension, and the chamber has no permutation duplicates. For m=0 noninjectivity is immediate. The Hilbert–Schmidt expansion indeed depends only on the sum of the a_i.

## originality

PASS

The supported distinct claim is optimal exact recovery from arbitrary k distinct scale samples of the trace-norm pencil. The block decomposition, fixed-distance formulas, interpolation theory and ordinary polynomial equal-weight moment inversion are not novel ingredients.

## value

PASS

Recovering the full invariant of two equal-rank subspaces from scalar trace norms is a concrete inverse problem. The theorem makes every permissible choice of scale informative at the optimal sample count, including pairs with repeated or endpoint angles; fewer samples provably leave residual freedom on the generic chamber. Hilbert–Schmidt data at any number of scales collapse to one sum, so this is an informative distinction between two natural measurement norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
