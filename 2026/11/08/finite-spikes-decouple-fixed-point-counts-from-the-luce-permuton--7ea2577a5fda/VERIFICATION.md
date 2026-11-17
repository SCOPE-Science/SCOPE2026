---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For fixed m and positive a_i, the exponential-race coupling rescales the m heavy clocks to independent Exp(a_i) and ordinary clocks to a unit-rate Poisson process. Conditional on all exceptional ranks, ordinary labels are uniformly matched to M=n-m positions, so their factorial moments equal (h)_k/(M)_k with M-m<=h<=M. Uniform convergence of the conditional probability-generating function to exp(z-1) gives a Pois(1) component independent of the finite exceptional-rank correction. Conditional hypergeometric rectangle means and O(n) variances give uniform permuton. The finite Markov recursion for H_m follows by competing exponential rates 1 and a_i. Independent exact recursion gives m=2,a=(1,1) PGF (10+5z+3z^2)/18; the one-spike Bernoulli parameter is w_n/(w_n+n-1). The finite check does not replace the n-to-infinity coupling.

## originality

PASS

The precise fixed-m, weights n*a_i limit Pois(1)+H_m and its non-Poisson uniform-permuton counterexample are not implied by the inspected Luce permuton literature or published constant-weight positive-proportion block models. Those assume diffuse weights and do not imply the finitely supported rate-n boundary. Borga–Chatterjee–Diaconis explicitly present fixed-point limit behavior as a question; Resultary homogeneous finite-step blocks have Poisson limits with distinct hypotheses. Best-of-knowledge PASS, not a universal priority certificate.

## value

PASS

The result answers a natural question about fixed points in a canonical ranking model with a sharp obstruction to inferring local coincidences solely from permuton weak convergence. It supplies an explicit computable finite correction and a weight-scale transition, a motivated probabilistic boundary rather than an arbitrary example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
