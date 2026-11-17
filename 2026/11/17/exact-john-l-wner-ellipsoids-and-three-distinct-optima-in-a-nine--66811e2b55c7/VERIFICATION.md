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

The included `verify.py` executes with the Python 3 standard library; the command `python3 verify.py` completed successfully with **18,199 finite assertions**. It reconstructs the nine sphere vertices, checks the fourteen supporting facets with exactly three incident vertices each, tests strict John contact counts, verifies enclosing-ellipsoid vertex contacts, and checks the ordered quartic minimizers and global-ratio benchmarks over a deterministic sample.

The core proof is analytic: symmetry reduces both extremal ellipsoids to spheroids, explicit support inequalities establish the inner one, explicit vertex inequalities establish the outer one, and monotonicity and polynomial root isolation establish the sharp extrema. Numerical sampling is supplementary and does not certify the continuum independently. The scope is the open parameter interval \(1/2<r<1\); nonsymmetric polyhedra and excluded endpoints are not covered.
