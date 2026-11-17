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

# Reproducible finite corroboration

Run `python verify.py` in the directory containing this file and `verification_output.txt`. The script uses the Python standard library only.

The verifier constructs cyclic distance graphs, rotation/reflection-generated vertex orbits, and source-orbit conflicts independently of the explicit indexed-path formula. For \(4\le n\le32\), all tested admissible \(k\le7\), every divisor \(t\mid n\), and tested reflection parameters, it compares the orbit graph to the predicted induced path-power graph. It also compares 452,220 orbit selections directly against the independence condition in the *original* graph and against the predicted simplicial face criterion. A separate finite graph argument verifies the mixed-dimensional seven-vertex fixed example.

Expected last-line marker: `mixed_example=n22_k3_edge_reflection: Ind(P7^3)=S0 wedge S1`.

The tested range is finite; no claimed infinite mathematical statement depends on extrapolating these checks. The general proof rests on the explicit orbit-distance inequalities and cited chordal splitting theorem. No independent audit was performed.
