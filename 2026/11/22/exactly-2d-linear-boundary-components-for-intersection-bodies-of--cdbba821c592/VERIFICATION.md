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

# Checks and boundaries

The exact coarea normalization was checked against independent Euclidean polygon sections in three dimensions and the corrected published coordinate offsets in dimensions three and four. The included \`verify.py\` uses Python's standard library and a fixed random seed; run \`python verify.py\`. It passed 7,741 exact-rational or independently constructed low-dimensional geometry assertions for dimensions two through seven. Those finite tests do not certify algebraic irreducibility or all-dimensional uniqueness. The universal proof is the truncated-power polynomial divisibility argument plus the finite-chamber algebraic-closure argument in \`RESULT.md\`.

No independent mathematical audit was performed. The script does not require network access or unavailable external files.
