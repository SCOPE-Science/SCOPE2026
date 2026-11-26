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

Conditional on the tag coordinates, neighbors are independent and the hit area is xy. The product-uniform beta mixture gives (H_n-H_k)/n; equivalently, the number m of labels satisfying one cross inequality is uniform on 0,…,n−1, and mixing over the other uniform tagged coordinate gives degree uniform on 0,…,m conditional on m. For the variance, the two tagged rectangles have intersection min(X1,X2)min(Y1,Y2); excluding the direct edge and taking the (n−2)nd power of the complement of their union is exact. When both tag products are ≤ε=10 log(n)/n, a direct edge forces one pair of coordinates near 0 and the other near 1 in one of two opposite boxes of volume O(ε⁴); elsewhere the union area gives a negligible exponential upper bound. The independent-baseline exponent adjustment is O(log²(n)/n) after n² rescaling. With t_i=nX_iY_i and u_i=−log X_i the Jacobian is 1/n per tag; after integrating out the common translation, its allowed length divided by log n tends to one. The rescaled overlap term is dominated by a constant times (1+|log t1|) max(t1,t2) exp(−|u1−u2|) exp(−max(t1,t2)/2), which is integrable. Averaging the limiting kernel over the independent exponential t_i gives exp(−|u1−u2|), of integral two. Hence the pair term contributes 2 log n+o(log n), and the one-tag term contributes log n+O(1); Chebyshev proves the stated concentration. Read RESULT.md, VERIFICATION.md and checker.py. The recorded finite and simulated checks were not rerun and do not certify the limit.

## originality

PASS

The underlying random digraph and the mutual-edge convention both have prior coverage. The finite harmonic law is an elementary distributional calculation in that model. The substantive supported distinction is the logarithmic reciprocal-isolation variance, including the overlap contribution of two, not an originality claim for the parent model or the beta integral.

## value

PASS

The variance quantifies the failure of the independent rare-isolation approximation in the reciprocal graph of an established random digraph. The one-vertex law alone predicts only the marginal unit of logarithmic variance, while the actual shared-neighbor geometry adds two more. The exact coefficient distinguishes dependence mechanisms at the natural isolation scale; the elementary degree calculation is not the sole value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
