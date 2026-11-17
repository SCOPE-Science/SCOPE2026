---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The unbiased integer stochastic rounding operator gives E[X_n]=u+a^n(X_0-u). For a>=0, {0,1} is invariant and integer states outside drift monotonically toward it almost surely. For a=-r, 0<r<=1/2, deterministic contraction plus subunit rounding error traps all states in S={-1,0,1,2}; transition inspection gives a single closed aperiodic Bernoulli class for b=(1+r)min(u,1-u)>=r and a three-state class otherwise. Solving stationary mass at -1 and mean determines all probabilities; the moment yields variance u(1-u)+2t[r-(1+r)t]/[1-r+(1+r)t]. Direct rational derivative is strictly negative and limiting inflation is (1+r)/(1-r)<=3, with unattained 3 at r=1/2,u->0. Independent exact-fraction stationary and derivative checks corroborate full transition arguments.

## originality

PASS

Best-of-knowledge new exact finite-overshoot stationary support/variance classification. Li et al. 2017 analyze small-step learning-rate limits and explicit stochastic-gradient noise, not noiseless overshoot a<0 in this parameter range. Connolly–Higham–Mary error analysis and Croci et al. stochastic rounding survey give general error behavior, not this exact Markov invariant law. A previous negative affine contraction theorem concerns deterministic floor quantization, mathematically different.

## value

PASS

Model is the canonical scalar quadratic contraction with ideal unbiased final-step lattice rounding. It exhibits a sharp phase transition from minimum-variance two-state equilibrium to three-state overshoot and a sharp factor-three stationary variance inflation; these are motivated quantitative limits on numerical noise, not an arbitrary tiny instance or known arithmetic table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
