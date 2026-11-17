---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

One-node SLQ outputs 2 log(m(1±r t)) with fair signs, so exact mean bias B(t)=log((1−r²t²)/(1−r²)) and variance U(t)^2/N. Derivative sign governed by H(t)=U/(rtB), strictly increasing from 2/B0 to infinity. This proves unique interior minimum only when N>2/B0, no interior maximum, worst endpoints switching at (logκ/B0)^2 with all equality cases; trace MSE is exact across every orientation, integer N and distinct SPD eigenvalues. Independently evaluated finite two-sign distribution, variance and endpoint inequalities; finite checks do not prove continuous result.

## originality

PASS

Best-of-knowledge new exact MSE classification for fair-sign one-node SLQ in dimension two, with both global worst-orientation and best-orientation sampling thresholds; primary SLQ and trace literature supplies method/tail estimates, not exact two-point optimization; 3D expectation theorem differs in dimension and loss. Possible identical Bernoulli-model calculation in specialist literature remains a risk.

## value

PASS

Exact sharp mean-squared risk thresholds in the one-node SLQ estimator isolate bias-vs-sampling tradeoffs and explain when additional independent sign probes change worst/best orientations. This is a genuinely motivated numerical linear algebra benchmark, not generic estimator normalization or a claim of large-scale optimal algorithm design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
