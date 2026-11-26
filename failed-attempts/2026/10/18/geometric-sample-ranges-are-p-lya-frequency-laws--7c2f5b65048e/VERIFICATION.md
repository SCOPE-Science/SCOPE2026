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

Stable sorting by (observation, label) makes the gaps nonnegative, with a mandatory unit gap at each descent; the contribution of gap j to the sum of observations is n−j times that gap. This gives exactly the comajor statistic and the claimed prefactor from the independent sum over the minimum. Independently, for M the maximum and L the minimum, translating all observations by k gives Pr(L=k,R=r)=q^(nk) Pr(L=0,R=r). Hence L and R are independent, L is geometric with ratio q^n, and M=L+R. Applying the classical q-Eulerian series to Pr(M≤k)=(1−q)ⁿ[k+1]_qⁿ, differencing the CDF, and cancelling the minimum PGF yields the same range identity. Savage–Visontai's exact comajor-index theorem holds for all q>0. With constant term 1 and all coefficients positive through degree n−1, the real zeros are strictly negative. Normalizing the linear factors and geometric factors at z=1 proves the independent decomposition. The nonnegative bidiagonal Toeplitz factors are totally nonnegative. Positive diagonal scaling reduces the geometric Toeplitz kernel to the indicator i≥j; prefix-row differences in a finite minor give disjoint ordered row intervals, hence nonnegative determinants. Cauchy–Binet gives the claimed PF-infinity closure and adjacent minors give log-concavity. All series used converge in the stated disk. Frozen finite verification was inspected and not executed.

## originality

FAIL

No exact fixed-geometric range statement was found in the nearby indexed or GEM sources. Nevertheless, the claimed generating function is an immediate probabilistic specialization of the inspected MacMahon–Carlitz identity: that identity enumerates weighted words with a cap on their maximum, and shifting by the minimum cancels precisely the factor for the initial gap. The Bernoulli and PF conclusions are forced by standard factorization of that same already real-rooted numerator. The failure is by explicit prior implication, not a claim that earlier papers printed the range law in those words.

## value

FAIL

The PF-infinity interpretation is stronger than log-concavity and is a useful way to explain the law. As a standalone finding, however, all its exact information is read off the classical generating function after the elementary geometric shift and standard factorization. The illustrative binomial-parent counterexample is a two-draw calculation, not a surviving classification of which parents preserve total nonnegativity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
