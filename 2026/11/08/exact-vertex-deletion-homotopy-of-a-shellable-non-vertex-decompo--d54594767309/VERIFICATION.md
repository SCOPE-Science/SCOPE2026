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

# Reproduction and limits

Run `python3 verify_c16_deletion.py`. The verifier uses only the Python standard library and deterministic integer/bitset operations. Compare its stdout to `verification_output.txt` byte-for-byte. It independently enumerates faces by scanning the complete sixteen-bit universe and by an incremental independent-set construction, builds and checks all ordinary nonempty Hasse matched incidences, and computes exact signed Morse differentials by contracting each paired incidence of coefficient \(\pm 1\). Separately, it computes unreduced simplicial mod-two boundary ranks. Vertex rotation acts simplicially and covers all sixteen deletion cases.

The deletion produces one critical zero-cell, two two-cells and one three-cell, with signed differential \(\begin{pmatrix}-1\\0\end{pmatrix}\); the link produces one zero-cell, one one-cell and three two-cells, with signed differential \(\begin{pmatrix}1&0&1\end{pmatrix}\). The exact integral matrices, not mod-two ranks alone, are the topological certificates. The ambient shellability used for the link-inclusion statement is an existing published theorem, rather than independently established by the program. The standalone verifier does not prove publication priority or replace independent peer review.
