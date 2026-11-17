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

For a degree d irreducible plane curve other than the conic with multiplicities m_i, Bézout gives Σ m_i<=2d and genus gives Σ m_i(m_i−1)<=(d−1)(d−2), hence strict self-intersection >=d−2>=0 for d>=2. Only exceptional E_i, secants L_ij (-1), and Q (4−n) are negative. Distinct selected −1 curves must be disjoint, hence secant edges pairwise intersect and avoid selected exceptional labels. Such edge families are stars (with singleton multiplicities corrected) or triangles; T_m=1+m[(1+t)^{m−1}−1]−binom(m,2)t+binom(m,3)t³. With Q, Schur complement against selected E gives −(n−4)+|E|<0, equivalently m>=5. BFN converts support classification to chambers. Since −K=H+Q is big and Q²<=−3, Bauer–Schmitz theorem gives infinite volumes exactly for Q supports. Independently reconstructed n=6 boundary total 1898 with 648 Q supports and n=7 finite 4671, infinite 3396, total 8067. All-n follows from Bézout/genus/Schur and star-triangle arguments, not finite tests.

## originality

PASS

Best-of-knowledge distinct principal theorem after comparison of actual pinned mathematics, equivalent formulations, stronger claims, exact tables and logical implications; do not construe source searches or inaccessible literature as proof of historical novelty.

## value

PASS

A complete natural geometric family with finite chamber count even at unbounded Picard number, all support sizes, and sharp finite/infinite volume partition is intrinsically useful. It extends beyond a known six-point special case and gives an exact general invariant, not just a generic algorithm execution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
