---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Convex parabola chord geometry gives success iff nearest opposite-sign magnitudes st<=c<=uv for extreme magnitudes u,v. Failure decomposes into insufficient extreme product and central gap st>c. Integrating joint order statistic densities yields the displayed A_m/B_m and P_m=1-A_m-B_m. Independent SymPy integral evaluation produces P3=(3c/2)(log(1/c)-1+c) and P4=2P3. Boundary Laplace for f(v)=(v+c/v)/2 yields A_m~[2/(1-c)]((1+c)/2)^m, while unique interior saddle of g(s)=1-(s+c/s)/2 yields B_m~sqrt(pi*m*sqrt(c)/(2(1-sqrt(c))))*(1-sqrt(c))^m. At c*=3-2sqrt(2), bases tie but sqrt(m) dominates. Verified symbolic low-m formulas and inspected verifier; not a uniform near-endpoint theorem.

## originality

PASS

PASS with strong chronological qualification: November 1 general-c exact feasibility/exponential rate and November 2 c=1/3 exact prefactor cover large portions, but not the generic-c sharp prefactors. A fully equivalent Jacobi-family theorem is currently published, and its parameter tau=1/(2alpha+3) ranges all c; Git source import of assigned result at 2026-11-08T22:51:25Z PRECEDES Jacobi source import at 2026-11-08T22:54:22Z and that publication 2026-11-09T01:09:49Z. Timestamp order is only observed repository chronology, not independently established scientific priority; no claim of independent discovery. Judgment passes distinct all-c asymptotic refinements at the earlier evidenced source snapshot, with this significant residual originality risk.

## value

PASS

The sharp coefficient and sqrt(m) critical amplification improve mere exponential-root bounds in an iid positive cubature feasibility problem; all c∈(0,1) is a motivated target moment continuum and the mechanism crossover is mathematically structural. Independent of novelty chronology, exact finite-m probabilities and leading-order failure costs are reusable sample-complexity benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
