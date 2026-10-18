---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The XLindley density at rate theta>0 decomposes by direct coefficient comparison into a Gamma(1,theta) / Gamma(2,theta) mixture with weights a=theta(theta+2)/(1+theta)^2 and b=1/(1+theta)^2, a+b=1. A sum of two independent same-rate gamma-mixtures has shapes 2/3/4 and weights a^2, 2ab, b^2. Poisson-gamma integration gives the stated three NB mixture. Separately Poisson(Y1+Y2) equals in law independent Poisson(Y1)+Poisson(Y2), so the defined PTS-XL model equals PXL convolved with PXL; PGF squares. Independent symbolic exact-rational algebra checked a+b, the gamma density, the PXL PGF formula and the NB-mixture generating function for indeterminate theta,z. This is correct mathematics on theta>0.

## originality

FAIL

FAIL based on implication from identified PRIOR MODEL DEFINITIONS, not merely a failed literature search: the 2026 PTS-XL publication explicitly defines its count as Poisson conditional on the sum of two independent XLindley variables; Ahsan-ul-Haq et al. 2022 define PXL as the count from Poisson mixing with one XLindley variable. The classical Poisson superposition property implies X_PTS-XL =d X_PXL,1+X_PXL,2 immediately, without an additional model-specific assumption or computation. The three NB weights then follow automatically by expressing the published XLindley density in its elementary common-rate gamma mixture and applying standard gamma-convolution and Poisson-gamma facts. The exact squared PGF is already algebraically implied by the published source PGF. Although the specific three-NB decomposition may not be printed, it is a direct re-expression of two published generative definitions, with no independently unentailed theorem.

## value

FAIL

FAIL: a direct sampler is practically convenient, but under a mathematical value bar this package contains only textbook mixed-Poisson/gamma closure calculations and a renaming of the already-defined double-sum model as a convolution square. No new inferential theorem, sharper tail property, identifiable parameter distinction, or nontrivial model boundary is established. Correct algebra/reproducibility and practical notational convenience alone do not make this already-determined model-specific re-expression a substantive new mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
