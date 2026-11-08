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

# Reproducibility and limits

Execute `python3 verify.py` using the Python standard library. It checks the independently integrated Gaussian absolute first moment and its closed form over five exponent choices; the conversion between the Pareto waiting-time integral and a uniform variable; and exact conditional reward-tail and truncated-moment identities for 25 specified parameter pairs. The recorded run returned `PASS: 77 deterministic algebraic and quadrature checks`. These finite checks cannot certify the limit law, which is established analytically in RESULT.md.

The proof additionally invokes standard named facts (von Bahr--Esseen inequality for \(1<p\le2\), Lévy--Khintchine one-stable domain-of-attraction theorem, finite-mean renewal-age tightness, and both Borel--Cantelli lemmas). It assumes no independence between reset count and cycle rewards. The input paper's physical model parameters are normalized to unit reset cutoff and unit diffusivity; translation to other fixed scales is by Brownian scaling. No independent audit has been performed.
