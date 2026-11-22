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

# Reproducibility and verification

Run `python3 artifacts/verify_k234.py` using Python 3 and its standard library. The script reconstructs the disjoint-product cubical chain complex for two unordered points on the graph with vertex shores \(\{0,1\}\), \(\{2,3,4\}\), and \(\{5,6,7,8\}\). It builds and checks all 198 columns of the signed second boundary, checks every composition with the first boundary, generates 4,395 simple cycles and 1,206 unordered vertex-disjoint cycle pairs, and tests the zero integral boundary of every product torus.

The exact proof certificate consists of a rank-129 lower bound modulo 101 (independently modulo 103), an integral 69-by-69 minor of determinant \(+1\) from 69 shortest triangle-pair tori, and the elementary rational-kernel and integral-coordinate argument documented in `RESULT.md`. The script produces and verifies all three explicit integral relations among the 72 triangle-pair tori; each relation has 36 nonzero coefficients. All 1,206 product tori reduce integrally to the same basis. The six natural adjacent-transposition actions preserve the relation lattice and give the rational character described in `RESULT.md`. The supplementary JSON certificate records the actual basis, minor, relations and generator matrices and can be inspected independently.

Observed successful command output:

```
K234_TWO_POINT_TRIANGLE_TORUS_INTEGRAL_PRESENTATION_OK
cells 36 182 198; rank_d2 129; rank_H2 69; tori 1206
shortest tori 72; independent integral basis 69; three full relations
relation character: S2 and S3 sign, S4 parity-twisted standard
```

This verification exhausts the finite combinatorial model for this one graph. The standard deleted-product deformation equivalence is supplied by the mathematical literature. No claim is made about arbitrary tripartite parameters, cup products, higher homotopy or independent certification.
