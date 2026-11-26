---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Over the algebraic closure at u=infinity, the roots in v all have valuation -(d-1)/p. Proper factor constant terms would have nonintegral valuation, proving geometric irreducibility. The affine v-derivative is 1; the degree-d leading term leaves only [0:1:0] at infinity. For the lower edge between a^d and ab^alpha, take a=x^alpha y^r, b=x^beta y^s with alpha*s-beta*r=1. On the torus in y the strict equation at x=0 reduces to y=c, the leading coefficient of f, so one transverse point gives one branch with valuations (alpha,beta). For the second edge substitute a=b^p A, divide by b^beta and solve A+1=0 at b=0. Every positive branch valuation must tie on a lower edge. On the first branch the powers b^j for 0<=j<alpha have distinct valuation residues modulo alpha and form the Weierstrass basis over the a-series ring; the semigroup is therefore <alpha,beta>. The transverse smooth branch meets it with order alpha. The two tangents distinguish the branches over the prime field. The branch conductor in the union is the intrinsic conductor multiplied by the other branch equation, so each conductor order increases by alpha; this gives delta and the stated genus. As a separate canonical check, Euler's identity locally gives a G_a+b G_b=-b^beta on G=0, and du=b^(beta-2) db/G_a. At the cusp b has order beta prime to p and G_a has order alpha*beta since 1-d is nonzero in the field; at the smooth branch b is a parameter and G_a has order alpha. The resulting orders are (p-1)d-p and p-2, with no affine zeros or poles because u is étale there. The cited primary theorem applies over exactly the stated q; replacing two rational points by one gives the stated counts and zeta function. The frozen arithmetic script was inspected only: it checks finite support and arithmetic, not the branch theorem or maximality.

## originality

FAIL

A distinct, same-day indexed result proves the embedded branch, semigroup, contact, delta and conductor theorem for a broader family and explicitly includes the frozen maximal-curve specialization. Its exact branch valuations give the infinity hyperplane pullback, so the canonical coefficients are ordinary conductor adjunction. The zeta correction is also immediate from its rational branch identification and the cited maximality. This is demonstrable statement coverage and implication, not a finding about which same-day record came first.

## value

FAIL

The two-branch conductor description is meaningful in its own right but already present in the broader indexed result. After removing that overlap, the two explicit formulas left are immediate adjunction and point-identification consequences of known data. No substantively independent invariant or claim remains to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
