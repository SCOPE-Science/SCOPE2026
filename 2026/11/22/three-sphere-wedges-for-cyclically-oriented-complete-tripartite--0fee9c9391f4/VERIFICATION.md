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

# Reproducibility

Run `python3 verify.py` using Python 3 without third-party dependencies. `verification_output.txt` records the successful output. The verifier constructs directed arcs from the definition, checks each arc subset for in/out degrees and directed cycles, independently reconstructs the crown-graph link decomposition, enumerates faces, and calculates mod-two homology using exact bit-vector Gaussian elimination.

It checks \(3\le n\le10\), including the first six members of the theorem's infinite family. The rank vector in degrees zero through three is \((1,0,0,n^3-6n^2+8n-1)\) for all tested \(n\ge5\). For \(n=4\), it is \((1,0,2,1)\). Only an ordinary \(H_0\) rank is reported in that vector; reduced \(H_0\) vanishes. Finite checks cannot establish the infinite statement or integral torsion-freeness by themselves. Those follow from the documented exact combinatorial-topological proof, including the integral cycle-lattice generation and integral surjectivity at the fifth-column threshold.

No external independent mathematical validation or expert certification is claimed.
