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

Every non-hub open neighborhood is a clique, so it meets the parity rule automatically in a proper coloring. At the hub the number of occurrences of a peripheral color equals its blade incidence count. On a fixed k-set of peripheral names the polynomial (product_i s_i!) times product_i e_{s_i} tracks these counts. Averaging over signs multiplied by their product projects onto exponents odd in every coordinate, hence onto colorings using all k names. Grouping signs by j negative coordinates yields K_{k,s_i}(j); choosing the hub and the used peripheral names gives (1). The upper summation limit can equivalently be S because binom(q−1,k)=0 for larger k at positive integer q. For odd t, s peripheral colors work and a blade requires s. For even t, the number k of peripheral colors is even and k(t−1)≥ts. The least qualifying even k also satisfies k≤ts, so distribute ts−k in increments of two over k initial unit column sums without exceeding t−1. These column sums can be realized by placing each column's ones in consecutive rows cyclically starting where the previous column ended, yielding s entries per row since there are ts placements. This also checks t=2, when each color can occur only once. Direct replay agrees with the signed formula on 4,046,901 hub-normalized proper assignments across 54 comparisons and verifies 570 uniform constructions.

## originality

FAIL

The strongest indexed windmill results state the same uniform optimum and the same sign-filter count on the optimal palette. Their proofs already supply the parity-incidence criterion and the parity indicator before summing over the chosen blade subsets. Neither prints the arbitrary-size arbitrary-palette formula. However, their exact indicator applies regardless of subset sizes: summing independently with sizes s_i replaces the common factor E_s^t by the product of E_{s_i}, and summing over the actually used k-set introduces binom(q−1,k). These two immediate counting operations exhaust the claimed extension; no new incidence constraint or counting argument is needed. The failure is proof-level mechanical coverage, not an assertion of an identical formula in the comparator or of historical priority.

## value

FAIL

A named-palette enumeration on arbitrary bouquets is a natural question. Here the all-palette display is obtained by row-wise substitution in the explicitly available incidence projector and grouping by support; the separate uniform scalar is already stated. The frozen extension provides no further structural classification, nontrivial evaluation, or independently useful unknown exact fact beyond this direct calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
