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

The five real Gaussian-polynomial Fourier +1 modes (degree 0 and 4) span the space after f(0)=0. Finite negative area forces nonnegative angular quartic leading coefficient B; zeros of B have even order 2m and the identity A=2B+Bʺ/2 implies A/B~m(2m−1)/t², forcing infinite negative area. For B>0 polar area is 〈A_+/B〉 and periodic integration by parts yields exactly 2+1/2〈(Bʹ/B)²〉+〈(-A)_+/B〉; equality requires constant B, hence no anisotropic modes. The local quadratic coefficient 1/4 follows from this identity. Symbolic CHECK.py basis and identity code inspected; analytic proof carries continuum quantifier.

## originality

PASS

The full nonradial first fourth-Hermite band receives a sharp negative-area optimizer and exact positive angular deficit; related Fourier positivity and sign-radius papers do not imply this result in inspected text.

## value

PASS

The degree-four +1 planar Hermite band is the first natural complete nontrivial Fourier-eigenfunction testing ground for the new definite-set area question. Proving a radial extremum over every nonradial mode and an exact Fisher-information deficit is a meaningful structural and quantitative classification, not just a radial test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
