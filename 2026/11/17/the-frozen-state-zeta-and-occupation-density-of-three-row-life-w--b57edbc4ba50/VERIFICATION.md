---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For each vacant cell on 3×n Moore torus n≥3, its eight distinct neighbors consist of the two other cells of its column and all three in each adjacent column. Thus population profile (a,b,c) is fixed exactly when b=3 or a+b+c ≠3. A closed cycle of 16 pair-population states (a,b)→(b,c), weighted by C(3,c)u^c, counts each labelled fixed configuration once, giving Z_n(u)=tr(T(u)^n). The 16-state source matrix was independently checked; the determinant zeta denominator and characteristic polynomial follow by integer matrix algebra, with primitivity from explicit reachability plus the (3,3) loop. Collatz–Wielandt positive-vector rational inequalities bracket dominant λ, and differentiating det(I−zT(u))=0 at z=1/λ gives exact limiting occupied fraction. Independently reproduced all population-profile total counts n=3..7 and direct distinct 2^(3n)-state neighbor-rule counts n=3..5: 428,2447,16635,117892,811242. n=1,2 formal transfer traces are excluded; no claim about attraction basins.

## originality

PASS

Primary published statements and actual full-text searches support provisional originality for the surviving mathematics; prior related inputs are explicitly credited; priority risks are retained.

## value

PASS

An exact all-circumference, full occupation-resolved enumeration and limiting density of a natural irreversible cellular automaton on the smallest nondegenerate fully periodic Moore strip are meaningful dynamical-combinatorial invariants. The degree-11 zeta and Perron entropy law are nontrivial exact consequences of a motivated local reduction, not a handful of small cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
