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

# Verification of exact three-step displacement law

Execute `python3 check.py` with Python 3 and no third-party packages. The source implements the same fixed map as in RESULT.md from the starting unit square, not a test fitted to a purported density.

The direct program constructs eight, then 56, then 320 nonzero-area polygons for one, two and three full shear steps using exact `Fraction` arithmetic. It checks that each partition has rational area exactly one. It integrates the exponential character on every final affine polygon by Green's theorem and checks the exact grouped phase coefficients: the zero-order and first-order sums vanish, while precisely the twelve stated second-order coefficients remain. Exact algebra over rational pairs representing \(a+b\sqrt5\) checks all sixty residue classes of the Fourier numerator; the unique zero class is zero modulo sixty. Exact Bernoulli-polynomial evaluations at all knots determine the sharp density extrema and positivity.

Actual package execution returned:

```
PASS: 320 exact rational polygon domains; A=B=0; 12 rational phase coefficients
PASS: exact Fourier zeros precisely k congruent 0 modulo 60
PASS: exact density extrema 893/1225 and 352/315
```

The finite algorithm is exhaustive for the threefold rational branch partition. The proof derives the piecewise-affine integral reduction and Fourier inversion for every integer frequency; the code validates the complete finite coefficient table and quadratic-radical residue step without relying on numerical experiments. The statement is specific to stationary Haar initial data and the defined symmetric map. No independent audit or external certification has been performed.
