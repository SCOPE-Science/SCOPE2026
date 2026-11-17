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

For XY!=0, z,Xz,Yz,XYz form a basis, giving the single regular E-module orbit of dimension16-4=12. The annihilating locus is the proper image of a rank-eight vector bundle over Gr(2,4), irreducible dimension12. In the rank2 X chart Y=(A,B;0,-A), A²=0 and [A,B]=0; nonzero nilpotent A has centralizer kI+kA, so its closure intersects A=0 precisely when B has repeated eigenvalues, with reduced char2 equation tr B=0. Thus intersection has dimension11. Counting rank0/rank1/rank2 square-zero X and corresponding Y fibers yields q^6(2q^6+q^5+q^4-q²-q-1), with nonzero-product regular orbit |GL4|/(q³(q-1)). Independently checked q=2 counts 10816 total and 2520 nonzero and algebraic polynomial identity. Computations only illustrate all-field geometric proof.

## originality

PASS

Levy already gives two dimension12 components in characteristic two, Schröer annihilating locus and a later published all-dimensional product-rank census covers the regular positive-product orbit. The surviving geometric claim is the precise all-characteristic rank-two discriminant intersection criterion and dimension11 incidence, not established by those inspected results. Total cardinality may be assembled from known pieces; this is not itself asserted as clearly new.

## value

PASS

Dimension four is the smallest exterior-algebra module carrying XY!=0. The divisor describing degeneration between the regular and annihilating components is an independently motivated geometric structural fact; point counts complement it, not sole value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
