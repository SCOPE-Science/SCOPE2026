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

The one-line cubic has no line through P=[0:1:0:0], giving one global affine Grassmann chart. Restricting the cubic yields a²+c³=0, 2ab+3c²d=0, b²+a+3cd²=0, b+d³=0; eliminating a,b without denominators gives f=c³+9c²d⁴+6cd⁸+d¹² and g=3c²d+6cd⁵+2d⁹. Dehomogenizing with c/d⁴ yields cubic F and quadratic G with exact resultant -1. Thus no nonorigin point in any geometric fiber; degree12/9 weighted regular sequence gives length27, Hilbert series (1-s⁹)(1-s¹²)/((1-s)(1-s⁴)), socle16, embedding dimension2. Proper and affine implies finite; equal fiber lengths imply Z-torsion free and free rank27. Mod3 gives precisely (c³,d⁹). No step divides by a prime. Finite line-enumeration checks are corroboration, not proof.

## originality

PASS

Prior work covers the unique geometric line, equation of the T1 surface and generic length-27 field-level Fano scheme, but does not supply the fixed integer model two-relation presentation, flatness at 2 and 3 or monomial char3 fiber in inspected material.

## value

PASS

The Hilbert scheme of a maximally degenerate cubic naturally retains 27 enumerative directions; its arithmetic deformation and bad-characteristic local algebra are genuine exact invariants not mechanically determined by the generic 27-line count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
