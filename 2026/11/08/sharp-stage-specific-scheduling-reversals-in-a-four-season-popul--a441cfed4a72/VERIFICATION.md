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

# Reproduction and boundaries

Run `python checker.py` from the directory containing this file after installing `requirements.txt`. The checker computes exact symbolic expressions (not floating point), verifies the 2×2 commutator/trace identity, the equality of monodromy determinants, three single-rate signed-square reductions, the binary cyclic-word classes through period four, and the rational determinant tests of both persistence examples. The successful check output is reproducible from the embedded files.

The general all-parameter implication is a direct algebraic proof in `RESULT.md`; finite word checks serve only as a small-period crosscheck. The exact witnesses establish deterministic per-cycle growth/decline, not probabilistic extinction. The two strongest historical-priority comparisons with older primary articles are limited to their accessible abstracts; no novelty certification or independent audit is claimed.
