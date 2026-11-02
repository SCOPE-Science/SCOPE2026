---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Reconstructed the exact polynomial vector field on R³, positive a,k,g,d, and universal quantification over compactly supported invariant Borel probability measures. Compactness legitimizes generator testing with H(X_i) for every continuous φ=H′: differentiating ∫H(X_i∘Φ_t)dμ at t=0 yields ∫φ(X_i)F_i dμ=0. Hence E[F_i|X_i]=0 with no density, ergodicity or support-connectivity assumption. Substituting F_i gives the three regressions and Rx=-dot x/a, Ry=-dot y/k, Rz=dot z/g. Conditional L² orthogonality proves all three variance and covariance formulas, including zero residual means. For equality E[dot x²]=0, continuity gives F_x=0 on support; invariance makes x and y=-x constant along each complete support trajectory, so x(1-kz)=0. At x=0 the trajectory (0,0,z+dt) is unbounded and cannot lie in compact support since d>0. Therefore z=1/k and x²=d/g; conversely every mixture of the two equilibria has zero defect. If Var x=0, the same constant-x argument forces equilibrium support, hence Var x>0 and Var y>Var x away from equilibrium; exact negative correlation follows. Exact independent sympy verification checked pointwise identities, equilibrium drift restrictions, same-object prior balance implication and reconstructed 8-file Git tree SHA. Finite algebra is not a proof of generic conditional expectations; analytic testing supplies that step.

## originality

FAIL

Prior results mathematically COVER the theorem at implication level. Published weak Liouville/continuity identities make every compact invariant smooth-flow measure satisfy E[F_i|X_i]=0 upon testing with one-coordinate antiderivatives; inserting Burke–Shaw F reproduces all three asserted regressions, and standard conditional L² orthogonality reproduces every covariance/speed-variance identity. Moreover an earlier published exact Burke–Shaw forcing-balance theorem gives E[x²]=d/g, E[xy]=-d/g and E[z]-1/k=(g/(kd))E[(x+y)²] with equality iff equilibrium mixtures. With E[y]=-E[x], these already imply the first variance defect, negative covariance, non-equilibrium strict gap, and exact anticorrelation formula. The claim is therefore not original even though the full three-regression list was not written verbatim in the prior same-object paper.

## value

PASS

The exact three-coordinate stationary covariance/regression network is a well-motivated statistical invariant of a canonical forced chaotic flow: it permits coordinatewise calibration and direct comparisons of signal variance with mean-square dynamical speed without estimating invariant density. Its sharp strict anticorrelation law and characterization of the equilibrium-mixture boundary distinguish recurrent activity from stationary fixed-point mixing, and the special chaotic parameter values make the identities potentially useful as diagnostics. This is mathematical utility in the natural object/invariant sense, although the calculations are short and the full claims are already implied by the earlier general weak-stationarity and Burke–Shaw balance results. Value alone cannot rescue the originality failure; no claim of a new global theorem or numerical discovery is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
