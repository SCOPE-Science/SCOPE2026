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
# Verification evidence

Run `python3 checker.py` with the standard Python library. It exhaustively enumerates every normalized real Fourier zero for each of 816 integer-step/Bernoulli-fairness masks, computes exact rational difference membership and largest clique of the resulting finite graph, and independently verifies both the predicted size \(2^r\) and the proposed explicit frequency cube. Output: `PASS 816 finite masks: exhaustive rational-grid cliques, construction, and 2-adic formula`.

The full proof does not use experimental extrapolation. The Fourier-product calculation is exact; the upper bound follows by induction on the number of permitted 2-adic valuation shells and the two residue classes modulo the next dyadic power; the lower bound is certified by exact odd-integer phase tests. The verification runs all possible real differences in each finite instance because any candidate orthogonal family may be translated to include frequency zero and its other frequencies then must lie in the Fourier zero set; integer-step measures have frequency period one.

Limitations: checked finite examples are not exhaustive over all parameters; the 2-adic proof is the all-parameter certificate. No independent external mathematical audit has been performed.
