---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For unnormalized Gaussian two-probe XNysTrace on arbitrary 2x2 SPD A, rank-one residual after holding out g_j is tau(theta_j) v(theta_j)v(theta_j)^T, tau=ab/(a cos²theta+b sin²theta), with independent Gaussian radial squares of means 2 and fourth moments 8. The centered leave-one-out terms T_i−tr A=tau(theta_j)(R_i² sin²(theta_1−theta_2)−1). Thus each term has variance 2X where X=E tau²=sqrt(ab)(a+b)/2. The shared angle produces covariance 2Y from E[tau cos4theta]=sqrt(ab) r² and E[(2sin²Delta−1)^2]=cos²2Delta, giving Y=ab(1+r^4)/4. Consequently Var(T_hat)=X+Y, and expected squared-proxy S=E[(T1−T2)²]/4=X−Y. Explicit positive polynomial factorizations in t=sqrt(b/a)>0 prove X≥4Y, the sharp ratio ≤5/3 and Var≤5(a²+b²)/8, equality at a=b; as t→0 or infinity the ratio→1. At A=I2 this gives variance 5/4, E S=3/4. Independent direct angular integrations for three spectra corroborate the Fourier moments; not an unrestricted proof.

## originality

PASS

PASS qualified. Original Epperly-Tropp-Webber XTrace paper states the unnormalized leave-one-out estimator and general posterior-calibration correlation identity; no complete anisotropic planar covariance or sharp all-spectra 5/8 Gaussian comparator bound is stated in inspected sections. A previously published October 13, 2026 identity-matrix XNysTrace covariance theorem already gives the isotropic 5/3 endpoint, which is NOT counted as new. The new exact arbitrary-(a,b) dependence through fourth angular Fourier moments and sharp Gaussian-Hutchinson comparison is not logically implied by the identity-matrix case. A 2025 Epperly thesis was not fully readable; record that priority risk.

## value

PASS

The estimator's own squared-error proxy is intended for reliability/calibration; its dependence on the full positive planar spectrum and worst-case undercalibration factor are natural joint-covariance invariants of the basic leave-one-out algorithm. The exact spectral sharpness and variance comparison allow a controlled small-budget stress test and reveal a genuine dependence mechanism. The result is intentionally a baseline diagnostic, not an information-theoretic optimal estimator: two 2D matvecs can reveal A, and residual-normalized XNysTrace is different and can be exact in 2D.

The dated certificate retains the supplied scientific assessment, sources and limitations.
