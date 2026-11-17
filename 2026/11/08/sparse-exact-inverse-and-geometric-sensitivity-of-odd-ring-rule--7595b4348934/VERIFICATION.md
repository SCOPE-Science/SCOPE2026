---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The indexed Rule-45 Boolean identity yields x_i=1 XOR y_{i+1} XOR y_{i+2}x_{i+2}; iterating around an odd cycle and using the terminal forced-alternation contradiction closes without division. Finite injectivity proves a global inverse for all outputs. Expanding its nested prefixes gives exactly n+1 squarefree monomials and degree (n+1)/2, while conditioning on independent uniform bits gives influence sequence 1,1/2,1/2,1/4,1/4,..., with all n variables essential. Independent exhaustive maps/influences checked every output of odd n=1,3,5,7,9, not used as the general proof.

## originality

PASS

Previously known odd-ring Rule 45 bijectivity does not determine the all-n inverse coordinate polynomials or their exact independent-uniform Boolean derivatives. A 2022 inverse search discusses low lengths only. Related 2026 quadratic-five-neighbor classification covers reversibility, not these inverse invariants. Best-of-knowledge novelty is qualified because the most directly relevant full thesis was inaccessible this run.

## value

PASS

For a natural nonlinear cellular automaton reversible precisely on odd rings, explicit linear-size inverse circuitry together with sharp radius and bitwise influence spectrum gives structural information unavailable from mere bijectivity. It separates global dependency from strongly nonuniform random-bit sensitivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
