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

The closed-form reduction is established analytically in RESULT.md and does not depend on a numerical solver. In particular, equation (9) supplies a universal polar norm upper bound and the endpoint witnesses attain it.

Run the standalone Python script as `python verify.py` with NumPy and SciPy available. It constructs two separate halfspace representations and compares their farthest squared norms in six low-dimensional sample graphs; it also checks the endpoint property for every farthest polar vertex found. Expected marker: `HANSEN_FRACTIONAL_ANTIBLOCKER_CHECKS_PASSED`.

The script additionally decodes the published \(35\)-vertex Ramsey graph6 string, checks its number of edges and absence of triangles, and performs exact integer-bitset maximal-independent-set enumeration without a solver. It confirms independence number \(8\); expected marker: `RAMSEY35_EXACT_CHECK_PASSED`. The graph6 instance is externally sourced, with attribution in the code and RESULT.md. The theorem's independent mathematical audit remains not performed.

Numerical halfspace intersection checks are finite corroboration, not exhaustive over all graphs. The Ramsey graph computation is an exact check of the specific embedded witness. The asymptotic random-graph argument is proved by its probability bounds rather than simulated.
