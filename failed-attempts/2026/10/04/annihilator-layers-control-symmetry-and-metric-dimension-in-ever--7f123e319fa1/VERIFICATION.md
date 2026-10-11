---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The chain-ring valuation decomposition gives \(|V_i|=(q-1)q^{\ell-i-1}\) and adjacency exactly when \(i+j\ge\ell\). In the simple graph, degrees are \(q^i-1\) or \(q^i-2\) according to whether self-annihilation occurs, and these degrees strictly separate layers. Hence every layer permutation is independent and all automorphisms are their product. Twin classes force all but one vertex per layer in determining/resolving sets; the proposed witness in \(V_{\ell-j}\) distinguishes omitted representatives from distinct layers. The \(\ell=2\) boundary agrees with the complete-graph formula.

## originality

FAIL

Rattanakangwanwong--Meemark already prove for arbitrary finite chain rings that the unit orbits are exactly \(R^\times\theta^i\), give their sizes \((q-1)q^{\ell-i-1}\), and prove the orbit-level adjacency threshold \(i+j\ge\ell\); their reduction graph is therefore the same valuation-layer blow-up, up to the paper's loop convention. Once this complete graph structure is known, the product automorphism group and determining number follow immediately from distinct layers and twins, while the metric-dimension upper witness is a short routine check. Sabeel--Paramasivam independently show the same twin/generalized-join method for \(\mathbb Z_n\). Under the implication-based originality rule, the combined final claim is covered/routine from prior exact structure even though the particular formula package was not printed together.

## value

FAIL

After the 2021 arbitrary-chain-ring reduction graph is taken as known, the remaining automorphism and resolving calculations are short standard consequences of complete/empty twin layers. Packaging them is useful exposition, but under the stated value bar it is a routine deduction rather than a distinct motivated mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
