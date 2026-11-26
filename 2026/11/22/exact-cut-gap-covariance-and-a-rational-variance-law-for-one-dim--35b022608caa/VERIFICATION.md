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

With almost surely distinct distances, an endpoint choosing a neighbor must also choose every intervening point, since each is closer. Thus components are consecutive. A cut after site i requires two closer same-side neighbors for each endpoint; this is exactly the pair of strict inequalities comparing G_i to the two adjacent gaps summed on each side. If they hold, vertices at least two positions from the break have two closer vertices between themselves and the break; the second vertex from the break on either side has the boundary vertex and its immediate neighbor on the outer side closer than the crossing, by the same inequalities. No cut can leave fewer than three vertices on a side. Consequently C_n is one plus m=(n-5)_+ cuts, including the deterministic n=3,4,5 cases. Dirichlet spacings are normalized independent exponentials and the common denominator cancels from the cut tests. Disjoint five-gap blocks at distance at least five give independence of families, while centers at distance one or two would each have to exceed the other, which is impossible. I separately integrated the joint probabilities by ordering the two exponential centers x<=y. With F the Gamma(2,1) CDF, lag 3 has conditional factor F(x)^2 F(y). At lag 4 the shared exponential and the two distinct exponential companions give the factor F(x)+(1-x-exp(-x))*exp(-y) in addition to the outer factors F(x)F(y). Exact polynomial-exponential integration gives p=7/54, q3=2071/90000 and q4=6389/324000; these are joint probabilities for lag 3 and 4, and the covariances subtract p^2. Counting m-h admissible pairs where positive yields precisely the finite variance and the stated slope and intercept. The positive long-run variance legitimizes the bounded stationary four-dependent CLT; the mean and O(n) variance imply the claimed L^2 law, and slope/p is 2463/5000. Replay: python -B branches/independent_reproductions.py 3 from /workspace with SymPy. This audit is for iid uniform points on a line and the union graph with exactly two neighbors, not a mutual-choice, circular, or random-link model.

## originality

PASS

Pass the exact two-neighbor cut joint laws, finite-sample moments and explicit asymptotic variance. General nearest-neighbor component-count Gaussian theory and positive component density are prior, not the novelty. The closest inspected explicit constants are for different observables, degrees or graph models. The Penrose–Yukich full-text limitation remains a risk, not evidence of noncoverage.

## value

PASS

The interval union of two-neighbor choices is a natural sparse geometric graph and connected-component count is a basic fragmentation observable. The exactly evaluated positive and negative overlap terms quantify why independent or Poisson cuts would fail: the true limiting variance-to-mean ratio is below one, and the finite correction is available without simulation. The main value is the finite-sample and local covariance information, not a generic Gaussian-limit theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
