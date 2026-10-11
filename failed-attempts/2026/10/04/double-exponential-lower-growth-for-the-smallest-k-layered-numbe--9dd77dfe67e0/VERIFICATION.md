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

Jokar’s necessary condition gives k <= sigma(L_k)/L_k. Grönwall’s maximal-order theorem gives sigma(n)/n <= (e^gamma+epsilon) log log n eventually. Along unbounded admissible k, L_k must tend to infinity because any fixed finite set of integers has bounded abundancy index. Combining and passing to the liminf yields the constant e^{-gamma}; the explicit double-exponential form follows by choosing epsilon to match any requested loss and exponentiating twice. No finite table is used.

## originality

FAIL

The quantitative claim is already implication-level covered by two pre-existing statements: Jokar’s published necessary inequality for every k-layered number and Grönwall’s classical maximal-order theorem. The entire proof is their direct asymptotic combination, so absence of the exact displayed liminf in the k-layered paper does not make the result original under the audit implication rule.

## value

PASS

Although not original, the consequence is mathematically informative: it exposes that any existing least k-layered representatives obey a far stronger lower-growth constraint than the source’s informal exponential phrasing. The rejection is originality, not lack of relevance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
