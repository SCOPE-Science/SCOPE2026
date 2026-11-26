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

Off a marginal-null set, write x=t+jr with 0<t<r and let S be the levels j=k-1 mod k. Every successful tuple has exactly one coordinate in S, so its probability is at most E[sum_a 1_S(U_a)]=k|S|, without assuming exchangeability. The fibers have N(t)=m+1 for t<s and m for t>s, so |S|=s floor((m+1)/k)+(r-s)floor(m/k). Rotating a uniform seed by a-1 within every complete disjoint k-block and fixing leftovers gives a measurable Lebesgue-preserving map for coordinate a; precisely the complete-block seeds succeed. This attains the bound and reduces to the stated formula. The deficit is the integral of N(t) mod k and vanishes iff s=0 and k divides m (ell>=2 in the open range). The three k=3 examples check exactly. Separate finite replay: 70 labelled-marginal LPs on rational grids, allowing every label permutation of each progression and diagonal failures, match to 1e-8. The analytic certificate treats all real gaps.

## originality

PASS

The distinct claim is the all-k attained subcritical exact-progression capacity for k>=3, not pair displacement, minimum separation or the general chain integrality argument. No statement inspected supplies this claim. The nearest comparisons provide substantial precedents in objective or method, and priority is provisional.

## value

PASS

Exact spacing is a natural sharp dependence-uncertainty event that neither independence (zero) nor subcritical hard-core separation (capacity one) resolves. An attained expression for arbitrary real gaps shows full-capacity resonances and intervening strict deficits, and makes the qualitative nonmonotonicity precise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
