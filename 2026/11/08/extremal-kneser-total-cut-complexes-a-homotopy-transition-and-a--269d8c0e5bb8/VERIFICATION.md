---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

Kneser KG(n,k), k>=2, n>=2k, m=binom(n−1,k−1). Equality in Erdős–Ko–Rado gives, for n>2k, exactly the n maximum independent stars. Complementary simplices D_i intersect in a nonempty simplex precisely for |T|<=n−k, giving nerve sk_{n−k−1}Δ^{n−1}, homotopy wedge^m S^{n−k−1}. The equivariant Čech double complex identifies integral top homology with the kernel of simplicial boundary on that skeleton, i.e. ∧^{n−k}U_n; over Q this is hook (k,1^{n−k}). At n=2k the Kneser graph is m disjoint complementary edges and the cut complex is a cross-polytope boundary S^{m−1}. The degree of a transposition is (-1)^{binom(2k−2,k−1)/2}; central-binomial 2-adic valuation s2(k−1) makes it −1 exactly if k−1 is a 2-power. An independent permutation-pair sign computation for k=2..10 matched this parity and the trace formula; no finite test is used to establish the all-k theorem.

## originality

PASS

Statement-level and mathematical-object comparisons with the inspected primary/published results identified no previous theorem determining the claim's precise new invariant. Negative indexed searches are not absolute novelty proof.  Prior work is credited separately for ingredients and any directly implied subclaims.

## value

PASS

The maximum independent-set cut parameter is intrinsic and marks the last nonvoid total-cut level. The two sharply different topological regimes (n=2k versus n>2k), complete integral equivariant top module, and unexpected power-of-two orientation sign boundary are motivated exact structural properties of the natural Kneser family, not a merely arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
