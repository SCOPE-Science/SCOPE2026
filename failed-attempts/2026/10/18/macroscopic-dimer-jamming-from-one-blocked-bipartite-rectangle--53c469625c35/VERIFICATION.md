---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With independent rate-1/n exponential first arrivals, an edge with two vacant endpoints cannot yet have rung, so memorylessness gives the three exact mass-action rates. On the invariant cube the polynomial drift is Lipschitz (it need not be globally Lipschitz on R^4); scaled counting martingales have quadratic variation O(T/n), which gives the fixed-time fluid limit by Doob and Gronwall. Balance yields b=(1-alpha)h, d=(1-beta)h and, with I'=h, a=alpha exp(-(1-beta)I), c=beta exp(-(1-alpha)I). Off the diagonal, balance gives the first zero of h at I*=log(beta/alpha)/(beta-alpha). On the diagonal, solving dh/dI=-(a+b) gives h=exp(-(1-alpha)I)(1-alpha I). In both cases h>0 before its first zero, so I tends to I* and the density tends to (r,0,r,0). The deterministic future-consumption bound by b_n(T)+d_n(T) makes the infinite-time transfer valid, and boundedness gives convergence in mean. Complement vacancies are in fact exactly zero at any finite graph's jam: either complement has edges to the entire opposite side, which would have a vacancy by balance. Class counts here are normalized by n. The perfect-matching construction is valid. As a finite check, for n=2 and one missing pair, exactly one of the three equiprobable first edges leaves a vacancy per side. This verifies the stated 1/3 for that case only; no frozen script was executed.

## originality

FAIL

The distinct indexed result a1a50e975e33 demonstrably covers the same two-parameter model, vacancy law in probability and mean, classwise endpoint, and positive jamming despite a perfect matching; it goes further by optimizing over the feasible region. This is a coverage decision, not an inference of historical priority from catalogue dates or an assertion that the frozen mathematics is false.

## value

PASS

An explicit kinetic vacancy law on a natural structured substrate quantifies an extensive separation between random greedy coverage and optimum coverage even when a perfect matching exists. The terminal transfer is essential and the two-parameter limit supplies a benchmark beyond a finite-time ODE or isolated example. This scientific usefulness does not make a covered finding new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
