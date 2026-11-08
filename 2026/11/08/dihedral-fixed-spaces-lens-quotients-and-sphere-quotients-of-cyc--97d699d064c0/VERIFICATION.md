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

# Reproducible verification
Run `python3 verify.py` from a folder containing the extracted `verify.py`; no third-party Python packages are required. The recorded output is in `verify_output.txt`.

The checker constructs the \(t\)-nonmatching complex from forbidden matchings of cyclic edge indices, without referring to the polytope model. It compares each actual maximal face with Gale-evenness facet sets. For cyclic and dihedral subgroups it constructs the complex of invariant barycentric orbit supports and computes reduced homology over \(\mathbb F_2\); its expected answer is a single sphere, or the empty space. For \(t=3\), it also enumerates all flags of nonempty faces, forms the full-dihedral quotient cellular boundary matrices, and computes quotient homology over \(\mathbb F_2\) and \(\mathbb F_3\).

Checks cover a finite set of lengths and thresholds, not all integers; finite homology does not establish homeomorphism or trivial fundamental group. The general proof instead uses Fourier orthogonality, a label-preserving cyclic-polytope realization, orthogonal group-fixed subspaces, the integral lens-space cellular chain complex, Armstrong's theorem and the Poincaré theorem. The standalone code has no external data dependencies, and may be executed after extracting the embedded bytes verbatim.
