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

Write u and v for the left and right action-1 minus action-0 counts. An untied right shore forces every flexible conformist to its majority; an untied left shore forces every flexible rebel to its minority. Below both weak thresholds the flexible players are strict majorities of their shores, so an untied shore yields contradictory majority signs around the two responses. Both ties require even-even, where they can be achieved without pins. Below both strict thresholds both shores retain flexible players and hence must be untied; each flexible bloc is at least half its shore, yielding the same sign contradiction. Unanimous eligible-side pins achieve the thresholds by having the flexible players on that shore take the other action. Necessity at a positive minimum puts all pins on one eligible side by the lower bounds. For left-only pins the right sign s is nonzero: the right is unanimous if u is nonzero, and if u=0 in the positive weak case the right size is odd. All flexible left players choose s. If p pins choose s then su=a−2k+2p, which must be nonpositive in the weak case and negative in the strict case. At the threshold either bound forces p=0. For right-only pins, similarly the left sign s is nonzero and if p pins use s then sv=2p−b, which must be nonnegative or strictly positive, respectively, so p=k. This also covers a completely pinned shore since the other shore is fully flexible. Count two unanimous assignments for each eligible labeled k-subset; the distinct shores give disjoint descriptions and the uniform denominator is 2^k binom(a+b,k). The examples reduce to 16/448 and 40/960. The inspected verify.py checks only sizes 1 through 5 and was not executed; the proof covers all nonempty shores under the stated topology and active-only strictness.

## originality

PASS

The even-even zero-pin criterion is known, and general sufficient conditions cover related constructions. The distinct result is the positive optimum and all minimum-budget pin descriptions and probabilities, with the active-strict contrast. No inspected theorem or indexed finding implies that combination.

## value

PASS

This class makes it possible to distinguish three operationally different questions: whether ties alone permit equilibrium, the least commitment that permits equilibrium without flexible-player ties, and the chance of success when minimum-cost placements and actions are sampled rather than designed. The necessity and full characterization give sharp budget and reliability information not conveyed by a single construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
