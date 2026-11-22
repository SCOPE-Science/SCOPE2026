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

The theorem follows from closed-neighborhood identities, the characterization of integer differences at weights two and three, and an explicit defender test. This is a mathematical proof, not an inference from the finite computations.

Compile the standalone verifier with `g++ -O3 -std=c++17 direct_crown.cpp -o direct_crown` and run `./direct_crown`. It directly constructs the crown-graph adjacency lists and exhausts \(4^{2n}\) assignments for \(n=3,4,5,6\), checking Italian and Roman conditions independently of the coefficient formulas.

Run `python3 symbolic_crown.py` for a separate convolution calculation of the two low-weight coefficients for \(4\le n\le10\). The recorded outputs in `verification_output.txt` are reproduced by these commands. The full infinite-family conclusion depends on the symbolic proof in `RESULT.md`. No independent audit or verification by another researcher has been performed.
