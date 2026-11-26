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

On the line, edges join consecutive sample points; a gap is skipped by both ends exactly when it is a strict interior peak (the two boundary edges cannot be missing). With distinct gaps, the sign pattern of successive differences therefore decreases then increases if and only if connected. The unique reciprocal pair sits at the minimum. The symmetric Dirichlet density gives an independent uniform rank permutation even jointly with the two exterior gaps and all sorted interior magnitudes. A connected rank permutation is uniquely determined by choosing the side of each of the n−2 nonminimum ranks, hence exactly 2^(n−2) admissible permutations and a binomial left-placement count. If a_r are the nonminimum gaps, the centered midpoint is half the exterior-gap difference plus the sum of (B_r−1/2)a_r over fair independent placement bits. The conditional covariance with the rank is one quarter the expected sum of the a_r, and the midpoint variance is one quarter the expected sum of their squares plus one quarter the exterior-difference variance. The minimum T satisfies P(T>u)=(1−(n−1)u)^n on its support by simplex translation. Subtracting its first and second moments from the full Dirichlet sums gives both stated finite formulas. In particular n=2 gives constant J=1 and midpoint variance 1/24. For the CLT the conditional characteristic function of each rescaled linear combination is a product of cosines. Normalized exponentials give sum a_r→1, n sum a_r²→2 and sqrt(n) max a_r→0 in probability; the minimum and exterior terms have vanishing normalized effect. The sum of quadratic terms in log cos yields the asserted covariance, and the sum of quartic remainders is controlled by the largest squared argument times the sum of squares. Bounded conditional characteristic functions then converge also after averaging; the determinant is 1/16. The frozen checker was read, not executed.

## originality

PASS

The qualifying component event and its exact probability are covered by earlier one-dimensional reciprocal-pair counts; novelty is not assigned to them. The exact conditional covariances and joint limit for the rank and physical midpoint of the sole pair use the spacing values as well as their ranks, and go beyond all located overlap. The frozen result appropriately makes its main distinction the joint conditional location law; a future revision should explicitly cite the earlier component-count recurrence for the connectivity probability.

## value

PASS

The midpoint of the unique reciprocal pair is a canonical statistic of a connected nearest-neighbor graph on a line. The result quantifies how an extreme global graph event changes spatial fluctuations, separating the random placement rank from the additional spacing-magnitude effect and identifying nontrivial correlation 1/sqrt(2). This is not just a rederivation of the known probability of a single component.

The dated certificate retains the supplied scientific assessment, sources and limitations.
