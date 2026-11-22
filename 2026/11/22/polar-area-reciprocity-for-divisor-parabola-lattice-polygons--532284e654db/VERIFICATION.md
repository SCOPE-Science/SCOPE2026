---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the polar-area reciprocity theorem

The complete exact checker is `checker.py` and requires only Python 3's standard library. Run `python checker.py` in a directory containing that file. It constructs both cyclic vertex lists directly: the original parabolic polygon and the polar from independently derived facet-normal intersections. It computes oriented shoelace determinants using `fractions.Fraction`, compares against both area identities, counts lattice boundary points using edge gcds, and verifies insertion triangles independently for rational sample parameters.

Executed checks: all heights \(2\le h\le500\) and eight additional heights (720, 840, 2520, 5040, 27720, 99991, 999983, 199982), yielding 507 complete exact-height comparisons; plus three exact insertion-triangle comparisons. The checker printed `PASS` on both suites. The proof of every positive integer height and of the limiting sharp gap is analytic, not justified by finite iteration. The checker is not an independent mathematical audit or a proof of historical priority.
