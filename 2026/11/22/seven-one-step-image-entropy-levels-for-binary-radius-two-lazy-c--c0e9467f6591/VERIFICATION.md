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

# Verification record

Run `python3 verify.py` with SymPy and compile/run the independent `verify_direct.c` with a C99 compiler, supplying `word_counts.csv`. Both procedures were executed successfully against the included exact catalogs.

The Python verifier builds the complete sixteen-state labeled input graph for each of sixteen center-zero active rules, determinizes the graph, constructs its reachable subset adjacency matrix, computes integer characteristic polynomials, and applies exact Sturm counts to isolate the Perron eigenvalue in the cataloged rational interval. It checks the claimed class polynomial divisor, the common fixed-SFT Perron polynomial for the six non-idempotent cases, all nine-input idempotence tests, class populations, and 160 direct-image language counts. The independent C99 implementation directly enumerates 176 output word counts for lengths zero through ten and all sixteen rules without using the subset automata. Complementing input and output yields the remaining sixteen rules.

**Limits:** The direct-word counts have bounded length; the infinite-length claims instead follow from the exact labeled-path identity and finite matrix growth. Root certification requires the Python/SymPy exact-arithmetic verifier; the C program is an independent finite-word consistency check only. The claim is confined to one-step image entropy and spatial fixed-subshift entropy of full bilateral binary shifts. Literature searches and inspections do not establish absolute historical priority. No independent mathematical audit has been performed.
