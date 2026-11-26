---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Uniformity follows because each flag A⊆K with dim A=r and dim K=n−r gives exactly |GL_r(F_q)| maps by isomorphisms V/K→A. For a fixed a-plane in an N-space the count of d-planes meeting it in x dimensions is G(a,x)G(N−a,d−x)q^((a−x)(d−x)), by choosing the intersection, the projected plane and its lift. This gives W_j for the two images. Given the images, the independent quotient kernels meet the other projected image with the stated H distributions, and these laws depend only on j, so conditioning on j preserves independence. Subtraction of the intersection dimension from the respective input-image dimension gives the two ordered ranks, including the zero-rank shells. At r=s=m the gap is at most min(d,m−j), d=n−2m. With disjoint images one kernel extension can be arranged to meet the other image in min(d,m) and the other kernel extension can be a complement. In dimension 2m+1 each kernel extension is a line, giving the stated independent Bernoulli indicators. In this regime W_j=q^(−j(j+1)) Q_m²Q_{m+1}²/(Q_{2m+1}Q_jQ_{j+1}Q_{m−j}²); the Q factors are bounded below by Q_∞>0. Dominated convergence and Q_{j+1}=Q_j(1−q^(−j−1)) give exactly the positive series reported. Pairwise disagreement does not imply unequal marginals, which are equal by exchangeability.

## originality

FAIL

The earlier Resultary record 442e4aaba275 already counts precisely these joint fibers, with complete support and the sharp gap for even unequal input ranks. The conditional-independent presentation is useful but re-expresses the same flag count. The odd-dimensional probability and Euler-series evaluation are not stated there verbatim, but reduce directly to single terms of the earlier sum and the standard rectangular matrix rank limit. No distinct substantial claim remains to repair.

## value

PASS

As a scientific problem, the full joint distribution retains dependence information lost by marginal laws, and the parity distinction separates deterministic rank rigidity from persistent disagreement. These are natural structural questions. The existing coverage and direct implication mean the frozen solution does not supply a new result on those questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
