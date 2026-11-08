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

# Verification methods and limits

The proof uses an exact structural characterization of total restrained dominating sets and a bijection from multi-block coalition partitions to partitions of the set of triangle blades. No nonstandard analytic identities or numerical approximations are required. The two-block count follows by subtracting the exact number of apex-containing TRD-sets from all apex-containing subsets. The Stirling counts use the definition of unordered set partitions; the total count uses the standard identity relating Stirling and Bell numbers.

The standalone `verify.py` separately constructs the graph, computes the TRD predicate directly from every vertex's adjacency, and exhaustively generates partitions of the labelled vertex set for \(1\le m\le5\). It checks each coalition graph's edge set and compares all counts to the claimed formulas. The local replay ended in `VERIFY_OK`. This does not exhaust graphs of larger order and is not a substitute for the all-orders argument or an independent mathematical audit.
