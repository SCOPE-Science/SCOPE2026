---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The gauge with h=v/(2D) yields the symmetric Robin pair (h,−h) and energy E in the original. For all u∈H¹, sup|u|²≤L^(−1)||u||²+2||u||||u'||, so finite measure perturbations are infinitesimally form bounded and the top eigenvalue is attained by compactness. Independently, the Green kernel of the positive free operator at zero is exp(−h|x−a|)/v: the derivatives meet the two Robin conditions and the derivative jump is −1/D. Hence the sharp evaluation norm squared in E is 1/v at every a, with equality only for a multiple of that kernel. This agrees with the original square identity, including at endpoint evaluations. Taking a maximizer of |u| bounds the measure term by (B/v)E; the stronger bound λ≤−(v−B)/L for B<v follows directly from E≥v||u||∞² and ||u||²≤L||u||∞². At B=v equality is attained only by a multiple of the peaked exponential and forces the measure to be supported at its unique maximizer; endpoint peaks cannot support the given nonzero measure on (0,L). A critical interior atom does attain zero, and testing with its peak gives the positive sign for β>v. For a supercritical atom, q=√(h²+λ/D)>h and the matched logarithmic derivative g of the positive interval solution satisfies g(0)=h, g'=q²−g²>0 and g''=−2gg'<0. Thus g(a)+g(L−a) increases strictly toward the center for fixed q, while its q derivative is positive by the linearized Riccati equation. The scalar jump condition gives the strict opposite order of λ and reflection symmetry. Finally, at D=.01 and v=L=1 the free constant shift gives λ(2 dx)≤2−25=−23, in contrast to positivity for the same-mass atom. The threshold in B is sharp; no sharpness is claimed for the entire quantitative bound below it. The supplied checker was inspected, not executed.

## originality

PASS

Pass for the joint spectral conclusion in the matched drift/Robin problem: the exact critical mass for the whole positive-measure class with its equality characterization, and the strict position law for supercritical attractive point interactions. Prior transport, variational and point-interaction methods are credited. The sources actually inspected do not supply this equality and location statement as a known specialization.

## value

PASS

The result resolves whether an integral constraint alone can imply a nonpositive spectrum in the fixed transport problem, gives the precise equality case among measures, and exhibits opposite principal-eigenvalue signs at one and the same above-threshold mass. The strict location comparison adds information not recoverable from the critical mass. These are exact spectral benchmarks rather than a discretization or a claim about biological realization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
