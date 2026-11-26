---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Normalizing by the lower diagonal unit gives B₂(R)≅R×₍units₎×(R⁺⋊R×₍units₎). At a fixed affine multiplier s, conjugation takes b to wb+(1−s)z, so translation classes are unit orbits on R/(1−s)R lifted through (1−s)R. If 1−s is a unit the quotient is trivial; if it is nonzero radical, its ideal is a k-line of size q; if s=1 the orbits are the units, the zero singleton and the nonzero radical lines. These give the six rows with coincident numerical sizes added. For the dual action, every radical character has q extensions; a nontrivial restriction is represented by a nonzero k-linear β via the trace pairing. Its stabilizer must reduce to 1, and invariance under 1+w is equivalent to β(w)=0 by testing χ(wr) over all residues r. It therefore has size q^{d−1}; the other orbits are the trivial character and the nontrivial quotient characters. Each invariant additive character extends to its inertia subgroup by being trivial on the stabilizer complement, so the abelian little-group rule gives the displayed degrees and multiplicities. These arguments apply to q=2, d=1, and mixed characteristic without a coefficient field. The class total, commuting probability and fixed-q limit follow by summation. Independent arithmetic (python3 /workspace/independent_arithmetic_checks.py) checked weighted class populations, degree squares and totals for 48 parameter pairs; the frozen checker was inspected, not executed.

## originality

FAIL

A distinct indexed finding on element orders already reconstructs the matching affine class and degree data, and explicitly gives the abelian direct factor relating them to upper triangular groups. Its element-order theorem assumes odd residue characteristic, but its separate class/degree calculation has no parity-dependent step and yields the q even rows as well. This is demonstrable overlapping coverage, not a judgment of temporal priority. That finding explicitly credits an earlier upper-triangular spectrum result without giving a resolvable ID; it may be referring to the bound finding under variant wording. The coverage judgment uses the distinct proof's self-contained calculation, not treating its ambiguous reference or a catalogue hit pointing back to the target as a distinct prior result.

## value

FAIL

These are natural invariants and the table is convenient, but after the inspected affine-spectrum reconstruction there is no separate substantive exact fact: merging the class rows, multiplying by the size of an abelian factor and summing for commuting probability are mechanical. The nonprincipal and even-characteristic rows are already controlled by the same recorded orbit decomposition; the parity-sensitive problem in the neighboring finding concerns element orders, not this census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
