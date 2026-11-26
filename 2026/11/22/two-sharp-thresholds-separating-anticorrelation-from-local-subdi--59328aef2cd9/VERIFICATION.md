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

Independently solved the stationary Lyapunov equation with F=[[-γ₁,0],[-γ₁,−γ₂]] (the first diagonal entry is −γ₁) and diffusion covariance diag(2D₁,2D₂). For velocity row ℓ=(γ₁,γ₂), C(t)=ℓe^(tF)Σℓᵀ has just the two stated exponential modes. The integrated covariance and its first signed moment are obtained as −ℓF⁻¹Σℓᵀ=D₂ and ℓF⁻²Σℓᵀ=(D₂/γ₂)(1−d/(1+q)), confirmed by symbolic matrix calculation. At d=1−q² the slow coefficient is zero and C remains strictly positive at finite lag; above it the bracket after removing the slow exponential decreases strictly from C(0)>0 to a negative constant. J′=C and J(∞)=D₂ imply positivity of J for all positive times and a unique overshoot when there is a sign change. The sign of ν−1 is that of H=tM′−M, with H(0)=0 and H′=2tC. Its negative-mode tail is strictly decreasing from a positive maximum. It crosses zero once exactly when H(∞)<0, which is strictly above d=1+q; equality leaves H(t)>0 at every finite positive time. Subtracting the first-moment tail at equality gives ν−1∼q e^(−γ₂t)/(1−q) after division by M∼2D₂t; otherwise the nonzero signed moment gives the reciprocal-time equivalent. Independently integrated the matrix-exponential covariance for γ₁=1, γ₂=1/2, D₂=1, D₁=1.8, obtaining roots 2.46428736 and 6.73178398, in order. Read the supplied checker and recorded finite tests, not run; the proof uses the signed moment and cannot be replaced by root sampling. Scope is stationary initialization, independent Gaussian noises and strictly ordered positive rates, not fitted finite-window exponents.

## originality

PASS

The exact stochastic solution is prior, and the anticorrelation threshold alone follows directly from the sign of the known slow covariance coefficient; the running diffusivity overshoot is its immediate integral consequence. The distinct contribution is the exact joint finite-time classification, especially the all-time strict absence of local subdiffusion in the intervening region and at the second boundary, the unique additional crossing outside it, and the cancellation law at the boundary. The exact earlier MSD contains the inputs to derive this result, but its stated transient-regime classification does not compare or control these two signs at a fixed finite rate ratio. The result is best understood as a sharp sign theorem about the known solution, not priority for the solution or phenomenology.

## value

PASS

A negative velocity-memory interval and a diffusivity overshoot can be observed while the instantaneous MSD slope never falls below one. The exact separation and endpoints show precisely when the two diagnostics disagree, even at fixed positive rate separation or equal noise amplitudes. This is a natural full-parameter distinction in a previously used model, with a testable change from inverse-time to exponential approach at the boundary, not a re-solution of the dynamics or a claim of globally anomalous diffusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
