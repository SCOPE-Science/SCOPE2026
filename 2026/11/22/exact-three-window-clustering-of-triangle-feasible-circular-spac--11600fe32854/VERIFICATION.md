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

With the cyclic list rooted at a uniformly chosen sampled point (equivalently, at a fixed sample label), the gaps have the Dirichlet(1,…,1) law; homogeneity removes the common exponential normalization. Independently recomputed the four probabilities as exact simplex-volume ratios: eliminate the last gap by sum x_i=1, intersect the simplex with the three linear triangle inequalities from each tested window, enumerate feasible vertices by full-rank active systems, and recursively cone each face boundary from its vertex barycenter. The sums of absolute simplex determinants in dimensions 2, 3, 4, 4 give 1/4, 1/9, 2/27, 232/4725 respectively (the last polytope has ten vertices). Dividing the last result by 1/9 gives 232/525. Disjoint windows depend on disjoint exponentials. For n≥5, exactly two ordered partners per index have each of the two nonzero covariance values 7/144 and 5/432; n=4 has twelve ordered pairs sharing two gaps and n=3 has identical indicators. This gives all variance cases stated. The bounded two-dependent linear sum satisfies Lindeberg using length floor(n^(1/3)) blocks separated by two deleted terms; the deleted variance is o(n), the retained asymptotic variance is 133n/432, and at most two boundary terms change under cyclic closure.

## originality

PASS

The distinct contribution supported here is the evaluated local overlap law, especially the five-gap triple-success probability and the resulting conditional cluster probability. The broken-stick marginal and generic dependent-spacing CLT and variance framework are not original. No inspected distinct record or primary result gives the same local joint probabilities or an evaluated formula subsuming them.

## value

PASS

The motif uses natural consecutive positions of uniform circular spacings. A researcher calibrating local cluster counts needs a joint probability, not just the marginal or asymptotic variance: the conditional chance of a third success after two is 232/525 rather than 1/4, a concrete higher-order effect. The pairwise probabilities additionally give the exact variance inflation and its small-cycle exceptions. Value rests on these exact local quantities, not on a new CLT or a claim about all triangle statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
