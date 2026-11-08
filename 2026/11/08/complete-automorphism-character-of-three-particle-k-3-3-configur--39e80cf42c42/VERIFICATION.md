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

Execute the five adjacent Python programs in order using Python 3: `k33_compute.py`, `k33_sym.py`, `k33_classes.py`, `k33_irreps.py`, and `k33_abrams.py`. Each `.out` text file contains one recorded reference run. The scripts do not use packages outside the standard library.

The integral chain computation enumerates all weight-three basis elements, verifies both integer boundary compositions, and carries out integer unimodular elimination. The only nonunit residual is rank one with all entries even and some entries of absolute value two. This proves a single \(2\) invariant factor and no others. The equivariant computation checks action/differential compatibility on every basis generator for each of the \(72\) automorphisms, then reconstructs rational traces from modular calculations using \(10007>2\cdot540\) and the finite-order trace bound. The character script enumerates all conjugacy classes, and the irreducible-character script checks all nine character orthogonality relations. The independent Abrams cubical model directly checks boundary compositions, homology ranks over two independent characteristics, and equivariant Lefschetz identities.

The cubical finite computation is exhaustive for the explicitly enumerated finite complexes; the identification with the actual unordered topological configuration space relies on the published graph-configuration comparison/subdivision theorems. This does not prove equivariant homotopy splitting, integral representation-lattice decomposition, or absence of undetected equivalent publications.
