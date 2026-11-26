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

The stationary transverse Bloch coordinate is the renewal transform r/(r+γ−iω), and the longitudinal component vanishes; the drift eigenvalues have negative real part and the Bloch radius is strictly below 1. Taking the local ω derivative at fixed γ and r in the polar full-rank SLD metric gives the stated rational QFI. Independent symbolic differentiation of that expression gives the stated sextic with positive derivative prefactor. For every t>=0 its ascending coefficient signs are ++++---. Descartes' rule and opposite signs at zero and infinity prove existence, simplicity and global maximality of the unique positive root. At t=0 the sextic factors as −(u−1)(u+1)^3(2u+1)^2, giving u*=1 and γ²F=1/16. Evaluating it at b=√(1+t) gives b^5(b−1)(b+1)^2, establishing strict separation above b for nonzero detuning. The derivative ratio at (1,0) gives the small-t coefficient 19/36. For v=√t tending to infinity and fixed c>0, v^(−8)P(cv,v²) tends to 1+2c²−2c⁴, with a unique simple positive root; bracketing on both sides and uniqueness give u*/v→√((1+√3)/2). Substitution into the scaled QFI gives 2√3/9. These are fixed-γ derivatives, not derivatives along the optimized reset schedule.

## originality

PASS

The principal distinct result is the global known-γ scalar-QFI optimizer, its sextic, and its strict detuning-dependent bound and weak-detuning behavior. The stationary state and scalar information formula are already derivable from the same-day joint-sensing metric; the strong-detuning constants also occur in the earlier undamped discrete scaling. Neither is credited as a standalone new contribution. No ordering is inferred from the same-day date.

## value

PASS

This solves a natural resource-setting problem for frequency estimation when dephasing is calibrated: a global, one-dimensional root test for all detunings, an informative strict threshold, and a clear contrast with joint estimation on identical dynamics. The new scalar optimizer is useful independently of the standard QFI calculation and known undamped scaling constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
