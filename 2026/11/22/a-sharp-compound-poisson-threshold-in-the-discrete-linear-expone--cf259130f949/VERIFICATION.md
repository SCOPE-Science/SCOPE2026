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

Reconstructed the normalized masses q^j(A+Bj) by telescoping the survival function (q=e^(−σ), a=σ/(1+σ³), A=1−q−qa>0, B=(1−q)a>0). Their log-concavity difference is q^(2j)B². The PGF is A(1+cz)/(1−qz)² with c/q=B/A−1>−1, giving log coefficients (2q^n+(−1)^(n+1)c^n)/n. For necessity, if a positive-at-zero PGF has convolution roots of every order N, each nonconstant coefficient of its normalized Nth root is ν_n/N+O(N^(−2)) at fixed n and must be nonnegative. For c≤q all ν_n here are positive and summable, and normalization yields the explicit compound-Poisson PGF including equality; for c>q sufficiently high even coefficients are negative. Algebra gives the criterion a≤2 tanh(σ/2). Checked the all-positive series for D(x) starting at degree six, and hence the strict decrease from infinity to zero of [(σ/2)coth(σ/2)−1]/σ³. Independently verified the exact numeric bounds using rational arithmetic: for each of the two rational endpoints and s=1/20 bound e^s between its degree-24 Taylor sum L and U=L+2s^25/25!, valid since all omitted successive term ratios are <1/2. For G(s,E)=(2−a(s))(E−1)−2a(s), G(left,U)<0<G(right,L). At s=1/20 the denominator E−1−a is positive on [L,U]; t(E)=a(E−1)/(E−1−a)−1 decreases, and exact comparisons give t(U)>1 and t(L)^102<2<t(U)^104. This certifies the specific obstruction at degree 104 without using the supplied script. Minor diagnostic reporting issue: check_exact.py prints 400 auxiliary compound-Poisson coefficient checks, but its conditional skips the fourth example (c/q=4/3), so that loop checks 300 coefficients; this does not affect any claimed theorem, interval or negative coefficient. The review is only of ordinary additive convolution on nonnegative integers, not thinning.

## originality

PASS

The discrete compound-Poisson criterion and its elementary rational-PGF implementation are background, not the distinct finding. The supported claim is the sharp unique parameter transition for the motivating published survival-discretized law and its explicit obstruction. Exact primary passages cover the model, and inspected comparator results cover other families, not this one-parameter threshold. Das et al. is a material unresolved citation comparison, not evidence of prior coverage; no credit is assigned to an independently demonstrated correction of the wording of its Theorem 3.3.

## value

PASS

The parameter curve is fixed by a published count model rather than chosen to manufacture a root. Despite strict log-concavity throughout the model, the rate determines precisely when an ordinary compound-Poisson representation is possible. Knowing the exact cutoff and jump intensities is useful for that interpretation and simulation, and the explicit high-degree failure demonstrates why checking some low logarithmic coefficients cannot decide the model's divisibility. Value does not depend on whether the witness contradicts the published Das theorem as worded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
