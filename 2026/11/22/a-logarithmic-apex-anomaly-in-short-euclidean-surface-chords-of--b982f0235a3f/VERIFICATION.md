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

# Verification record

The analytic calculation uses an exact conditional azimuth integral. With \(k=\sqrt{r^2-h^2}/(2q)\), the integrand in the macroscopic regime is \(kx+(-kh^2/8+k^3/6)/x+O_q(r^5/x^3)\). Its first two integrated terms yield the area and rim corrections; the second gives the exact positive logarithmic coefficient. The bounded apex layer and the integrated macroscopic remainder are both \(O_{q,L}(r^4)\). This is a mathematical argument for all sufficiently small radii, not a finite enumeration.

Run `python checks/verify_cone_short_chords.py` after installing the dependency in `requirements.txt`. The actual test returned `CONE_EXTRINSIC_SMALL_CHORD_LOG_CHECKS_OK numerical=9 inversion=3 sampling=200000`. The checker uses exact arcsine conditional-angle quadrature, comparisons with the analytically derived logarithmic coefficient, reconstruction checks, and 200,000 independently simulated pairs of embedded Euclidean cone points. These checks do not establish historical priority, uniformity in the opening, or an all-distance distribution.

Independent mathematical audit has not been performed.
