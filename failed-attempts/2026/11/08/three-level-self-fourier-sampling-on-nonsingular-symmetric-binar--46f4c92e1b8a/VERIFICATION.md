---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Q(a,b,c)=ac−b² identifies the singular cone in F_q³. With J(u,v,w)=(w,−v,u), Q(Jy)=Q(y) and B_Q(x,Jy)=tr(XY); J permutes the cone and nonsingular complement. The complete odd-dimensional cone self-Fourier theorem at dimension three gives squared cone singulars q³ once,q² with multiplicity q²−q−1, q with multiplicity q. Complementary square blocks in the q^(−3/2) ambient unitary Fourier matrix have the cone spectrum plus q³−2q² extra q³ singular squares, yielding exactly the submitted formula. This also independently proves the submitted projection-conic Gram argument. Independent q=3 and q=5 Gram computations gave squares (3×3,9×5,27×10) and (5×5,25×19,125×76).

## originality

FAIL

FAILED: Published Resultary exact odd-dimensional quadratic zero-cone self-Fourier theorem (dimension three) has the exact cone spectrum; the isometric coordinate permutation J converts its polar pairing into this trace pairing. Unitary complementary-minor singular-value transfer yields every nonsingular-complement singular level/multiplicity. The entire final claim is an immediate corollary, despite different nouns and parameters.

## value

FAIL

FAILED: The submitted distinct matrix parametrization and conditioning formula are obtained mechanically by cone-preserving change of variables plus standard unitary complementary-submatrix spectrum transfer from an already published complete cone theorem. No independently motivated new classification or invariant remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
