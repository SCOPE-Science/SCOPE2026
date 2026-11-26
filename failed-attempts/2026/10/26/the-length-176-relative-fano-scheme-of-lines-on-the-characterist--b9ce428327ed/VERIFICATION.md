---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The relative scheme and nodal-fiber claims check. In a pivot chart (s,t,as+ct,bs+dt), the only s²t² term is λ(ad+bc). The sentence at RESULT.md:35 saying that binom(4,3) vanishes mod 3 is a local exposition error: it is 1 mod 3, and the displayed equations, all subsequent calculations, and the claim use the correct surviving mixed terms. For λ≠0, a zero chart entry forces an impossible zero pivot-row norm. Otherwise c=ζa, d=−ζb and the s³t and st³ equations imply 2λζ²ab=0. At λ=0 the zero-entry lines are the 3·4² coordinate-pair lines; in the nonzero case the two mixed equations force c/a=−d/b and a⁴=b⁴=(c/a)⁴=1. All six pivot minors are nonzero for the latter type, so the fixed X,Y chart counts all 64 of them. The four nonmiddle equations have invertible Jacobian at each line. Thus the completed ring is k[[λ]]/(λh(λ)), h=ad+bc. The coordinate-pair lines have h(0)≠0; the others have h(0)=0 and h′(0)=(αβ)²≠0. This gives 48 simple and 64 double relative points, 112 reduced central points and length 176. The absence of any other geometric points and finite type give a finite scheme supported on the central fiber. The gradient at λ≠0 forces nonzero coordinates with equal fourth powers; normalization gives 16 solutions exactly at λ⁴=1, and the off-diagonal quadratic form has nonzero determinant there.

## originality

FAIL

A separate published Resultary record states the entire same relative scheme and both geometric consequences, not just the known central count. This establishes equivalent indexed coverage, not priority or derivation in either direction. No distinct scientific remainder is supported by the submitted claim.

## value

PASS

The underlying scheme computation is substantive: it determines whether each embedded line deforms over the specified pencil and separates support from scheme length. Neither a line census nor the mere existence of special nodal fibers answers that geometric question. This value is not a new contribution from the frozen record because the whole result is already covered in the separate indexed finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
