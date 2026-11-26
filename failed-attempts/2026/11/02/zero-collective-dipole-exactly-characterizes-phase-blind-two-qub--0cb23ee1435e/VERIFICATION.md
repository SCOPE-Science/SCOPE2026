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

In both bright exchange blocks, use the ordering (battery ground, battery excited). After removing the sector-dependent scalar phase the propagator has diagonal entries conjugate(u), u and off-diagonal entries v. Within the two final excited components that can interfere, the products of incoming charger amplitudes are conjugate(a)b and conjugate(b)d, with the same factor conjugate(u)v. Each other component contributes only a population. Thus the first harmonic in the input phase vanishes exactly when Q=0 for an interior population and 0<p<1; the phase imposes no condition at the population poles or at p=0 or 1. J_- connects |11> to |B> and |B> to |00> with matrix element sqrt(2), so its expectation is sqrt(2)Q. The local measurement construction is valid: the traceless difference of normalized postcollision charger-column projectors has three relevant contractions with the two axes, killed by choosing n perpendicular to r and then m perpendicular to s and T^T n. Every outcome of nonzero total probability preserves the unconditional battery population; if either column vanishes this is immediate. The affine recurrence follows regardless of the resulting branch phases. The product |+>|-> gives b=0, A=1/4 and B=1/2, as claimed. The upper endpoint pB=2 requires p=1 and the pure bright charger, outside the generic-pulse classification.

## originality

FAIL

The claimed necessary-and-sufficient classification is mechanically implied by the same-model arbitrary-amplitude phase map of Gong–Zhang–Li, Eq. (15): collecting its first harmonic in the battery phase gives exactly the collective-dipole cancellation, and their proposition already supplies local product equalization. A distinct catalogue record also formulates the same interference coefficient and treats the more general concurrence-resolved phase swing. The basis change, the different proof of equalization, and evaluation at one antiphase product state do not establish the frozen classification and protocol as an original result. This judgment rests on verified coverage, not on the inaccessible coherent-ancilla paper or on inferred priority from a catalogue date.

## value

FAIL

Phase-independent population under adaptive charging is a meaningful target, and the dipole notation makes the mechanism easy to see. But the proposed increment is a regrouping of the published phase coefficient, a new construction of an already-established measurement property, and one substitution in a known map. It resolves no separate charging boundary or capability beyond that map and protocol; the product example alone is not a new nonmechanical invariant of the model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
