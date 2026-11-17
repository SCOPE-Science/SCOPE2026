---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For independent Gaussian left/right sketches of size ell>=r and fixed orthonormal U,V, write N=U_perp C V_perp^T. Oblique Q and R reproduce tangent terms and the difference on N decomposes into three pairwise Frobenius-orthogonal blocks AC, CB^T and ACB^T (left and right sketch errors). The standard inverse-Wishart trace gives E A^T A= a I and E B^T B=a I with a=r/(ell-r-1) when ell>r+1, so expected squared Frobenius error is (2a+a^2)||N||^2. At ell=r+1 the one-sided coefficients have finite absolute first moments but infinite quadratic moments; independence gives zero mean of the full correction and divergence of norm square for N!=0. At ell=r the square diverges without a first-moment claim. N=0 yields zero identically, and ell/r->gamma>1 gives the asserted finite constant. Independent exact-rational algebra and Gaussian simulations for (r,ell)=(1,5),(2,8) agreed with the formula, which rests on the known inverse-Wishart identity, not those simulations.

## originality

FAIL

FAIL on mathematical implication: The one-sided exact Gaussian oblique projection squared-risk multiplier a=r/(ell-r-1), its integrability threshold, and unbiasedness are already established by Tropp et al (2017), Lemma A.5, and restated in stronger residual-spectrum result (2026-10-12). The submitted two-sided oblique tangent expression separates into two independent one-sided errors and their product. Because the two fixed normal supports are orthogonal, the three mean squares multiply to a+a+a^2 without any new probabilistic lemma. The boundary and 2r scaling immediately follow the *same* known inverse-Wishart cutoff and algebra. The Carrel–Grigori oblique tangent construction itself is prior. This exact submitted joint theorem is a direct routine tensorized corollary of the cited one-sided result and prior oblique tangent operator, not an original stochastic law.

## value

FAIL

FAIL for the submitted mathematical increment: a local error risk for dynamical low-rank projection is motivated, and the size 3 at ell=2r is potentially useful as a diagnostic, but the complete formula is (1+a)^2-1 for the already published one-sided inflation a. Orthogonal block expansion plus independence makes it a short mechanical propagation of known results, with no new nonstandard bound, classification or invariant beyond that algebra. The submission does not independently resolve a mathematical gap under the stated value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
