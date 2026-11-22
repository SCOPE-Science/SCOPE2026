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

The proof determines all compatible skew derivations from the image of the algebra generator and proves all power-rank formulas over every field admitting the required primitive root of unity. The standalone `checker.py` reproduces deterministic exhaustive checks over specified finite prime fields; the output marker is `TAFT_JORDAN_VERIFIED`. Test computations are finite evidence and do not independently establish the universal proof.

The parameter is the polynomial \(D(x)\). When \(N\not\equiv0\pmod m\), the constant coefficient must vanish. The formula for \(D^j\) and the distinct-leading-degree rank argument are the critical proof steps. No finite enumeration is used to prove coverage in arbitrary dimension or field.

The stated relationship to cited literature is limited to material inspected and does not certify publication priority. The prior \(N=m\) case is explicitly credited. Independent audit: not performed.
