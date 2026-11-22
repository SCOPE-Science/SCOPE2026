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

# Verification of the four-by-four transpose quotient

The standalone Python 3 standard-library program `verify.py` and the explicit finite certificate `certificate.json` are sufficient to reconstruct and check the computational premises of the main result. Run `python3 verify.py` from any working directory with those two files placed together. The program requires no network, computer-algebra package, external file or precomputed homology table.

Actual results from replay of the packaged files:

```
CHESSBOARD_TRANSPOSE_4X4_WEDGE6_OK
original_faces=(16,72,96,24)
quotient_orbit_cells=(125,586,768,300)
certified_top_collapses=300 remaining_cells=(125,586,468) chi=7
fundamental_group_tietze_eliminations=462 generators_remaining=0
```

The program checks exact signed orbit-cell boundaries and zero boundary compositions, 300 sequential free faces (unique active cofaces), the final Euler characteristic, a spanning tree in the complete quotient one-skeleton, and every relation and generator substitution in the 462-step trivial-fundamental-group argument. The reduction is exhaustive for this finite complex; no timeout, experimental extrapolation or probabilistic rank estimate is used. The topological inference from these finite checks to a wedge of spheres invokes standard elementary collapses, van Kampen, Hurewicz and the homological Whitehead theorem. This does not provide an independent external proof review, nor a classification of larger chessboards.
