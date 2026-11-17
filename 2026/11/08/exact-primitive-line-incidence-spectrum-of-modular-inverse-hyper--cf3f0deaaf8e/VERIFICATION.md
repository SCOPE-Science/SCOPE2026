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

A primitive affine ring line has exactly one canonical form X+bY=c or aX+Y=c with a∈pR, so T=q²+q p^(k-1) lines. On the hyperbola xy=1, each form reduces to a quadratic in unit x. The second family yields only single roots by Hensel; in the first, discriminant z²=c²-4b has 2 unit roots, 2p^h roots for nonzero square strata valuation 2h, and p^floor(k/2) roots for zero discriminant. Correct unit-root exclusions and line counts yield N1=2(p-1)S², N2=(p-1)(p-2)S²/2, N_(2p^h)=(p-1)U p^(k-2h-1)/2, N_(p^floor(k/2))=U for k>=2, separate k=1 branch and N0 by subtraction. Independent exhaustive line-point counting of 7 (p,k) cases including (3,3),(5,2),(7,2), 4672 total canonical lines, corroborated exact spectrum and first incidence moment.

## originality

PASS

Khan–Magner–Senger–Winterhof use classical quadratic roots for Euclidean straight-line collinearity of integer representatives, not all primitive modular ring-affine line subsets. Survey and Ford–Khan–Shparlinski examine Euclidean geometric statistics. Closely related Resultary finite-chain-ring additive convolution is a different invariant. No inspected paper supplies complete all-lines N_j, maximum-attainer count and limiting fractions.

## value

PASS

A uniform complete incidence multiplicity classification for the natural inverse hyperbola and all primitive affine lines over finite local rings is a geometrically meaningful exact invariant, with sharp tangencies and stabilized distributions, beyond any isolated finite-case enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
