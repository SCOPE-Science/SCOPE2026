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

The proof is analytical and is provided in `RESULT.md`. The independently runnable numerical sanity check is `verification/check.py`; install only the pinned minimum dependencies from `verification/requirements.txt` and run `python verification/check.py` from the extracted artifact root.

The check explicitly draws 2,500,000 independent sphere-inscribed tetrahedra, and 1,500,000 product-uniform proposals for the exact conditional change of variables, comparing the probabilities of \(V<t\) at \(t=0.001,0.0025,0.005\). It also draws 2,000,000 random triples of circle angles and checks their triangle-area mean and negative-half-moment, together with the plane-height variance profile. The observed successful exit marker was `SPHERE_TETRA_COPLANAR_CONDITIONAL_LAW_OK`.

These samples are finite and random; they cannot establish any mathematical convergence, exact identity, novelty, or historical priority. Proof of the two-term expansion uses uniform rejection-event bounds, dominated convergence, and the known circular Dyson integral. The exact rejection law is algebraic; no informal finite experiment substitutes for the proof. Independence of any audit is not asserted.
