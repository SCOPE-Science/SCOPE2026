---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Re-derived incoming-edge PGF H_XY(q,z)=q^(2s)+z(F_X F_Y-q^(2s)); expansion H_UU H_VV-H_UV^2=q^(2s)z(1-z)(F_U-F_V)^2. Since F_U(1)=F_V(1)=1, difference has (z-1)^3 and first two raw moments coincide; third derivative yields -6q^(2s)(mu_U-mu_V)^2. Independent integer polynomial and 65536-subset checker verifies C vs balanced B on 16 leaves and exact score-five difference q^14(1-q)^2. Earlier 16-leaf uniqueness and >16 extension are correctly removed as original claims in complete revised files.

## originality

PASS

REPAIRED: original 16-leaf cutoff and unique pair are decisively COVERED by stronger 2026-10-18/26 fixed-size rarefaction theorems; surviving explicit arbitrary U,V bivariate full-PGF swap-square identity and third-raw-moment formula were not stated in those inspected published full texts. Best-of-knowledge for corrected claim only.

## value

PASS

The exact PGF swap-square law explains an entire family of moment-indistinguishable distributions and controls the third and all higher discrepancies by a structural identity. It remains a mathematically meaningful stand-alone result, without claiming a known finite threshold anew.

The dated certificate retains the supplied scientific assessment, sources and limitations.
