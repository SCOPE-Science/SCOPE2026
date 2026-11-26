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

With y=v−x the scalar equation is cos x+P_v(x)/R³=q, with P_v=x(x−v)²−x. On rescaling, the two level equations have single real roots near the nonzero limiting endpoints; the extrema of the perturbed cubic have rescaled values O(R⁻³), away from either level. The nonvanishing endpoint slopes give O(1) localization shifts in x and an inner margin c/R, uniformly on the stated compact sets. In each complete π-cell the endpoint signs alternate and all roots are simple and have the same crossing direction, since |sin x|≳R⁻¹ᐟ² dominates the O(R⁻¹) cubic derivative. The leftover endpoint regions must include any partial inner π-cells (at most π extra per end); splitting into π/4 cells gives at most two zeros per cell by first or second derivative, so this minor bookkeeping omission has no effect. Matching inner roots to their cells and renormalizing the O(1) leftovers gives W₁=O(R⁻¹), including the v/R shift in y. The oriented triangular coordinate change, cubic tails uniform for bounded v, and real analyticity give properness, degree +1, surjectivity and finite fibers at β>0. Fixed points force x=0 and then x′=α; at β=0 the scalar cosine has precisely the asserted strip and infinite fibers. The finite checker is supplementary, not a proof or a formal certificate and was not executed.

## originality

PASS

On the inspected evidence, the exact target-dependent global one-step inverse count with bounded error and the quantitative all-preimage distribution are distinct from the published forward-orbit and different-map inverse laws. The map and fixed-point-free feature are not claimed as new.

## value

PASS

The result quantifies both the number and the spatial distribution of branches lost to infinity in a singular proper-to-nonproper limit, including for targets outside the limiting image. The explicit target dependence, bounded count error, and quantitative distribution are useful beyond showing noninvertibility. The two exceptional target lines and forward dynamics are out of scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
