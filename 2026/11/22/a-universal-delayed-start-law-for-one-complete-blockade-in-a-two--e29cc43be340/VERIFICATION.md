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

# Verification and reproducibility

The analytic argument in RESULT.md proves the theorem for the entire stated domain. No finite numerical test replaces the uniqueness, all-rate quantifiers, duration monotonicity or limiting arguments.

The standalone standard-library script `checker.py` was executed using `python checker.py` and reported: `All 1231 checks passed (including independent piecewise-ODE integration).` Its strict example uses rational identities; its second implementation integrates the latent, infectious, and transmitted forward probabilities under the piecewise transmission control. The script also checks random strictly positive rate triples, the coincident-rate limit, strict delays, optimality against sampled starts and strict advancement of the best start with longer blocks. Random generation uses a fixed seed.

The exact example has \(\alpha=\beta=2\), \(\gamma=1\), \(L=\log2\), \(s_*=\log(6/5)\), optimal target infection probability \(307/648\), and immediate-block infection probability \(1/2\). Their difference is \(17/648\). This is a finite exact certificate, not a claim that numerical sampling exhausts the continuous parameter domain.

Reproduction assumptions: Python 3.10+ standard library and the two locally supplied files `checker.py` and `RESULT.md`. No data downloads or external executables are necessary. Timing, biological realism and historical-priority limitations appear in RESULT.md and REVIEW.md. Independent verification has not been performed.
