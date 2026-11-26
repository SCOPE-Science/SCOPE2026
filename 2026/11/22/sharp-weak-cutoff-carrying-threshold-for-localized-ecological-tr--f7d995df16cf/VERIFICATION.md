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

The matched potential is continuous at the cutoff and has its above-threshold maximum at b=1-r, of height b^3/6-epsilon^2/2. This is positive exactly on the stated mortality interval. Only the first root A is reachable from the tail; at the double root the travel time diverges. The C1 monotone pulse follows by the two energy quadratures; their mass has the stated factor 2 sqrt(D). At fixed cutoff the mass is bounded away from zero at r=0 and diverges at r_c: U(b)-U(v)=(b-v)^2(b+2v)/6 gives a logarithmically divergent lower estimate on the core integral as A approaches b. Continuity and vanishing of r/M at both ends give attainment and at least two distinct subcritical pulses. On compact mortality intervals, rescaling the turning point and removing the simple square-root endpoint singularity give M/(2 epsilon sqrt(D)) -> 1/sqrt(r)+sqrt(r)/(1-r) uniformly. The scaled competition is bounded by r sqrt(r+2 epsilon/3)/2 from the tail and by r(1-r) from the peak-height and curvature bound, so no maximizing sequence escapes to r=0 or r=1. The limiting objective r^(3/2)(1-r)/2 has its unique maximum at 3/5, with value 3 sqrt(15)/125. Continuous ODE dependence up to the transverse cutoff crossing and tail initial-value dependence give the locally uniform matched profile; the two slopes agree at -sqrt(3/5). Independent bounded quadrature (Python 3, branches/73d7376f-3156-4edf-81bd-609344c9374f/independent_capacity_check.py) at D=1 from epsilon=0.08 to 0.01 gave sampled optima tending toward these constants (at 0.01: r about 0.589100 and epsilon kappa about 0.090795). This is corroboration, not a global certificate; frozen verify.py was inspected, not run. No finite-cutoff uniqueness or stability conclusion is needed.

## originality

PASS

The supported distinct contribution is the global weak-cutoff capacity asymptotic, including selection for every maximizing pulse and the threshold-scale matched profile. The stationary-pulse family, self-consistency parameterization and numerical finite-cutoff fold are not credited as new. No verified exact equivalent or stronger result was identified; the closest same-equation primary paper remains access-limited.

## value

PASS

The maximum permissible competition is a natural invariant of the stationary pulse family. The global sharp asymptotic determines a capacity scale and coefficient that fixed-competition or local fold information does not supply. It also distinguishes the maximizing, cutoff-scale localized shapes from the broader branch and pins down the mortality and profile for every maximizer, while leaving dynamics and stability open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
