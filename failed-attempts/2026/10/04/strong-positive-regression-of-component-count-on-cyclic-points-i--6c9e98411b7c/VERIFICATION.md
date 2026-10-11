---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The mathematics is correct. Counting the cyclic set, a permutation on it, and the rooted forest gives the stated cyclic-point mass and tail. Conditional on L=m the component count is the cycle count of a uniform m-permutation, so the Bernoulli-sum coupling, strict stochastic increase, and positive covariance for increasing transforms follow. Tail summation gives the exact covariance identity. Birthday scaling gives L divided by square-root n converging to Rayleigh with moment convergence, and H_m equals log m plus Euler's constant plus a vanishing error; this yields the stated covariance constant. The conditional cycle-count variance is H_m minus the second harmonic sum, so total variance is one half log n plus a bounded term and the correlation constant follows. The package's exact enumeration through n=7 is consistent with the analytic proof.

## originality

FAIL

Originality fails under the implication standard. The 2013 Hansen--Jaworski construction explicitly conditions on the number of cyclic vertices and then applies a uniform permutation to those vertices in the uniform case; the same paper gives the sequential cycle construction, whose new-cycle indicators are independent Bernoulli variables with probabilities one over the insertion index. Together with the classical exact cyclic-point law for a uniform mapping, this already yields the audited joint mixture. Strict stochastic regression and covariance positivity are immediate monotone-coupling corollaries. The exact covariance sum and the displayed constants then follow by routine tail summation, the classical birthday/Rayleigh scaling of cyclic points, and the harmonic-number expansion. The final claim is therefore a useful synthesis, but it is mechanically implied by established ingredients rather than an original theorem under the required bar.

## value

FAIL

The two statistics are important, but after the published conditional-permutation construction is recognized, the regression coupling and mixed moments are routine consequences of standard permutation-cycle and birthday asymptotics. Under the required value bar this is a polished consequence package rather than a distinct motivated mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
