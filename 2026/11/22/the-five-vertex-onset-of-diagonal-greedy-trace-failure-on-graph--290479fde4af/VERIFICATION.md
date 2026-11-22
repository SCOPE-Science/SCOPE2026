---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction record

Execute `python3 green_kernel_checker.py` from the extracted package using Python 3 (standard library only). The checker enumerates \(2^{\binom n2}\) labelled graphs for each \(n\in\{2,3,4,5\}\), filters connected cases, performs exact rational Gauss–Jordan inversion, checks all two-element subsets, and branches over every maximizing greedy tie. The completed certificate printed connected counts `[1, 4, 38, 728]`, failing counts `[0, 0, 0, 60]`, and exact witness trace values `37/39` versus `22/23`, regret `7/897` and ratio `858/851`.

All cases covered by the finite theorem are enumerated, not just representatives or randomly sampled graphs. Arithmetic is exact; there are no floating-point thresholds. The certificate does not address arbitrary weighted graphs, graph orders above five, or other diagonal regularization strengths. No independent audit has been performed.
