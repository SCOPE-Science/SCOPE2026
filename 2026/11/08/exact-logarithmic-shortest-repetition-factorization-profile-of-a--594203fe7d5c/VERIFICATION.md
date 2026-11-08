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

Run `python3 verify.py` using Python 3 standard library only. The verifier constructs \(w(n)\) from \(\lfloor\log_2(n+1)\rfloor\bmod 2\), checks every candidate square with starts below 320 and half-length at most 80 in the generated finite prefix, tests independent minimum-factorization dynamic programming for 4,440 short factors, and verifies the explicit length-wise witnesses for \(2\le L\le1024\). The observed result was `VERIFY_OK checks= 31063 max_length= 1024 dp_factors= 4440`.

The numerical test is finite and cannot establish the universal statement. The published proof uses the strict growth of all ambient run lengths and an explicit algebraic covering of every positive length class; no external theorem prover or independent human audit is claimed.
