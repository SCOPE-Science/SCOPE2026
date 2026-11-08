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

# Verification of stated scope

The proof in `RESULT.md` independently derives each claimed stochastic limit from the exact deposition transition probabilities; it does not assume a general limit law for this adsorption regime. Every claim uses integer arrays \(n\to\infty\), \(k\to\infty\), \(0\le u<n\), \(u=o(n)\), with the stopping event being exactly \(n-u\) accepted proposals and with rejected proposals counted in time.

The normalizing probability is exactly \(\pi=\binom{k(u+1)}k/\binom{kn}k\); both the finite-parameter mean and variance identities and the upper bound on consecutive waiting weights were rederived. In the bounded-ratio regime, convergence of each fixed weight, a summable tail and convergence of the first two normalized moments were checked algebraically. For diverging \(u/k\), the proof uses power sums for orders one, two and three, verifies that the last included index tends to infinity on the scale \(r/k\), and invokes the standard Berry–Esseen inequality for independent centered geometric waits to obtain the advertised error. The limiting infinite-product law is not claimed to be a new abstract distribution.

A standalone Python 3 standard-library checker `verify.py` was executed from the packaged path and printed `PASS 2249 exact and diagnostic assertions`. Its finite checks enumerate admissible proposals, compute absorbing-chain hitting-time probabilities, independently convolve geometric waits, compare exact means and variances, and numerically stress-test the asymptotic weight profiles. The finite test has bounded parameters and cannot certify the infinite-array asymptotics.

The source-first-public date comes from the arXiv version history of arXiv:1908.00940, August 2, 2019, and not the later journal publication date. Historical priority and expert validation remain unresolved; see `REVIEW.md` for closest sources and risks.
