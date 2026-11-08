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

# Verification record

The reproducible source is `verify.py`, executed with Python 3 and SymPy using the command `python verify.py`. It exited successfully with the message `PASS: 95 exact/symbolic/finite-sample checks`.

The checker uses exact rational numbers for the images of 48 dyadic cells under the two affine maps and for four rational-bias versions of the return and mean formulas. Symbolic power-series computations test the first seven coefficients of the occupation pgf at \(p=3/4\), its normalization, and its mean. Direct evaluations at four small positive bias values and three Laplace parameters check compatibility with the crossover law. Seeded Monte Carlo draws for two offcritical biases test four return-count frequencies and the occupation mean against explicitly declared tolerances. An independent sample directly iterates the two interval maps (rather than the cell chain) and checks occupation means and first-return probabilities.

The full proof is mathematical: exact conditional cell uniformity, Markov-chain first-passage, resolvent identities, and limiting Laplace transforms. Finite checks do not establish the infinite-horizon laws. The right/left reflection and endpoint exponent use the analytic argument in `RESULT.md`. The experiment does not test or claim uniform numerical precision in the singular limit or provide a quenched trajectory theorem.

No independent audit or external validation has been performed.
