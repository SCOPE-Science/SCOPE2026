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

# Reproduction of the finite-state calculation

The proof's substantive finite certificate is the exact solution of the backward equations for every unordered two-site or three-site occupancy state of each sixteen-vertex graph. The script `coalescence_exact_check.py` needs only the Python standard library. Execute it with `python3 coalescence_exact_check.py`.

The script reconstructs the \(1152\)-element rook automorphism group and the \(192\)-element Shrikhande affine group, obtains triple partitions with 4 and 8 classes respectively, repeats the partition using transition-signature refinement with no automorphism input, solves both with rational arithmetic, and checks each of the \(560\) three-site backward equations per graph. It asserts mean triangle times \(143/14\) and \(1145/112\), the difference \(1/112\), two-particle times \(15/2\) and \(9\), and the uniform triple mean \(2203/196\).

As an independent numerical cross-check, `coalescence_sparse_check.py` (requiring NumPy and SciPy) constructs the full \(680\)-state transient Poisson system directly, without symmetry reduction. It verifies the triangle and uniform triple means within \(10^{-10}\).

These computations certify a particular *finite* model once the standard backward-equation reduction and transient-chain uniqueness argument are accepted. They do not prove novelty or establish any claims for larger networks, distinct clock laws, or non-Markovian walkers. The results have undergone self-review only; independent scientific audit has not yet been performed.
