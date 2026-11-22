---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS: With ordered lifted car coordinates p_i(t+1)=min(p_i(t)+v,p_{i+1}(t)-1), induction gives vt+min_{0<=j<=t}[p_{i+j}(0)-(v+1)j]. The period-m increment n-(v+1)m is nonnegative so each car has reached its unrestricted v-motion by t=m-1. A strict new minimum at j=m-1 characterizes delay at the last step. Reversed m-1 gaps u_j must have nonnegative entries with partial sums <=vj-1, which is a standard v-root full (v+1)-ary ordered forest word. Two last-delayed cars would give negative sums on disjoint complementary arcs, contradicting total increment >=0, so the marker is unique. Lagrange inversion for H=1+zH^(v+1) gives [z^(m-1)]H^v=binom((v+1)m-2,m-1)/m; closing gap >=v+1; n labelled choices divided by unique marker give n/m times binomial. Fixed-surplus probability follows from two elementary binomial ratios, including h=0. Independent full gap-recursion enumeration for v=2,3,4 and m=2,3,4 at n=(v+1)m yielded maxima m-1, extreme marked-gap counts binom((v+1)m-2,m-1), and labelled 12,63,360,24,180,1456,40,390,4080 respectively. Entire parameter proof is analytic, not finite extrapolation.

## originality

PASS

PASS best-of-knowledge with archival risk: Fukui–Ishibashi high-speed deterministic traffic and Fukś's Fuss/Raney ballot preimages are known, and a published speed-one cyclic Rule 184 theorem already has Catalan last-step extrema. The source's speed-dependent full (v+1)-ary v-forest enumeration and exact labelled maximal-delay population for every v>=2 were not found in the material read. A 1997 two-page Wang–Wang–Hui treatment is relevant to finite-time convergence, but full text was inaccessible; this limitation alone is not a scientific refutation. A 2018 paper with a very close title studies low-density stationary entropy and velocity distributions, not the claimed finite-ring extremizers in the material actually read.

## value

PASS

PASS: For a canonical, physically meaningful deterministic high-speed ring model, the exact maximum relaxation clock and the number/probability of worst-case configurations are natural observables independent of average flow. The unique delayed-car cyclic marking and ordered v-root (v+1)-ary forest bijection are structural enumerative content, and the nonzero fixed-surplus limiting probability gives a useful critical-window distribution. Novelty is not asserted for the speed-one Catalan predecessor or classical Raney coefficients alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
