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

# Verification notes

The standalone `verify.py` recomputes palstar membership by dynamic programming over all even-palindromic blocks, with no use of the closed gap test. Every binary word of Hamming weight four is enumerated at each even length from \(4\) through \(22\), giving \(18{,}832\) direct word tests. Its output is `VERIFY_OK checked_words=18832 positive=5958 closed_forms=38`.

The same program independently evaluates the three rational-family coefficient contributions, including the intersection, at semilengths \(2\) through \(39\), and checks them against the quasipolynomial. Shorter lengths also receive a separate five-gap composition sum.

The unbounded correctness argument is the exhaustive symbolic case split into either one four-one block or two two-one blocks; the finite checker does not certify all lengths. No external or independent audit is represented.
