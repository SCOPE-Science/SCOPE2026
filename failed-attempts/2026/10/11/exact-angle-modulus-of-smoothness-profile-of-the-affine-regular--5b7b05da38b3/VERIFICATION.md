---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

PASS for the actual real two-dimensional norm N(s,t)=max(|s|,|t|,|s-t|), for each epsilon in [0,2]. Direct algebra shows R(s,t)=(s-t,s) and Q(s,t)=(t,s) permute the six signed facet forms and generate edge-transitive dihedral symmetry. The four unordered edge-separation types exhaust all pairs: same-edge pairs have N(x+y)=2 and distance <=1; adjacent edges x=(1,u),y=(v,v-1) yield d=1+u-v and s=max(2+u-d,2-u), sharply minimized at u=d/2, giving s=2-d/2 for d in [0,2]; next-nearest edges x=(1,u),y=(-q,-1) give d=1+max(u,q), s=2-u-q, yielding 4-2d for d in [1,2]; opposite-edge pairs have d=2. The branch intersection is 4/3, and both explicit attaining families lie on the unit sphere at all permitted parameters. This proves m_H(d)=min(2-d/2,4-2d) with the next-nearest branch infeasible below 1, equivalent to the displayed piecewise law; squaring gives rho^a=1-m_H^2/2, with rho^a(1)=-1/8 and rho^a(4/3)=1/9. Independent LP cross-check enumerated all 36 ordered edge pairs times 6 active signed distance facets at each of 11 rational separations (2376 finite LP subproblems), agreeing to reported floating precision. This corroborates rather than proves the continuum theorem. Equivalently, the entire formula is independently supported by the exact 2009 Baronti-Papini Example 1; see originality.

## originality

FAIL

FAIL: decisive exact prior coverage was found in Baronti and Papini, "Convexity, smoothness and moduli", Nonlinear Analysis 70 (2009), 2457-2465, Example 1 and Eq. (8.5). Its norm is explicitly max(|s|,|t|) when st>=0 and |s|+|t| when st<0, which is identically max(|s|,|t|,|s-t|) for ALL real s,t. It determines the Banaś fixed-chord modulus rho_B(epsilon)=max(epsilon/4,epsilon-1) on [0,2] and provides both sharp witness families, with the same edge-class transition at epsilon=4/3. The 2022 Du-Ahmad-Din-Li primary paper, Proposition 7, proves rho_X^a(epsilon)=1-2(1-rho_B(epsilon))^2, so the candidate is an exact algebraic substitution: m_H=2(1-rho_B)=min(2-epsilon/2,4-2epsilon); the quadratic branches and diagnostic values follow immediately. The prior 2009 x,y witnesses already realize adjacent and next-nearest edge pair classes. This mathematical implication settles originality negatively, not merely a textual coincidence or absence of newer searches.

## value

FAIL

FAIL as an independent new scientific contribution. The hexagonal plane and Banaś/angle modulus are well motivated, and the formula is useful, but precisely this entire invariant and both optimizer families were calculated for the identical norm in Baronti-Papini (2009), Eq. (8.5), Example 1. The 2022 Proposition 7 changes its normalization by a monotone quadratic function; the breakpoint and chord-type switch are immediate from the two already published sharp constructions. The candidate does not classify all minimizers or establish a new generalization or unknown exact fact beyond this substitution. Known-table recomputation and a renaming cannot pass the requested independent mathematical-value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
