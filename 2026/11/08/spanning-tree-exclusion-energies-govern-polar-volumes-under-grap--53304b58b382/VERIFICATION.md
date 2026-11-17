---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: For fixed connected simple H with e edges, v vertices and g=e-v+1, replacing every edge by m segments yields edge-difference cube section ker B_m. Chord segment coordinates provide the unit anchored Jacobian and W_m=2^(me)f_{B_m U}(0) with W_m=sqrt(N_m) intrinsic-volume normalization. Fundamental cycles repeat columns m times, and log sinc(u)=-u²/6-u^4/180+O(u^6), after t=sqrt(3/m)Q^(-1/2)z, yields relative first correction -3/(20m) sum_f(b_f^TQ^-1 b_f)^2. Cauchy-Binet gives det Q=tau(H), uniform subdivision gives tau(H^(m))=m^g tau(H), and the cycle-space projector diagonal is r_f=Pr(f excluded from uniform spanning tree). The claimed exact tree case follows with g=0. Independently evaluated exact rational Irwin–Hall central densities for subdivided triangle m=1,2,3,4,5,6,8,10; their ratios converge to the stated 2-term 1-1/(20m) expansion. For K_{2,3} each edge has exclusion probability 1/3, giving coefficient -1/(10m). Bounded exact profiles do not replace the all-fixed-H Fourier argument.

## originality

PASS

PASS, best of knowledge: the inspected 2022 D’Alì–Delucchi–Michałek primary paper develops primal/polar symmetric edge-polytope face, Ehrhart and flow invariants, not the fixed-H uniform-subdivision continuous polar-volume asymptotic or its squared spanning-tree exclusion-probability coefficient. Xu’s 2008 multivariate splines work provides general cube-section/box-spline volume machinery (abstract inspected), and Fourier–Edgeworth and transfer current are standard tools. No inspected result combined the universal 1/m coefficient with the original graph’s spanning-tree exclusion vector, though broader uninspected spline asymptotics are an originality risk.

## value

PASS

PASS: the formula identifies the first nontrivial, strictly negative geometric correction to a polar-volume asymptotic on every fixed connected graph and expresses it by a concrete probabilistic/electrical graph invariant. It distinguishes trees (exact cube) from cyclic graphs and yields exact cycle and K_{2,3} constants. Researchers studying graph polytopes or spanning trees could use the precise correction independently of any larger conjecture. Known central-limit methods alone do not settle its graph-specific coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
