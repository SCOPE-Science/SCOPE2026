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

For canonical right-continuous BV with trace endpoints, a unit jump at s∈(0,1) samples as the tail beginning at k=ceil(ns); telescoping gives J_{n,k}^α. Equivalently the integrated jump response is E|Y−s| for the random variable with CDF J_{n,k}(x)^α (a CDF power of Beta(k,n−k+1)). On each fixed cell the derivative in s is 2J_{n,k}(s)^α−1, strictly increasing; the maximum on the cell closure is at an endpoint, with disallowed endpoints interpreted only as limits. Signed step-measure superposition gives the upper norm bound and individual jumps or limits of jumps give the reverse bound; free nodal or endpoint assignments would not be justified for this variation seminorm. At n=1 the two one-sided values are 1/(1+α) and α/(1+α). For an interior sequence s_n→s, in the √n window x=s_n+z√(s(1−s)/n) the centered standardized binomial threshold tends to −z, so its survival function tends to Φ(z). For x<s_n, k_n≥ns_n gives the needed upper-tail bound at distance |x−s_n|; for x>s_n, k_n−1<ns_n gives the lower-tail bound. Using 1−J^α≤max(1,α)(1−J) and the Lipschitz variance yields the bound exp(−c_α n u²/[s_n(1−s_n)+4u/3]) up to constants, where u=|x−s_n|. On an interior scaling window this is integrable uniformly, and splitting the unscaled bound at u=s_n(1−s_n) gives O_α(√(s_n(1−s_n)/n)+1/n). Thus boundary-convergent sequences contribute zero to the scaled norm and all interior subsequences have the indicated Gaussian limit. Maximizing the remaining factor √(s(1−s)) gives the sharp constant and forces asymptotically norming jumps to the midpoint. For the parameter claim, locally in α>0 the needed log-weighted derivatives are integrable by the Gaussian tail. In c'=A_α−B_α the log-magnitudes for A are below log 2 and those for B above log 2; hence (log(A_α/B_α))'>0. Strict concavity of −q log q+(1−q)log(1−q) for 0<q<1/2 gives c'(1)<0; the endpoint integrands at α=1 and 2 both equal 2q, so the unique critical point is inside (1,2) and the full comparison window follows. Independent composite Simpson diagnostics using a normal tail integrated backwards to 0 from z=14 with step 0.001 gave α≈1.40542923498526, c≈0.75749746452316 and fractional gain 0.0506177. These are diagnostics, not substitutes for the uniform bounds or parameter proof. The supplied VERIFICATION.md and check.py were read without execution.

## originality

PASS

The classical α=1 norm, Gaussian limit and midpoint localization match the comparable portions of a distinct same-day catalogue record. The sampling family itself and pointwise BV estimates are older. Neither covers the sharp integrated parameter profile for fixed α>0, its unique minimizer, or the strict improvement window in the inspected statements. The absence of full text for the two cited 1998–2000 papers leaves a specific historical-priority risk; no claim of exhaustive novelty is made.

## value

PASS

For an established positive approximation family, the exact worst-case integrated error over a natural low-regularity class gives a practical criterion for choosing its parameter. The finding identifies the entire improvement interval rather than a single tuned example, and the reversal from worse degree-one behavior to a smaller sharp asymptotic constant shows why that interval is not apparent from low-degree tests. The jump localization and unique parameter optimum make the classification more useful than an order estimate or the classical α=1 recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
