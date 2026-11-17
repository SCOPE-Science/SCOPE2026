---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The positive real kernel-overlap constraint forces a-bar b real and the exact hyperbolic parameterization a=(w-k)/(1-kw), k=sqrt(1-q²). Swapping inputs bounds the non-dominant branch. The attained scalar F(w)=qw(1-w²)/D(w), D=1-βw²-(1-β)kw>0, vanishes at 0,1; differentiating yields N=1-(3-β)w²+2(1-β)kw³+βw⁴. N decreases strictly from 1 to -2(1-β)(1-k), giving one root u. N(k)=q²[(2-β)q²-(1-β)] establishes sign geometry; envelope differentiation gives β_c=(1-2q²)/(1-q²) for q<1/sqrt2 and unique q sqrt(1-q²) minimum. Double-root rescaling yields small-q and β→1 expansions; q=1 and β=0 endpoints explicitly covered. Independent 90 parameter/root tests support, but do not replace, these analytic arguments.

## originality

PASS

The prior Bhattacharya–Patra theorem already gives circularity and a two-branch scalar maximum for this exact family; these are not counted as new. Its inspected Section 3.3 and Remark 3.20 do not establish a unique global quartic root, alignment threshold, full minimization over damping, or sharp two asymptotics. A related same-day Resultary theorem treats higher powers m≥2 and explicitly credits the first-power analysis. New claim survives as a genuine sharpened parametric optimization, with residual equivalent-parametrization risk.

## value

PASS

Optimizing geometric damping at fixed kernel fidelity is a natural compact-operator design question. The exact nonmonotone β phase below q=1/sqrt2, unique optimal damping and antipodal-to-aligned kernel transition solve a structural optimization left open by the published scalar branch representation; asymptotics quantify singular boundaries. The result adds meaningful mathematics beyond the already known circular range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
