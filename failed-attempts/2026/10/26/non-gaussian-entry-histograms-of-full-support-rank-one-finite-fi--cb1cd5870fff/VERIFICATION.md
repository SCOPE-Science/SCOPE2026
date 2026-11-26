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

Every full-support matrix has exactly d outer-product representations by nonzero factors; the two factors can therefore be chosen independently with uniform coordinates. A shared row or column factor can be conditioned on without changing the joint uniform law of the two distinct cells. This proves the covariance, including shared-index cases. The count vectors are independent multinomials, with N_a the convolution of the two count vectors; this gives the finite probability mass and cancels both first-order terms exactly. The independent centered multinomial CLTs and continuous mapping give the bilinear Gaussian limit even when the two dimensions diverge at unrelated speeds. For a real contrast, conditioning on one Gaussian yields the stated determinant on the centered subspace. In the complexified character basis the contrast matrix sends each nontrivial character to its inverse times the Fourier coefficient; the two members of each conjugate pair thus give two real singular values. This gives all scales, the positive fourth cumulant, the half-product normal at q=3, the Laplace law of rate 3 at q=4, and the zero law at q=2. The all-rank-one support probability follows by comparing the two orbit counts. The written proof rather than the finite checker is decisive.

## originality

FAIL

The unconditional scalar Gaussian limit is not the same theorem and cannot be conditioned to obtain this law. But the decisive prior comparison is with the exact character identity in the proof of Sanna's Lemma 5.4, before taking any limit. Its rank-one restriction to nonzero factors is already the complete character-by-character representation of the centered histogram. The stated joint limit then follows directly from the ordinary finite-dimensional CLT for those character sums and their elementary Gaussian-product characteristic functions. Thus the central mathematical result is mechanically implied by the prior identity, even though no earlier verbatim statement of the conditional characteristic function was located. The finite moments and multinomial mass formula are direct count consequences of the same uniform-factor model, rather than an independent originality-bearing remainder.

## value

FAIL

The conditioned example is a useful illustration that pairwise independence does not force a histogram CLT, and the Laplace case is explicit. But the narrow proposed exact invariant is obtained mechanically from the known factor-character identity: conditioning replaces the masks by constants and leaves orthogonal finite-alphabet CLTs and standard product-Gaussian integration. The ancillary exact formulas are immediate multinomial counting. No further structural assertion beyond this direct specialization was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
