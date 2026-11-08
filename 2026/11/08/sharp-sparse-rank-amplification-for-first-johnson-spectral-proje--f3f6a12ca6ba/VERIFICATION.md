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

Run `python verify_johnson.py` using Python 3 and no third-party dependencies. The program calculates exact rational hypergeometric point masses and their absolute centered first moments, compares the norm formula for all integers \(3\le n<90\) and \(1\le k\le\lfloor n/2\rfloor\), verifies the one-boundary flux identity, and checks exact matrix idempotence on a sample of smaller slices. It also checks the first 100 Poisson peak heights for strict descent and prints finite-rank maximizers in several large dimensions.

The successful run printed `JOHNSON_EXACT_KERNEL_FLUX_IDEMPOTENCE_CHECKS_PASSED 1979` and `JOHNSON_POISSON_PEAK_ORDER_PASSED 100`.

All computations run from the standalone embedded file. Exact arithmetic certifies only the finite cases actually tested. The proof of all dimensions, the Stirling regime and the uniqueness of the asymptotic maximizing rank is analytical and is fully stated in `RESULT.md`. A uniform finite-dimension error bound and an exact finite-dimension optimizer are not claimed. No independent mathematical audit has been performed.
