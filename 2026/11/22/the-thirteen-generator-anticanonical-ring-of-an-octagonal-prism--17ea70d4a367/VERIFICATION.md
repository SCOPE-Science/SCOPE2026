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

Writing g(a,b)=max(|2a+2b|,|a+2b|,|-a+b|,|-2a-b|), the dual lattice cone is exactly m>=g(a,b)+|c|. The pairs of consecutive planar boundary rays are oriented, have determinant one, and share a linear piece of g. Thus each sector has nonnegative integral coordinates in its two boundary generators; the spare degree and the height are supplied by the degree-one generators. The six nonzero planar vectors at first degree two cannot decompose in degree one, and the four first appearing at degree three are outside 2Q. For an independent all-degree Hilbert series calculation, partition the plane into the origin, positive rays, and open sectors. With A_i=t^d_i/(1-t^d_i), the series is (1+t)/(1-t)^2 times [1+sum A_i+sum A_i A_(i+1)]. Clearing the frozen denominator gives exactly the stated numerator. Exact direct lattice counts start 1,3,11,29,59,105,173. The dual vertices give Cartier index lcm(2,3)=6. The degree-one ratios use only z and have conic image closure, while three degree-two ratios give generators of the full torus function field. The first birational multiple is therefore two; nothing is inferred for a deformation.

## originality

PASS

Pass for the evaluated anticanonical semigroup and section series and their low-degree map calculation for this specific X. The polytope, polar vertices and volume are prior; the Cartier index is a direct consequence of the published polar vertex denominators and is not credited as a distinct contribution. A closely related indexed result computes a different ring of the same variety.

## value

PASS

The central fibre of a specific obstructed K-polystable example is independently motivated. Its minimal section degrees, exact Hilbert function and change from a conic image to a birational map are useful precise invariants not supplied by the volume. The gap between the first birational multiple and the Cartier index is informative; it is not inferred from deformation behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
