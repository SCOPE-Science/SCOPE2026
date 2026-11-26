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

With w=0 the two branches a=0 and v=0 meet only at the zero input; positive norm representation counts for d≥2 account for all scalar targets, including the anisotropic binary case. With w≠0, v=w/(2a) and t=a² give exactly two roots per distinct t in H solving t²−bt+Q(w)/4=0. For c=Q(w)/4, collisions other than equality require tu=c, impossible for c=0 or nonsquare. For c∈H the involution t↦c/t has fixed points precisely at square roots of c within H; their count is gcd(2,h) if c is a fourth power and zero otherwise. Summed over the h square norms, the fixed-point counts total h, by assigning one norm s=4t² to each t. This gives M₂ and M₄, with the subtraction for M₄ using only the singleton orbits in the square-norm class. Diagonal Gauss sums give the stated determinant signs for even d and the character of s times the determinant sign for nonzero norms in odd d. Substitution gives the signed correction ±h(h−1)/2 times the stated power of q; it vanishes exactly at q=3. This exception is about image size, not equality of all pointwise fibers. Division by q^(d+1) gives both limits. Independently enumerating (a²+Q(v),2av) for all inputs with d=2 and Q(x,y)=x²+u y², taking u a square and a nonsquare, gave images (11,11), (49,47), and (127,133) for q=3,5,7 respectively, with every target fiber checked including missing outputs. This is a set-theoretic fiber law, not a scheme ramification claim.

## originality

PASS

The supported increment is the combined pointwise finite-field root census, quartic-residue branching, and exact discriminant-sensitive image count, not the spin-factor product, quadratic norm counts, or general cyclic-group inversion. The strongest distinct indexed statements concern different maps or counted objects. Primary passage access was limited; no universal priority is inferred.

## value

PASS

Squaring is intrinsic to the Jordan algebra. The formulas separate scalar fibers from 0/2/4 nonzero-vector fibers, identify where quartic residues matter, and show when the exact image invariant loses all determinant-class separation. The latter cancellation is invisible in separate norm-value tables and in the common limiting density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
