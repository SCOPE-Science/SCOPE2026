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

# Verification and proof limits

The independent finite checker bundled as `verify_pasm_diameter.py` uses binary vertical-prefix-state column generation and exhaustive pairwise integer distances. The following independently generated configurations were exhaustively verified: `(1,1)`, `(1,2)`, `(1,3)`, `(2,1)`, `(2,2)` through `(2,6)`, and `(3,2)` through `(3,6)`. The first saturation cases include `(2,4)`, `(2,5)`, `(2,6)`, `(3,6)`; their exact numbers of unordered farthest pairs are `1`, `5`, `15`, and `1`. It additionally checks 1,626 explicit staggered-diamond pairs and verifies both orientations by transposition, through seven-row cases.

Execute `python verify_pasm_diameter.py` in a directory containing the embedded checker. The expected success marker starts `PASM_RECTANGULAR_SHARP_DIAMETER_CHECKS_PASSED`.

The finite enumeration cannot establish a universal theorem or historical novelty. The universal bound, strict threshold, and complete equality-pair classification are supplied by the analytic proof in `RESULT.md`. The unsaturated regime is not classified numerically or analytically beyond strictness. No independent audit has been performed.
