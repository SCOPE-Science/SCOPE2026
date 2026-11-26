---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For z on the unit circle, λ3 is the common root of Q(t,z) and Q(t+d,z), since Q(λ3+d,z)=Q(λ2,z)=0. This is the intended substitution in line 53: λ3+d is a root of the unshifted polynomial, not the shifted one as the wording suggests. The resultant vanishes identically as a Laurent polynomial. On a pole-free arc every specialized gcd root r is a real eigenvalue and r+d is also an eigenvalue; the ordered list of four and empty middle interval imply r∈{λ3−d,λ3,λ3+d}, also with repetitions. Its root mean has a constant offset from λ3 on the arc, so subtracting that offset gives a rational branch a satisfying both unshifted evaluations Q(a,z)=Q(a+d,z)=0 identically. Monicity over the integrally closed Laurent ring removes nonzero finite poles; the characteristic coefficient bounds on Laurent exponents then force a to have exponents −1,0,1 only. Equality a=λ3 propagates globally by continuity: near an equality point any nonzero difference of magnitude less than d/2 puts either a or a+d in the empty middle interval. Antipodal symmetry fixes the constant term −d/2, reality pairs the Laurent coefficients, and the values along the two coordinate directions fix the center uniquely. Li–Sze then gives the disk by intersection of supporting half-planes. In a homogeneous direction (x,y) the candidate quadratic has two distinct roots for (x,y)≠(0,0), both pencil eigenvalues; the polynomial remainder after monic division vanishes at both, hence is identically zero. Nothing requires spectral simplicity.

## originality

PASS

The distinct theorem is recovery of the two ordered middle branches of an arbitrary size-four pencil from a constant raw separation. The known half-plane representation and Jiang's resultant technique are inputs, and the two-block disk example is not credited as new.

## value

PASS

Size four is the first nontrivial middle pair for rank two. The result locates a sharp regime where a raw spectral width, which need not be the width of the compression range, actually forces a disk and a determinant factor. The proof identifies why a dimension-four relation survives the extra spectral pairs that invalidate a direct transplant of the extreme-gap argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
