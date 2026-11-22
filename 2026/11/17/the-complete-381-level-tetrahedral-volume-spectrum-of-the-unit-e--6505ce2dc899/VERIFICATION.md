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

The coordinate normalization q=2u+v for all 60 directed icosahedron edges produces twice the unit-edge truncated polyhedron vertices. Determinant/q volume scale is exactly |det(qj−qi,qk−qi,qℓ−qi)|/48 in Z[φ] using φ²=φ+1; sign comparisons use 2(a+bφ)=2a+b+b√5, exact integer comparisons. The pinned check_spectrum.py visits all C(60,4)=487635 quadruples, groups exact algebraic values and checks every row of spectrum.tsv, the two top shape classes and sum of squared determinants. Independently reimplemented different exact coordinate/ring and quadruple enumeration; obtained 381 distinct levels, first three (100,164)×120,(100,160)×120,(96,160)×60, zero-level 10635, and a unique six-edge squared-distance congruence signature for each of the first two levels. Full independent squared-determinant sum (1996320000,3162240000) agrees with 480000(10+9φ)^3 in basis (1,φ). The actual TSV has 381 rows, totals 487635, first/last entries match source. This is a finite complete classification, not a sampled histogram.

## originality

PASS

The October 18 full prior theorem already determines the maximum and its 120 vertex-support maximizers and complete continuous maximal families over all truncation parameters. The surviving precise contribution is the 381-level multiplicity census, second-largest volume with exact gap and congruence of the top two layers. No inspected prior covers that finer spectrum for this exact polyhedron.

## value

PASS

The 60-vertex uniform Archimedean solid is a canonical object, and exact complete distributions of vertex-supported simplex volumes, second-best gap, and multiplicities are natural invariants useful for optimizing discrete tetrahedra, symmetry-class testing and future polyhedral comparison. Unlike a re-reporting of the known maximum, the 381-level census resolves all nonmaximal levels and supplies a checkable independent moment identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
