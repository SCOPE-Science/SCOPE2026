---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The polygon support-functionals are normalized by c=cos(pi/(8m)), s=sin(pi/(8m)); dihedral reduction leaves smooth-edge and vertex Birkhoff sectors. In smooth case x=(c,t), y=(0,c) up to sign, the chord norms are sqrt(2)±t/(sqrt(2)c); at vertex x=(c,s), the first sector half y=(-r,c) has sqrt(2)±(s-r)/(sqrt(2)c). The other sector follows from adjacent dihedral symmetry. These cases give the displayed threshold and quarterturn equality. Independently, the stronger *unrestricted* pointwise threshold follows from J(X)=g(X)=sqrt(2), established by published theorems for every pi/4-rotation-invariant norm, so no correctness defect is asserted.

## originality

FAIL

FAIL: Komuro–Saito–Tanaka (2016), Proposition 3.5 and Theorem 3.10, establish ordinary James J(X)=sqrt(2) for all pi/4-rotation-invariant normed planes, including all regular 8m-gons. Baronti–Papini (2022) establish g(X)J(X)=2 and g(X)≤g_perp(X)≤J_perp(X)≤J(X). These implications force *both* proposed orthogonal constants to be sqrt(2) without a new polygon argument. Moreover the claim’s pointwise min≤sqrt(2)≤max holds for all unit pairs from J=g=sqrt(2), so the stronger pointwise wording is also covered. Known quarter-turn extremizers require only elementary norm symmetry. The old source-package originality assessment overlooked this dominating-parameter deduction.

## value

FAIL

The all-8m constants and pointwise threshold add no independent mathematical invariant or meaningful gap once Komuro–Saito–Tanaka and Baronti–Papini are combined. The facet-coordinate derivation is a valid alternate proof of a covered corollary, not sufficiently valuable as a distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
