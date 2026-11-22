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

# Reproducibility

Execute `python3 verify_maclane_boundary.py` with Python 3; no external dependencies are required. The program enumerates the \(8\) nonzero points of \(\mathbb F_3^2\), the \(8\) affine three-point lines and \(4\) two-point lines, constructs the \(16\)-vertex, \(28\)-edge Laplacian, performs exact unimodular diagonalization to \(1^{[9]},2,6,12,12,48,48\), and checks matrix multiplication, determinant-one transforms and both reduced determinants. The output is included in `verification_output.txt`.

This is a complete finite exact computation of a stated explicit matrix, not a proof of any claim about uncomputed geometric configurations. The geometric identification follows the cited MacLane incidence description and blowup geometry. Raynaud's theorem applies only to regular, unit-thickness semistable smoothings; independent mathematical review has not been performed.
