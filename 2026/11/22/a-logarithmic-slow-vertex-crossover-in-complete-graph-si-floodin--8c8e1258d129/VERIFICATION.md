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

For m=N-1 and k ordinary infected vertices, the competing rates before marked infection are k(m-k)/N and rho_N k/N. The product of ordinary-win probabilities is the stated gamma ratio, with log probability -rho_N log N+O(rho_N+rho_N^2). In the ordinary-only birth chain, the time to any fixed interior fraction has mean log N+O(1) and bounded variance by summing reciprocal rates and their squares. The expected infected count is at most exp(t), which controls the early side even when rho_N log N diverges. Thus the normalized integrated count is (x-1)_+ at time x log N. Conditional Poisson survival gives the delayed exponential limit for the marked time and both boundary regimes. Ordinary completion is squeezed between the ordinary-only chain and one with a fully active marked vertex from time zero; the two bounds have means 2 log N+O(1) and bounded variances. Taking the maximum with marked time requires no independence. The half-population hitting time plus a rate-rho_N/3 exponential bounds marked time from above and gives uniform L^2 control in the critical window. The resulting mean is 2+exp(-c)/c and the atom has mass 1-exp(-c).

## originality

PASS

The homogeneous logarithmic baseline and general birth-chain and hazard techniques are known; the precise marked-last and mixed completion laws are not covered by the strongest relevant statements inspected.

## value

PASS

A canonical dense flooding model usually concentrates at a deterministic time at leading logarithmic order. This natural one-vertex perturbation identifies exactly when a single exceptional clock defeats that concentration, yielding a mixed law, a last-vertex probability and a nonzero explicit mean penalty. The model is an abstract graph benchmark, not a claim about physical spread.

The dated certificate retains the supplied scientific assessment, sources and limitations.
