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

The accompanying `verify.py` reads `certificate.json` and reconstructs the original icosahedron from a closed combinatorial rule. It derives all 60 truncated vertices, 90 graph edges, and all 802 faces of the graph-square clique complex. For each of the 120 pairwise deletions, it checks inclusion, codimension one, and **the unique remaining strict coface**. The residual complex has precisely \((60,270,232)\) faces in degrees 0, 1, 2.

The same verifier checks the 12 pentagonal and 20 hexagonal original faces form a connected closed triangulable sphere by edge incidence, cyclic vertex links, and Euler characteristic. Every polygon boundary has an explicit disk filling inside the original scale-two Rips complex. The original graph surjects on the Rips fundamental group, hence these fillings kill all generators; the remaining integral homotopy argument is in RESULT.md.

Recorded output is in `verify_output.txt`. Run `python verify.py certificate.json` with standard Python 3; no third-party packages, internet connection, or external certificates are required. This is a complete finite verification, not an infinite-case inference. The scientific finding has not received independent mathematical audit.
