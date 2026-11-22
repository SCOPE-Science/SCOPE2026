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

# Reproduction

Run `python3 gp_tensor_verify.py` with Python 3.9 or newer in the same directory as `verification_output.txt`, and compare the resulting standard output byte-for-byte with that file.

The code builds the categorical product directly, independently finds its shortest paths and general-position faces for widths 3 through 6, exhaustively checks free-face collapse conditions and five-triangle fillings for widths 3 through 8, and calculates mod-two boundary ranks for widths 3 through 8. The resulting sphere ranks agree with the closed formula. No external libraries or remote services are required.

# Mathematical verification boundaries

The uniform proof is in `RESULT.md`: complete face classification, explicit row and rectangle collapses, actual combinatorial disk fillings of every missing triangle, and integral Hurewicz–Whitehead. These are mathematical arguments for every integer \(n\ge3\); a bounded computation alone would not justify them. The finite code does not calculate higher homotopy groups, does not certify an infinite family, and is not an independent mathematical audit.
