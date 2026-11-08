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

# Reproducibility and checks

Run `python3 verify.py` using Python 3 standard library. The program constructs full binary-spin and two-coordinate continuous-time Markov generators independently and solves their absorption equations exactly over rational numbers for the first five nontrivial sizes. It checks the stopped-magnetization identity and a uniform excursion bound exactly at those sizes, with additional explicit no-switch inequalities for larger instances. The observed test summary is `PASS 34 exact/rational or numerical inequality comparisons`.

Analytical checks, not computational extrapolations: first-copy times are independent exponentials in the hub-fixed case; at a fixed leaf, every fixed-center spell terminates its current excursion with conditional probability at least \(e^{-2}\) and duration of mean at most \(H_n\), the generator satisfies \(\mathcal LM=(1-h)/(2(n+1))\), and geometric renewal yields the limiting exponential law. The stated conclusions require the precise rate-one node-update normalization.

This work has undergone self-review only; the finite checks are neither an independent audit nor an infinite certification. No external audit evidence is asserted.
