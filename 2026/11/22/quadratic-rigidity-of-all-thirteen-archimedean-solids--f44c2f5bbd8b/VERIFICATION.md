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

Re-audited the complete replacement RESULT.md. On the circumradius sphere, quotienting by the sphere equation leaves harmonic degrees 0,1,2 of dimensions 1,3,5. Orbit evaluation is equivariant; a kernel submodule in the multiplicity-free real representation must be a sum of killed irreducibles. In the proper octahedral group the class-weighted character cross-products of the linear, diagonal trace-free and mixed quadratic blocks vanish, their squared norms after dividing by 24 are one, and all have mean zero. At a nonzero v the constant and linear blocks survive. The entire diagonal block vanishes iff all squared coordinates coincide, giving the eight-point cube, and the entire mixed block vanishes iff all pairwise products are zero, giving the six-point axis orbit. Other proper octahedral orbits have rank nine, including all six listed Archimedean cases (each has at least twelve vertices). The known icosahedral design input applies to the proper rotation group: the Hopf map sends the binary group to the proper action and the balanced harmonic indices through five give exact quadrature. Averaging the square of a quadratic then gives injectivity. Independently the checked icosahedral character norms and cross-product give the same rank by the orbit argument. The truncated tetrahedron arises by trisection of the starting tetrahedral edges: the four independent even-sign characters separate the constant/diagonal equations from linear/mixed pairs. Comparing coordinates of magnitude three versus one gives all diagonal coefficients equal and the linear/mixed determinants equal to 8 up to sign, so those coefficients vanish. This covers the remaining solid. The intact exact checker corroborates representative cases and the character data; it was inspected but not run and does not establish the universal classification.

## originality

PASS

This PASS is for the replacement only. The frozen result's claimed all-icosahedral-orbit strengthening is already covered by a stronger published design result and does not pass as new. The replacement explicitly credits that result as input and credits the prior cuboctahedron and truncated tetrahedron cases. What survives is the necessary and sufficient proper octahedral orbit criterion and its use, with these inputs, to complete the thirteen-solid proof. No inspected result gave that criterion or the all-thirteen proof.

## value

PASS

The repaired biconditional gives a complete exact criterion on the continuum of seed directions, including a geometric explanation of each exceptional orbit, not a finite rerun of known rank calculations. It is strictly broader than certifying a few spherical 4-designs and supplies the octahedral portion needed to resolve the named thirteen-solid conjecture alongside credited prior inputs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
