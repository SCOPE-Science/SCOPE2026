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
# Reproducibility and limits

Execute `python3 verify.py` using Python 3. No third-party packages are required. It independently enumerates every edge subset in four distinct cactus graph topologies, computes exact rational random-cluster weights from connected component counts, and evaluates all mixed cumulants with the Möbius set-partition formula rather than using the theorem's generating-function proof. Six rational cluster weights are tested at each graph; 2,154 exact-rational comparisons, including zero cumulants between blocks, succeed. Additional exact tests check Eulerian polynomials of orders 2–5 and two-/three-reversal sign witnesses. Expected output: `CYCLE_BLOCK_CUMULANTS_EXACT_OK 2154 polynomial_orders_2_to_5 cycle4_signs [1, -1, 1] cycle5_signs [1, -1, 1, -1]`.

Finite enumeration does not prove an infinite-family statement. The proof in `RESULT.md` establishes the all-order formulas using graph cyclomatic rank, exact moment-generating functions, differentiation and polynomial interlacing. The output does not certify historical novelty, generalizations beyond cactus graphs, or any independent external audit.
