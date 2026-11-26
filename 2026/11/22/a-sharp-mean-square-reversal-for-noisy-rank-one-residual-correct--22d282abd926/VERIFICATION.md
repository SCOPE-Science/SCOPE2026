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

Independence of the fresh read from the current error gives the exact noncentered second-moment map C ↦ E₀CE₀ᵀ+δ tr(C)I: the mixed terms vanish and each row-noise quadratic mean is δ tr(C), with off-diagonal row terms zero. In the orthonormal u,v basis the mean maps v to 2Ku and kills u. The diagonal transfer is [[δ,4K²+δ],[δ,δ]], with eigenvalues δ±√(δ²+4K²δ); no off-diagonal moment feeds back. Its strictly positive left Perron vector detects every nonzero deterministic initial error, including the nondecay at the equality threshold. The positive eigenvalue is below one exactly for δ<1/(4K²+2). Shah et al.'s residual identity at A=I gives Q E_j; hence after its first application the error lies on n. Direct contraction of the entry covariance gives Var(nᵀG_j n)=δ and Var(nᵀG_j e₀)=δ‖e₀‖². Thus the first moment factor is strictly positive for e₀≠0 and each subsequent second-moment multiplier is K²cos²(2θ)+δ, giving both extremal angles and the equality case. For K=2 and δ=1/100 the two factors are 0.410124980474851… and 4.01; the raw threshold is 1/18. The one-step norm ordering does not order products. Conditional on a nonzero unit probe the learned vector is Gaussian with covariance εI, so any arc within γ≥1+c has positive probability. Integrating the conditional lower bound δ‖e₀‖²(1+c)^(j−1) on that fixed arc proves unconditional divergence. At ε=0 a probe with nonzero image gives the stable complement v. This discontinuity concerns infinite-horizon classification, not finite-time behavior, typical devices, almost-sure failure or FGMRES. Inspected both support files but did not execute them; verify.py lines 66–67 make a tautological numerical comparison, which is not credited as covariance evidence. The proof and the separate symbolic covariance check do not depend on it.

## originality

PASS

A bounded pass for the quantitative stationary Richardson counterexample and learned-space discontinuity together. The pointwise correction, fresh reads, probe setup and general multiplicative-noise moment lift are not novel. The closest inspected source supplies the one-step operation and no equivalent stability analysis of this model; a moment-lift method by itself does not give the simultaneous projection reversal or the adverse fixed-setup expectation.

## value

PASS

The example gives a sharp warning about a practical inference in analog–digital solvers: every realized single-application improvement can be consistent with arbitrarily worse mean-square iteration factors. Exact best/worst orientation factors and the discontinuity for a fixed learned space distinguish solver noise from setup noise rather than just give a deterministic instability. The strongly nonnormal case and rare-event qualification appropriately limit the interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
