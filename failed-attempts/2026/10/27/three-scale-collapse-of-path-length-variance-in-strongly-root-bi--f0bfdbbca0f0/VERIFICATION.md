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

The normalization is the variance of total depth divided by n², with n tending to infinity at each fixed α. Independently, the weighted mean depth updates by p_j(1+Z_j), where Z_j is the depth minus its conditional mean. The expected weighted variance updates by (1−p_j²)v_j+p_j(1−p_j). The weighted-mean martingale is L² convergent (for α≤−1, and also for α>−1, p_j=O(1/j) and v_j=O(log j)); the centered ordinary average depth has the same L² limit by Cesàro averaging and orthogonality of the Z_j. Set a=2^α, b=3^α, c=4^α. The j=3 term is ab²/[(1+a)²(1+a+b)²]=18^α−4·36^α+O(54^α). The j=4 term is c²[a+O(b+a²)]/(1+a+b+c)²=32^α+O(48^α). For α≤−2 the sums of k^α over k≥2 and j^(2α) over j≥5 are bounded by constants times 2^α and 5^(2α), respectively, by factoring out the first base and comparing with a fixed convergent power sum. Since v_j≤Σ_{k≥2}p_k, this gives O(50^α) for the whole remaining tail. The positivity and order of the resulting scales check out. The frozen exact n=6 checks and finite numerical truncations in verify_ultraold.py and verification_output.txt are corroboration only; the script was inspected, not run.

## originality

FAIL

The three-term form was not found printed in the parent paper; the issue is stronger prior mathematical coverage, not a verbatim duplicate. Its exact variance series for the same weights over all fixed real α and explicit scalar recurrence reduce this particular endpoint expansion to Taylor expansion of two rational terms and a direct summable majorant for the rest. Neither the coefficients nor the O(48^α) scale require an additional variance identity, a new approximation theorem, or control beyond the immediately dominated tail. Section 10 singles out parameter dependence for further study; that is broader than the elementary extraction here. A later indexed record explicitly prints only the first two scales and is not claimed as an earlier publication of the third.

## value

FAIL

The strongly root-biased endpoint is natural, and the ordering of the second and third scales is informative. But the only added exact statistic is a short coefficient extraction from an existing exact series with an elementary tail, with no separately justified need for this particular precision or independent structural result. This narrow finding does not meet the independent-value criterion; the failure is not because it concerns a single endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
