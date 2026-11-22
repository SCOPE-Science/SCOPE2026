---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The four-point failure events split into four disjoint triangle-containment alternatives. For fixed x at radius r, q(r)=1−I(r)−3A(r)/π, with A(r)=4/(3π)(1/3+r²/2−r⁴/8+r⁶/48) from the exact pair-line Jacobian; independently verified A(0)=4/(9π), A(1)=35/(36π), and mean triangle area 35/(48π), giving Q(D)=1−35/(12π²). At r=0, I(0)=1/4 yields S(0)=1−19/(3π²)>0. For r→1, I(r)≤4√2(1−r)^(3/2)/π by the circular cap area, so q(r)−Q(D)=5(1−r)/(2π²)+O((1−r)^(3/2)), yielding S(r)<0 at r≥.99 and slope −10/π². The exact normalized-measure mixture μ=(1−h²)ν_h+h²τ_h gives S=4[Q(D)−q(r)] for each fixed center, with no uniform near-boundary moving-center error claim. Monte Carlo scripts were read but are not substituted for these proofs.

## originality

PASS

Best-of-knowledge originality relative to compared statements and actual independent material, not a proof of absolute priority. The problem can be rewritten as the fixed-vertex four-point q(r) crossing the full-disk Q(D), which requires A(r) as well as I(r). Known I(r) alone cannot give the near-rim opposite sign.

## value

PASS

The sign of the small-hole susceptibility of Sylvester four-point convexity unexpectedly reverses with the puncture position, answering a natural nonconvex stochastic-geometric sensitivity question. The exact center coefficient and near-boundary sign/slope together provide a motivated structural boundary and not merely an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
