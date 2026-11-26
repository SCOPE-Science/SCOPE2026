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

Stationarity and reversibility give the separated-jump product E[dK_s dK_{s+u}]/(ds du)=<a,exp(uL)a>; the diagonal contributes E K. This is a jump-count calculation, not a conditional-Poisson approximation. Random labeling makes the ordered gap uniform on N=n-1 states; each allowed gap step has rate 2 and the two endpoint intensities are 2 (interior 4). The reflecting cosine basis has eigenvalues 4(1-cos(pi h/N)); endpoint symmetry selects h=2j with squared projection 32 cos^2(pi j/N)/N^2. Integrating gives (1); positive decaying modes give strict increase when N>=3, while the two-state N=2 intensity is constant and gives exactly Poisson. Endpoint Green pairing is 2g(0)/N for the mean-zero quadratic in (87), hence 8 times this pairing divided by mu gives (N-2)/(3N). For fixed t, the excess variance is at most t^2 Var(a), which is O(t^2/N). At t=xN^2 the sin lower bound gives an O(j^-2) Fano summand majorant, and the limit uses N^2 lambda -> 8 pi^2 j^2. The theta expansion gives S''=-64 pi^4[(2 sqrt(8 pi x))^-1-1/2+exponentially small], yielding the positive sqrt(x) and negative 4x terms in (4); zeta(4) gives 1/360 at the long-window edge. Inspected both supplied scripts as source without executing them. Independent full-chain marked-moment exponential replay checked 32 sizes/times for n=3..10 (maximum mean/variance discrepancies 1.599e-14 and 1.776e-13); at n=4 the unique decay rate is 6, integrated covariance prefactor 16/9, F'(0+)=1/3 and F(infinity)-1=1/9. Only the analytic argument covers all sizes and the double limit.

## originality

PASS

The claimed increment is the explicit finite-window variance and the diffusive observation-time theta law at particle count exactly two. Prior long-time mean and Fano benchmark are already credited; the finite-time tilted-semigroup method itself is also known.

## value

PASS

At fixed time the dilute system looks Poissonian in variance, while the known infinite-window limit is not Poissonian. The full Fano function quantifies when repeated collisions become visible, with the natural mixing scale, a sharp square-root onset, and the reciprocal-time approach to the late-time benchmark. This resolves a motivated connection between two distinct limits and is not just a recomputation of the long-time cumulant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
