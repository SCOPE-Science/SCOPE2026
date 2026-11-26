---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Strong Markov and spatial translation yield iid adjacent-site passages, and reflection gives independence of passage time and sign. On the central half-cell, with K=r+z and b=sqrt(K/D), the solution is f(z)(r+z cosh(bx))/K. On the exterior half-cell it is [r+z cosh(b(ℓ-x))]/K plus a multiple of sinh(b(ℓ-x)); matching eliminates that multiple and gives f=(z+r cosh a)/(r cosh a+z cosh 2a). Thus 1/f=1+z A(z) with A(z)=2sinh²(a_z)/(z+r cosh a_z), so μ=A(0) and CV²=1-2A′(0)/μ², yielding the claimed expression. For the pole step, the survival numerator in time is E[exp(kX_t);τ>t]. It is bounded by exp(|k|ℓ) times an exponentially small survival probability (a fixed reset-free interval has a uniform positive probability of Brownian exit). Its transform is analytic in a strip. The explicit f decays as exp(-c sqrt(|Im z|)) high in a narrower strip by the hyperbolic-cosine formula. At k=0, nonlattice τ excludes all other imaginary-axis roots, and f′(0)=-μ supplies simplicity. Compactness on bounded frequencies and the high-frequency bound give an isolated dominant pole for all sufficiently small complex k. After subtracting the survival term, the transformed renewal expression has the decaying factor cosh(kℓ)f(z), so contour shifting gives a locally uniform exponential remainder and justifies differentiating the logarithmic expansion. Expanding cosh(kℓ)f(Λ)=1 gives fourth rate ℓ⁴(3m₂-5μ²)/μ³. The series for 2F has vanishing linear and cubic terms and positive higher coefficients by (9/4)^n>2n+1 for n≥3 and direct n=2. The upper bound follows from the strictly positive higher coefficients of α(cosh(2α)+3)-4sinh α. The endpoint expansions give both sharp bounds and the stated small- and large-rate fourth-coefficient limits. Independent numerical evaluation with ℓ=D=1 at α=1.606115298802767 gives CV²≈0.7216066686, D_eff≈1.1692300894, fourth rate≈0.3854250203 and excess prefactor≈0.07048228031. The supplied checker was read, not run.

## originality

FAIL

The two main conclusions are both explicitly covered by a distinct Resultary record on the identical model, with a further scaled-cumulant-generating-function result. That record is catalogue-dated after the frozen one; this is duplicate statement coverage at review time, not evidence of earlier publication, dependence, or priority. In the inspected earlier same-model primary paper the transform is known, the formulas are derivable, and the strict all-rate window/sign were not found stated.

## value

PASS

As a mathematical statement the strict all-rate sign and sharp variability interval answer a natural question beyond the known mean/diffusivity. They identify the threshold CV²=2/3 for symmetric fixed-length renewal displacements and predict the sign of the leading non-Gaussian correction without a finite-rate fit. This scientific motivation does not remove the exact coverage on originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
