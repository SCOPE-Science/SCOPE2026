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

The finite-length formula was independently reconstructed by conditional entropy and by direct enumeration of each binary word and first-stage reveal set. The executable `checker.py` (Python standard library) tests 125 finite scenarios, lengths 2–6, and reports a largest absolute discrepancy of approximately \(4.44\times10^{-15}\). It also verifies sampled positivity of the exact rational second-derivative expression and illustrative small-transition-noise scaling.

The actual infinite-chain proof does not rely on enumeration. Its critical analytical checks are: the absolutely convergent positive-geometric expansion of binary mutual information; the factored positive second derivative; the Markov-bridge conditional-entropy identity; the local-uniform, square-root rescaling of the geometric flank distances; and the Gamma–uniform identity yielding coefficient one. The logarithmic entropy remainder has expectation \(o(\sqrt\delta)\) at \(p\asymp\sqrt\delta\). Convexity then transfers the limiting optimizer and value.

Checks do not establish priority over every unindexed reference and are not an independent audit.
