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

In the monomial basis the residue chains reduce both the operator and its adjoint. Phase removal gives one positive Gram chain B=D_q T D_q with tridiagonal Toeplitz T. Its one-coordinate tail is q²B, giving normalized squared eigenvalues x_j that decrease, by min–max interlacing. Principal minors split into consecutive runs; each length-l determinant satisfies the stated two-term continuant recurrence and is sum_{h=0}^l a^(2h). In trace class the order-n principal minors sum to the trace of the nth exterior power. Its norm is the product of the n largest eigenvalues and bounds below that trace; the leading coordinate wedge supplies the lower bound on the norm. The normalized leading products lie between 1 and a q,a-dependent constant for 0<a<1: each run contributes at most (1-a²)^(-1), v runs require displacement at least v(v-1)/2, and the weighted partition sum is finite since q²<1. At a=1 the product is at least n+1; the same run bound gives a subexponential upper bound, by absorbing exp(sqrt(2L) log(n+1)) into q^(2L) with the stated completing-the-square estimate. Thus the monotone x_j have limit 1 and are at least 1. Bounded log products are equivalent to summability of sqrt(x_j)-1 on their bounded range; divergence at a=1 follows from the leading product, and monotonicity of summable excess gives o(1/j). There is also entrywise Gram duality B(a)=a² B(1/a), confirming the paper's isometry argument. For finite m the lists r^{mk+b} h_k have a strictly geometric separation eventually because M≤h_k<M/r. Once the finite head is passed, all earlier terms outnumber the tail by exactly the corresponding index offset, so the natural ranks are correct. Coordinatewise comparison with the geometric baseline also survives rearrangement for the whole sequence. Jensen's formula, or integrating the unit-circle logarithm at the boundary zero, gives M. Finite reproduction gave 924 exact rational determinant/composition checks; a separate analytic check bounds the critical normalized squared product above by C_q(n+1), sharpening but not needed for the frozen proof. The 'one-tap' label denotes one residue chain (m=1); the weight still has two monomials.

## originality

PASS

Provisional for the fixed-parameter geometric coefficient together with the excess transition. The same operator was studied before; this is new explicit tail extraction, not a new operator or a claim that the spectrum had never been implicitly encoded. Related compact Jacobi results must be compared also after the off-diagonal selfadjoint block embedding, not excluded merely by observing a nonzero diagonal in the squared operator.

## value

PASS

For a canonical compact weighted composition model, eigenvalue or Schatten estimates do not give this high-rank singular-value scale. The coefficient captures the interior versus exterior factorization of the Hardy weight, while the total excess sharply detects a boundary zero even when the same first-order coefficient holds. The block interlacing and determinant-growth explanation are useful quantitative spectral information distinct from a routine compactness or Schatten check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
