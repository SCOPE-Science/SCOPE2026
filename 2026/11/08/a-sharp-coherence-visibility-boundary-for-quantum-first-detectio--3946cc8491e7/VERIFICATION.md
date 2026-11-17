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

For two-level unitary evolution p_01(t)=p_10(t)=a sin²(omega t/2). Under exponential inter-probe times, nonnegative kernels K=re^(−rt)p(t), L=re^(−rt)(1−p(t)) yield exact renewal equations f_tr=K+L*f_tr and f_ret=L+K*f_tr. Their survival difference equals G_r*(delta_0+sum_{n>=1}L^{*n}), G_r(t)=r e^(−rt)[(1−a)t+(a/omega)sin(omega t)]. The positive renewal measure implies stochastic order for every rate iff the seed is nonnegative for all times, and its first negative sinc minimum occurs uniquely at z* in (pi,3pi/2) with tan z*=z*, giving a*=1/(1−sin z*/z*)=0.821534976... . Necessity uses fixed-t small-r expansion at t=z*/omega, plus initial positive rt term to force crossing. A separate exact Laplace transform comparison proves return < transition in Laplace order for all a,r, including the crossing regime; means differentiate from the same transforms. Independent symbolic renewal-transform identity and local root/sign calculations supported the analytic proof. Finite tests are not a substitute for the all-r,t arguments.

## originality

PASS

Best-of-knowledge originality: the exact assigned final claim (not its already-known general machinery) was compared with primary published theorems, more general methods, aliases, semantic research records and matched objects. The four structured comparisons and materially read source inspections below identify no inspected prior theorem implying this full result; residual risks remain real, and non-discovery is not a mathematical proof of priority.

## value

PASS

This gives a sharp quantitative boundary at which return detection ceases to dominate transition detection at every finite time, despite retaining strict Laplace transform order. The separation is a natural and nontrivial probabilistic phenomenon for experimentally motivated randomly probed quantum dynamics; it supplies a threshold and unavoidable crossing mechanism not answered by existing mean or long-time tail optimizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
