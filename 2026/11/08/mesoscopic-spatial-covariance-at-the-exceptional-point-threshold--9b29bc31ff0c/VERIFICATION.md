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

The drift is Hurwitz for every finite N with positive damping. Expanding the nilpotent shift in the stationary covariance convolution and integrating t^(2q+d) exp(-2κt) gives the exact binomial sum with D/κ, consistent with the Lyapunov boundary recursion and N=1. For q/N in [ε,1] and d=O(sqrt(N)), the uniform centered-binomial Stirling expansion has prefactor 1/sqrt(πq) and exponent -d²/(4q)+o(1). With d/sqrt(N)→|y-z| and κ_N=1+ζ/N, the remaining factor κ_N^(-2q-d-1) converges uniformly to exp(-2ζq/N) on that range. The finite sum ends at N-max(i,j)=N-o(N); the omitted small q contribution after N^-1/2 scaling is O(sqrt(ε)+N^-1/2) by the maximal binomial-mass bound, also when d=0 and for fixed negative ζ. This yields the improper kernel by Riemann summation; exact Gaussianity then yields the stated finite-dimensional convergence, including coincident observation sites. Integration by parts and division by 2D/sqrt(π) give the erfc correlation at ζ=0. The fixed-microscopic-distance remark is read within the stated upstream observation window, not at fixed distance from the downstream boundary.

## originality

PASS

Credit is limited to the coupled stationary large-N spatial and detuning limit, not the exact finite covariance, noise normalization, exceptional-point mechanism, or variance dichotomy. Pal–Gupta's Eq. 84 is precisely the same finite covariance after reflecting site labels and reindexing for the open one-way chain. That is stronger prior overlap than a shared integral alone, but the inspected passage does not quantify the mesoscopic separation and damping window or state the resulting continuum covariance. The older infinite-chain result changes the order of limits and does not include this cutoff kernel.

## value

PASS

The spectrum alone stays uniformly stable in this limit and the familiar critical diagonal growth does not predict which distances decorrelate. The kernel identifies a nontrivial spatial correlation at order sqrt(N), while resolving the effect of damping changes of order 1/N and the terminal-chain cutoff in one expression. It is a useful benchmark for feedforward nonnormal covariance amplification beyond the exact finite sum or a scalar variance law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
