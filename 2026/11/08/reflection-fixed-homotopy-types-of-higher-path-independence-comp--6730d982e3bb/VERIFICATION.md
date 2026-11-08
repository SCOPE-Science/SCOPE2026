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

# Reproducibility and limits

Run `python3 verification/reflection_path_verifier.py` from the extracted directory. The supplied verifier directly constructs the action on original path vertices, enumerates every permitted reflected orbit face, and checks it against the explicit mirrored-run model for all \(2\leq n\leq22\) and \(1\leq r\leq9\). It verifies an actual acyclic augmented face-poset matching by generating **all** Hasse covers and checking the full directed graph for cycles. It verifies the exact remaining critical cells and their dimensions, in 189 finite cases comprising 254,981 tested Hasse covers. The actual recorded output, including totals, appears in `verification/verification_output.txt`. The verifier has no external library requirements.

The infinite-family mathematical proof is given in `RESULT.md`, especially the four-step reduction and base cases. Finite enumeration, even when complete for tested cases, is not an infinite proof. The integer homotopy conclusion follows from the explicit acyclic matching theorem, including the exceptional empty \(S^{-1}\) endpoint.

Prior scientific overlap comparisons and independent-validation limits are stated in `REVIEW.md`. Independent mathematical audit was not performed.
