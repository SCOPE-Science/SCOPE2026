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

For real scalars a,b I independently expanded the binomials (a+tau b)^6+(tau a-b)^6 and reduced the proposed remainder to (L^2-A L-B^2/4)(a^2+b^2)a^2 b^2/L, exactly zero by the stated positive-root equation. L>0 for tau>0; integrating the nonnegative identity gives the sharp upper estimate. The two null slopes of a^2-b^2-gamma ab are real and have product -1, and independent sixth-power mass conditions lead to the stated 1/(1+s^6), s^6/(1+s^6) branch masses when tau!=1. Disjointly supported normalized functions implement both branches on any real L6 with dimension>=2. Involution T_tau^2=(1+tau^2)I transfers the upper identity to the exact lower deficit and yields the reciprocal endpoints. Orthogonally diagonalizing the trace-zero quadratic form proves the squared-distance cone bound and shows pointwise coefficient optimal at its eigenvectors. Tau=1 and tau=0 special cases are handled separately. Independent SymPy algebra and tau=1/2,1,2 radical values corroborate the source checker.

## originality

PASS

Best-of-knowledge PASS for a sextic-specific explicit radical, complete sextic equality-set classification and nonnegative exact deficit identities. The strongest 2026 Xu–Liu primary paper was materially read in full text (not merely its abstract): Theorem 3.2 gives the all-p reduction to a 2x2 operator norm and one-variable supremum, with p=1,2,infinity and tau=1 special values, but no p=6 exact polynomial or two-ray quantitative remainder. The published p=4 two-ray deficit does not logically give the sextic polynomial or coefficient. The general reduction/product identity are credited as already known.

## value

PASS

Exact optimal constants for a natural power-mean Banach-space invariant are meaningful, and the stronger sixth-degree nonnegative polynomial identity classifies every extremizer and gives global stability to two orthogonal rays. It supplies mathematical information genuinely absent from the generic all-p variational reduction and from the previously known quartic factorization. This is a motivated exact structural fact, not a numerical bound or a trivial reparameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
