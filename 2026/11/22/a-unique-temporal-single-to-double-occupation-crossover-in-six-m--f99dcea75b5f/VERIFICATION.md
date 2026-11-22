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

# Verification of the mathematical result

Use \(\texttt{python3 verify.py}\) in the extracted directory. The proof is the finite first-attempt reduction and the exact subset recurrence, followed by Descartes' rule of signs. The code checks all 16 six-mer dominance-polynomial coefficients and asserts that seven low-degree nonzero coefficients are positive and nine high-degree coefficients are negative. It also verifies exact rational bracketing of the crossing, reproduces the terminal six-mer vector, and crosschecks the k-mer means with independent established formulas for \(k=2,3,4,5,6\).

The script has no external dependencies; it uses exact integer/rational arithmetic. Its result is a finite arithmetic check, not an independent mathematical audit, and it does not establish claims about other kinetic rules or polymer lengths above six. No numerical exploration is used to justify global root uniqueness; the proof uses the exact sign-change certificate.
