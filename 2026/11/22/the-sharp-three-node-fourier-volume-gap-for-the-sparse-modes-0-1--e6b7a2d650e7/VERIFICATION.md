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

Dividing the alternant by the Vandermonde gives the symmetric quadratic S²−P. Rotation to Q=1 gives P=conj(S); complex conjugation gives minus the Vandermonde for this normalization, hence its modulus squared is minus the cubic discriminant. Writing r=|S| and u=Re(S³)/r³ gives the two stated factors. Their product is strictly concave in u for r>0. The discriminant factor plus four times the Schur-modulus factor is H=3r⁴−14r²+27, so the unclipped product is bounded by H²/16 with equality at the stated quadratic vertex. The two clipping polynomials increase for positive r and their rational brackets place the cubic root ρ strictly on the u=−1 branch. The derivative on that branch has only one positive critical root; the middle branch is <22 by the two endpoint bounds for H, and the upper branch peaks between 2 and 2.1 with value <17. The rational witness at r=3/4 exceeds 22. Thus the relaxed rectangle has only the optimizer (ρ,−1), and it is realized: after a cubic-root rotation S=−ρ, the node polynomial factors as (X−1)(X²+(1+ρ)X+1). This gives exactly the rotation/permutation orbit. The omitted r=0 case and coincident nodes have zero volume. Hadamard equality forces the first power sum to vanish, giving an equilateral triple; the other two inner products vanish precisely when neither m nor m−1 is divisible by three. Compactness gives a strict gap otherwise.

## originality

PASS

The distinct narrow claim is the exact unrestricted maximum for sparse columns 1,z,z⁴ and its non-equilateral equality orbit. No inspected distinct result covers it. The classical generalized alternant/Fekete formulation and elementary modulo-three tightness context are not included in this originality pass.

## value

PASS

Three minimal evaluations of a sparse trigonometric polynomial give a natural square design with determinant as its information-volume criterion. In the first degree-two Schur case in this family the equilateral rule actually gives zero determinant and the orthogonal ceiling is unattainable. The exact best volume and forced non-equilateral orbit resolve both how large the gap is and which designs achieve it without postulating symmetry or spacing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
