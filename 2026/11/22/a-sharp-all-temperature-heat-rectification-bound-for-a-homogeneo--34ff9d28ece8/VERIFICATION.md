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

Independently reduced the spin chain to the bond variables X=σ₁σ₂ and Y=σ₂σ₃. An outer flip negates one bond, and a central flip negates both with rate (1−v(X+Y)/2)/2. Reflection and stationarity give 2x=t+v(1+z)/2 and z=tx for x=E[X]=E[Y], z=E[XY]. The center supplies J[2x−v(1+z)]; solving and substituting v=2u/(1+u²) gives 2J(t−u)(1−tu)/(2(1+u²)−tu). Hence the sum of the outer currents is its negative, and both assignments give the stated ratio of positive hot-bath currents, not a per-site ratio. The b-derivative has strictly positive numerator for 0<a<b<1 by a³+ab²≤2b³<4b. As a separate maximum certificate, with M=1+4/√15 and a*=4−√15, M(2+2a²−a)−(4−a)=2M(a−a*)². The ratio extends continuously to the closed triangle since its denominator stays positive. Strict improvement up to b=1 for each a<1 and uniqueness there force every maximizing sequence to converge to (a*,1), and the converse follows by continuity. On two spins the bond mean is (t+u)/2, so the current is J(u−t)/2, invariant in magnitude on interchange. One spin cannot transport interbath heat in this family.

## originality

PASS

Nearest records share the two-temperature kinetic Ising mechanism or the three-site count, but the consulted exact laws do not specialize to the open path and do not yield the sharp ratio. The novelty judgment is limited to this geometry and ratio, not the heat-bath formalism or stationarity method.

## value

PASS

This is an exact minimal-system mechanism rather than a numeric rectification example. It locates asymmetry in the topology and reservoir placement despite equal bond strengths and update clocks, quantifies the direction and sharp extent for every temperature pair, and gives a nontrivial interior hot temperature at the cold-limit maximum. The dimer calculation gives a meaningful minimality comparison within the stated family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
