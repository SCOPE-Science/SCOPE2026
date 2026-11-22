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

# Verification and limits

`CHECKER.py` is standalone Python 3 with no third-party dependencies. Run it from this directory using `python3 CHECKER.py`.

The checker independently enumerates output-packet labelings for \((a,n)=(2,5),(4,5),(4,6)\), and uses exact fractions to compare all \(86\) position–card marginal probabilities against the original two-binomial mixture formula. It also constructs seeded packet-label decks at three fixed packet counts and checks the pathwise equality between extreme-packet correct guesses and the finite geometric-arrival occupation score. It performs coarse normalizations against the analytically calculated limiting mean and variance. This is finite corroboration only, not a proof of asymptotic distributional convergence.

The rigorous argument in `RESULT.md` proves all moments by a Fourier lattice local limit theorem, Markov-factorization occupation-moment expansion, evaluation of a Dirichlet integral, an exponential localization bound, and independence of the two label halves. In particular, no limit assertion is inferred from the checker. The result uses the sufficiently-large-deck optimal strategy established in the cited 2026 primary paper. Independent mathematical validation remains unperformed.
