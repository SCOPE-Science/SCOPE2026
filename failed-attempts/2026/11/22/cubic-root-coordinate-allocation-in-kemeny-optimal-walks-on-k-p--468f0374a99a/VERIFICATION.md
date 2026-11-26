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

On the zero-sum subspace the irreducible Laplacian is positive definite; in its eigenbasis the second variation of the inverse trace is a sum of 2|H_ij|^2/(lambda_i^2 lambda_j), positive for a nonzero symmetric zero-sum perturbation. Coordinate-permutation averaging preserves connectedness and strict convexity forces any optimum to be invariant. The three rates alpha, beta and alpha+beta have multiplicities p-1, q-1 and (p-1)(q-1), respectively; both rates must be positive. The budget saturates by positive common scaling. Differentiating the saturated objective gives the positive prefactor in RESULT.md times q t^4+2q t^3-2pt-p. The quotient t^3(t+2)/(2t+1) increases from zero to infinity, so the critical point is the global minimum. For fixed p the equation gives t=(p/(2q))^(1/3)(1+O(q^(-1/3))). Substitution into the exact value expression leaves pq plus (p-1)/t+(p-1)q t^2/p+O(1), giving the stated coefficient. For p=2, averaging cannot increase ||P-J||, and the averaged candidate with SLEM r must have alpha,beta>=1-r and alpha+beta<=1+r. This forces r>=1/3; the stated feasible design attains it. Multiplicity substitution gives (9q-3)/4 and the ratio tends to 9/8. This is a statement about the specified optimal mixing design. The checker was inspected, not executed; the argument is analytic.

## originality

FAIL

The main optimizer, including unrestricted edges, uniqueness, exact weights and leading allocation asymptotic, is the spectral-order-one case of the separate published rectangular rook-network result once its total budget is rescaled. The statement-level coverage is established; the two records have the same publication date and priority within that date is not established or alleged. The printed Kemeny value asymptotic and comparison are not found verbatim in that result, but are direct evaluations of the covered solution and the elementary three-eigenvalue mixing benchmark, not an independent surviving allocation theorem.

## value

FAIL

The mathematical question is natural, and contrasting first-passage and mixing is useful. But the structural optimizer and anisotropic scaling are contained in the stronger rook-network result. The additional coefficient is immediate expansion of its exact optimizer and spectrum, and the 9/8 comparison is obtained by substituting one elementary mixing design into that spectrum and comparing leading terms. As additions to the covered theorem these are useful explanatory corollaries, not a sufficiently distinct valuable repaired finding. No repair submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
