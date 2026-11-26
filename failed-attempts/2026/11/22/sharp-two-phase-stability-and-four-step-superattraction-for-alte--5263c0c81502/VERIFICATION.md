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

FAIL

The opening Finding admits s∈(0,1] and says that b=1 always has a gain with a nonzero nilpotent return Jacobian. At the included orthogonal endpoint u=e₁, v=e₂, b=1, the return Jacobian is diag(1−a,0); it is nilpotent only at a=1, when it is zero. Exact annihilation then takes just two steps in the quadratic model. The detailed theorem restricts its nonzero and four-step assertion to 0<s<1, and that qualified theorem is correct. Independently, T=(I−bvvᵀ)(I−auuᵀ) has trace 2−a−b+ab(1−s) and determinant (1−a)(1−b); the three quadratic Schur inequalities reduce to the two displayed inequalities and abs>0. If the determinant exceeds one then some modulus exceeds one, and a negative characteristic-polynomial value at −1 forces a real root below −1. For b=1 the spectrum is {0,1−as}; at a=1/s with s<1 the return is nonzero of rank one and squares to zero, while invertibility of the first phase precludes uniform three-step annihilation. At a nonlinear stationary point the chain rule gives the same return derivative and a Taylor bound gives local quadratic attraction of G², not exact nonlinear annihilation. Thus the frozen opening assertion, not the restricted derivation, is refuted.

## originality

PASS

Bounded pass only for the explicit treatment of all positive gains in this fixed two-gain model and its formulation for local nonlinear returns, on the available comparison statements. The identification with two relaxed linear projections is exact and earns no novelty credit; the Schur and Taylor tools and the nilpotent-product mechanism are also standard. The exact GAP spectral/parameter theorem was not retrieved, so independent historical priority is not established and no whole-paper noncoverage judgment is made. This bibliographic distinction does not establish a nonroutine contribution (value assessment).

## value

FAIL

The model is natural, but the surviving facts are routine deductions without a substantive new boundary phenomenon beyond the standard product calculation. The unrestricted 2×2 region is the textbook second-order Jury test applied directly to trace and determinant. With b=1, the return lands on the line v⊥; for a unit w on that line it acts by the scalar 1−a(uᵀw)²=1−as. Therefore placing this scalar at zero both forces the two-return cancellation and makes the large gain 1/s transparent; its divergence as the angle closes needs no additional result. The claimed nonlinear effect is then exactly the universal chain-rule/Taylor consequence of a square-zero derivative, with no new nonlinear coefficient, boundary behavior, or robustness quantified. Correcting the orthogonal sentence would leave only these standard deductions, so no valuable repair was supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
