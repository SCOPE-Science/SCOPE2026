---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For Phi_D={x_i} union {Dx_i}, Hadamard orthogonality gives frame operator S=I+D^2. By Casazza–De Carli–Tran Theorem 5.7, scalability of the canonical dual is equivalent to nonnegative weights on the original vectors whose weighted frame operator is S^2. Flat Hadamard coordinates reduce every diagonal coordinate equation to (A+B t_j)/n=(1+t_j)^2, with A and B the two block weight sums. An affine function can agree with the strictly quadratic right side at at most two distinct t_j values. For two levels u,v, interpolation gives A/n=1-uv and B/n=2+u+v, so nonnegative scaling exists exactly when uv<=1; strict positivity is uv<1. A fresh rational replay verified the interpolation identities for representative uv<1, uv=1 and uv>1 cases and the three-level source example fails the affine fit.

## originality

FAIL

The 2022 primary paper already gives the decisive general criterion (Theorem 5.7): the canonical dual is scalable exactly when weighted original vectors can realize S^2. It then applies that criterion in Proposition 5.10 to precisely the same diagonal-Hadamard construction with levels 1,4,9 and proves non-scalability by the resulting incompatible affine equations. The assigned “phase diagram” merely leaves the diagonal levels symbolic: Hadamard flatness turns Theorem 5.7 into one affine interpolation problem, whose elementary solution is “at most two levels” and uv<=1. Under the required implication bar this is a routine parametric completion of an already published same-family argument, not an independent original theorem. The 2024 dual-scalability paper broadens the subject but is not needed for this decisive comparison.

## value

FAIL

The at-most-two-level and uv threshold statements form a clean family classification, but after the published general criterion and its exact same-family three-level obstruction, the derivation is only an affine interpolation exercise. It therefore falls on the routine-corollary side of the common value bar despite being useful expositionally.

The dated certificate retains the supplied scientific assessment, sources and limitations.
