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

# Reproduction of finite proof certificates

From the package root, run `python3 src/verify_bipyramid.py` with Python 3.9 or newer. No third-party libraries, downloaded papers, environment variables or external files are required. The checker reads `certificates/bipyramid-collapse.json`, independently enumerates the perfect matchings two ways for each specified graph, reconstructs every simplex, validates every ordered elementary collapse and surviving core, checks connectivity or the explicit spanning-tree and triangle-relator elimination, and verifies the integral signed boundary minor and two kernel vectors at the ten-rim case. The complete output of the successful test run is in `verification_output.txt`.

These certificates prove the finite combinatorial and linear-algebra claims stated in `RESULT.md`; they do not establish a formula for arbitrary rim sizes, nor guarantee independent mathematical review. The homotopy conclusion also invokes the standard topological arguments written explicitly in `RESULT.md`.
