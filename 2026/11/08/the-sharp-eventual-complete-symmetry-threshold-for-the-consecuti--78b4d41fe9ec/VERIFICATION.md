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

# Reproduction and limits

`python3 verify.py` reconstructs the generating-function denominator, the finite-period difference polynomial, and the asserted integer-polynomial identity entirely using Python standard-library integer arithmetic. It independently enumerates selected Diophantine solution counts, verifies the full \(5814\)-residue exact negative-difference list and maximum, checks the boundary \(r(2394)=505\), \(r(2395)=504\), and produces the reproducible output in `CERTIFICATE.txt`.

The polynomial identity is a finite algebraic certificate, not a statement inferred from observed samples. Together with the first-period table it proves that no downward step starting above \(505\) can occur anywhere. Only self-review has been performed; this document reports no independent audit or certification.
