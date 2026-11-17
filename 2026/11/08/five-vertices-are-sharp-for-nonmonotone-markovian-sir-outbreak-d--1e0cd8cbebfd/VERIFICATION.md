---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Reconstructed the first-step recurrence (|I|+beta*m)F=1+sum_recoveries F+beta*sum_transmissions F on disjoint susceptible/infectious subsets. Every transition decreases lexicographically (|S|,|I|), so the exact rational recursion terminates. Independently enumerated all simple graphs on n=1,...,4, quotiented connected graphs under vertex permutations (1,1,2,6 classes), and exactly differentiated F for each of 33 rooted connected representatives: numerator and denominator of every derivative have nonnegative coefficients, and numerator is nonzero for n>1. Disconnected components reduce to the rooted component. Independently computed the five-vertex K2+3 isolates graph at beta=100, seed3: F=3233110817579844486927395030461/1415931898971338608037919183261, exceeding H5=137/60 by exactly 1326298572426638149591240301/28318637979426772160758383665220>0. The high-transmission limit follows by a spanning-tree transmission-time coupling and uniform integrability against the sum of infectious lifetimes. This establishes a sharp counterexample, not a full five-vertex classification.

## originality

PASS

The sharp number of vertices at which expected extinction duration is nonmonotone in the homogeneous continuous-time, exponential-recovery one-seed SIR model is not supplied by the inspected general SIR duration methods or the previously known discrete-time fixed-infectious-period nonmonotonicity. Exact parameter-dependent inequality and full n<=4 exclusion are the substantive distinction; novelty remains best-of-knowledge.

## value

PASS

The minimal network order for a qualitative reversal in an epidemic observable is a natural structural boundary: all rooted networks up to four nodes obey a monotone law, while the explicit cyclic five-node witness violates it. The single time-expectation invariant is mechanistically meaningful and the cutoff is not automatic from previously studied models. A modest sharp finite threshold is mathematically valuable without purporting to predict actual outbreaks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
