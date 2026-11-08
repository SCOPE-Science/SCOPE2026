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

# Computational reproduction

Run `python3 verify.py` using Python 3.10+ standard library in a directory containing this script. The actual recorded output is in `verification_output.txt`. No external packages, graph database, or private files are used.

The script reconstructs each original graph's edges; enumerates involution orbits without trusting the proposed quotient model; deletes exactly those orbits containing an edge; enumerates all cross-orbit adjacency; then independently constructs the open/circular/Möbius ladder expected by the theorem and checks exact edge equality under canonical vertex maps. It further enumerates complete finite independence complexes and performs reduced mod-two homology via all boundary matrices. The tests cover every involution type on widths \(5\le n\le18\) and homology on widths \(5\le n\le14\), including empty fixed-point spaces and the smallest open-ladder model.

The expected output is `ALL_CIRCULAR_INVOLUTION_CHECKS_OK: orbit_graphs=70, graph_edges=840, homology_cases=50, faces=6320`. No finite test proves the infinite statement. The proof in `RESULT.md` supplies the arbitrary-width fixed-point orbit homeomorphism, graph identifications and open-ladder recurrence, then cites the established ordinary circular/Möbius ladder homotopy classifications. Independent audit is not performed.
