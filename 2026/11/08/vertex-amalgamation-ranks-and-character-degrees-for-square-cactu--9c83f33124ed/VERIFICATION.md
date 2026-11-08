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
# Mathematical verification

The reproducible code `checks/check_square_bouquets.py` directly constructs the original skew-symmetric edge-weighted matrices and performs modular Gaussian elimination. It compares every rank cell against the theorem for the displayed small cases. For odd prime fields it independently tests the irreducible degree-squared sum against the group order, and evaluates Rossmann's vertex-support conjugacy-class enumeration by enumerating all vertex subsets independently of the weighted rank enumeration. The actual program output is stored in `checks/direct_output.txt`.

The tests include complete enumeration of all \(3^8=6561\) edge assignments to a two-square bouquet over \(\mathbb F_3\), and all \(2^{12}=4096\) assignments to a three-square bouquet over \(\mathbb F_2\). Every checked rank, character sum, and total class count agrees. These are exhaustive only for the listed finite cases. The unlimited theorem follows from the matrix/row-space and group-algebra arguments in `RESULT.md`, not from extrapolation.

The code is standard Python and has no nonstandard dependencies. Run `python checks/check_square_bouquets.py` from the package root to reproduce the stored output.

Limitations: the script enumerates only prime fields, while the proof covers all prime powers; finite-field extension cases and t beyond the listed test range are not exhaustively checked. Neither full priority certification nor external independent audit is claimed.
