---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For x=hc/(λk_B), the positive wavelength prefactor cancels. Differentiation in T gives K=x csch²(x/(2T))/(4T²); its log mixed derivative is (coth y−y csch²y)/T²>0 because sinh y cosh y>y. Integrating that strict mixed derivative gives strict ordering of the K ratios across hot versus cool derivative temperatures. The FTC and Tonelli represent both branch contributions by positive derivative mixtures on opposite sides of T0. Integrating the strict determinant over both measures then makes H/C strictly increasing; an atom at T0 contributes zero. Compact positive support justifies the uniform Rayleigh–Jeans expansion and continuity. The long-wavelength limit is M+/M−; the finite-wavelength inequality is strict even at equality of the area mean. A positive hot submass separated from T0 makes H/C tend to infinity in the Wien limit since C≤b(T0,x). The inverse-wavelength orientation gives the stated blue/red signs and uniqueness. Strict Jensen for T⁴ gives the bolometric consequence under exact fourth-moment neutrality; the transit-depth sign follows from the positive ratio under the stated model. Own scalar replay: python3 /workspace/branches/review_checks.py reproduced the three-temperature pivot as 0.5302843394245897 micrometres using the example constants. The supplied verifier was inspected, not executed; the example is not a proof for arbitrary measures. No inference is made for non-Planck spectra or noisy data.

## originality

PASS

The known transit contamination factor, Planck derivatives, and perturbative blackbody mixing are not new. The supported contribution is the exact, nonperturbative one-pivot criterion for arbitrary compactly supported mixtures via separated derivative supports. Relevant stellar, dust and CMB statements were checked against it; they do not state or give this global classification in the inspected material. This is a bounded historical comparison, not priority certification.

## value

PASS

The theorem decides from a single physically meaningful moment whether there is any cancellation wavelength and determines the full sign pattern, uniformly over all nonparametric temperature mixtures in scope. Exact bolometric balance supplies a practical analytic case, and uniqueness identifies what an ideal contamination pivot can and cannot diagnose. This is more useful than a three-temperature numerical example or a perturbative estimate, while expressly not covering line spectra or limb darkening.

The dated certificate retains the supplied scientific assessment, sources and limitations.
