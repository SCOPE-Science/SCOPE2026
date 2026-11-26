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

The fair-bit Hamiltonicity condition is strict positivity of every reversed partial sum. The clique identity counts the 1 bits plus the initial vertex, and edge counting with weight j on creation bit j gives the sum of the reversed partial sums with the stated normalization. The interpolated area differs from that sum divided by L^(3/2) by at most 1/(2 sqrt(L)). With r trailing 1 bits off the complete graph, the graph is the join of K_r and a disconnected remainder (the last vertex of the remainder was added isolated); the Laplacian spectrum of the join gives lambda_2=r, including zero for a disconnected graph. The exceptional complete graph has lambda_2=n, yielding the extra 2^(-L) needed for the exact unconditioned mean 1. Reflection at zero from height a subtracts binom(t,j+a) for an endpoint reached by j up-steps, and summation telescopes to B(t,a). The exact-r prefix is r up-steps then a down-step, leaving height r-1 and time L-r-1; the all-up word has its separate mass. Central-binomial asymptotics give (r-1)2^(-r). For the claimed uniform tail, the at-least-r prefix count is B(L-r,r); for r<=L/2 use the central-binomial bound, and for r>L/2 use B(L-r,r)<=2^(L-r) and sqrt(L)<=2r. This also controls moments, with the complete-graph moment correction exponentially small. Conditional on any fixed exact-r prefix, the surviving continuation is a walk from fixed positive height, with the same finite-horizon meander limit; the prefix vanishes on rescaling. Tightness allows summing over r, proving independence from the entire path, not just its endpoint or area. The latter two are dependent: the meander bridge at endpoint y has the law of a three-dimensional Bessel bridge to y (the positive Brownian kernel and its h-transform have the same bridges), so by convexity of the norm its expected area is at least y/2. This cannot be constant over the unbounded endpoint law.

## originality

PASS

Credit the already known threshold-graph encoding, Hamiltonicity and spectral identities, survivor count, unconditioned law, and meander endpoint/area law. The remaining supported contribution is the exact conditioned spectral run law and its joint path-level asymptotic independence. The inspected sources give ingredients or different joint observables, not an equivalent joint theorem covering this conditioned local variable. This is a bounded comparison, not a priority guarantee.

## value

PASS

Hamiltonicity is a natural rare-event conditioning that changes an actual graph invariant: the limiting spectral mean is 4 rather than 1, and the entire conditional spectral law is available at finite order, including the complete graph. The joint theorem separates a local spectral statistic from all continuous path functionals while retaining the dependence of the global endpoint and area. Neither the finite spectral comparison nor that joint interpretation is supplied by quoting the separate global and unconditioned spectral laws. The added value is this conditioned exact distribution and local/global separation, not the standard walk tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
