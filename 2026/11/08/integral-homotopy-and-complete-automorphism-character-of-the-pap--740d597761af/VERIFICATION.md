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
# Reproducible finite certificate

Run `python3 pappus_forest_certificate.py` from a directory containing the standalone program. No network or nonstandard packages are used. Compare its standard output byte-for-byte with `pappus_forest_certificate.txt`.

The code enumerates all \(262{,}144\) possible vertex subsets, compares two independent forest predicates, and finds \(204{,}492\) allowed faces. It pairs \(204{,}446\) augmented faces and leaves \(46\) critical higher-dimensional faces. Its directed Hasse graph has \(1{,}704{,}456\) relations and a successful topological ordering of every vertex. For the three critical eleven-cells, it computes the complete \(3\times43\) integral boundary and a determinant-\(-1\) minor, proving the claimed homotopy equivalence by the topological argument in RESULT.md.

Run `python3 pappus_crosscheck.py` to recompute a *different* acyclic matching and a full-rank four-row mod-two Morse boundary (corroboration, not a substitute for the integral unit minor). The saved output is `pappus_crosscheck.txt`.

The code also performs graph-automorphism backtracking, conjugacy grouping, per-element invariant-orbit Lefschetz sums and direct signed simplicial-chain traces for class representatives. The expected terminal line is `PAPPUS_FOREST_CERTIFICATE_PASS`.

**Limits.** The program is a transparent finite exhaustive check for this specific graph; it is not an external or independently authored mathematical audit. The homotopy step invokes standard discrete-Morse theory and the description of maps between high-dimensional wedges of spheres by degrees. The full integral representation lattice and equivariant homotopy type are not determined.
