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

# Reproducibility

Run `python3 verify.py` from a directory containing the embedded script. No third-party Python packages are needed. The script uses the exact quadratic integer ring \(\mathbb Z[\varphi]\), with \(\varphi^2=\varphi+1\). It reconstructs all twelve icosahedron vertices, thirty edges and twenty triangular faces; verifies that every original edge lies in two triangles; tests all four facet normals of each of the thirty rectified vertices against all twelve axial directions; checks fourfold exact coverage; exhausts all \(64\) antipodal sign transversals; identifies the twelve size-ten maximizers; checks their pairwise overlaps and a four-direction cover; and confirms the tight-frame matrix identity.

Actual invocation: `python3 verify.py`. Actual result: `EXACT_OK vertices=30, faces=32, signed transversals=64, distribution={5: 12, 6: 20, 9: 20, 10: 12} fractional=3, ordinary=4, exact facet inequalities=1440`.

The finite checks are a complete certificate for the discrete claims only because every arbitrary real direction is analytically reduced to a six-pair transversal. Analytic arguments establish weighted optimality, ordinary optimality and illumination of all boundary points. The program does not certify historical novelty or independent audit.
