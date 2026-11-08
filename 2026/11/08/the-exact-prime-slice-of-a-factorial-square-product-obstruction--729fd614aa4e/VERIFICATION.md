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

Run `python3 verification/check.py` with Python 3, without external dependencies. The script computes exact Legendre exponents for all factorial arguments \(12\) through \(50\), checks the failure at \(11\), and independently verifies the first eighty factorial squarefree kernels by direct integer factorization. It also checks explicit witnesses for the small primes and samples the general prime assertion; the theorem's unbounded half is established from Nagura's prime-gap result, not this finite script.

The claim uses the squarefree part \(s(v)\), not the radical \(\operatorname{rad}(v)\). The two operations are different and are never interchanged. No independent mathematical audit has been performed.
