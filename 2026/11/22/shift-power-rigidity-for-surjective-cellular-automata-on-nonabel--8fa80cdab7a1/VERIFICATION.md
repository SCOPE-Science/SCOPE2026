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

Continuity and shift commutation give a single finite neighborhood; group homomorphism of the global map makes the coordinate rule a homomorphism on the direct product. Restrictions to individual coordinates are uniquely determined and have mutually commuting images. A surjective global rule is locally onto. If every coordinate image were proper then each would be abelian (order at most p²), and their commuting product would be abelian. Hence exactly one coordinate is an automorphism, and all the others are central. Here Z=[G,G]≅C_p and G/Z≅C_p², so the central maps vanish on Z and there are p² of them. The quotient of the preimage is first recovered via the shift and induced automorphism; all central corrections are computed from it and removed before applying the inverse alphabet automorphism, giving a continuous inverse. For H=σ^(−k)F, H^t fixes the quotient and acts equivariantly for translation by any central configuration, so on each quotient fiber it is translation by a fixed central configuration. Its pth power is the identity; H and σ commute, giving F^(pt)=σ^(kpt) on all bi-infinite sequences. Division by pt in the entropy identity gives the claimed formula. For k=0 only finitely many continuous iterates occur; for k≠0 the power is a mixing shift, and applying its mixing property to the preimages under each of the finitely many residue iterates proves mixing of F. The census follows by independent choices, allowing trivial maps on named offsets; a nonzero quotient character at offset one gives an exact order-p centered shear. These arguments include p=2, r=1 and negative k. The archived verifier was inspected, not run; its finite-size and random periodic checks are not needed as proof.

## originality

PASS

Credit the all-prime normal form, exponent bound and census as a package. The general architecture of automorphism coordinates and central corrections, the quaternion case and effective group-CA entropy computation are not claimed as new. The available comparisons do not establish prior coverage of the uniform exact p³ identity and count.

## value

PASS

A complete reversibility classification for a natural nonabelian family gives a sharp obstruction to removing p from an explicit uniform time-to-shift bound, not merely decidability. It turns the alphabet's algebra into an exact census and separates periodic equicontinuity from mixing. The bound need not be the minimal exponent for each individual rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
