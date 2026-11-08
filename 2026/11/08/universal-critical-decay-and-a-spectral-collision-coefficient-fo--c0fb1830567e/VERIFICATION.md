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

# Reproduction and evidence boundaries

Execute `python3 checker.py` with Python 3, using no nonstandard modules or external files. The program independently computes the Perron vector of each small graph, evaluates the quadratic collision sum directly, and compares it against the closed spectral expression. It also compares the full product map to its second-order expansion at small amplitude and numerically observes the large-time asymptotic on five illustrative networks.

The finite verification consists of 3,084 connected labelled-graph/recovery-parameter comparisons for graphs on 2–5 vertices, and five separate critical-orbit calculations of length 100,000. Floating-point tolerances and iteration limits are explicitly present in the script; this is computational corroboration rather than a proof over all finite networks. The complete analytic justification is in `RESULT.md`, especially the decay, alignment and Taylor-coefficient steps. Independent mathematical audit or certification has not been performed. No real-world epidemic observations or stochastic Markov-chain experiments are claimed.
