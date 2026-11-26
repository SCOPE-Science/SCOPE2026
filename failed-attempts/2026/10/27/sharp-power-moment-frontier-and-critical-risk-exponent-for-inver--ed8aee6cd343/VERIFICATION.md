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

OPT equals the closest-pair distance δ: some two agents share a facility, so their distances sum to at least δ, and placing at all reports except one endpoint of a closest pair attains δ. Omission costs d_i. With u_i=δ/d_i the moment is Σu_i^(2−p)/Σu_i², and at least two u_i equal one. For 0<p<2 put v_i=u_i²; x↦x^(1−p/2) is strictly concave. For fixed total of the n−2 unfixed v_i, the numerator is thus maximized by making them equal. The resulting one-variable ratio [2+(n−2)z^(2−p)]/[2+(n−2)z²] has derivative with sign given by 2(2−p)−4z^p−(n−2)pz²; its unique zero gives the displayed root, value and equality condition. The gaps 1,1/z,…,1/z realize equality. For p=2 the numerator is n and the denominator strictly exceeds two; for p>2 it is unbounded as z→0, using the same family, but finite on each profile. Replay: the scalar derivative and gaps above or RESULT.md lines 26–53. The supplied verify.py was inspected, not executed. These are all-metric supremum statements for distinct locations, not risk-sensitive incentive results.

## originality

FAIL

A distinct indexed reciprocal-power mean-welfare theorem gives the entire frontier, via an exact profile transformation and q=2/p. The comparison is about coverage, not date-based priority. The p=1 case is also stated in the original inverse-square mechanism paper.

## value

FAIL

Worst-case cost risk is a natural question, but on this exact scope the claimed new frontier gives the same invariant as the indexed full power-law mean theorem, under an onto power substitution. The frozen claim establishes no statistic beyond that reparameterization, and does not address a fixed-metric restriction, strategy under risk preferences, or another mathematical gap that survives the equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
