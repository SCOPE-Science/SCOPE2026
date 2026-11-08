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

# Reproducibility and verification

The bundled standalone Python script `checks/graph_width_checker.py` executes with Python 3 and no third-party packages. Run `python checks/graph_width_checker.py` from the package root.

It reproducibly constructs 810 small perfect graphs from five separate structural families, computes chromatic numbers and maximum cliques by exhaustive enumeration, and evaluates support widths directly from all stable-set indicator vectors. It checks 23,936 nonzero directions against the theorem's lower bound, all 2,391 maximum-clique contacts, and 7,284 qualifying stability-bound instances. The expected output is:

`STABLE_SET_MINIMUM_WIDTH_CHECKS_PASSED graphs,directions,near_cases,clique_contacts= 810 23936 7284 2391`

There is no assertion that the finite tests cover all graphs or all real directions; the infinite result is established by the exact proof in `RESULT.md`. No independent mathematical audit has been performed. Bibliographic novelty remains provisional.
