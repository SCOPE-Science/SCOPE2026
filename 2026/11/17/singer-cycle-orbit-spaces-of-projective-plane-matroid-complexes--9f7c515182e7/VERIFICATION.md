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

# Reproducibility and limits

Run `python3 verify_singer.py` with Python 3. No third-party dependencies, network access, private datasets or precomputed topology tables are required. The expected full terminal output is recorded in `verification_output.txt`. The checker searches for cyclic planar difference sets for finite projective-plane orders \(q\in\{2,3,4,5\}\), checks their pair-line incidence, enumerates all independent triples, tests every nontrivial cyclic rotation for fixed triangles, and compares two independently specified quotient Euler-characteristic counts: the cell orbits of the barycentric subdivision and the fixed-point Burnside formula. The expected final line is `SINGER_PLANE_QUOTIENT_FINITE_CHECK_PASS q=2,3,4,5`.

The mathematical proof handles **all prime powers** by linear algebra over a cubic extension, the general shellability theorem and Armstrong's fundamental-group theorem. The verifier does **not** prove this infinite quantification and does **not** calculate fundamental groups independently. It checks finite combinatorics and numeric consequences only. The nonfree case is explicitly included at \(q=4\); the other tested cases check the free branch. No claim about integral higher homotopy groups or the cup-product structure is verified or asserted.

Scientific review status: self-reviewed; independent mathematical audit not performed.
