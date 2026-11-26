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

The valuation at each nonzero branch point detects its own Kummer generator, even after geometric base change. There are five inertia-two branch fibers and no ramification at infinity, giving genus five. The nontrivial characters indexed by subsets of three or four generators are exactly the five elliptic quotients; the other characters have two branch points. The elliptic quotients have four finite roots, remaining value -1 before twisting, and two or zero rational points at infinity according to the leading square class. This gives traces -2 eta_j and their quadratic-extension traces -6; the five character spaces give the stated numerator and ordinarity. The five quartic classes span the full Kummer subspace: the product of the class indexed by 0 and the class indexed by j recovers the jth original radical class. Therefore the permutation of their signed classes under affine substitutions (the scalar is u^4) really lifts to an isomorphism of the extensions. The even sign vectors are in bijection with presentations, with one affine orbit for each sign count 0,2,4. Distinct rational-point counts exclude further identifications of abstract curves. In an independent count on the smooth diagonal model v_0^2=U, v_a^2=epsilon_a(U-aV), normalizing the first nonzero coordinate among v_0,v_1 and counting the other three square roots gave distributions {16:1,8:10,0:5} and {56:16} over the two fields; replay with python /workspace/review_check_4.py. This count corroborates the point statistics, not the isomorphism proof.

## originality

PASS

The accepted contribution is the three abstract arithmetic classes, their frequencies in the specified deck-twist set and their exact Weil numerators. The type-4 Humbert–Edge model, elliptic factorization and branch symmetries are prior ingredients; the inspected prior statements do not supply the arithmetic signs and their full orbit classification.

## value

PASS

The complete affine rational branch set is a natural fixed configuration; its sixteen constant square-class modifications are a complete, nonarbitrary set of deck twists in this presentation. The computation distinguishes the unique zero-point abstract class and the unique sixteen-point class from the middle trace class despite identical quadratic-extension counts, and gives a test for isomorphism in the specified set rather than just examples or a point census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
