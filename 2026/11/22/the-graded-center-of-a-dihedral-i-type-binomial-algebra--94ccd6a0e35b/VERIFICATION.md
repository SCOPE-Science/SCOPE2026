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

The semidirect images respect all six defining relations. Independently, each relation swaps one of the six unordered distinct coordinate-increment pairs at the identity, and a prefix with permutation p transports that swap by p. Each ordered increment list decodes to a unique word, so adjacent swaps identify exactly words with the same nonnegative translation coordinate. The word x_0^2 x_1 x_3 gives the central translation q=(1,1,1,1), and the increment argument expresses it with any x_i first. Thus every x_i inverse is a positive word times q inverse, giving first-coordinate existence and uniqueness on the fraction group by translating far enough by q. In particular left translation cosets of N correspond to coordinate cosets and its index is eight; this fills the index step explicitly. The four stated translation vectors satisfy the congruences and have determinant of magnitude eight, and the congruence map onto Z/2 × Z/4 is surjective. Thus N is precisely Lambda. Conjugation by its full-rank translation subgroup gives infinite classes for elements with nonidentity permutation and finite F-orbits for translations. Finite-support central elements have constant coefficients on conjugacy classes in every characteristic; commuting with the monoid generators implies commuting with their inverses in the group algebra. This gives the stated positive-support center. The exact independent script /workspace/review-work/algebra_check.py verifies the local swaps, translation vectors, all eight fixed-vector residue polynomials by cross-multiplication, and their Burnside sum numerator 8(1-t^2+t^4) over the common denominator. Hence the series is an infinite rational identity and remains characteristic-independent, not merely a degree-sixteen fit.

## originality

PASS

The exact coefficient-free algebra and its semidirect structure are known from Bhatoy. The inspected primary and indexed claims do not give its graded center; specifying the embedded translation lattice and carrying out the dihedral fixed-vector count are additional mathematical work, not renaming the abstract kernel or reading a table entry. This verdict is limited to the sources checked.

## value

PASS

This determines a natural invariant of a previously specified I-type algebra with nonabelian holonomy. The embedded congruence lattice describes actual central orbit sums, while the full graded series gives their multiplicities in every characteristic, including modular characteristics where averaging vectors over the group is not valid. This is concrete center information not given by the abstract group extension or a finite-dimensional census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
