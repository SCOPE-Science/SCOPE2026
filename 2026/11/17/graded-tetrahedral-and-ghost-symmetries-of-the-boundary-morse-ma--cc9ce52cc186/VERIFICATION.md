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
# Reproducible finite verification

With Python 3 standard library, run `python3 tetra_boundary_char.py` in this directory. Expected terminal marker: `BOUNDARY_TETRAHEDRON_S4xC2_GRADED_CHARACTER_PASS`. All printed results are in `VERIFY_OUTPUT.txt`. The program independently builds the full complex rather than reading a table or assuming previously generated complex data. Its computed face vector is `(24,216,896,1692,1248,256)` (4,332 nonempty faces). It checks rank 256 for the boundary in degree five and 968 in degree four modulo both 1009 and 10007; the invariant identity calculation also checks degree-three boundary rank 703. The published integral homotopy classification establishes the exact rational boundary ranks used in the proof. The modular fixed-boundary ranks are consequently exact in characteristic zero by the localization/averaging argument in RESULT.md, **not** by interpreting one modular calculation as an unconditional rational-rank proof.

The ten group elements include permutations of types identity, transposition, double transposition, three-cycle and four-cycle, each with and without the central ghost involution. Their orders are respectively 1,2,2,3,4 without ghost and 2,2,2,6,4 with ghost. The program constructs invariant matrices for each element and each relevant power, computes eigenvalue traces by exact cyclotomic arithmetic, and verifies all results against direct signed oriented simplex traces all twenty irreducible character multiplicities, and the independently known relative four-regular tetrahedral character. A separate `CHARACTER.csv` provides a compact copy of the final character values.

No higher-dimensional complexes, integral group-ring classification or quotient-space torsion calculation is attempted. Independent mathematical audit remains unperformed.
