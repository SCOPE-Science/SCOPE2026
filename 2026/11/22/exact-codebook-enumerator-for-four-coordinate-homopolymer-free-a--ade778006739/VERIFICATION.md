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

At most one swap preserves the multiset, and the adjacency constraint precludes any letter occurring three or four times. Multiplicities 2+2, 2+1+1 and 1+1+1+1 have counts binom(q,2), q binom(q-1,2) and binom(q,4), respectively. Relabeling preserves ball intersections, so codebooks are independent choices in the corresponding components; the global polynomial multiplies their independence polynomials with no ordering factor. The independent script /workspace/replay/1/independent_check.py (results in independent_results.json in the same directory) rebuilt the full output sets including forbidden-as-sources words, and counted coefficients (1,2), (1,6,4) and (1,24,180,472,366,48); no size-six set exists in the last component, excluding all larger sizes by heredity. The degree and leading coefficient therefore give the stated maximum size and number of maxima, including (35,51539607552) at q=4. LP constraints split by the same multisets. For aabb the common output abba bounds the optimum by one; for aabc outputs abca and caab cover all centers, while abac and acab give a two-center packing; for abcd uniform primal and dual weights 1/4 are feasible by four-regular incidence in both directions, giving six. The component optima sum to P_q=q^2(q-1)^2/4, so the gap is binom(q,4), and the leading coefficients of P_q and M_q give 6/5. The finite enumeration is decisive for all q only because the exact symbolic decomposition reduces all q to those three component types.

## originality

PASS

The supported distinct claim is the full labeled source-constrained length-four codebook enumerator, including the distribution by size and count of maxima across multiplicities. The distinct-symbol maximum is known; the distinction between six fractional and five integral in that regular component is a direct consequence of the known optimum and ball incidence. Neither that fact nor the superficially similar exact capacity for a different channel covers the full enumerator. The gap in the full model is a verified consequence, not evidence of priority by itself.

## value

PASS

Four is the first length allowing two disjoint swaps, so the precise distinction from the nearby channel matters. Full packing counts in the source-only constrained channel answer a different question from capacity and give the number of optimal choices across arbitrary alphabet sizes. The decomposition turns one small but nontrivial component enumeration into a complete family, giving an exact benchmark and identifying precisely where the output-incidence relaxation is not integral in objective value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
