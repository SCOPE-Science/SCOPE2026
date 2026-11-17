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

# Checks of the local boundary-probe law

The proof in `RESULT.md` supplies the general smooth-curve and total-variation claims. The standalone diagnostic `check_boundary_probe.py` requires packages pinned by lower bounds in `requirements.txt`; run with `python check_boundary_probe.py`.

The checker integrates \(\int_0^\infty e^{-u-x/u}\,du\) using numerical quadrature and independently evaluates \(2\sqrt{x}K_1(2\sqrt{x})\) for three \(t\)-parameters on the unit circle. Agreement was below \(2\times10^{-10}\) in absolute error. It next samples exact finite-\(n\) neighboring arc gaps from the Dirichlet\((1,1,n-1)\) law and evaluates the exact chord-normal intersection, without applying the parabolic approximation. There are \(260{,}000\) generated samples per configuration.

Observed versus limiting exposure frequencies were:

| Scaled depth \(t\) | Vertex count \(n\) | Simulated | Limiting Bessel |
|---:|---:|---:|---:|
| 0.2 | 60 | 0.954796 | 0.954732 |
| 0.2 | 300 | 0.954223 | 0.954732 |
| 2 | 60 | 0.764300 | 0.764627 |
| 2 | 300 | 0.764158 | 0.764627 |
| 12 | 60 | 0.391335 | 0.397389 |
| 12 | 300 | 0.396846 | 0.397389 |

The checker independently sampled \(18{,}000\) complete 35-vertex circle polygons and classified the normal probe by **all** oriented edge halfplanes. In every case the classification agreed exactly with that from the single chord joining the two sampled neighbors of the boundary point.

Final successful output: `BOUNDARY_PROBE_BESSEL_AND_CHORD_OK`.

No simulation or quadrature establishes the asymptotic law on every smooth curve, the multi-site total-variation limit, or priority in the literature. Those claims rest on the analytical argument and remain subject to independent review. No external audit has been performed.
