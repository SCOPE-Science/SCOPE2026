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

Finite numerical tests reconstructed the source's top Laplacian and independently checked the intrinsic hull volumes, polar volumes, facet contacts, and conical-simplex second moments for even ambient sizes 4, 6, 8 and 10; the checker also inspected odd sizes 3, 5, 7 and 9 as a separate control. The script prints `LAPLACIAN_METRIC_FINITE_CHECKS_PASSED` upon success.

Analytical evidence: (i) the source's alternating matrix equals \(NI-ss^{\mathsf T}\); (ii) the centered columns occupy two mutually orthogonal centered regular simplices; (iii) polarity, unique symmetric extremal ellipsoids, conical facet-simplices and elementary simplex integration give exact identities in every dimension; (iv) Stirling's formula supplies the asymptotic. All volumes are in the intrinsic Euclidean \((2k-2)\)-space. The finite checker does not prove the unbounded-parameter theorem or establish novelty. No independent mathematical audit was performed.
