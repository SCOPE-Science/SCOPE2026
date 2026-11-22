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

# Verification of the clipped-Gaussian mortality theorem

Run `python check_reentrant.py` using Python 3. The script uses exact rational arithmetic to verify the finite Taylor bounds \(0.238<\Phi(-0.71)<0.240\) and \(\varphi(0.71)<0.312\), then proves the strict rational lower bound for \(D(1)\). Its optional `mpmath` integration estimates the two phase-crossing intensities; those estimates are **not** part of the infinite mathematical proof.

The proof of unique unimodality is analytic. In the exact derivative formula in RESULT.md, the positive contribution has support \((0,A-\varepsilon)\) and the negative contribution has support \((A-\varepsilon,\infty)\). Differentiating the logarithm of their ratio with respect to inverse variance proves strict increase of the negative-to-positive ratio with noise intensity; endpoint limits force a unique crossing. The mortality limit follows by dominated convergence.

The source's mean-field density closure, not a theorem about the spatial random process, converts death probability into a predicted growth sign. We verify the distinction between zero-noise, intermediate-noise, and high-noise signs. Nothing here proves an actual stochastic lattice survival transition, the accuracy of the closure outside small noise, or historical novelty.
