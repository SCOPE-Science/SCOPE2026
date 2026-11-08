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
# Verification of the joint octahedron-shadow circumradius law

The self-contained `verify.py` requires Python 3, NumPy, and SciPy as recorded in `requirements.txt`. Execute `python verify.py` in a directory containing the two files.

The recorded package-path execution returned `OCTAHEDRON_SHADOW_RADIUS_SILHOUETTE_LAW_OK 600000 2400 48`. That program: (i) directly projects and enumerates planar convex-hull vertices and radii at 2,400 independently drawn normals, (ii) checks nine joint probabilities against an independent 600,000-sample Haar-normal simulation, (iii) quadratures the angular-width formula and checks the known four-/six-vertex mass, (iv) verifies strict conditional ordering over 48 thresholds, and (v) checks each of four endpoint coefficients for three decreasing perturbations. Its tests are bounded checks, not an exhaustive search or proof of a continuum claim.

The mathematical proof itself is in `RESULT.md`. Its critical identities are: central symmetry forces the center of a minimal enclosing circle to the origin; projection gives squared vertex norm \(1-U_i^2\); elimination of one projected vector gives the triangle-inequality silhouette criterion; and a signed-and-ordered spherical coordinate chamber has area element \(dt\,d\varphi\). The end behavior follows by Taylor expansion of the two angular boundaries. A joint stochastic-ordering argument uses a strictly decreasing likelihood ratio; its conclusion is conditional on the stated geometric Haar model.

The closest full texts inspected include Finch (arXiv:1203.2464), Böröczky–Henk (preprint SC-97-21), Rivin (arXiv:math/0305252), and the published records on the octahedron planar-shadow inradius and triaxial-octahedron shadow vertex count. None of these inspected texts gives the specific **joint** radius–silhouette theorem as stated. The available literature may omit an equivalent result under different terminology, and independent historical verification is not performed.
