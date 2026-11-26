---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Uniform convergence of partial scores on the compact ray space ensures attainment. The root decomposition is D=(1−B)+min(D₁,D₂)/2 in law and, for x<1, gives f(y)=p(2y−y²). No use of the recursion at x=1 is needed: the first iterated argument is x/2, while the initial value at 1 includes the failed-root/zero-child-deficit event. The atom is the all-success survival probability r, with the root factor included. For any x>0 a finite cylinder with all early successes and a compulsory later failure gives positive mass in (0,x], so the seeds above r are strictly positive after centering. Then the noncritical centered iteration is z↦a z−p z², with a=2p or 2(1−p); the normalized orbit product converges to a finite positive limit since z_n≤a^n z_0 and all factors are bounded below by 1/2. At criticality, reciprocal differences tend to 1/2 and give nF(2^−n x)→2. Dyadic monotonicity proves the all-scale comparison and converts the critical logarithm with the factor log 2. It does not prove an all-scale ratio limit in either noncritical regime.

## originality

FAIL

The exact discounted-ray model and CDF recursion are already specializations of inspected max-type recursive-distribution results. The asserted endpoint laws, including the positive scale-specific limits, follow mechanically from the same quadratic map: the atom and critical constant are ordinary binary Galton–Watson survival facts, and the noncritical arbitrary-seed limits are the elementary attracting-fixed-point normalization of that explicit map. The statement does not evaluate the amplitudes, show phase oscillation or regularity, or otherwise go beyond the normalization. Failure rests on this implication, not on an unavailable paper or a catalogue miss.

## value

FAIL

The critical transition is a useful interpretation of the model, but as stated it is a routine survival/iteration deduction from the known exact quadratic CDF recursion. No independent information about the actual scale amplitudes or the distinction between a constant and a genuine phase dependence is proved. The result is suitable as an example of the established framework rather than as a new exact endpoint finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
