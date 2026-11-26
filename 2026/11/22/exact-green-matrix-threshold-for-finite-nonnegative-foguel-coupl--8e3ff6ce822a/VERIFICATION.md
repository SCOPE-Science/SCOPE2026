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

Coordinatewise absolute values bound every numerical-radius direction by the Rayleigh quotient of H_t=Re F_{tA}; nonnegative real vectors give the converse. The essential spectrum is [−1,1]. An independent threshold check uses the identity ⟨(1−J)x,x⟩=(|x₀|²+Σ|x_{j+1}−x_j|²)/2, J=(S+S*)/2. For a prescribed prefix x₀,…,x_{N−1}, the infimum over square-summable tails is the energy of the existing prefix increments (extend the last value by a long linear taper to zero). Its matrix is G₀⁻¹ because G₀ is twice the product of the unit lower triangular cumulative-sum matrix with its transpose. Applying this infimum independently to the two components reduces 1−H_t≥0 to the finite block form with diagonals G₀⁻¹ and off-diagonal −tA/2; congruence gives the norm bound including equality. For λ=cosh s>1, the quoted Green kernel solves the half-line recurrence with boundary at −1 and a unit delta at j. If V=(λ−J)^(−1/2)P_N*, then V*V=G_s and the polar factors identify the compressed singular-value norm via VAV*. Hence λ−H_t is strictly positive exactly when the stated norm multiplied by t/2 is below one, and at equality its kernel is nonzero by finite-rank norm attainment. Strict decrease follows from strict reverse Loewner order of G_s and the variational quotient with G_s⁻¹ in both denominators (the finite maximum is achieved and nonzero). In particular positivity holds ABOVE the top spectrum point, correcting the wording about the resolvent in line 68. The supercritical top eigenvector can be taken nonnegative by replacing it with coordinatewise moduli in the maximizing Rayleigh quotient. At w=1 an attaining vector would likewise give a nonnegative eigenvector at one; in each component the affine tail must vanish by square summability, and the eigen-equation at each zero forces both available chain neighbors to vanish by nonnegativity, including within the coupled support. For E_ij the singular norm is the geometric mean of the two Green diagonals; G_s(ii)=2h(1−hs+O(s²)), h=i+1, gives t/t_c−1=(i+j+2)s/2+O(s²). In the two-way case the endpoint matrix has diagonals 1−b² and (1−a²)/2 and off-diagonal −(1+ab)/2; its determinant is the displayed quartic divided by four, giving both stated special thresholds.

## originality

PASS

Credit the antecedent positive-direction comparison, single-site diagonal examples and Schur-complement methodology. The supported distinct claim is the exact criterion and secular root for every finite entrywise nonnegative A, including nonsymmetric A, not those techniques or previously known diagonal cases.

## value

PASS

Determining when a nonzero finite perturbation actually raises the lower numerical radius is a natural extremality problem. The theorem reduces it to one explicit finite singular value even for directed couplings, and gives the whole supercritical curve, separating spectral threshold from vector attainment. The nonsymmetric criterion is a usable classification, not merely a different parameter for a known diagonal example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
