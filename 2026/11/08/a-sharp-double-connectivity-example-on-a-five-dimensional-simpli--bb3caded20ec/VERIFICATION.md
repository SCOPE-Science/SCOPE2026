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

# Verification

Run `python3 check_double.py` from the extracted package directory using Python 3.9 or later. The verification enumerates exactly the pair-collections allowed by the two missing four-faces, checks the decomposition and cone links, and reports modular homology over three primes. Its recorded output appears in `check_output.txt`.

The integral proof does not rely on modular calculations. Its critical noncomputational inputs are the published connectivity bound for the \(4\)-by-\(4\) chessboard complex, elementary generation of complete-bipartite graph loops by squares, the van Kampen/cone argument, and standard Hurewicz/Whitehead and homotopy-pushout facts. The checker does not verify those general topological theorems or imply independent certification.
