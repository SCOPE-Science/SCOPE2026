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
# Reproducible exact checks

Extract `verify_kneser.py` next to this file and execute `python3 verify_kneser.py` with a standard Python 3 installation. It requires no internet connection or third-party modules.

The program verifies the incidence/adjacency decomposition for \(5\le n\le8\); enumerates and tests all \(252\) choices of \(n\) unactuated pair-vertices at \(n=5\), and all \(5005\) choices at \(n=6\), using rational Gaussian rank for the two nonconstant PBH eigenspaces. It also tests \(1000\) reproducibly sampled cases at \(n=7\) by exact ranks, structurally enumerates all \(116280\) seven-edge complements, and uses rational formal power series through \(n=9\). The program emits `VERIFY_OK` only when all assertions hold.

For a complete mathematical proof for every \(n\ge5\), see the eigenspace, incidence-rank and complementary-edge analysis in `RESULT.md`. These finite computations do not serve as an exhaustive verification for unbounded \(n\). No independent audit has been performed.
