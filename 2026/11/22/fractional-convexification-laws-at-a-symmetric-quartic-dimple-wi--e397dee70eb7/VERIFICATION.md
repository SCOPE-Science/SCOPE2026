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

The analytic argument comprises a global exposed-chord characterization and a local quartic normal-form calculation. The exact integral formulas for the limaçon are separately checked by independent direct quadrature and sampled polygonal convex hulls. Run `python check.py` using Python 3.9+; no third-party modules are required.

The finite checker is supplementary: it does not certify the universal theorem or prove a limit. The parameter domain is explicitly \(0<q<1\), and the fractional expansions refer to positive \(\delta=q-1/2\) only. The stated original-curve area differs from the area added by convexification.
