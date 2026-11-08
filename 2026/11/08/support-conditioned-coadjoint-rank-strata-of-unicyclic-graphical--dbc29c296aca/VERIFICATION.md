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

# Verification

Execute `python3 check_unicyclic.py` in the directory containing that file. No external packages are required. The separately embedded `verification_output.txt` holds the stdout of the final checker replay.

The exhaustive mode enumerates thirteen distinct unicyclic test graph shapes and fifty-two graph/field configurations over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), totaling 126,870 matrices. Every rank is calculated using Gaussian elimination on the original weighted alternating matrix, whereas the independent predicted histogram uses exhaustive graph matchings and leaf-pair pruning. The extension field \(\mathbb F_4\) is implemented as \(\mathbb F_2[t]/(t^2+t+1)\); an additional 1,200 seeded assignments check larger examples.

This confirms the implemented formulas only for those finite cases; no finite experiment proves the unrestricted theorem. The mathematical proof is in `RESULT.md`. The displayed character counts use the published class-two character/rank correspondence; the checker does not enumerate irreducible characters themselves.
