---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limitations

`odd_area_certificate.py` runs with standard Python 3 and requires no third-party packages. Run it in the same directory as this file with `python3 odd_area_certificate.py`.

The checker represents the seven centers by integer pairs in the basis \((\sqrt3/24,0),(0,1/8)\). It uses integer-square-root rational enclosures for radicals, Machin's arctangent identity with alternating remainder for \(\pi\), and a positive-term \(\arcsin\) expansion with explicit tail. It verifies that every relevant pairwise circle-intersection event is strictly ordered, and integrates signed Green boundary arcs by rational interval arithmetic. The algebraically simplified expression is enclosed independently and cross-checked against the Green calculation. An additional midpoint radial integration with 8,192 and 65,536 directions produces concordant approximate values but does not enter any proof or certificate.

The certificate proves \(-0.033502<\operatorname{OA}-\pi<-0.033500\), which is stronger than the strict inequality needed to certify the perturbation neighborhood. It does not establish an optimal configuration, an optimal area or an optimal perturbation radius. Independent mathematical validation is not yet performed.
