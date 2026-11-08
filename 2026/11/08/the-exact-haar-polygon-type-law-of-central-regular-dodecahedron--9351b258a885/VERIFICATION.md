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

# Verification

Run `python verify_dodeca.py`. No nonstandard libraries are required. The exact finite certificate uses integer pairs \((a,b)\) for \(a+b\varphi\), with \(\varphi^2=\varphi+1\), and determines signs through integer comparisons against \(5b^2\). It verifies all 20 vertex coordinates, the 30 true edges, all ten pair-normal great circles, 90 oriented intersection rays, the absence of triple intersections, and all \(2^{10}\) candidate sign chambers. Exactly 92 chambers pass the strict feasibility test, with counts 20, 60, 12 and corner-angle signatures determining their areas.

Expected output begins `EXACT_CERTIFICATE_OK` and gives section-vertex probabilities approximately 0.638408811559, 0.238989468900 and 0.122601719541. The script asserts total probability one. As an independent analytical check, the result's expected vertex count is \(30\arccos(\sqrt5/3)/\pi\), by edge separation. All exact combinatorics use integer arithmetic; decimal output is presentation only.

The continuous spherical area formula is proved in `RESULT.md`, rather than delegated to simulation. The exact script certifies the finite combinatorial cases on which that proof depends. These checks do not establish prior-publication priority or extend to noncentral planes.
