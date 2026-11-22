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

# Exact reproducibility checks

The unnormalized complex Fourier matrix at order ten and its \(63{,}504\) independent five-row/five-column restrictions are defined in `RESULT.md`. Compile and execute `fourier10_rank.cpp` and `fourier10_cyclotomic.cpp` using C++17 and compare their JSON outputs with the included `rank401.json` and `rank_exact.json`. Both independent exact algorithms returned ranks zero through five in counts `[0,0,0,240,6640,56624]`. The finite-field computation checked all nine affine row classes, all orbit-member profiles, and the exact rank-three residue-occupancy characterization on all pairs. The cyclotomic calculation reduced every potentially relevant determinant to \(\mathbb Z[X]/(X^4-X^3+X^2-X+1)\), with no numerical tolerance.

The finite-field certificate is rigorous in characteristic zero because \(401>2\cdot5!\), and the four distinct primitive tenth roots modulo \(401\) are enough to distinguish every degree-at-most-three reduced minor polynomial with the proven coefficient bound. The order-ten result does not assert any analog for larger matrices or noisy reconstruction. An independent scientific audit has not been performed.
