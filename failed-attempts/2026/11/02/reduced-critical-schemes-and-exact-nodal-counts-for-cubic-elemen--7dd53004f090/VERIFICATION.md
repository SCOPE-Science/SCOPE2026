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

Each derivative is x_i²−e₁x_i+e₂, so the coordinates of a critical point have at most two values. For distinct t,u with multiplicities m,ℓ, put a=m−1 and b=ℓ−1. Subtracting the two derivative equations gives at+bu=0; the derivative at a t entry then equals −(at²+bu²)/2, as the extra u entry contributes zero against the remaining sum. The two equations imply at=bu=0. If both values were nonzero, a+b=n−2 would vanish, contrary to hypothesis. The surviving nonzero support has size 1 mod p, including the all-equal case from (n−1)(n−2)t²/2=0. Conversely both types of derivative vanish for those supports. At an indicator vector the Hessian blocks are I−J on the support and J−I off it, with mixed block zero. The first has kernel the radial line; the second is invertible because ℓ−1=n−2 in k when the block is present. In an active affine chart the radial kernel meets the chart tangent complement trivially, giving full derivative rank and a reduced simple critical point. The restriction of the Hessian to that complement is nondegenerate since the radial line is the radical; thus points on the hypersurface are ordinary double points. Euler's identity puts all critical points on X for p≠3. In characteristic 3, at m=1+3a the coefficient of T³ in (1+T)(1+T³)^a is a mod 3, so the singular subset is precisely m=1 mod 9, reduced since it is defined inside a finite reduced scheme. Any factorization e₃=GH would make the intersection of the two factor hypersurfaces singular of dimension at least n−3≥1, including factorizations with a repeated factor. Hence X is integral; hypersurface S₂ and regularity in codimension one give normality. The examples give 36 nodes for (p,n)=(5,8), and five critical points but four nodes for (3,4).

## originality

FAIL

The earlier October 13 Resultary theorem supplies the exact critical support and count and already computes the Hessian at nonzero points of those support lines. Although it states generic smoothness rather than global projective reducedness, the displayed block ranks hold for every nonzero scalar. Projective reducedness and the node property are direct consequences. The hypersurface selection and global geometry then follow by routine Euler/binomial and codimension arguments. The specific mod-9 statement was also explicitly found in a later catalog record; its later date is not used as earlier priority evidence.

## value

FAIL

Projective scheme structure and counts in characteristic three are natural invariants, and distinguishing Euler-critical points from singular points is important. In this range, however, the exact support and rank calculation are known, and the residual distinction is a single evaluation of the cubic on that known support followed by standard local- and global-geometry consequences. It adds no surviving classification or structure not mechanically accessible from the prior result. No new theorem about the harder exceptional congruence or cone vertex has been established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
