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

The affine Jacobian criterion at Y=0 gives nonzero X derivative for X=0 or X^3=c; infinity is smooth and is the rational hyperflex. The diagonal order-nine automorphism preserves the smooth quartic in every allowed characteristic. Faithfulness needed here follows for this nonhyperelliptic genus-three curve from its canonical embedding and the tangent representation of its Jacobian. The mod-two reduction kernel on the Tate module is pro-two, so the action still has order nine. Since ord_9(2)=6 its characteristic polynomial is Phi_9, and the linear centralizer is multiplication by F64^*. The adjoint involution for the Weil form sends the primitive ninth-root multiplier to its inverse, hence acts on F64 by the eighth-power automorphism. The symplectic centralizer is exactly the norm-one subgroup b^9=1. Arithmetic Frobenius commutes with the rational automorphism and preserves the form, so its linear action lies in this subgroup. Using the rational hyperflex theta characteristic as origin makes all these actions linear on the theta torsor. Under transport by (X,Y) -> (t^3 X,t^4 Y) with t^9=c, the exponent changes by 4j where t^(q-1)=zeta^j. This character is surjective with equal fibers, independently of the base exponent. Every nonidentity power has no eigenvalue one on J[2], so its only fixed theta is the odd hyperflex theta. The odd nonfixed and even orbit lengths are exactly the order of the Frobenius power; this gives the table and the zeta factors. A Frobenius-fixed theta line bundle descends over a finite field by the vanishing Brauer group (and the square relation is checked after injective Picard base change). Even theta characteristics on a smooth plane quartic are ineffective, so the shortest even cycle gives the asserted minimum symmetric determinant extension degree. An independent F19 enumeration used all 381 projective lines and compared homogeneous quartic restrictions with a precomputed set of projective quadratic squares. It found 28 rational bitangents exactly at c=4,15 and one otherwise; together with the shift proof this reproduces the sample degrees. Replay: python /workspace/review_check_3.py.

## originality

PASS

The geometric order-nine action and orbit patterns, and the twist and determinantal frameworks, are already known. The accepted distinct contribution is the realization and exact frequencies of three arithmetic strata, including the minimum degree-nine obstruction, uniformly for all the allowed finite fields. These follow by combining known ingredients with the finite-characteristic symplectic-centralizer and uniform Frobenius-transport calculation; they are not a new classification of geometric actions, a new twist parametrization, or a specialization of an inspected theorem of arithmetic theta-cycle distributions.

## value

PASS

The order-nine Picard quartic is a distinguished geometric source of a Frobenius obstruction. The calculation upgrades an abstract allowable permutation to guaranteed geometric realizations with exact multiplicity over every admissible finite field, and separates the existence of a rational hyperflex from that of a rational symmetric determinant by a sharp ninth-extension barrier. This goes beyond either listing nine twists or restating the geometric order-nine cycle type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
