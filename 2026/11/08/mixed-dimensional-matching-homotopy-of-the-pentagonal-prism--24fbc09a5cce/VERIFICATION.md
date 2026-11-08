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
# Reproducible verification

The enclosed `verify.py` uses Python 3's standard library only. It reconstructs the graph exactly as specified, independently enumerates all \(32768\) possible edge subsets, verifies the nonempty face vector \((15,75,145,95,11)\), computes all \(1020\) nonempty-face Hasse incidences, and constructs a deterministic \(168\)-pair matching. It checks the whole reversed-arrow Hasse graph is acyclic, determines critical dimensions \(0,2,2,3,3\), and evaluates the signed integral Morse chain differential. The computed \(2\times2\) differential is zero over \(\mathbb Z\).

Separate original-simplicial-complex homology reductions over \(\mathbb F_2\), \(\mathbb F_3\) and \(\mathbb F_5\) all yield reduced Betti ranks \((0,0,2,2,0)\) in dimensions zero through four. This is a cross-check, not the infinite proof. The integral homotopy conclusion follows from the complete acyclic discrete-Morse matching, the integral boundary, and Hurewicz on the simply connected Morse two-skeleton.

The expected stdout is embedded in `verification_results.txt`. Re-execution terminates with `ALL_VERIFY_OK` when all assertions succeed. No external audit or independent review is claimed.
