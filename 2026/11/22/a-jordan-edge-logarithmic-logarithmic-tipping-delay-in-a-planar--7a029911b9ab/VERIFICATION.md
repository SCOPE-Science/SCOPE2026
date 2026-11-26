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

Eliminating y gives x_{−1}=0 and x_{n+1}=τ_±x_n−δx_{n−1}+μ with branch selected by x_n. With q=μ/α the formal incoming deficit is q−x_n=Aλ^n+Bρ^n for distinct roots, with A=(λ(h+q)−δq)/(λ−ρ)>0 and limit hλ/(λ−ρ). At δ=t² the matrix is defective (off-diagonal entry 1), and the two initial values give q−x_n=[h+q+n(h+(1−t)q)]t^n. In either case the formal deficit stays positive, tends to zero, and all fixed indices remain negative in x as q→0. Thus the actual switch agrees with the first crossing N of this formal deficit below q. Adjacent deficit ratios at N are bounded away from zero and converge to the appropriate stable root, even as q varies. They bracket the threshold, making both x_N and x_{N−1} O(q). At the Jordan edge, the bracket in the deficit divided by hN equals 1+(1−t)q/h+(1+q/h)/N, tending to 1. Consequently aN−log N=L+O(1), a=|log t|, which first implies N∼L/a and then N=(L+log L)/a+O(1). The simple-root case instead has N=L/|log λ|+O(1). On the outgoing side, x_{n+1}−x_n=αx_n+δ(x_n−x_{n−1})+μ is positive inductively, including exact x_N=0. With u=x+q, the unstable coefficient is (γu_0−δu_{−1})/(γ−ζ), bounded above and below by positive multiples of q since u_0≥q and u_{−1}<q; the stable coefficient is O(q). The first outgoing crossing therefore takes L/log γ+O(1) steps. This verifies actual discrete passage, not an inadmissible branch extension. The frozen code and supports were inspected but the code was not executed.

## originality

PASS

The map and virtual-fixed-point divergence are known. The contribution is the actual fixed-section two-flight passage estimate with a bounded remainder and distinct correction at a stable double multiplier, not Jordan matrix algebra by itself or a claim about nonlinear folds generally.

## value

PASS

There is a meaningful quantitative gap between no bounded invariant set and the residence time starting at a fixed section. The natural discriminant boundary changes that time by a diverging positive log-log term, not just a bounded offset. The bounded remainder and first-passage control make the comparison usable for the specified affine map. This does not assert robustness to nonlinear feedback or uniformity near the discriminant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
