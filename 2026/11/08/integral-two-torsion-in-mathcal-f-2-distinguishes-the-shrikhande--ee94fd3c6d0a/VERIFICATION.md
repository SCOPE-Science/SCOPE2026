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
# Exact verification and limits

The reproducible source `verify.py` regenerates two adjacency matrices from closed definitions, examines the complete Boolean vertex lattice, computes two independent face tests, checks all graph intersection parameters, and constructs two acyclic Morse matchings for each complex. It checks every oriented face-cover incidence for directed cycles, derives signed integral Morse matrices, verifies their chain relations, and computes exact integer Smith forms using SymPy. A separate unreduced simplicial mod-two elimination checks all boundary ranks and universal-coefficient implications. The actual boundary matrices for both matching orders are embedded as `MATRICES.json`.

Run `python verify.py --check-certificate MATRICES.json` with Python 3.10+ and SymPy 1.11+. Compare stdout with `verification_output.txt`. The verification output was replayed from the finalized source and matrix file with exact agreement.

The precise data are: rook complex \(6,521\) faces including empty, \(3,204\) matched pairs, \(32,608\) Hasse incidences, critical cell counts \((4,37,72)\) in degrees \((4,5,6)\), and degree-five Smith invariants \((1,1,1,1)\). Shrikhande complex \(5,945\) faces including empty, \(2,934\) pairs, \(29,024\) incidences, critical cell counts \((22,19,36)\), and degree-five Smith invariants \((1\text{ repeated }12\text{ times},2)\). Both degree-six Morse differentials are zero. Independent original-chain mod-two Betti ranks are \((33,72)\) in degrees \((5,6)\) for the rook complex and \((10,7,36)\) in degrees \((4,5,6)\) for the Shrikhande complex.

This is a same-model exact finite computation, not an independent audit. It proves only the reduced integral homology groups for the two specified complexes, not a homotopy classification or a universal graph-family result.
