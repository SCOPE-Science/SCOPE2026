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

# Reproduction and limits

Run `python3 verify.py` from the directory containing the extracted files. The program uses only Python's standard library (`fractions`, `itertools`, `random`), constructs the exact diagonal Markov generator for the ordered-arc two-body exchange plus the local anchor jump operators, and verifies the first-moment generator identity for every configuration of each tested finite system. It checks the two distinct rational three-agent examples, followed by 48 pseudo-random row-stochastic directed matrices with two through five agents, including zero and full stubbornness values.

The analytic proof in RESULT.md separately verifies the two-qubit adjoint operator identity on the entire Hilbert space and extends it to every finite network, including correlated quantum initial states. The checker does not certify all sizes or quantum coherences; the extension follows from the local operator algebra. Classical symmetric-exclusion moment closure is acknowledged as prior theory. No independent scientific audit was performed.
