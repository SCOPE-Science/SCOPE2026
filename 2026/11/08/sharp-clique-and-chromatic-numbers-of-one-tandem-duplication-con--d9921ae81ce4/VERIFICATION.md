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

# Reproducible computational checks

The final included Python programs have no third-party dependencies. Run `python3 check_direct.py` to construct raw output sets and all confusable pairs from the original duplication operation; the program verifies the proposed coloring against every edge and the explicit lower-bound clique for each tested parameter triple. Run `python3 verify_components.py` for an independent combinatorial check of modular colorings and sharp cliques on every composition graph with \(1\le d\le8\), \(0\le B\le8\). Both programs passed, with terminal messages `VERIFY_DIRECT_OK` and `VERIFY_COMPOSITION_OK` respectively.

These checks inspect the actual packaged source files. Direct enumeration is finite and not substituted for the proof covering all \(q\ge2\), \(k\ge1\), and \(n\ge k\). Uninspected earlier literature could affect historical priority but not the stated computation. The accompanying correctness and originality assessment is a self-review only; independent validation has not been performed.
