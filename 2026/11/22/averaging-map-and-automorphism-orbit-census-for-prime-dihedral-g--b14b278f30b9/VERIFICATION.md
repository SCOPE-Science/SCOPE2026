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

Reconstructed the four image-generated subgroup strata from equivariance under the images. A rotation-valued map has p individual rotation inputs and one common reflection input; a fixed reflection target subgroup has two fixed inputs and two families of opposite pairs. Full equivariance sends exactly all reflections to themselves if the image is to generate G, and leaves an arbitrary odd function on rotation exponents. For the reflection stratum normalize by Aut to <s>; the same cyclic multiplier permutes the two sets of pairs, giving four colors, with two independent singleton bits or one if pointed. For the rotation stratum a nonidentity multiplier of order d forces the 0 input and the common reflection output to be zero and leaves (p-1)/d free values on cycles. In the full stratum the coordinates f(j)/j descend to opposite pairs and are permuted regularly by the effective multiplier quotient. This proves all four formulas, including each deletion of the constant identity map and addition of the trivial stratum. Independently enumerated every 6^6 set map for p=3 by testing the identity on all pairs and computing affine automorphism orbits: (129,51,60,25). Also evaluated the formulas at p=5: (15965,3305,3969,824). The supplied artifacts/verify.py was inspected, not executed; it is a finite consistency replay and not the reason the proof holds at all odd primes.

## originality

PASS

Pass for the general odd-prime formulas only. The equivariance lemma and all four p=3 counts are credited existing results. The checked sources do not give the resulting necklace and totient-sum laws for varying p.

## value

PASS

Gives exact symmetry-reduced as well as raw counts of a natural class of set maps across an infinite family. The two distinct cyclic necklace actions and the nontrivial multiplier stabilizers quantify the orbit collapse, which neither a raw count nor the single S3 example supplies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
