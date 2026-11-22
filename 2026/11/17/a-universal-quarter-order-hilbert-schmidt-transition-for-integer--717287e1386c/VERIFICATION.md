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

PASS. Using normalized radial Fock monomial norms Gamma((2k+2)/m)/(alpha^(2k/m)Gamma(2/m)), the reproducing kernel is exactly the series in the frozen proof. The entire Mittag-Leffler weight has beta-integral and decaying weighted evaluation profile, yielding boundedness and compactness by cutoff in output radius plus Montel. Basis-Tonelli gives exact S2 energy ∫|psi_gamma|² K(az,az)dmu. Distinct angular monomials z^(mk) make angular integral 2pi sum x^(2k)/Gamma(k+1+gamma)². A Stirling saddle at k≈x has e^(-2x) sum ~x^(-2gamma-1/2)/(2sqrt(pi)), and the positive-real kernel has leading (m/2)Gamma(2/m)alpha^((m-2)/m)a^(m-2)r^(m-2) exp(alpha a^m r^m). Combining gives H'_gamma~[m²alpha a^(m-2)/(4sqrt(pi))]c^(-2gamma-1/2)r^(m/2-1-2m gamma). Integrating yields HS iff gamma>1/4, all three spatial energy asymptotics, and parameter residue C_(m,1/4)/(2m). Independently recomputed the saddle ratio at x=40,160 (gamma=.2,.45), ~1.00157 and 1.00039, not a proof.

## originality

PASS

PASS (best of knowledge with important access risk). General Fock compactness/Hilbert–Schmidt criteria and Gaussian compact/non-HS examples are prior, including exact Gaussian Fourier-edge thresholds; the proposed theorem is not novel as an existence claim at m=2. Full published October/November Fourier-edge RESULT files do not cover Mittag–Leffler z^m angular coefficients and uniform m=1/m>=3 spatial-energy constants. The general Barik–Sen–Paul primary full article could not be newly read because legitimate retrieval and authorized Oxford service returned VPN disconnected; its abstract and theorem statements do not give a directly covering evaluated family.

## value

PASS

PASS. A sharp exact endpoint threshold, divergence constants and pole law valid simultaneously in sub-Gaussian m=1, Gaussian m=2 and every higher integer radial power is a meaningful analytic family, extending beyond the already-known Gaussian existence question. The Mellin/Gamma saddle and kernel normalization make the cross-power constant nontrivial. This does not claim a general Schatten-class classification or novelty of compact non-HS in Gaussian Fock space.

The dated certificate retains the supplied scientific assessment, sources and limitations.
