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

# Reproducibility and scope of verification

Run `python3 proof/verify_cylinder.py` from the directory containing the six documents. Python 3 and SymPy are required (SymPy 1.14.0 used). The complete recorded output is `proof/verification_output.txt`. The critical-face ordering and full signed 31-by-10 integer Morse boundary are serialized in `proof/morse_boundary_31x10.csv`; labels are 25-bit integer masks in the edge order defined in the source.

The program reconstructs the graph without external input, branches over all admissible edge-inclusion choices, verifies the augmented f-vector \((1,25,240,1125,2710,3227,1645,240)\), constructs 4,586 disjoint pairs, and checks that all 9,213 vertices of the oriented Hasse diagram can be topologically sorted (42,405 incidences). After excluding the augmented empty-face pairing, its ordinary Morse CW model has one 0-cell, 31 four-cells and ten five-cells. Signed gradient recursion computes the exact 31-by-10 Morse differential; its nonzero Smith entries are seven ones, leaving ranks 24 and 3. Separately, uncompressed original simplicial boundaries over \(\mathbb F_2\) give reduced Betti ranks \((0,0,0,24,3,0)\) in dimensions one through six.

**Limits.** Finite-field homology alone would not establish torsion-free integral homology or the homotopy wedge; the exact signed Morse differential and connectivity argument are essential. The certificate is exhaustive for only the specified 25-edge graph. It does not assert values for other cycle lengths or independently validate the work beyond the stated review status.
