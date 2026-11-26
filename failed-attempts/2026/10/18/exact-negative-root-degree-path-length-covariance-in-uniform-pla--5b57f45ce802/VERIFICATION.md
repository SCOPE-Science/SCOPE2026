---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For the uniform ordered rooted n-vertex law, the root decomposition gives T=z/(1−T), and adding one unit of depth per subtree vertex gives F=z(F+zT')/(1−T)^2 for the total path-length series. Root marking gives T²/(1−T) and the mixed series z(F+zT')(1+T)/(1−T)^3. Substitution of T=(1−sqrt(1−4z))/2 and division of the resulting coefficients by C_{n−1}=B_n/[2(2n−1)] give all three moments in Finding. The covariance is negative iff 4^n/B_n<2(n+2)/3. At n=3 the sides are 16/5 and 10/3, and the growth ratio of the right side exceeds that of the left by (n−1)/[(n+2)(2n+1)]. The sole n=2 tree gives zero and the Stirling expansion yields −2n+3sqrt(pi n)−1+O(n^(−1/2)). Independent exact enumeration checked 2055 shapes through n=9, including (E D,E P,E[DP],Cov)=(3/2,5/2,7/2,−1/4) at n=3. To replay the finite check, recursively compose n−1 into ordered positive subtree sizes, include the empty list for n=1, compute D as list length and P as the sum of child path lengths plus their sizes, and sum D, P and DP over the resulting Cartesian products. The supplied verifier was inspected, not executed. Neither enumeration nor the recorded checks certify arbitrary size; the generating-function and induction arguments do.

## originality

FAIL

A distinct indexed result states exactly this covariance, boundary, sign and asymptotic in edge indexing; a different same-day result also supplies an exact depth-resolved mixed family whose weighted sum is the claimed moment. These are determinations of scientific coverage, not of historical priority or intra-day order.

## value

FAIL

Root degree versus total depth is a natural tree dependence question, and the exact negative sign is informative. The submitted exact invariant adds no surviving gap once the explicit size-translated duplicate and the richer depth-resolved calculation are accounted for. Re-extracting the same coefficients in vertex notation is not a distinct scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
