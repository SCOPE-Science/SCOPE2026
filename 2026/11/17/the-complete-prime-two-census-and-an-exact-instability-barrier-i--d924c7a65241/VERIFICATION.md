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

Two-cycle p,q equations split exactly into p²=q² and pq=(1+b)(1+c), with p²+q²=-mu(1-c²)/c in the non-antipodal case; discriminant and sign constraints yield the strict counts, equality collisions and c=1/3 order. Independently formed one-step Jacobian J(y,z) and symbolic K=J(p,z1)J(q,z0); SymPy factors det(I-K)+2c/(1+c)(p²-q²)² to identically zero, ensuring h(1)<0 and a positive real root >1. Source checker.py inspected; no finite extrapolation.

## originality

PASS

The complete real primitive period-two census and c=1/3 threshold ordering are NOT original by themselves: the prior 2026-11-17 T_- census and Gonchenko 2024 square-map duality imply them after ν1=-b, ν2=-μ, ν3=c and fixed-point subtraction. The surviving independently checked exact det(I-J2)=-2c/(1+c)(p²-q²)²<0 for all off-antipodal two-cycles, hence positive real Floquet multiplier >1, is an additional meaningful global dynamical instability obstruction not supplied by the earlier census. This composite claim remains correct and has a substantive original component; no claim of novelty for the count alone. Priority risk remains.

## value

PASS

The exact global obstruction to attraction of the off-antipodal symmetry-broken primitive period-two cycles is a structurally significant Floquet invariant for a natural axial-symmetry quadratic family, strengthening mere orbit counts with a universal instability assertion; no novelty/value credited to already dual-covered census alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
