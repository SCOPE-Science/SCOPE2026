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

# Reproducibility and verification

The complete infinite-family proof is in `RESULT.md`. Its decisive identity is the matrix-heat trace derivative \(-2t(e^{-tA_\theta})_{uv}\), strictly negative for all positive times under the stated one-edge completion exchange. The exchange strictly increases the number of deleted matching pairs wholly among followers, and exhausts every nongrouped placement.

Run `python3 verify.py` with Python 3, NumPy and SymPy. A replay of the embedded script returned `Verification passed {'matrix_spectrum': 240, 'all_orbits': 960, 'all_subsets': 5446, 'heat': 720, 'exact_charpoly': 35} total 7401`.

Checks include direct grounded-matrix diagonalization with \(2\le m\le9\), all budget sizes, and three screening strengths; comparisons for spectral inverse orders \(p\in\{1/2,1,2,3\}\); all placement orbits at three positive times; exhaustive subsets through \(m=6\) including tied-set counts; and exact characteristic-polynomial reconstruction for every size and budget through \(m=6\). Neither those finite checks nor the log certify the infinite-domain theorem by themselves; strict positivity of the heat kernel and the full exchange induction are necessary.

Scientific limitations include unit conductances, uniform screening, perfectly grounded leaders, and a finite nonempty follower set. Independent audit is not performed.
