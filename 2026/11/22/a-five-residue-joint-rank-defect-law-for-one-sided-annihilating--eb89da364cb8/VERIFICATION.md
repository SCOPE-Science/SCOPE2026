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

On im(E)⊕ker(E), EF=0 forces F=[0,0; C,D], and F²=F holds exactly when D²=D and DC=C. Hence rank(F)=rank(D)=s, and at fixed r,s the free map C has the uniform rectangular s×r rank law and rank(C)=rank(FE). Choosing complementary projections and the free maps yields the exponent D_n=2n(r+s)−2r²−2s²−rs and the Euler quotient in the record. Completing its square gives the exact center (2n/5,2n/5), exponent 4n²/5, and eigenvalues 3/2 and 5/2 of Q; extending weights by zero off the feasible triangle gives a fixed summable Gaussian bound on each residue class. For fixed shifted ranks and defect the limiting conditional mass follows from the finite rectangular formula; Φ_∞>0 and the uniform q^(−k²) tail bound make each conditional limit a probability. Pointwise convergence to joint mass one on the countable lattice then gives total variation. The dependence on imbalance is genuine: at k=0 the conditional mass Φ_∞/Φ_|i−j| increases with |i−j|. For FE=0 as well, C=0 loses exactly the factor q^(rs); equivalently these pairs are ordered decompositions into im(E), im(F), and the common kernel. The new saddle at (n/3,n/3) with top exponent 2n²/3 yields Xi, and division by the first saddle gives q^(−2n²/15) times the stated prefactor. The formula is valid on all 15 residue classes; it does not require 15 distinct values. In the mixed case the count of the flag and isomorphism defining N, followed by the choice of ker(P) containing im(N) and its complement, gives mixed weight q^D times Φ_n Φ_(n−s)/(Φ_s Φ_(n−2s) Φ_r Φ_(n−r−s)). At each fixed site n−2s→∞, so the extra ratio tends to one; the same summable bound up to a constant applies irrespective of the narrower support. This proves the shared total and rank law. Direct evaluation of maps by images in /workspace/branches/matrix_rank_replay.py independently checked all feasible cells in both ensembles at (n,q)=(1,2),(2,2),(3,2),(2,3),(3,3); at (3,3) the one-sided, two-sided and mixed totals are 6789, 2109 and 5020. These finite checks corroborate the block argument, not the unrestricted limit.

## originality

PASS

The finite joint rank weights and rectangular defect distribution have earlier coverage, as the record acknowledges. The fixed-field growing-dimension joint local law, sharp opposite-annihilation asymptotic and equal total asymptotics for the two models require distinct lattice-saddle comparisons beyond those inputs. No examined theorem supplies the combined claim; priority is bounded by the literature inspected.

## value

PASS

One-sided annihilation for random projections is a natural asymmetric constraint. The law quantifies how much rank survives in the reverse direction, with the defect retaining dependence on rank imbalance. The sharp q^(−2n²/15) rarity with a lattice correction goes beyond mere high-probability nonannihilation. A comparison with a different natural representation model then identifies genuinely equal leading populations without finite equality. These are precise probabilistic invariants not conveyed by top-stratum dimension or finite counts alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
