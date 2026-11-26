---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

With L=lcm(5,q), the determinant is a cyclotomic integer, degree at most 8. Hadamard bounds every conjugate by 5^(5/2), so |norm|≤5^20. Each modular evaluation at a primitive root has prime-ideal kernel of residue degree 1; zero in both distinct characteristics forces divisibility of the norm by their product, larger than the bound. A nonzero reduction suffices in the opposite direction. The code's column and root powers agree with the displayed convention, and the scalar action is free with exactly q indexed words per normalized word. An independently written exact census (/workspace/branches/gabor_replay.py; supply the frozen witnesses.tsv as argument) used 2,130 column-set representatives for the translation action on (Z/5)^2: simultaneous time-frequency translation acts by an invertible left factor and nonzero column scalars. A mod-3001 elimination filter proved nonvanishing; every possible zero reached by the filter was decided by reducing the signed integer determinant polynomial modulo the appropriate cyclotomic polynomial. It reproduced normalized successes 0,5,60,205,0 and checked all 709 stored singular witnesses separately by exact reduction. The five binary successes had four equal signs and one opposite sign; restoring the scalar phase gives 0,10,180,820,0. The conclusion concerns exact linear inversion, not numerical stability.

## originality

PASS

The generic full-spark theorem and algebraic constructions do not enumerate or bound this finite set of unit-modulus windows. Known symmetry-based obstructions do not yield the entire five-alphabet census. No matching table was located in the examined literature or indexed records; priority is best of knowledge.

## value

PASS

Dimension five is a small prime benchmark for exact frame designs under coarse phase constraints. The exact finite answer separates generic existence from attainable designs: two phases already permit arbitrary five-atom recovery, whereas every fifth-root word fails, even though the alphabet matches the ambient modulation order. The classes are nonnested, not a monotonicity contradiction. The full counts, small explicit binary designs and certified obstructions provide exact design information not supplied by generic full spark, without extrapolating to other dimensions or stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
