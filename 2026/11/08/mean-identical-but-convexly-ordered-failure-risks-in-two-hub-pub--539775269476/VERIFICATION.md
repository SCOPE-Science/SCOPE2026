---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For n>=4, a+b=n-2 and exactly m surviving vertices, classify outcomes by the two hub survival indicators. With both hubs surviving largest component m; with one hub surviving it is 1 plus the number of surviving leaves on that hub, while the other leaves are isolated; with no hub surviving output is 1 for m>0 and 0 at m=0. This yields the displayed formula [m*binom(N,m-2)+(m+1)*binom(N,m-1)+1_{m>0}binom(N,m)]/binom(n,m), independent of split. For fixed leaf-survivor count r=m-1, the hypergeometric function f(k)=E phi(1+H_k) has nonnegative second difference E[I_{k+1} I_{k+2} Delta2phi(1+H_k)] and strictly positive for interior 3<=m<=n-1 with strictly convex phi. Therefore increasing split imbalance increases every convex expectation and gives the exact variance gap by factorial second moments. Conditioning the independent Bernoulli model on hub states yields the stated full PGF, same split-neutral mean and Bernoulli convex order with variance difference s^3(1-s) times the squared-part-size difference. Direct independent component BFS enumerated all m-subsets for all splits n=4..7 (122 profiles) and confirmed exactly equal means. Financeable bill v(2n-2) follows from known withdrawal responsibility theorem and is not a new equilibrium result.

## originality

PASS

The novel invariant is not the existing public-good participation supportability theorem, nor generic percolation expectation or elementary Jensen convexity. It is the equal entire mean-output curve across all two-hub splits despite a strict *whole convex risk order* and exact variance gap for both fixed-size failures and iid survival. Nearby published Resultary variance ordering counts isolated surviving vertices, a mathematically distinct random variable, and only at site-retention one half. Angulo supplies the largest-component public-output convention and one-withdrawal welfare interpretation, but not these inspected all-count convex distribution laws. Primary Angulo complete text could not be inspected; note historical-priority risk.

## value

PASS

Different connected public-good networks can have identical finance capacity and identical expected post-failure largest-component outputs at every failure count while materially different spread/tail risk. This explicit, exact all-size counterexample to mean sufficiency has mathematical significance in network robustness, beyond a tiny numerical gap; the variance scale can grow quadratically with n under independent outages.

The dated certificate retains the supplied scientific assessment, sources and limitations.
