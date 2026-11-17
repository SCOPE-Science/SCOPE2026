---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS: With reflected Brownian generator D∂xx, boundary local time D times the near-boundary occupation density, and independent rate-r Poisson jumps relocating only position, the Neumann boundary resolvent is e^{-x√((s+r)/D)}/√(D(s+r)). The rank-one reset resolvent gives G^r_s(0,0)=[1+(r/s)A(√((s+r)/D))]/√(D(s+r)). At X=0 when local time grows, strong Markov and Poisson memorylessness make inverse local time a subordinator; occupation-density inversion yields φ(s)=s√((s+r)/D)/(s+rA). An independent first-contact renewal sum yields initial-μ prefactor (s+r)A/(s+rA); differentiating s↓0 gives exactly both stated means. Inverting the inverse-subordinator LLN gives throughput J=√(Dr)A(√(r/D)). For two reset sites, J=(D/a)F(y), F(y)=y[p e^{-y}+(1-p)e^{-βy}], β=b/a, y=a√(r/D). All interior F' zeros are Hβ(y)=p/(1-p), y∈(1/β,1), H=e^{-(β-1)y}(βy-1)/(1-y). Independently differentiated log H: -(β-1)+1/(y-1/β)+1/(1-y). Its minimum criterion yields discriminant β²−6β+1, cusp 3+2√2, exact three-stationary-point region. Log high/low peak ratio strictly increases with p, with opposite endpoint signs, so exactly one coexistence crossing. Independently bracketing roots reproduces p*(10)=.1228819699964 and rates .020660588845 and .983120201416. Assumes positive R and thresholds ℓ>0; finite checks supplement rather than prove universal uniqueness.

## originality

PASS

PASS (qualified): Bressloff (2022) establishes retained-local-time first-passage means for a SINGLE reset distance and normalizes the same boundary local time. Julián-Salgado–Dagdug–Boyer (2024) show abrupt optimal-rate changes for TWO sites but in the mean first-hitting-time objective with absorbing boundary and different threshold equation. The exact two-site retained-contact throughput, positive-distance ratio 3+2√2, and unique weight-driven coexistence do not follow from either inspected published claim, even though the two-exponential mixture technique and qualitative first-order switching are related.

## value

PASS

PASS: Keeping accumulated local time is a natural surface-reaction memory mechanism; long-run boundary contact predicts completion-time scaling for large local-time demand. The exact universal geometry threshold, bistable optimizing rates and unique mixing-weight switch provide a motivated structural phase diagram and operational reset design insight. It is not merely the old single-site or first-hitting result with changed notation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
