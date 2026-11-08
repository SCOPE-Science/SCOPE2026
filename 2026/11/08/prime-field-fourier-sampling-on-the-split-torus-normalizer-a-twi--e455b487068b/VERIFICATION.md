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

# Reproduction and scope

Run `python check_normalizer.py` with Python 3 and NumPy. The standalone script constructs the \(2(p-1)\)-square entrywise Fourier matrix independently of the two-block reduction and checks the full singular-value multiset predicted by multiplicative twisted sums for primes \(2,3,5,7,11,13,17,19\). At odd primes it tests additive parameters \(b=1\) and \(b=2\). The output ends with `NORMALIZER_FOURIER_PASS`, and no test discrepancy exceeds \(10^{-12}\). Its direct rank checks agree with the theorem, including the rank-one exceptional case at \(p=2\).

A separate numerical determinant comparison at odd primes \(3,5,7,11\) for additive parameters \(1,2\) gave relative errors below \(3\times10^{-14}\). Those supplemental calculations are not required for replay. Numerical experiments cannot prove all-prime nonvanishing: the written cyclotomic proof does that. The Weil bound used for spectral separation is a classical theorem cited in RESULT.md; the checker does not certify that theorem.

No outside dataset, private file, or unstated checkpoint is needed for replay. Independent mathematical verification has not been performed.
