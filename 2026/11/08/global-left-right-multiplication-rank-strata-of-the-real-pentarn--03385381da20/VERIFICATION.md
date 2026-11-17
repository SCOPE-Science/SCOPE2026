---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The supplied multiplication table reconstructs a five-by-five real-linear L_p. Independent SymPy reconstruction (not executing the supplied checker) verifies det L_p=N(p)F(p), det R_p=N(p)F(conjugate p) as exact polynomial identities, with N=a²+2(b²+c²+d²+e²)>0 outside zero. In orthogonal coordinates x=S/sqrt3,y,z the identity ∂aF+∂eF=3[(a−e)²+x²] forces a=e,x=0 at every real cubic singularity; ∂aF then forces y=z=0. Conversely [1:0:0:0:1] is singular, with directly checked rank L=3 and R=5; conjugate has the reversed ranks. Rank≤3 implies all 4-minors vanish, hence det-gradient zero, so the sole exceptional line is exhaustive. On F=0 away from it rank=4, and otherwise rank=5. The real-field and canonical-gamma=1 qualifications are essential; a finite integer grid is not an infinite-field proof.

## originality

PASS

Best-of-knowledge distinct claim after exact comparison with the originating source, adjacent indexed literature and stronger published findings; gaps are expressly recorded.

## value

PASS

The principal structural invariant is the global left/right zero-divisor geometry of a specifically introduced five-dimensional nonassociative algebra, not a numerical choice of coordinates. A full cubic real hypersurface, its exact corank strata, unique corank-two directions and opposite-sided invertibility answer natural questions left by the source's restricted slice and distinguish global multiplication from the positive quadratic norm. An unindexed equivalent calculation remains possible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
