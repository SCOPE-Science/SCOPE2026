---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The claim is χ_top(A(C^n))=n!/2^floor(n/2), n≥2, for the smooth projective standard complete-skew-form compactification. For a generic one-parameter diagonal subgroup with distinct pair weights 2^i+2^j, a fixed projective first skew form has one coordinate wedge, whose kernel is the complementary coordinate subspace. Repeating on coordinate kernels gives precisely ordered disjoint unordered label-pairs, leaving a singleton for odd n. These fixed points are isolated and correspond to n!/2^floor(n/2) possible ordered pair sequences. Since the moduli is smooth projective, Bialynicki–Birula fixed-point stratification gives χ=#fixed. The n=2 case is a point, n=3 is P², both agree. Independently reconstructed exact recurrence 2≤n≤80 and pair-weight distinctness 2≤n≤30; finite checks corroborate only the symbolic argument. Git tree object and all seven named blobs were inspected.

## originality

FAIL

The complete all-n Euler evaluation is already implied by substantially stronger earlier primary results, despite the absence of its exact string in those papers. For even dimension 2m, Brion–Joshua Lemma 2.1.1(i) describes torus-fixed points of the wonderful compactification X of PSL(2m)/PSp(2m) as W_G/W_L. Their Example 1.4.4(2) explicitly gives W_G=S_{2m} and W_L=(S_2)^m, so |X^T|=(2m)!/2^m and smooth projective Bialynicki–Birula (or torus localization for Euler characteristic) gives the same Euler number. The open nondegenerate skew-form orbit, Thaddeus blow-up and Massarenti Proposition 3.6 identify this X with the submitted complete-skew-form variety. For odd dimension 2m+1, Borisov–Libgober Proposition 3.1 gives a flag model with first flag space F^0 a line and nondegenerate 2-forms only on successive even-dimensional quotient spaces; forgetting all but F^0 realizes the odd-dimensional space as the associated even-dimensional complete-skew-form bundle over P^{2m}, so chi_odd=(2m+1)chi_even=(2m+1)!/2^m. At n=3 this is P(Lambda² C³*)=P², Euler 3; n=2 is one point. These prior implications cover the complete claim, not merely a sample or a similar title. An independently written ordered-matching proof is a useful explanation but cannot be counted as a new theorem under this protocol.

## value

FAIL

The Euler characteristic of classical complete skew forms is a natural geometric quantity, and ordered pairings provide a clear exposition. However, for even dimensions its exact formula is a one-line specialization of the pre-existing Brion–Joshua Weyl quotient fixed-point theorem, and the odd case is a routine projective-bundle Euler multiplication from Borisov–Libgober Proposition 3.1. The remaining statement adds neither an independent topological invariant unknown under the literature, a nonstandard lemma, a new structural obstruction, nor a classification not automatically implied by those stronger results. As a mathematical contribution it is a useful explanatory corollary but falls below the independent-value bar; no assertion that all Euler computations are valueless.

The dated certificate retains the supplied scientific assessment, sources and limitations.
