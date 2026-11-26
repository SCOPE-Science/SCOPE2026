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

With the impulse at index one, the binary recurrence gives F(z)=z/(1+z²+⋯+z^k) for n≥0 with coprime numerator and denominator. The state transition is invertible because the oldest bit has coefficient one. A scalar period T holds exactly when the reduced denominator divides 1+z^T: in the converse direction the numerator after clearing that denominator has degree 1+T−k<T. Reciprocation gives the unit order modulo C_k=x^k+sum_{i=0}^{k−2}x^i, and the scalar sequence equality extends to negative indices by invertibility. The derivative of (x+1)C_k=x^{k+1}+x^k+x^{k−1}+1 is x^{k−1} for odd k, and x^{k−2}(x+1)² for even k. The product has nonzero constant term, so in even order only x+1 can repeat. C_k(1)=0 and C'_k(1)=(k−2)/2 mod 2 for even k, giving a simple root if 4|k. Otherwise the product has multiplicity at least three, and cannot have multiplicity four or more because its derivative vanishes to exactly order two there. Thus C_k has exactly a square factor (x+1)² in that case, with squarefree part Q_k coprime to it. All orders in the squarefree quotient are odd; the squared factor contributes exact order two, including k=2 when Q_k=1. The divisibility C_k|(x+1)(x^{L_k}+1) says the difference of the sequence and its half-period shift is constant, and minimality excludes zero. Hence the flip holds on every index and gives exact balance only in this class.

## originality

PASS

The supported distinct result is the all-k residue-class classification of the scalar binary impulse least period's 2-primary part and the exact complement action of its odd half-period. The recurrence, ordinary periodicity, polynomial-order framework and finite-group Pell period theory are antecedents. The checked statements either concern a different recurrence, a fixed order, another modulus/invariant, or finite-group rather than scalar periods. Older articles' uninspected interior tables leave a real risk, not evidence of coverage or demonstrated absence.

## value

PASS

This classifies the exact 2-primary period of a standard recurrence uniformly in its order without computing its variable odd part. It explains why perfect binary balance occurs despite very different periods: there is an explicit involution on positions pairing every occurrence with its complement. This makes the result a structural statement on the impulse orbit rather than a finite table or parity spot check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
