---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For a marked set of size m, choosing ordered disjoint designated blocks and partitioning what remains gives the stated mixed factorial moment, with zero moment if the selected vertices would exceed m. Log-concavity of B_n/n! gives the claimed uniform factorial-moment bound. The needed Bell ratio also follows from Dobiński's sum: for weights k^n/k!, consecutive ratios (1+1/k)^n/(k+1) decrease in k; at k=(1±epsilon/2)n/W(n) their logarithms have strictly positive or negative leading terms of order W(n), respectively. Geometric tail comparison therefore gives exponentially small weight outside (1±epsilon)n/W(n), even after multiplication by n/W(n). The expectation of 1/k under these weights is B_{n-1}/B_n and is asymptotic to W(n)/n. The factorial-moment bound dominates each finite-coordinate generating-function series uniformly on compact sets; coefficients converge, and a tail bound by the sum of (mb_n)^j/j! above J upgrades convergence to full-array TV. Exchangeability makes the conditional law of each agent's counts constant over marked sets of the same size, so conditional independence is already exact for deterministic size. The Bernoulli size has scaled variance at most (np_nb_n)b_n, and the fixed-size limit along all deterministic sequences with mb_n tending to c yields the claimed TV limit for the conditional product mixture. The logical event is nonzero total count. The subcritical bound is a union bound on all fully marked blocks; the supercritical second-moment argument for marked singleton blocks works in both models by the fixed-shift Bell ratio asymptotic.

## originality

FAIL

A distinct earlier indexed record already proves the same one-agent Bernoulli full marked-size Poisson process with the same intensities, witness probability, and endpoint regimes. Its result implies the one-agent discrete TV limit by its finite-coordinate convergence and explicitly controlled aggregate tail. The fixed-size and shared-predicate product extensions follow routinely from that result by monotone removal of the random size and conditioning on the fixed-size mark set. Thus the fact that the earlier record does not print the multiagent statement is not a substantive unfilled mathematical gap. This is an implication finding, not a claim that the earlier record literally states every formula here.

## value

FAIL

The sparse logical threshold and marked-size spectrum are natural, but they are already present for one relation. The proposed new joint information follows from standard size bracketing and the conditional product identity; none of the stated events requires joint interaction of the equivalence relations beyond sharing the mark set. There is no independently useful unknown exact invariant or quantitative dependence result left after crediting the earlier law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
