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

The complete certificate consists of `CERTIFICATE.json` and `verify.py`. With both files in the current working directory, run `python3 verify.py` and compare its JSON output with `VERIFY_OUTPUT.json`. All four cases passed in the recorded replay.

The program enumerates every nonempty face by an arc-mask in/out-degree and no-directed-cycle criterion and independently by recursive valid face extension with directed-path tracing from indegree-zero sources. The candidate Hasse matching is constructed solely from the fixed pivot order in the certificate, not from recorded facet counts. Every cover relation is regenerated and the reversed-matched-cover directed graph is checked acyclic. Oriented incidence numbers use the natural ascending arc-index order, and recursive matched-facet elimination computes all integer Morse boundary coefficients, all zero. Every face count and critical-cell multiplicity is independently checked against the certificate.

This is an exact finite check for the four specified digraphs, not a general-algorithm certification for all cycle lengths. The homotopy implication also uses standard discrete Morse theory and the Hurewicz theorem as explicitly argued in the proof. The complete computations are repeatable with Python 3 standard-library support; no network access or external proof assistant is required.
