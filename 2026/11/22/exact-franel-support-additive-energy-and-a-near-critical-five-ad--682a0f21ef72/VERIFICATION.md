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

Run `python3 CHECK.py` with the Python standard library. It enumerates the one-digit signed-carry matrix from digit pairs; checks the two-dimensional reduced matrix, recurrence and exact first fourteen energy values; directly computes the first 513 Franel residues from integer binomial sums; and independently calculates all ordered sum representations at depths zero through five, checking the full sumset and complete energy totals. The checker was executed successfully before packaging.

Its finite comparisons establish reproducibility of the certificate calculations, not the infinite theorem. The unrestricted proof is given in `RESULT.md`: Lucas factorization, carry-state enumeration, Cayley--Hamilton, an interval induction and a uniform two-sided comparison of continuous-grid masses. The strict spectral threshold is checked exactly by evaluating the characteristic polynomial at \(256/5\).

Independent mathematical audit was not performed; this verification does not claim external certification.
