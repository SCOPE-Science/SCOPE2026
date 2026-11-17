---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Summing even modulations (p=N/2 channels) forces frame-operator couplings only between antipodal j,j+p, with Hermitian blocks diag 3/2 and off-diagonal σ_j/2, yielding the exact 3/2±|σ_j|/2 spectrum. Tight iff σ_j=z_j+z_(j−s)+z_(j−2s)=0, where |z_j|=1 and z_(j+p)=conj z_j. Along an s-cycle of length ell the zero-sum recurrence enforces w_t=w_(t−3), so 3|ell and unit triples must be equilateral. If ell even, antipodal offset is (ell/2)s, a multiple of three steps, forcing z=conj z, impossible for three real unit numbers summing to zero. For ell odd multiple three, addition p pairs the d=N/ell cosets and allows exactly two orientations with arbitrary phase u per pair. A q-phase window exists iff 3|q, with q choices of u and 2 orientations for each d/2 coset pair, plus q^p independent antipodal lifts: q^p(2q)^(d/2). Independently exhaustively enumerated q-phase triples at (N,s,q)=(6,2,3),(6,2,6),(6,1,3),(10,2,3), obtaining 162,2592,0,0 respectively; infinite classification rests on the recurrence proof.

## originality

PASS

Best-of-knowledge PASS for this noncritical three-translation, even-modulation subgroup and its arithmetic step-order obstruction and exact phase-alphabet windows. Asipchuk--De Carli--Rodriguez general subgroup block equivalence supplies a reduction but not the cubic-root recurrence, half-period incompatibility or exact q-phase count; Magsino gives broad ambiguity-function tightness/CAZAC criteria without this classification. A nearby published SCOPE three-translation Gabor basis instead uses modulations divisible by three, N=3M and critical orthonormality, not the present p=N/2 modulation channels and 3p/N=3/2 overcomplete frame.

## value

PASS

It classifies the natural smallest nontrivial odd-size arithmetic-progression translation pattern under a codimension-two modulation subgroup, including the sharp spectral blocks, existence obstruction and exact finite-alphabet design count; the 3 mod 6 dichotomy offers concrete frame design beyond a generic tightness test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
