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

# Verification evidence

The standalone `checker.py` rederives and tests all 18 explicit polynomial pairs in `CERTIFICATE.json` and uses the vertex coordinates and the two-tetrahedron decomposition written in `RESULT.md`. It enumerates all \(18\) open sectors, computes and cancels each exact rational area profile with SymPy, confirms coprimality, the complete degree multiset \(\{3^8,4^2,5^8\}\), and all \(153\) pairwise distinctions. The projective homogenization argument in the mathematical proof establishes absolute irreducibility. An independent computation of the planar convex hull of intersections with the eight original pyramid edges agrees with the analytic formula at \(180\) sector-interior directions, and the vertical slice gives the exact square area \(64/25\).

Keep `checker.py` and `CERTIFICATE.json` in the same folder and run with Python 3 and the packages in `requirements.txt` via `python checker.py`. The script prints the degree/sign certificate rows and exits nonzero if a check fails. These finite calculations do not replace the analytic all-direction proof. The numerical plane-section comparison uses a stated tolerance rather than exact geometric interval bounds; exact symbolic checks establish the component count and degrees. The claims have not undergone independent mathematical audit.
