---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The Leibniz equations kill the cross-shore blocks by disjoint supports, make each within-shore block symmetric, and kill the two shore-sum vectors. Conversely those conditions suffice on basis products, including a singleton shore. For a symmetric square-zero block P, U=im P is totally isotropic, ker P=U⊥, and B(x,x)=B(x,1)² implies U⊂1⊥ and P1=0 automatically over any characteristic-two field. A rank-r block with prescribed image U is exactly an invertible symmetric map U*→U. The odd hyperplane is symplectic, so its isotropic-plane count follows by choosing successive independent vectors in the current orthogonal complement. In the even hyperplane the radical is k1; rank-r images containing it correspond to (r−1)-planes in its symplectic quotient of dimension 2h−2, while those avoiding it are lifts of r-planes with q^r possible linear sections. This independently gives the coefficient (I_{h−1,r−1}+q^r I_{h−1,r})S_r, with out-of-range terms zero. For the frozen equivalent rank-shift expression: on a symplectic complement, T has square zero and Tw=0. If w∈im T, P(v) belongs to the rank-r image of the complement for exactly one scalar a; all other a add one rank. If w∈ker T outside im T, the image of the complement already gains the radical line and P(v) adds an independent direction, giving rank r+2. The symmetric matrix product follows from the 1×1 and 2×2 Schur complement recurrence, with S_0=1 and S_1=q−1. For geometry, every image extends to a maximal isotropic plane in 1⊥ over the algebraic closure. Maximal planes are parametrized by a Lagrangian Grassmannian (in the even case they all contain the radical); the incidence of blocks with image contained in such a plane is a vector bundle of symmetric maps, generically with invertible fiber forms. The rank-maximal locus identifies the plane as its image, giving an irreducible dense rational locus defined over k via the affine big cell. The base and fiber dimensions sum to h(h+1) for odd size and h² for even size; equivalently the same projective incidence projects onto every geometric point and shows geometric irreducibility. Dimension and rationality add/multiply as appropriate for the product. Independent replay python3 /workspace/checks/03_rank_certificate.py exhausts binary symmetric row-sum-zero blocks up to m=6 and compares 32 exact even-formula cases across q=2,4,8,16. These checks support, not replace, the all-field arguments. The 13 spectra and full Leibniz enumerations in the frozen VERIFICATION.md are recorded checks, not rerun here.

## originality

FAIL

The complete finite-field rank census is a central finding, not just ancillary evidence. Its coefficients are special cases of Brouwer–Gow–Sheekey's explicit shape-by-shape symmetric nilpotent counts, and Reis–Cadavid already give the complete bipartite derivation reduction. The row-sum condition does not restrict the square-zero symmetric count. These prior results recover the full labeled product by direct specialization and multiplication. The different rank-shift expression does not establish a new census. This failure is not a claim that the reduced-variety rationality statement appears in the 2014 paper or that the geometry is false.

## value

FAIL

A labeled rank census for square-zero graph derivations is a natural invariant, but the record's central claim is precisely a census already obtained by combining a published complete derivation characterization and exact labeled counts indexed by nilpotent shape. Re-expressing those coefficients via even rank shifts and verifying examples does not supply a new invariant or independently motivated benefit over the covering formulas. The separate geometric description is correct and gives a useful proof viewpoint; it does not turn the announced census into a new exact result. No narrowed replacement is being accepted by this review.

The dated certificate retains the supplied scientific assessment, sources and limitations.
