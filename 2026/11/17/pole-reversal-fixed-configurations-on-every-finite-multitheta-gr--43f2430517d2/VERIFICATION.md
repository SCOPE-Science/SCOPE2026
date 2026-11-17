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

# Computational verification and reproducibility

Run `python3 verification/pole_theta_check.py` with a Python interpreter supporting the standard library's `math.comb`; no third-party packages are needed. The saved output is `verification/pole_theta_output.txt`.

The program independently enumerates cubical cells for sufficiently subdivided ordinary stars. For each number of arms in \(\{3,4,5,6\}\) and each particle count in \(\{0,1,2,3,4\}\), it computes the alternating sum of cells made of pairwise disjoint occupied vertices and open edges, and compares this against the proposed closed formula. All twenty cases agree. A separate comparison checks the radial-tree rank formula in Farley–Sabalka, Corollary 4.2, against the closed binomial expression in 192 cases (3–14 arms, 2–17 particles); all agree.

It separately constructs theta graph vertex involutions with four-edge arms, enumerates invariant vertex subsets, and compares each fixed-point-count sector with the predicted number of fixed midpoints and swapped pairs. Twenty-one finite parameter cases agree. These vertex tests check orbit counting, not the homotopy type of the continuum fixed set.

The script emits exactly:

```
STAR_CUBICAL_EULER_CHECKS 20
RADIAL_TREE_LITERATURE_RANK_CHECKS 192
POLE_INVARIANT_DISCRETE_VERTEX_SECTORS 21
THETA_POLE_FIXED_SECTOR_CHECKS_PASS
```

The proof of the all-particle fixed-space homeomorphism is the continuous orbit-sector argument in `RESULT.md`. The dimension bound for star configuration spaces uses the published radial-tree discrete Morse theorem. No finite computation proves the universal statement, and no independent mathematical review is represented by these checks.
