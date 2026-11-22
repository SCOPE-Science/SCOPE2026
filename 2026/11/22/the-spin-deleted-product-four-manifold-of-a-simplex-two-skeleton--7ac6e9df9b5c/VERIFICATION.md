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

# Reproducing the exact finite calculation

Use Python 3.10 or later in the same directory as `check_intersection.py`. Run:

```bash
python3 check_intersection.py
```

Compare stdout with `check_output.txt`. No optional libraries or external datasets are needed. The exact generated cell model uses ordered disjoint nonempty subsets of a seven-element set, of size at most three in each factor. The boundary is the product cellular boundary. A deterministic binary echelon algorithm constructs all mod-two degree-two cocycles, quotients by all degree-two coboundaries, and produces forty basis representatives. The three-term Alexander–Whitney diagonal computes the mod-two middle-degree cup form on the complete four-dimensional fundamental cycle. The checker verifies all forty diagonal entries vanish, full rank, symmetry and coboundary invariance. A separate signed integer fundamental-chain check proves zero boundary; coordinate exchange reverses its orientation.

The external theorems that the complex is a simply connected closed oriented PL four-manifold with torsion-free rank-forty middle homology are found in the cited 2025 and 2026 papers. The conclusions about the integral intersection lattice and TOP homeomorphism additionally use the Wu formula, lattice classification and Freedman's theorem. These are mathematical deductions, not outputs from the program. The checker does not establish diffeomorphism or PL homeomorphism and does not investigate larger complexes.
