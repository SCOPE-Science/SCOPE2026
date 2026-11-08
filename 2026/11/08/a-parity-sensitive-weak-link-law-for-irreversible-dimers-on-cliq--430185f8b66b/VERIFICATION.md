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

Both standalone programs use only Python 3's standard library and exact fractions for finite identities. Run `python3 verify_direct.py` to compare the reduced bridge recurrence against a separately constructed graph-level Markov recursion over every available edge. The same graph-level recursion independently checks the entire jammed dimer-count distribution. This gives 72 exact comparisons for clique orders between 2 and 6 and several rational bridge rates.

Run `python3 verify_laplace.py` to construct the pure-death transition probabilities of isolated complete graphs, integrate the two survival functions by partial fractions, and compare all results to the reduced first-edge recurrence. This gives 588 exact rational comparisons for clique orders 2 through 15 and three bridge rates. The program separately checks residual hub survival and prints illustrative finite-size convergence values for size ratios 1, 2, and 3.

The analytic proof in RESULT.md establishes statements for every integer clique size and all positive real rates. Finite exact comparisons are consistency checks, not exhaustive enumeration over infinitely many graph orders or proof of the scaling limits. The proof's rescaled martingale argument, expectation comparison bound and dominated-convergence decomposition are needed for the asymptotic results. The source comparison includes fully read material for arXiv:cond-mat/0611413 but only abstracts for two older possibly relevant works. Independent scientific audit has not been performed.
