---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

For smooth reciprocal octics y²=x8+A x6+B x4+A x2+1 in characteristic5, Hasse–Witt coefficient matrix of f² has shape [[A²+2B,0,2A],[0,2A²+B²+2,0],[2A,0,A²+2B]]. Constant F5 diagonalization proves p-rank is number of nonzero λ±,λ0 and a-number=3−p-rank, avoiding the untwisted-matrix fallacy. Polynomial elimination shows only smooth rank1 coefficient pairs (0,0),(2,0),(−2,0), transverse reduced. The Möbius identity (z−1)^8+(z+1)^8=2(z8−2z6−2z²+1) in F5 plus z↦2z identifies all three over algebraic closure. Independent checked exact family expansion and marked-pair map from previous Howe theorem; inspected standalone symbolic and GF25 enumeration sources.

## originality

PASS

A stronger earlier theorem of 2026-11-02 completely determines the Hasse divisor and six reduced rank-one points for Howe form (x4−u x²+1)(x4−v x²+1). Substituting A=−(u+v), B=uv+2 maps exactly those six points in symmetric pairs to the three marked reciprocal points. Consequently **all rank-stratification and reducedness is prior coverage**, NOT a novel result. The previously inspected prior does not classify the three marked reciprocal presentations up to geometric curve isomorphism; the surviving specific new assertion is that all three lie in one geometric genus-three moduli class, proved by explicit Möbius transform. This is a narrowly limited best-of-knowledge PASS subject to the risk that a known automorphism normal form already implies the moduli collapse.

## value

PASS

Determining whether three natural marked rank-one Howe parameters give one or three geometric curves is an intrinsically motivated moduli classification. The exact equivalence has utility when comparing arithmetic coefficient strata to isomorphism-class enumerations; the already-known Hasse strata are not recredited. The distinctive value is small but specific and non-tautological, an explicit fractional-linear identification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
