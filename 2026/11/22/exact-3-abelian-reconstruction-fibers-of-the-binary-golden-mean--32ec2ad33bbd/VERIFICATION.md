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

For each two-gram, subtract counts of its extensions on one side from its two-gram count to recover the indicator of the corresponding boundary two-gram. For n≥3 and m≥1 these boundaries determine u,v; 101 counts the interior single zeros and 000 counts exactly the excess zeros over length two. Conversely, the five allowed triple counts in the proof follow by counting the long gap ends (001 and 100), the short interior gaps (101), the ones with two zero neighbors (010) and the three-zero windows (000). The triple data and the boundaries recover all shorter counts. The all-zero word and lengths 0,1,2 are correctly separated. Choosing c of m−1 interior gaps to be long and distributing h among the r labeled long gaps gives precisely the binomial product, also checking realizability and the singleton condition. Independently simplified the geometric interior sum to z/[(1−z²)(1−z³)]. Allowing all h and removing excess when r=0 gives the stated C series; summing c=0, then c=m−1 with m=2 and m≥3 separately, gives the U series. Partial fractions give the stated parity formulas and small-length checks give the two listed first collisions. Independent replay compares the complete partitions, not just their sizes, through n=19. The zero-error claim follows by exactly one representative per profile.

## originality

PASS

The general exact Euler-trail fiber formula and general singleton criterion already apply, since any 3-Abelian equivalent word has the same count zero of 11. The supported distinct result is the explicit feasible endpoint/run spectrum, binomial reduction, and its exact all-length profile and singleton counts for the linear forbidden-11 language, not a new general class-size method or a new generic polynomial-growth theorem.

## value

PASS

Forbidden-11 is a classical finite-state source. Exact capacity versus singleton counts distinguish choosing one codeword per observable profile from the stronger property that the full source word is uniquely identified. The quadratic versus linear growth and every-fiber binomial formula quantify both properties uniformly and enable exact finite-length ambiguity checks beyond a general Euler method or asymptotic growth bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
