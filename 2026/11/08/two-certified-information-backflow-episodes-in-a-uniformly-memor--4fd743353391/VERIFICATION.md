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

The theorem reduces to four strict inequalities for \({}_1F_1\) at exact rational-complex parameters. `verify.py` independently reconstructs the Kummer Taylor series using exact Gaussian-rational arithmetic, bounds the infinite series remainder by an explicit geometric tail, and compares each squared trace distance with its stated rational threshold.

To reproduce: run `python3 verify.py`. It requires only Python 3's standard library. The mathematical reduction of the qubit trace distance to the modulus of the coherence multiplier is given in `RESULT.md`. Finite sums with explicit infinite-series remainder bounds are rigorous certificates for these four inequalities, not merely sample plots. The verifier does not certify a global optimizer, a full non-Markovianity phase diagram, or a precise total BLP integral. No independent audit has been performed.
