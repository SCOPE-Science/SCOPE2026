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

An independent kernel derivation uses the mutually orthogonal ramps t_i (supported on arm i, squared norm a_i/3) and g=φ₀−Σt_i/2, equal to 1 at the atom and 1−3t/2 on the arms, with squared norm h=w+A/4. The hub kernel is g/h, and leaf i has kernel 3t_i/a_i−g/(2h). The norm of each functional is the integral of the absolute kernel, attained by its sign; continuity and full measure support ensure that taking the output maximum includes leaves of zero point mass. The hub negative triangle integrates to A/(12h), giving R_o=1+A/(6h) since the signed integral is 1. The negative mass at leaf i is w/(2h)+(A−a_i)/(6h)+a_i²/[6h(4h+a_i)] by the single crossings on each arm. Adding twice this negative mass to 1 gives R_i=2+1/(3z)−4r_i/[3(z+r_i)], r_i=a_i/A. R_i strictly decreases in r_i, and R_i−R_o is strictly positive by comparing with its zero at z=r_i=1 (it increases in z and decreases in r_i). The triangle inequality for interior evaluations, which interpolate hub and leaf, gives strict nonattainment there. The positive-denominator phase sign and the ε→0 new-arm limit follow directly and agree with all thresholds. The frozen rational checker was inspected but not executed; the analytic argument establishes all parameters.

## originality

PASS

The prior no-atom theorem is exact at z=1 and already has the same minimum-mass leaf pattern and an arm-collapse phenomenon. Compared with the strongest exact passages available, the positive hub term changes the kernel's absolute mass, produces a genuinely new two-parameter threshold, and gives a different, mass-dependent collapse limit. This does not claim novelty for spline projection, Gram inversion, or the atomless law.

## value

PASS

A concentrated hub weight is a natural perturbation of continuous least squares, not a change only in length units. The norm and all worst evaluation sites are exact for unequal masses, and the threshold tells when a junction penalty removes amplification beyond two, including regimes in which it cannot do so. The quantified vanishing-arm limit separates arbitrarily light new degrees of freedom from omitting them, without claiming convergence failure on a fixed space. These are usable distinctions absent from a uniform stability bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
