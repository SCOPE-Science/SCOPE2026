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

# Reproduction and boundaries

The proof is self-contained in `RESULT.md`. Its pivotal verifiable identities are the overlap decomposition (1), the differentiated first-hit generating function (2), the bounded-ratio integral (3), and the strict inequality for \(t=z/s<1/2\). The independent finite checker re-evaluates border-sign predictions over finite alphabets, and compares numerical first-hit integrals with a prefix-automaton dynamic program.

Execute `python checker.py` with Python 3 and SciPy installed. The checker does not replace the infinite symbolic argument. No separate human or external audit has been performed.
