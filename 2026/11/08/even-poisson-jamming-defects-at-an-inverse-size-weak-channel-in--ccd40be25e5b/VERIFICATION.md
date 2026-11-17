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

The embedded Markov chain at vacancy sizes (a,b,c) has AB,AC,BC rates wab,ac,bc. Invariant c=a+b+2K and positive c whenever a+b>0 imply terminal (0,0,2K) and R=2K exactly. Rare-event hazard p=w ab/[c(a+b)+wab]<=w/4 gives binomial stochastic domination, K=O_P(1) and uniformly bounded exponential moments when nw->lambda finite. For imbalance d=a-b, conditional drift of d² <=1 and Doob/optional-stopping controls max|d|/n; conditional on s>=delta n, hazard n p→lambda/4 uniformly in probability. Uniform-variable coupling across ~2n initial events gives Poisson((2-delta)lambda/4), with tail AB probability <=delta lambda/4. delta→0 and exponential-moment bound give all moment convergence. Independent exact rational reduced-state recursion for n=3,6,10,18 and finite comparisons point toward the predicted mean and vacancy law; finite cases are not an asymptotic proof.

## originality

PASS

PASS. Earlier October 26 2026 published full text proves a superficially similar Poisson terminal-jamming correction on unweighted tripartite graphs with a superlinearly dominant class M_n≫n and two minorities n, whereas here c=2n initially and depletes on the same scale as a+b while AB rate is w_n~lambda/n. The earlier regime cannot be specialized or rescaled to these simultaneous balanced-capacity/weak-channel dynamics. Pippenger 1989 addresses sparse regular or tree-like graphs, not this dense weighted tripartite boundary. No matching prior exact even-Poisson law was found in targeted Resultary or published-abstract searches.

## value

PASS

The capacity identity makes an exact random terminal vacancy count from successful rare bonds, and the inverse-size weak channel exposes a nontrivial Poisson-to-perfect-coverage transition with convergent moments. It is a naturally motivated critical scaling for a dense weighted adsorption system and can be used as a benchmark for stochastic matching and jamming limits, not a redundant fixed-weight law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
