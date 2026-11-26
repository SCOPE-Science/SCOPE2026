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

For v>b each orientation velocity has fixed sign and magnitude at least ε. Over each finite trajectory segment the occupation time of a spatial null set is zero, so any invariant probability has absolutely continuous spatial components. Its integrable total flux is constant and therefore zero. The common orientation flux solves the scalar linear stationary equation with slope L on force +b segments and −R on force −b segments; continuity of flux through the cusps leaves one normalization and proves uniqueness. The normalized solution satisfies the stationary transport equations; both tails are integrable exactly for L,R>0, equivalent to the stated strict bias inequality. With A=1/L+1/R the right and left masses are proportional to Ae^(aL)−1/L and Ae^(aR)−1/R. In the critical window their ratio is logistic up to exponentially small end corrections and a(L−R)=θ(1+ε/(2b+ε)); Taylor expansion gives the stated first correction uniformly on compact θ-sets. For α±→r the rescaled exponents εL,εR both tend to r; translated well densities converge in L¹ by exponential domination while the inner truncations recede, giving total variation and independence. If dimensionless bias diverges while α±→r, both tail exponents still grow and the sign of a(L−R) gives the claimed polarized limit. On each regular segment f=−b·sgn(Yε), so zero flux makes the orientation mismatching Yε have conditional probability ε/(2v) exactly. No claim at v=b is needed. VERIFICATION.md and check.py were inspected, not executed.

## originality

PASS

Pass for the simultaneous zero-thermal-noise, weak-bias and near-speed-threshold asymptotic: the sharp occupation window, first correction, and joint rescaled location law. The generic zero-current formula and its exact finite-parameter specialization, including the confinement check and flux-ratio identity underlying the orientation mismatch, are not independent novelty. The closest inspected papers do not analyze this singular window or give a limiting theorem that specializes to it.

## value

PASS

The vanishing opposing speed makes the order of the symmetry and active-threshold limits consequential. The result identifies the scale of directional bias that still leaves both wells populated, gives each well's asymptotic weight plus its first correction, and resolves the width and shape of the peaks in the same limit. This sharp classification is useful beyond just recomputing a stationary density, without making claims about kinetics or thermal smoothing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
