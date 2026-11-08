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

Using Python 3 (standard library only), run `python3 verify_rhombicuboctahedron_euclidean.py` from this directory. All three machine-readable certificates are complete and included: `collapse_certificate.json`, `rank_certificate.json`, and `filling.json`. No external files, unpublished tables, notebooks, or packages are required. The supplied `verify_output.txt` records the successful result and can be compared with a fresh replay.

The script enumerates all 24 Euclidean coordinates and all 276 unordered distances exactly in \(\mathbb Z[\sqrt2]\); builds the full simplicial complexes at the first five nontrivial Euclidean shells; checks surface links, Euler characteristic, exact oriented boundary cancellation, every single free-face collapse and the final residual face sets; and verifies both the 751 unit-pivot third-boundary certificate and the independent 193-rank mod-two second-boundary calculation. The existence of a 751-by-751 unimodular minor is stronger than rational rank and is what excludes unobserved integral torsion. It checks the stated 79-tetrahedron integral filling directly. The last penultimate-stage sphere is proved using the twelve forbidden antipodal pairs, avoiding an impractically large explicit simplex list.

All proof claims concern this finite, explicitly enumerated vertex set. Computational certificates are exact, but correctness still depends on the transparent reduction from these finite checks to the stated topological lemmas. No independent scientific audit was performed. The machine verifier verifies finite premises, not literature novelty or value.
