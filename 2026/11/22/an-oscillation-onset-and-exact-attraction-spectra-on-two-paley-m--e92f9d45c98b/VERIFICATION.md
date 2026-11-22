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

# Finite census reproducibility

Run `sh run_checks.sh` in the directory containing all six supplied computational artifacts. It independently rebuilds the Paley-13 and Paley-17 adjacency lists and synchronous majority functional graphs with Python 3 and C++17, checks every possible input mask, compares all shared census summaries, checks finite population identities, and verifies the produced bytes match the included reference outputs. No external data, code dependencies, symbolic prover, or probabilistic sampling is involved.

The Python algorithm uses neighbour bit-mask generation from actual quadratic residues and Kahn indegree peeling to classify recurrent cycles and reverse-propagate attraction basins. The C++ algorithm uses modular exponentiation (Euler criterion), signed neighbour sums, and independent successor path tracing. The deterministic comparator checks agreement of every published common statistic, exact total population, attractor count and maximal depth. The run output was `PASS: Both independently generated graph, update, and orbit algorithms agree at every published statistic on both Paley graphs; exact mass and sharp-depth identities hold.`

Scope: exactly two labelled finite graphs with 8192 and 131072 possible initial states. The finite enumeration and correctness of its graph-theoretic decomposition constitute the proof; no assertion is made for larger graph sizes. Results are same-project cross-checks and are not independent external audit findings.
