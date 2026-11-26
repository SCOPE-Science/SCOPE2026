---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

In the row-sum Laplacian convention, replacing an ordinary edge by −a subtracts (1+a)ddᵀ with d=e_u−e_v. Side exchange and permutation of the m−1 ordinary vertices give the stated two symmetric 2×2 blocks and mI on the residual space. The antisymmetric block has determinant 2[m²−(1+a)(2m−1)], nonzero off-diagonal √(m−1), and a lower diagonal entry 2m−1>m, so λ_-<m<λ_+ and λ_->0 exactly in the claimed stable range for a>0. The spectral projector entry w and the even block give the four-term F. Its derivative scaled by 2e^(mt) is strictly convex, starts negative and diverges to +∞; hence F falls from zero and then rises to 1/(2m), with one positive root. At criticality the positive contribution to F' decays faster than the negative term and is already smaller at zero. Beyond criticality Duhamel and oddness of d give ∂_aF<0: the factors have opposite signs since dᵀH(s)d>0 even if L is indefinite. The other entries were checked by orbit: the same-side endpoint entry uses the Laplace numerator 2(m−1−a)s+λ_-λ_+, whose terms invert to positive exponential convolutions; the opposite-side endpoint entry is a sum of positive terms. The ordinary crossing entry uses slow weight ρ≤1/m and λ_-<m<λ_+, making the odd-block qq term strictly smaller than the even one. Ordinary same-side entries increase from the connected unperturbed kernel at 1+a=0 by the qq Duhamel formula, and this orbit is empty when m=2. Symmetry and row sums now give the exact two induced norms while stable. At small a, the first surviving path term at a=0 is (m−1)²t³/6, so taking t=k√a on either side of k=√6/(m−1) brackets the unique crossing. At the other end strict critical negativity at each fixed t implies T→∞; the small eigenvalue has slope 2w_c in a_c−a by the antisymmetric eigenprojector, and dropping the decaying fast terms gives λ_-T→log(mw_c)>0. Replay is RESULT.md §§1–4; VERIFICATION.md and check_signed.py were inspected, not executed. The sampled checks are supplementary. Entrywise positivity is strict only after T, whereas nonnegativity holds at T; the symmetric matrix exponential is positive definite even when individual entries are negative.

## originality

PASS

Credit existing signed-Laplacian stability/eventual positivity and the structural analogues in the triangle and fractional complete-network results. The distinct contribution is the full square-biclique heat-entry classification and exact recovery profile, in particular the three-decay-mode equation with its biclique coefficients and square-root weak-edge delay. The induced norm formula follows generically once the entry census is known and is not independently novel as a norm identity. No inspected separate statement implies the full square-biclique result. The closest unresolved bibliographic hit on signed complete bipartite spectra was not available in full and is retained as a risk, not assessed as non-covering from a snippet.

## value

PASS

The natural single-repulsive-edge model separates spectral stability from positivity at finite times. A complete entry census on an infinite graph family, a unique sharp first horizon, and two distinct scales quantify the negative transient. In particular the shortest alternative path causes a square-root onset, whereas a nearly persistent odd mode causes inverse-distance divergence; neither feature is supplied by an eventual-positivity existence statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
