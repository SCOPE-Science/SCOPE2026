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

# Reproducibility and scientific limits

Run `python3 verify.py` with the Python 3 standard library only. The script generates 208 test tetrahedra (regular, two-axis symmetric, strongly anisotropic and 200 seeded randomly chosen nondegenerate cases), reconstructs facet normals/centers, verifies the relevant squared-distance identities, calculates three edge thresholds, and computes all tested Čech Betti ranks from actual finite mod-two boundary matrices. The verified output ends with `PASS: 208 geometric configurations`.

The analytic proof in `RESULT.md` is the evidence for every positive choice of the three box semiaxes. Its critical nonstandard facts are: positivity of the disphenoid's acute-face barycentric weights, uniqueness of each triple unit-ball intersection by a weighted squared-distance identity, emptiness of fourfold unit-ball intersections by a centroid identity, and nonbounding of the original 2-sphere before the first central-plus-three-outer simplex appears. These prove the exact core threshold and explain why numerical samples alone are insufficient.

The barcode is computed for the four equal-radius outer balls, whereas the separate core statement concerns one origin-centered ball of varying radius added to four fixed unit balls. These two radius parameters are intentionally different; no claim of a five-ball equal-radius persistence barcode is made.
