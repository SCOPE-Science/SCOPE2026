---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For every assumed finite-time interior collision with positive C^1 density, reconstruct rho ddot(rho)->-2G sigma(x*) by the scaled Newtonian kernel; ddot(rho)<0 gives eventual monotone infall and dot(rho)^2~4G sigma(x*)log(1/rho). The split axial integral cancels the odd constant-density part and gives ddot(x)=2G sigma'(x*)log(1/rho)+o(log), integrable against dt~d(rho)/sqrt(log). Thus dot(x)->v*, x-x*=O(rho/sqrt(log)); uniform finite-part potential expansion U=-2G sigma(x*)log(1/rho)-G B*+o(1) follows from C^1. Energy conservation yields dot(rho)^2=A log(1/rho)+(2H+2GB*-v*^2)+o(1); integration of 1/sqrt(A log+C) yields coefficient -(1+C/A)/2 for the remaining-time clock. Twice integrating axial acceleration gives stated 2G sigma' and G sigma' impulse/position limits. The theorem does not establish a collision basin, endpoint law or uniform-in-density estimates. Independent linear-density finite-part calculation at rho=.02,.001,1e-5 had errors 2.87593e-4,7.19143e-7,7.19e-11; these are corroboration, not proof.

## originality

PASS

Best-of-knowledge novel higher-order interior-collision observables, conditional on occurrence of collision; earlier same-model work supplies the planar reduction, leading transverse force and final cone but not the finite-part transverse energy, two-term logarithmic flight clock, or variable-density gradient-driven axial impulse. Search not a certification of priority.

## value

PASS

A nontrivial refinement of a singular mechanical impact problem: a finite renormalized transverse energy and quantitative time-to-collision correction depend on global density and energy, whereas tangential impulses detect only the local density gradient. These are distinct asymptotic observables relevant to sensitivity and collision timing; neither a routine substitution nor simply restating the known leading log singularity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
