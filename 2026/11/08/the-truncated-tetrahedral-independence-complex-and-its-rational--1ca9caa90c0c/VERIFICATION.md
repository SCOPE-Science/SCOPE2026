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
# Reproducibility and limits

Run `python verify.py` using Python 3 and its standard library; no network or third-party packages are required. The program reconstructs \(T\) both from the ordered-pair adjacency rule and from incidence of edges in a once-subdivided \(K_4\). It exhaustively compares two face-generation strategies, proves acyclicity of the complete discrete-Morse gradient Hasse graph by topological sorting, and computes independent mod-two boundary ranks. It also enumerates every element of \(S_4\) and computes the signed fixed-face Lefschetz trace on every conjugacy class.

The exact expected output is supplied as `verification_output.txt`. The computations are finite certificates: they do not establish results about arbitrary graph families. The homotopy conclusion follows from the critical-cell dimensions plus acyclicity; the rational quotient calculation further uses the standard averaging/transfer result for finite group actions. No external or independent mathematical assessment has been performed.
