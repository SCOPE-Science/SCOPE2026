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

The provided `verify.py` and `collapse_certificate.json` are complete standalone companions; run `python3 verify.py` with Python 3 and no third-party packages. The checker enumerates all nonempty faces at squared Euclidean distance thresholds 3, 4, 8, 11, and 12; verifies the exact shell multiplicities; checks the 24-triangle sphere's vertex links; replays all 80 certified free-face collapses; verifies the four antipodal cube pairs and seven antipodal full-set pairs; and checks the squared-threshold-12 cone condition. The included `verification_output.txt` records an actual successful run.

Complete reduced mod-two boundary ranks are computed separately. Their ranks agree with the claimed sphere dimensions; the **integral** homotopy equivalences come instead from the geometric triangulation, explicit elementary collapses, and joins of discrete two-point spaces. The finite verifier does not establish novelty in the literature, does not certify computations outside this model, and is not an independent audit.
