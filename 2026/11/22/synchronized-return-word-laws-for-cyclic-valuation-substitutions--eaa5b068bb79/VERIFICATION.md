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

The claim is proved symbolically for every integer base \(b\ge2\), modulus \(q\ge2\), and symbol \(r\in\{0,\ldots,q-1\}\). `check_returns.py` directly enumerates \(4{,}549{,}860\) consecutive return occurrences across 140 parameter triples, comparing all observations with the independently generated theoretical return words and checking synchronization of all observed type prefixes. `check_morphism.py` constructs the fixed point by substitution and independently as a divisibility sequence, then checks the exact transduction and rational mean-return calculations across 30 pairs and \(5{,}107{,}077\) derived symbols. Captured output is in `check_returns.log` and `check_morphism.log`.

The finite checks do not prove that all return types occur for each unbounded parameter choice, nor do they prove natural-density convergence. Those statements are established in the proof by the structure of the complement of the valuation-zero shell and by geometric divisibility-class densities. No independent scientific audit has been performed.
