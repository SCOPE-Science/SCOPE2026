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

# Reproducibility and verification

Run `python verify.py` with Python 3 and `mpmath`. The verification program independently samples the actual cotangent-transformed angular formula and evaluates the closed Fourier alias expression on three mixtures for node counts from 1 to 23; independently solves the odd exactness and even stationary equations; checks closed one- and two-node cases; checks a positive convexity factor; and tests two-scale exact identities and geometric endpoint asymptotics. The actual execution returned **PASS 1898 checks**.

The proof in `RESULT.md` is the evidence for existence, uniqueness, and all-node asymptotic assertions: the tests cover only finitely many cases. In particular, high-precision checks do not certify uniform error bounds or independently verify publication priority. The exact angular value at the cotangent endpoint is retained, not replaced by zero.

Independent scientific audit has not been performed.
