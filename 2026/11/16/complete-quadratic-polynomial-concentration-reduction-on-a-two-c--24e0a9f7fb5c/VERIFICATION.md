---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

All-dimensional d>=3 solid-ball normalized Lebesgue polynomial degree<=2 space decomposes under swaps of x1,x2 and O(d-2) on remaining y: symmetric scalar 4, antisymmetric scalar 2, (d-2) copies of symmetric vector 2 and antisymmetric vector 1, and residual quadratics dimension C(d-1,2). Beta/Gamma moment formula for |x|^alpha is exact, with the quarter-ball moments one fourth of signed absolute moments for first two coordinates, and odd residual exponents killed. Conditional expectation E(|y|²|x1,x2)=(d-2)/d(1-x1²-x2²) yields orthogonal radial-residual polynomial, plus trace-free y modes with eigenvalue 1/4. Gram normalization yields antisymmetric A_d and vector V_d with off diagonal c_d and 2c_d; 4x4 generalized spectrum uses explicit b0..b3 moment matrices. Multiplicities sum C(d+2,2). Independently constructed full monomial Gram moment pencil and invariant reduced blocks (not executing unchecked package code): eigenvalue lists match numerically at d=3,4,5,7; analytic orthogonality gives all-d proof. Trace = dim/4 and Rayleigh extrema sharp.

## originality

PASS

Best-of-knowledge new exact full polynomial degree-two two-coordinate solid-ball wedge spectrum. Compared actual full text of Gerhards–Huang polynomial Slepian high-band theory; an all-positive-orthant solid-ball polynomial reduction and spherical quarter-wedge harmonic result differ in mask or function space. Neither directly implies the four/two/two block spectrum stated here; common gamma moments and Schur decomposition alone are frameworks requiring nontrivial new block evaluation.

## value

PASS

A complete fixed-band concentration spectrum for a geometrically canonical two-coordinate quarter-ball with total-degree-two polynomials is a motivated exact Slepian localization invariant; reducing O(d²) operators to constant 4x4/2x2 blocks and enumerating protected quarter-energy multiplicities is useful without a higher-degree theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
