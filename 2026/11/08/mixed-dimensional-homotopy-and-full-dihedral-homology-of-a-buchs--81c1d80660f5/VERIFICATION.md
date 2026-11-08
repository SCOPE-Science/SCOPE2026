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

The bundled `verify.py` runs with Python 3's standard library. It constructs the exact graph and every independent face, tests every matched Hasse incidence and acyclicity over all cover arrows, and checks the resulting critical-cell profile \((1,1,0,4)\). It enumerates the full graph automorphism group using adjacency/nonadjacency constraints; the 32 elements agree with the dihedral formulas.

It checks the 15-edge-support closed integral one-cochain against every triangle and finds primitive evaluation one on the stated five-edge cycle. For each of 32 graph symmetries, the program computes the transformed cycle pairing and the reduced signed Lefschetz sum over every setwise-fixed simplex, obtaining the complete two homology characters. The complete actual program output is in `verification_output.txt`.

The homotopy conclusion follows from the checked acyclic matching and the standard attachment argument. The rational module and quotient conclusions also use semisimplicity of finite-group representations over \(\mathbb Q\) and transfer/averaging after subdivision. The program is a finite certificate checker for the claimed finite graph, not a universal theorem prover. It does not check integral representation lattices, priority against all possible literature or independence of mathematical verification.
