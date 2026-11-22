---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The Sonine radial Fourier identity gives a Bessel J_{d/2+beta} tail whose L1 radial exponent is r^{-1-(beta-beta_c)}. Fixed-order large-r Bessel asymptotics uniform in a compact beta-neighborhood, periodic |cos| average 2/pi with bounded primitive, and an integrable r^{-2-epsilon} remainder yield the exact residue and uniform logarithmic window; local r=0 power is integrable. Independently checked the prefactor and numerical cutoff slopes at beta_c: d=2 0.6387808 versus A2=0.6366198; d=3 0.8082687 versus A3=0.8105695; d=4 0.9582345 versus A4=0.9549297. For finite TV, Cauchy–Schwarz applied to a signed spectral measure gives E|w|^2>=||mu||_TV^2 and sampling proportional to |rho| attains equality. At infinite TV, uniqueness of Fourier transforms of finite measures precludes any finite-variance unbiased all-displacement single-frequency representation. Scope expressly excludes other estimator families.

## originality

PASS

The standard ball-power Bessel transform and average |cos| are established inputs; the inspected relevant Wang–Langrené–Chen (2026) abstract introduces signed random Fourier features and integrable-spectrum requirement but does not exhibit the sharp d-dependent beta threshold, residue, uniform cutoff crossover, or optimal single-frequency cost. Its FULL manuscript could not be read (arXiv and OA failed; Oxford access reports VPN disconnected), which is a material priority risk, but alone is not a scientific failure. Older critical Lp physical-space ball kernel results concern a different norm/parameter.

## value

PASS

The spectral integrability threshold pinpoints when unbiased signed random Fourier features have finite second moment, and the residue/critical window quantifies exactly the blow-up and finite cutoff tradeoff. It addresses a motivated meaningful boundary of a widely used compact radial kernel family rather than merely renaming a textbook Bessel identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
