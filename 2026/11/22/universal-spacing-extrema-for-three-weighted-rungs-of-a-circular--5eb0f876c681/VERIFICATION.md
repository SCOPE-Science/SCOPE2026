---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The layer-symmetric and antisymmetric Laplacians are L_C and L_C+2D. The former has nonzero eigenvalue product n² and the latter is positive definite for t>0, so the matrix-tree prefactor is n/2. The rank-three lemma and periodic delta-source recurrence give the specified I+uK_S (u=t−1) and normalized cyclic kernel with q=2−√3. Independently expanded the difference of the two 3×3 determinants and recovered the exact positive certificate. The contrast bracket 1+q^(2z)+(u/√3)(1−q^(2z)) exceeds 1−1/√3 for u>−1; the other nonzero factors have the required sign for y≥x+2. Gap balancing terminates by decreasing the sum of squared gaps. For the minimum, repeatedly transfer a unit from a nonlargest gap ≥2 to a largest gap; each is the inverse of a strict balancing move and terminates at (1,1,n−2). Permutations of three cyclic gaps are realized by rotations/reflection, so strictness and symmetry give all equality cases. At t=1 all placements tie. Replay: python3 /workspace/branches/independent_exact_checks.py prism. Independent full cofactors give (2480040,2432232) at n=9,t=2 and (147015,414421/3) at t=1/3 for balanced and consecutive placements, respectively. The frozen scripts were inspected, not run; the calculations support, not replace, the universal proof.

## originality

PASS

The closest distinct screened-cycle result already orders the principal determinant of the very same kernel under gap balancing, and contributes the cubic-coefficient comparison. The supported distinct claim is the full shifted determinant with exact strict finite-contrast ordering on both sides of t=1, especially the weakening side. The unweighted kernel and ordinary principal-determinant spacing order are not claimed as new. No earlier or same-date inspected independent statement was found to supply the full finite-contrast inequality.

## value

PASS

A natural discrete network-design problem has both exhaustive extremizers and an explicit strict local order, uniform over every size and all positive weights. Three defects introduce the first cubic interaction; the ratio bound explains why a sign reversal of the conductance perturbation cannot reverse the ordering even though it reverses the cubic term. This is not just computing the unweighted tree count or repeating a pairwise spacing law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
