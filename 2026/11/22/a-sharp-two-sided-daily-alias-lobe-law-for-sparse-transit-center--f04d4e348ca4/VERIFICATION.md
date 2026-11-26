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

For δ=|P−1| the residues of consecutive nights step by ±δ modulo P. Reflection and a common shift give intervals with starts jδ and width w; the lifted span is <1/2<P, so no additional copies overlap. Each window sees at most one center, and disjoint nights cannot count the same event center. A phase with at least r hits belongs to an intersection of r consecutive intervals. Those intersections are translates of an interval of length ℓ=w−(r−1)δ; the union has length ℓ+(N−r)min(δ,ℓ) when ℓ>0 and measure zero otherwise, including the touching case. Divide by P for uniform phase. At δ=w/r the numerator changes from slope N−2r+1≥1 to slope −(N−r+1)(r−1); dividing by either 1+δ or 1−δ preserves the respective strict signs on the two positive branches since w<1≤r−1. Hence resonance is a strict local minimum, and the denominators r−w and r+w give the higher short-period peak and the unique global maximum. The limiting c/r follows directly by substitution. The attached checker was inspected, not executed; the interval proof supplies the universal result.

## originality

PASS

In the evidence inspected, phase-fraction window functions and mechanisms for computing them are established, but the specific short-window all-N, all-r formula together with the strict two-lobe classification and asymmetric global optimizer is distinct. A generic exact phase partition does not give a formula or determine the maximizing period without the consecutive-intersection reduction and branch analysis. This is a best-of-knowledge decision, not a priority certificate.

## value

PASS

A useful exact benchmark for the near-resonance behavior of phase-coverage calculations: it identifies when nightly redundancy is maximal at resonance, why detectability instead peaks at a small detuning, and why the two peaks differ despite symmetric raw coverage. The peak remains of order one for w=c/N at fixed r while the resonance coverage goes to zero. The application is narrowly a coverage test for ideal point events, not a claim about actual exoplanet yields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
