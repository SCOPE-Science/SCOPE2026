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

# Verification

The package includes `verify_enriched2.py`. Run `python verify_enriched2.py` with Python 3 and SymPy. It enumerates normalized length-two tuples, constructs exact integer boundary matrices in dimensions one and two, proves each test matrix satisfies \(\partial_1\partial_2=0\), and computes ranks modulo \(2,3,101\). Tests include paths, a star, five- and six-cycles, a unicyclic graph, a three-arm theta graph, and the excluded triangle and four-cycle. All nine cases pass. It also checks that each explicit signed edge two-cycle has zero boundary.

These finite checks are supplementary. The general statement is proved using a free CW pair for each unique distance-two shortcut, then explicit primitive backtrack-disk attaching maps. There is no numerical extrapolation to longer graph sizes and no classification of the full later-scale filtration.
