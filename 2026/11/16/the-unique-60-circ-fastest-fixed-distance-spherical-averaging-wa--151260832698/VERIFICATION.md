---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the fixed-distance projective averaging theorem

Run `python3 verify_cp2.py` from this package. The checker uses Python's standard-library `fractions.Fraction` and `math.comb`, constructs the normalized Jacobi multipliers independently from terminating hypergeometric sums, and compares them with the Jacobi–Legendre difference formula. Executed checks: 280 exact rational assertions, including seven rational test parameters and degrees 1–25, seven exact optimizer-mode values for degrees \(3\)–\(9\), strict high-degree envelope comparisons, harmonic dimensions and the two-mode polynomial factorization.

## Analytic coverage

The all-angle global lower bound comes from degrees 1 and 2 and the displayed exact quadratic factorization. The all-degree upper bound at the candidate uses exact rational Legendre recurrences up to degree 9 and the classical bound \(|P_n(t)|\le1\) on \([-1,1]\), which gives an explicit strict bound for every degree \(n\ge10\). The finite checker does not verify the classical spherical-function formula or the Legendre inequality independently; the argument openly invokes those standard analytic facts.

## Scientific limits

The claim is restricted to one deterministic fixed distance on complex projective plane and mean-zero L2 norms. Other radial step distributions and mixing metrics are not covered. Historical-priority searches do not establish absolute novelty. Independent audit has not been performed.
