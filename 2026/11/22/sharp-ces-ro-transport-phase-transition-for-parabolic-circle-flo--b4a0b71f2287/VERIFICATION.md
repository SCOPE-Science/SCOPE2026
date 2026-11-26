---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reconstructed RESULT.md lines 55–87 and inspected the package's analytic VERIFICATION.md. The speed is globally Lipschitz for γ≥1/2 and its reciprocal has divergent integrals at both ends of the punctured circle. In the resulting global time coordinate, the geodesic distance profile is even and strictly decreasing on the positive half-line. The pointwise Lipschitz upper bound is attained simultaneously at all starts by the scalar-matrix distance observable. Differentiating the sliding-window integral shows its unique maximum is centered at the antipode in time, not in angular displacement. Substitution back to angle gives the unique cutoff and integral with factor 2/T. For γ<1, s/v(s) is integrable; at γ=1, the profile 2 arctan(1/w) yields the displayed finite-time formula and leading 4 log(T)/T. For γ>1, the tail is (2^γ/((2γ−1)w))^β where β=1/(2γ−1); integrating to T/2 gives the stated Cγ. At γ=1/2 the profile is 4 arctan(exp(−w/√2)), whose time integral is 4√2 times Catalan's constant. The uniform operator norm 2 follows from a continuous separator with values in [−1,1] for the fixed point and one compact finite nonfixed orbit segment; uniformly bounded residence time outside any small neighborhood gives strong convergence for each continuous observable, not convergence in operator norm. No finite simulation is needed.

## originality

PASS

Best of current evidence, the sharp finite-time geodesic-Lipschitz norm, worst phase and quantitative three-regime profile are distinct. The γ=1 model and qualitative convergence are prior, the general transport reduction is standard, and the auxiliary norm-two fact is a direct support-separation observation, not an independent novelty basis.

## value

PASS

Starting from a concrete qualitative mean-ergodic example, the result answers a natural quantitative question: how large can the finite-time error be on a Lipschitz ball, and where does it occur? The exact time-window solution captures a change from integrable residence profile to logarithmic and power-law regimes, with computable constants and the same extremizer for every matrix dimension. This is a stronger quantitative distinction than the absence of full operator-norm convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
