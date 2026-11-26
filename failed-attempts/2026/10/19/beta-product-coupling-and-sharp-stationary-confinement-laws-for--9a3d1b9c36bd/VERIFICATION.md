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

PASS

The displayed mathematical claims check out; the frozen proof and verification narrative have two specific errors noted below. The two-sided linear-filter solution of the irreducible chain is stationary with |Z|≤1; the exponentially damped initial term tends to zero in probability in any stationary solution, giving uniqueness. For n≥1 the generator equations give m_n=C_{n-1} and C_n=n A_{n-1}/(n+R), with A_j=(j+T)m_j/(j+R+T) also at j=0. These give the displayed compact-support moment recurrence and the Beta(T/2,R/2) times Beta(1/2,R/2) square law. The two U densities have ratio proportional to u^{(T_2-T_1)/2}(1-u)^{(R_2-R_1)/2}, strictly decreasing throughout (0,1); the V densities are weakly ordered in the same direction. Conditioning the product tail on v>x² yields strict comparison for all interior x since the V densities are positive. The quantile and strictly increasing cost claims follow. For the density write a=T/2, c=R/2, t=x², D=B(a,c)B(1/2,c). For 0<|x|<1 the product integral is D^{-1} I_{a-1/2}(t), where I_p(t)=∫_t^1 u^{p-1}(1-u)^{c-1}(1-t/u)^{c-1}du. For p>0 split at 2t; the lower interval is O(t^p), and dominated convergence on the rest gives B(p,c). The substitution u=t/y gives I_p=t^p I_{-p}; for p=0 the middle interval [2t,1/2] gives log(1/t)+O(1) and both ends are O(1). At t→1 the substitution u=t+(1-t)s factors out (1-t)^{2c-1}, with remaining integral tending to B(c,c). These yield exactly the displayed constants and transitions, and c=1 reduces the same integral to an elementary power or logarithm. In the frozen proof line 71 the intermediate formula expressed as E|Y|^{-T}/B(T/2,c) omits a factor of two, though the displayed central coefficient is correct. The frozen script's 24 rate entries give 576 iterations but only 21 distinct rates and 441 distinct ordered pairs; the reported 37,096 assertion count is consistent with repetitions, not the distinct-pair claim. The frozen script was inspected, not executed.

## originality

FAIL

The fixed-rate stationary law was already given by an exact characteristic function and hypergeometric density. More decisively, a distinct indexed result gives the same independent-beta representation and strict all-threshold ordering in both rate coordinates, as consequences of a result for the stationary position–motility joint law. The simultaneous partial order and rate-budget consequence follow by chaining the coordinate comparisons. The density coefficients and elementary line follow directly from the already known density by standard endpoint formulas. The close indexed overlap is later-dated, so this is a conclusion about coverage, not prior authorship, dates of derivation or dependence.

## value

FAIL

A strict all-threshold confinement order is useful, but this exact ordering and factorization are already supplied by a matching stronger joint-law result. What remains is the Gauss endpoint expansion of a known density and its elementary c=1 specialization; this does not warrant a separate finding. Correcting the intermediate factor and clarifying the finite test counts would improve exposition but would not produce a substantive repaired claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
