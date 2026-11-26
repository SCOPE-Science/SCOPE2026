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

For s=t−ρ the bounds put s strictly between H(t−2ρ) and H(t), both in the history/trajectory domain. Thus the continuous strict inverse defines a continuous retarded argument. With H(d)=s, sign(g(d))=sign(s−d), and strict order gives sign(s−d)=sign(H(s)−H(d))=sign(Ψ(g(s))); this works at zero even if the relay takes an independent value there. It gives the reference equation almost everywhere. On each compact forward interval a competitor's continuous positive delay has a positive minimum. Advancing in steps shorter than this minimum forces each competing algebraic root to be evaluated on the already agreed history; injectivity of H identifies the reference root. Equality of right-hand sides almost everywhere and absolute continuity propagate equality of states, then roots, on the whole interval. This needs no order assumption on the competitor. The one-sided slope criterion gives H(v)−H(u)≥(1−q)(v−u). I checked the periodic pieces glue, their slopes are 0, 2 and −1/2, and the forcing can be set to zero at the corners to make it bounded and periodic. For all s in (0.24,0.26), the nested arguments are s, −s, 3s, s−1 and then alternate s+1 and s−1, by the plateaus of g; even samples are negative throughout that interval. The implicit root there is s/3 with positive sample, as is the constant-delay sample. This proves a discrepancy on an interval, not a single exceptional time. The frozen witness checker was read, not executed; the interval calculation verifies the witness analytically.

## originality

PASS

The inverse-coordinate technique, implicit invisibility under contraction, temporal order under contraction, and local nesting cycles with implicit uniqueness are credited. The distinct contribution is global equality and uniqueness for the implicit nonsmooth relay along a bounded monotone reference coordinate beyond contraction, with a separating periodic forced example. No verified source subsumes that combination.

## value

PASS

The condition distinguishes well-posedness and unchanged dynamics of the implicit model from success of the natural nested iteration. It is verifiable on a reference history and admits positive slopes forbidden by contraction, while the explicit periodic example forces an actual wrong relay response on a time interval for each even nesting order. This is a usable extension and a concrete warning about substituting nested equations, not a claim about arbitrary nonmonotone branches or physical sinusoidal forcing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
