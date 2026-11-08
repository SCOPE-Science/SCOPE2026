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

# Verification and limits

The finite test in `check.py` runs a direct \(k\)-tuple recurrence state machine modulo \(2^r\) and a separate quotient-polynomial powering implementation. For each \(2\le k\le30\) and \(1\le r\le8\), it checks the exact least state period against \((k+1)2^{r-1}\), then checks the quotient-ring unit power and available smaller candidate powers. The captured execution output is `verification_output.txt`.

Mathematical coverage does **not** depend on these finite tests. The full proof in `RESULT.md` establishes the two exact orders and the coefficient-pairing equivalence for every integer \(k\ge2\) and \(r\ge1\). No independent scientific audit has been performed, and originality beyond accessible literature has not been externally certified. The 2006 Lü–Wang primary full text remains an overlap risk.
