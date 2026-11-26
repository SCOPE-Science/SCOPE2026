---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

FAIL

The frozen error definition in RESULT.md line 39 subtracts a normalized predictor from raw f(x). The unit vector satisfies ⟨f,k_x⟩=e^(−x²/2) f(x), not f(x). At x=L and f≡1 (unit Fock norm), Πk_L=k_L, so the frozen error is 1−e^(−L²/2)>0, but P_L(L)=0. The optimal raw-evaluation recovery error instead is e^(x²/2)P_L(x); even with the predictor properly scaled it cannot have a maximum at the midpoint, since there P_L>0 and P'_L=0 and the derivative of the raw error is positive. The normalized error, exact Gram determinant maximum and spectra in the record are mathematically sound. In the Schur complement the anchor determinant is 1−q⁴ and the midpoint determinant is (1−q)³(1+q). For the auxiliary midpoint inequality, F'_a(u) has the sign of A(u)−a, and A strictly increases since sinh(su)/sinh(u) strictly decreases for 0<s<1. Thus F_a has no interior maximum and F_a(a)=e^(−a)>F_a(0). The resulting strict monotonicity gives the stated midpoint determinant. The antisymmetric eigenvalue is 1−q² and the other two come from the symmetric 2×2 block, whose discriminant is q⁴+8q. In the collision the first perturbation compressed to the orthogonal complement of the ones vector is (Pt)(Pt)ᵀ, t=(0,a,1)ᵀ, P the orthogonal projection. Its nonzero eigenvalue is 2(a²−a+1)/3. Expanding the Gram determinant by Gaussian monomial features gives leading term a²(1−a)²L⁶/2 from the first three monomials; dividing by the two larger eigenvalues gives the stated smaller one. The factor 144 is for κ₂(G), the Gram ratio, not its square (the ratio is the squared sampling-map condition number).

## originality

FAIL

Even after correcting the normalization, the determinant optimum follows from known Gaussian heat-kernel log-concavity in an ordered chamber and the Karlin–McGregor determinant identity, by restricting to the diagonal, taking a symmetric one-dimensional slice and ruling out a constant analytic segment. This is a direct implication, not a claim that the exact displayed formula was printed in the sources. The flat-limit spectral law, including its a-dependent coefficients, is a direct case of Barthelmé–Usevich. The midpoint exact value and finite-distance spectrum require only evaluating a 3×3 determinant and a symmetry block at the already determined midpoint. Failure is supported by these implications, not by an unavailable paper or unsuccessful search.

## value

FAIL

The normalized maximum uncertainty and the loss of conditioning during collision are natural quantities, but the correct mathematical remainder consists of an exact convex-domain heat-kernel specialization and a known flat-limit specialization. The record supplies a self-contained elementary calculation but no substantive additional invariant or mechanism beyond those implications. Repairing just the evaluation convention would make the main formula correct in scope, not establish a new valuable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
