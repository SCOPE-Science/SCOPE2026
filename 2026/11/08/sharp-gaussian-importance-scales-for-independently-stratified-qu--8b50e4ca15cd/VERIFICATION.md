---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The density ratio under x=sqrt(s)z gives the stated unbiased f_s and elementary Gaussian integration shows f_s is square integrable exactly for s>1/2. If s<=1/2 an endpoint stratum has infinite second moment, and the estimator is a nonnegative sum with finite mean. For square-integrable f, independence gives Var(Q)=||f-P_N f||_2^2/N. The sharp smooth limit is obtained from the variance h^2/12 of the uniform offset on cells of width h=1/N and a uniform Taylor remainder. Cellwise Poincare and density extend the norm limit to H^1; restricting the same smooth calculation to full interior cells gives a liminf bound for every compact interval and hence divergence when the derivative's integral is infinite. Substitution u=Phi(z) in the derivative norm gives the weight exp(-(s-3/2)z^2) times [2z-(s-1)z^3]^2. No polynomial cancellation changes the boundary at s=3/2. The Gaussian second, fourth and sixth integrals yield the displayed C(s) after the factor 1/12. The log derivative has the stated cubic, whose shifted coefficients have one sign change, with a negative constant and positive leading coefficient. Both finite-range endpoint limits are infinite, so its unique root is the unique best fixed scale. Independent decimal evaluation gives s*=3.771072680736151, C(s*)=6.561382327199923, C(3)=7.2551974569368705 and a 9.563008% drop. The unstratified second moment is 3s^3/(2s-1)^(5/2), with derivative sign s-3, giving its unique optimum s=3.

## originality

PASS

Independent probability strata, the 1/12 derivative-energy principle and general importance-sampling strategy are not credited as new. The supported distinct contribution is the exact two-threshold classification and constrained Gaussian optimum for the standard quadratic benchmark, separated rigorously from its ordinary variance optimum. Published Gaussian RQMC results and the same-day Gaussian stratified tail problem overlap on the importance-proposal mechanism but do not give this particular Sobolev boundary and optimizer. The closest one-dimensional quantile-stratified importance paper was identified, but its full-text passages were unavailable. No retrieved result was shown to give the claimed benchmark as its own specialization without the singular endpoint analysis and scale optimization.

## value

PASS

Estimating the already-known normal second moment is a deliberate benchmark, not practical numerical integration. It isolates a material method-choice distinction: finite ordinary importance variance starts at s>1/2, the nominal N^-3 stratification coefficient needs s>3/2, and optimizing ordinary variance gives the wrong fixed Gaussian proposal even within the regular regime. The exact mismatch, variance gain and endpoint classification are useful for checking general claims about what stratification changes; they are not significance inferred from the small numerical difference alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
