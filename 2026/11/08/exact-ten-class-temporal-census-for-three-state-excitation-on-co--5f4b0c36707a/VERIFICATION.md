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

# Reproduction and limitations

The exact proof is the representative-state reduction and inclusion–exclusion coefficient identity documented in RESULT.md. The following independent runtime checks were actually executed:

- `python3 verification/quotient_certificate.py`: covers exactly all 343 possible triples of nonempty initial color supports. It checks ten class counts and the complete 27-term exponential coefficient basis by exact integer arithmetic. See `verification/quotient_output.txt`.
- `g++ -std=c++17 -O2 verification/direct_graph.cpp -o /tmp/ghm_tripartite_check && /tmp/ghm_tripartite_check`: constructs the original complete-tripartite adjacency and exhaustively evolves every one of 267894 labelled initial states over ten sizes; see `verification/direct_output.txt`.

The two implementations use distinct state representations and evolution logic. The finite direct-graph experiments do not constitute a proof for unbounded shore sizes: that deduction is made by the complete 343-mask symbolic analysis, since every full labelled initial condition is exactly represented by one history in this finite quotient, and the inclusion–exclusion expansion is exact for every positive size. Historical novelty cannot be formally proved from unsuccessful searches. No external independent audit or certification has been performed.
