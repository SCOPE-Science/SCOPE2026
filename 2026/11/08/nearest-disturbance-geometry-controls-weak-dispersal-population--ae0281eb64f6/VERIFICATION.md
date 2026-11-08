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

# Reproducible checks

The included `verify.py` is standalone Python 3 standard-library code. Run `python3 verify.py`. It builds weighted Laplacians using exact rational arithmetic, independently solves the stationary covariance Lyapunov equation coefficient-by-coefficient in the migration parameter, and compares those coefficients against shortest-path formulas.

Four networks were tested: a three-vertex one-source path, a four-vertex two-source diamond with asymmetric edge weights, a five-vertex two-source path with unequal source intensities, and a five-vertex one-source network with two competing shortest paths. The run produced 46 exact diagonal/pairwise checks, including 24 pairs sharing a nearest source and five pairs with disjoint nearest-source sets. Every coefficient below the predicted first nonzero order vanished, and the coefficient at that order equaled the theorem's prediction. A three-patch path yielded exact squared limiting correlations \(1/2\), \(1/6\), and \(3/4\) for pairs \((0,1)\), \((0,2)\), and \((1,2)\), respectively.

The formal checks are finite examples, not exhaustive verification of arbitrary-size graphs. Infinite-uniform generality comes from the semigroup shortest-path argument and integrated Taylor remainder bounds in RESULT.md. None of the output constitutes an independently executed scientific audit.
