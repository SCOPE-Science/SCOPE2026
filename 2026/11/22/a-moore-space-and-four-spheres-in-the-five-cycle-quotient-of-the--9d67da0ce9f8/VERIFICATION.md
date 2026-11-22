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

# Computational verification

The standalone `verify.py` and `certificate.json` encode a deterministic exhaustive computation for the stated five-label case. Execute them from their containing directory with `python verify.py`. Python 3 standard library is sufficient.

The program reconstructs 52 Bell partitions; filters 50 non-extremal partitions; enumerates 205 edges and 180 triangles; forms 10, 41 and 36 quotient cells; confirms all 36 compositions of cellular boundaries vanish; finds a spanning tree with nine edges; obtains 32 generators and 36 relators; and executes 31 explicitly recorded one-occurrence generator/two-cell cancellations. It checks the final two degree-five attaching words and three empty words and exact identity of the regenerated data with the included certificate. The successful run prints `VERIFY_OK`.

The certificate supports only this finite exact computation and the accompanying topological cancellation argument, not an infinite-family conjecture. Independent mathematical auditing and formal proof-assistant verification have not been performed.
