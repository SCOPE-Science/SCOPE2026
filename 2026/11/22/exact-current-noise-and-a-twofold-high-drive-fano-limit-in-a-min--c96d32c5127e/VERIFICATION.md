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

I reconstructed the continuous-time jump graph directly on the 35 three-element subsets: particle v may jump to v+1 iff v-1 and v+1 are vacant, and each edge is reversed at unit rate. Exact reachability in this small graph is 35/35, so zero is simple for each q>0. Rotation preserves the signs as well as the rates, hence the tilted problem on functions of a rotation type closes on five seven-element orbits. If f is the orbit matrix counting forward jumps in column-source convention, the reverse count matrix is its transpose because the orbits have equal size. At z=exp(s) the tilted matrix is q*z*f+z^(-1)*f^T minus the original diagonal exit matrix; this retains the same-orbit jumps in the tilt. The derivatives of the simple eigenvalue at s=0 yield total signed-hop cumulants per time by the analytic finite-state semigroup and the spectral gap. Independently of the frozen stationary-vector perturbation calculation, I formed the symbolic determinant of z times (lambda I minus the tilted matrix) and used implicit differentiation at (lambda,z)=(0,1), with d/ds=z*d/dz. It gives 2(q^2-1)/((2q+1)R) and 2(q+1)P/((2q+1)^3 R^3) exactly, with the frozen P and R. Divide both by seven for the stated densities. Coefficients of P are positive, substitution at q=1 gives 8/105 for V, and leading powers give q^2 J -> 1/7, q^2 V -> 2/7. The ratio on q>1 tends to 2 only with the specified count and long-time-then-large-q limits. Replay: python -B branches/independent_reproductions.py 2 from /workspace with SymPy; this is exact symbolic calculation, not parameter sampling or trajectory simulation. The finding does not establish a burst law or a size-uniform limit.

## originality

PASS

Pass the evaluated second signed-current cumulant and high-drive ratio for the specified finite active ring. The local model, its faster-is-slower regime and its exact finite-size mean-current computation are prior. Generic finite-state cumulant perturbation is established methodology; the inspected related results do not evaluate this specific second cumulant or its limit.

## value

PASS

Seven sites are the first ring below half filling with three particles. This is a motivated benchmark for the same process whose mean transport is suppressed by clustering. The exact full-rate noise separates the small mean at high bias from independent Poisson-like current: only for the prescribed signed total count the limiting variance is twice the mean. This materially supplements the known mean curve, while not identifying a burst-size distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
