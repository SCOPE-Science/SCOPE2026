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

# Reproducible checks and scope

The attached standard-library `verify.py` reconstructs every mathematical object used in the claim from its definitions. From the directory holding the script, run:

```sh
python3 verify.py
```

The recorded output is `verification_output.txt` and its last line is `ALL_CHECKS_PASS`. The checks include independent construction of every face of the open-neighborhood complex, a complete acyclic discrete-Morse matching with \(160\) pairs and \(1040\) Hasse incidences, exhaustive enumeration of the \(1920\) graph automorphisms, two separate fixed-chain character algorithms, all \(360\) stabilizer Fourier traces, reconstruction of the character from induced irreducibles on each of the \(1920\) elements, and affine equivalence with the four-cube closed-neighborhood Čech model. The published \(384\)-element four-cube group character is checked on the entire smaller group, rather than treated as an unrelated complex.

This is an exact finite computational proof and self-review of the specified graph; it does not supply independent audit, a classification for infinite graph families, or definitive publication priority. It establishes a rational homology representation, not an equivariant homotopy type or an integral-lattice isomorphism.
