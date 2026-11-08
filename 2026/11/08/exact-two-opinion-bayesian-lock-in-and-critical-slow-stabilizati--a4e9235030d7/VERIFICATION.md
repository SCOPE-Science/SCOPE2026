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

# Reproducibility checks and boundaries

Execute `python verify.py` under Python 3 with no third-party packages. The script independently enumerates valid first-passage words up to length 15, checks rational Catalan first-switch probabilities, verifies renewal and finite series equations in exact fractions, confirms the strict inferior-option example \((a,b)=(7/10,9/10)\) and the formula for even-time fair first-passage survival. The output is `VERIFY_OK 368 exact-rational and combinatorial checks`.

The proof, not the program, establishes the infinite-horizon phase classification and the Tauberian tail limit. These checks cannot certify the absence of an equivalent historical theorem, the source's network behavior, or any independent review. The source's one-institution quit probability is known prior work; the result concerns its two-opinion alternating reset extension.
