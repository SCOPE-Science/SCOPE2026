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

# Mathematical verification

The complete derivation appears in `RESULT.md`, Sections Proof 1–6. The critical normalization is \(S_{K}=2\pi\nu\), perimeter \(2\pi\), and Steiner point \(0\); here \(N=2m\), \(m\ge3\), \(|\varepsilon|\le1\). The exact geometry identities in (4), geodesic optimal transport certificates in Proof 4–5, and convexity dominance in Proof 3 were separately checked algebraically during self-review. The formulas include \(\varepsilon=\pm1\), when half the facet masses vanish.

The embedded `verify.py`, executed after extraction and with NumPy and SciPy, returned `INTERLACED_GRID_OK 1215`. It checks 342 parameter pairs in dimensions \(m=3\) through \(40\), including the endpoints, and 189 transport-cell moment identities; it is not an exhaustive proof for all parameters. A separate discrete linear-programming check at \(m=3\), \(\varepsilon=0.6\), using 480 uniformly distributed source points agreed with the exact W1 value to within \(2\cdot10^{-15}\).

The claimed exact formulas are proved analytically, not inferred from sampling. The bibliography and equivalence comparisons support provisional self-review only. Independently sourced or independently audited mathematical validation has not been performed.
