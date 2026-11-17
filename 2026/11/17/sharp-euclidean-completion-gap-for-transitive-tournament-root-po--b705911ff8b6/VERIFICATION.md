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

# Reproducible verification

Run `python3 verify.py` with Python 3. The program uses standard-library rational arithmetic and prints `POSITIVE_ROOT_HAUSDORFF_PASS small=2,3,4 all_negative_certificates=5..16 large_highest_KKT=30,61,103` on success. It checks nonnegative convex weights summing to one, all root-vertex projection inequalities, the exact upper bounds, and the positive directional improvement separating every nonextremal negative root in dimensions five through sixteen. Additional highest-root projections are checked at dimensions thirty, sixty-one, and one hundred three.

Optionally, with NumPy and SciPy installed, run `python3 verify_qp.py`. This was executed and printed `INDEPENDENT_QP_PASS negative_roots=220 dimensions=2..11`. It independently minimizes squared Euclidean distance over root convex combinations for every negative root in dimensions two through eleven and checks the winner, the claimed formula, and projection coordinates. This is numerical corroboration only. The analytic proof, not either finite computation, establishes the infinite-dimensional claim.

The scripts use the fixed orthonormal coordinate realization and do not require external files, network access or private data. They do not constitute independent mathematical auditing or certification.
