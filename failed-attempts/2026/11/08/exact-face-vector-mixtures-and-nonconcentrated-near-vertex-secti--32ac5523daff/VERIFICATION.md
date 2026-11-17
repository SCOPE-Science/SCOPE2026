---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For 0<h<1 the plane separates p=1+#(|G_i|>h|G_d|) antipodal coordinate pairs. Counting simplex faces crossing positive/negative sides yields 2^r binom(d,r)-binom(p,r)-[z^r](1+z)^p(1+2z)^(d-p). Conditional Bernoulli sampling given |G_d| produces the half-normal mixture. At h upwards to 1 the Gaussian rank is uniform, yielding stated moments. For h_d→h_*>0, conditional binomial L2 law and bounded vertex counts prove Q(2-Q) limit and displayed CDF. Independent full signed-face enumeration matched every rank for d=3..6, all possible p. No gap found.

## originality

FAIL

FAIL: The Nov 1 full prior theorem gives exactly the same all-face polynomial (after expanding its (1+2z)^d expression), same conditional Gaussian-binomial integral, same one-sided near-vertex uniform law, identical vertex means and variances. The remaining high-dimensional nonconcentration is a routine conditional LLN and continuous-mapping corollary of that preexisting mixture, including its CDF by elementary inversion.

## value

FAIL

FAIL as new result: the submitted finite joint-law theorem and limiting moments reproduce the full published Nov 1 calculation; the h_d→h_* nonconcentration is an immediate standard-law-of-large-numbers consequence of its explicit conditional binomial representation, not a separately motivated unknown invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
