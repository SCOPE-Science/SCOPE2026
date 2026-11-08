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

# Mathematical verification and scope

The proof is in `RESULT.md`. Run `python3 check.py` with Python 3 and no dependencies beyond the standard library. At preparation, the checker returned `PASS 313 exact assertions` and independently evaluated the explicit three-label mixture by summing exact multinomial occupancy probabilities for sizes 2 through 26. The formula-based conditional-covariance computation agreed for each of those sizes. Exact sample-size-seven and sample-size-22 rational values, strict signs of the prescribed finite examples through 120 observations, and the limiting two-component covariance were checked.

Correctness does not rest on this finite computation. Integer-convexity occupancy bounds prove the distribution-free n≤6 result, a two-profile algebraic comparison proves the all-n≥7 negative cases, the two-label identity proves the alphabet lower bound, and de Finetti mixture conditioning plus bounded convergence establish the infinite-exchangeability claim. The complete list of possible nonzero richness levels is explicit.

**Limits:** No earliest negative size for all infinitely exchangeable three-label mixtures is asserted. Negative finite exchangeability does not imply infinite extendibility. The source comparisons do not certify historical priority. This is a self-reviewed mathematical result; independent audit has not been performed.
