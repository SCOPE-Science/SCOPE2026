---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Deleting the new vertex from a spanning tree of the root-weighted augmentation designates exactly one root per forest component, so the matrix-tree cofactor is the multiaffine root enumerator. Substitution of signs computes the unnormalized Walsh sum with no positivity requirement. In the bipartite Schur complement the off-diagonal block has rank one and both diagonal blocks are invertible for m,n≥2, yielding the determinant prefactor and the product of the two reciprocal-diagonal sums. Its vanishing gives the exact zero-product equality; each weight pair contributes binomial multiplicity (eigenvalues for different pairs need not be distinct). The even-even equality is blocked modulo 2. At balanced odd d, write Q=d²−1 and c=(d−1)/2. Same-side weights cannot give equality except at (c,c); opposite displacements a and −b require Q(a−b)=2ab with 0<2ab≤Q/2, impossible. Stirling gives 2/(πd) for the resulting relative nullity. For d,d+1 the zero equation determines v=(d²−1)u/[d(d+2)−2u] where u=d−x and v=y. For 1≤u≤d, the positive difference u−v is strictly below one: the denominator is at least d², and u(2d+1−2u)≤(2d+1)²/8<d² for d≥2. Thus only u=v=0 remains, giving exactly one zero character. The computation supports, but does not prove, the all-size classifications.

## originality

PASS

The Walsh transform is a direct signed evaluation of a classical root enumerator and uses a standard rank-one determinant reduction. The substantive distinct contribution is the exact multiplicity and uniqueness of the balanced and consecutive-shore zeros. No prior statement or stronger root-count theorem inspected here supplies those arithmetic conclusions without the new exclusion arguments. Historical priority remains bounded.

## value

PASS

The exact kernel measures lost Walsh modes in a natural forest-root convolution. Proving zero loss for both even shores, an explicit central-binomial defect for odd balanced shores, and one lost mode for consecutive shores exposes distinct behavior on natural infinite families, useful beyond raw root enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
