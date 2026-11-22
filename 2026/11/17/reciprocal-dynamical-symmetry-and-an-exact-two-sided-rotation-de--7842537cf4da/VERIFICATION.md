---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Cε(x,y)=(x,sqrt ε y) exactly conjugates the full map to reciprocal ε with kick sqrt ε b, without pretending coordinate scaling is symplectic. For b=0 the full negative-lift band has |y| between 1 and ε^−1/2 and area 2|1−ε^−1/2|; the conditional variable T=sqrt ε |y| is uniform between sqrt ε and 1. Change to U=(T²−ε)/(1−ε), density (e+1)/(2 sqrt(e²+(1−e²)U)), yields Z=4U(1−U) and the stated survival law. Reciprocal e->1/e reflects U around 1/2. Explicit survival derivative in r=|1−e|/(1+e) proves strict stochastic order on (0,1); the band is empty at ε=1, only a weak Beta(1,1/2) limit is claimed. Independent SymPy integrations verified mean, variance, reciprocal identities and flux critical a/6 coefficient.

## originality

PASS

The underlying quartic nontwist profile/collision is prior; the complete continuous normalized conditional-area rotation-depth law, strict reciprocal stochastic order and cubic flux are additional quantitatively motivated assertions.

## value

PASS

The negative-lift rotation band is a canonical finite-area region of an integrable nontwist map, and its physically meaningful conditional area-frequency law quantifies the disappearance of reverse rotation at a shearless collision. Exact stochastic ordering, nondegenerate two-sided beta weak limit, moments and cubic flux resolve a natural distributional question rather than a decorative parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
