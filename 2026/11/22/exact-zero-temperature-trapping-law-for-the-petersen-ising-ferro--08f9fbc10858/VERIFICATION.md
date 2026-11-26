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

A flip with two or three discordant incident edges reduces the cut by one or three. While the spin configuration is unchanged, the waiting time for a genuine flip is an exponential race among the enabled vertices, uniform over them because their rates are identical. The cut descent and finite waiting times prove almost-sure absorption and the proposed recurrence. Every mixed absorber has monochromatic minimum degree at least two in both colors. Girth five forces two complementary induced five-cycles; exact enumeration verifies twelve such assignments, one S5 orbit. Independently I built KG(5,2) and performed forward probability transport, not the supplied backward recursion: starting with one unit of mass at each state of size k, visit the states in descending cut and distribute mass equally to enabled successors. This verifies all eleven unnormalized Bernoulli coefficients (nonzero at k=3,4,5,6,7 with values 88/9,8242/189,12788/189,8242/189,88/9), equal mass at the twelve mixed sinks at each k, and Q(1/2)=4121/24192. Both proposed polynomials in p have degree at most ten and agree at eleven distinct exact rational points. I also verified the frozen CSV entries for all 18 symmetry classes and their exact absorption values from the representative states. The endpoints are consensual and the formula is strictly increasing in p(1−p), giving the unique maximizer at one half. This does not model a parallel update or random fields.

## originality

PASS

Credit the exact fixed-state count and the overlap with the same-graph three-state Potts certificate. The latter's statewise computational method can reproduce binary coefficients on restriction, but its stated exact probabilities and published results table are for other initial laws; its own prior-work section already acknowledges an exact two-spin Petersen freezing law. The explicit Bernoulli trapping polynomial and its quantitative seed and bias dependence are the supported contribution, not the fourteen fixed points or the generic cut-descent recursion. No independent earlier exact statement or exact table of this law was verified.

## value

PASS

The Bernoulli trapping law measures kinetic accessibility rather than the mere number of locally stable patterns. It gives an exact bias-dependent benchmark, including suppression to third order at small seed probability and the exact extremum at an unbiased quench, for a canonical non-bipartite cubic graph. The finite coefficient profile is useful independently of a larger-family solution and is not supplied by the standard fixed-point census or the reported three-color aggregates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
