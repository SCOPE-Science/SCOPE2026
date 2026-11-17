---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The cone contains 1+(q-1)(q+1)^3=q(q^3+2q^2-2) points. Trilinear character orthogonality reduces pair-frequency means to Hamming distances 1,2,3 and same-coordinate contrast. Splitting labels into uniform and contrast spaces gives a scalar level q^3/D, Hamming cube levels q(2q-1)^2/D (3), q(2q-1)/D (3), q/D (1), and the 2x2 coupled block L±. The strictly positive shifted 2x2 determinant at q/D rules out L− reaching the checkerboard eigenvalue; remaining levels exceed q/D for all q≥2. For binary q=2 independent exact enumeration of 28 cone points gives eigenvalues 1/7, 3/7 (3), 9/7 (3), and 13/7±6sqrt3/7. This supports, not substitutes for, the all-field proof.

## originality

PASS

The multilinear Cayley graph eigenvalue theorem of Byrne–François gives raw rank-one tensor character sums and thus overlaps core input, while Lavrauw–Sheekey classify geometry/orbits. Neither inspected primary statement gives this specified 1+8(q-1) coordinate-character Gram frame, its unique checkerboard least mode or sharp Riesz condition number. Plücker and two-factor matrix coordinate sampling rely on different Johnson/rook geometry. An overlooked reduction of the general tensor graph theorem remains possible.

## value

PASS

This is the first nonmatrix Segre cone and the complete full one-coordinate Fourier band is a natural sampling family. Identifying its exact minimal Riesz eigenmode and sharp instability order across all q gives precise reconstruction stability and a structural Hamming-cube obstruction; not a random parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
