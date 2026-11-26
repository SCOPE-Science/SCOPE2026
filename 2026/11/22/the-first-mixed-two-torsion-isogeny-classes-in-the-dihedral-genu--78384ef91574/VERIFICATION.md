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

For odd q≡1 mod 4 the excluded s are exactly the repeated-root cases in the sextic. The fixed quadratic splits; the quartic is either fully split or two irreducible quadratics. If s²−4 is square the reciprocal quadratic roots have the same square class; if nonsquare, exactly one of 2−s and −2−s is a square, giving the two quadratic factors with no linear root. Every nonzero geometric Jacobian 2-torsion class has a unique two-element branch-set representative; Frobenius fixes 15 such pairs in the split case and 3 in cycle type 1²2². The full split s are parametrized by free inversion orbits of the nonzero squares other than ±1, giving (q−5)/4, with twist unchanged. Independently counted exact fibers including infinity over F_p and F_{p²} for every admissible s and both classes at p=5,13, and reconstructed the reciprocal genus-two Weil numerators via the first two counts (no reliance on N1 alone). The two displayed F13 witnesses each have (N1,N2)=(18,214), yielding (1+2T+13T²)², and quartic root counts 0 and 4, yielding 4 and 16 for rational Jac[2]. The full unit-class table, twist sign, seven marked bins and two mixed bins agree. There is no full split at the only earlier allowed prime 5. The cited square-Jacobian structure is also consistent with the two conjugate elliptic quotients and their complementary differential spaces. The finite-field isogeny theorem yields base-field isogeny, while different rational 2-torsion orders rule out base-field isomorphism. Recipe and outputs: /workspace/branches/independent-math.md, section 1.

## originality

PASS

Arul et al. already give the model, the elliptic-square decomposition and an aggregate F13 count that includes the standard-action versions of the witness pair. Their P(13) counts pairs of isomorphism classes with specified dihedral action, not coefficient-marked equations and not completely unmarked curves; the frozen prior-work paragraph's use of 'unmarked' should be read only as a contrast with its coefficient marking. The supported distinction is the explicit mixed rational Jac[2] witness and minimum within the stated prime regime, together with the marked stratification by Weil type and torsion. The inspected prior tables and supplements give neither that refinement nor the specific mixed witness. The uniform splitting formula is supporting structure, not claimed as a new dihedral classification.

## value

PASS

The first explicit mixed class in this natural family is a concrete demonstration that coincident zeta functions over every extension do not force identical rational Jacobian two-torsion, even among these elliptic-square isogeny classes. The exact witness and marked bin breakdown refine, rather than recompute, the published pair count and identify where the distinction can be observed. The scope is a threshold for the specified prime fields and model family, not a threshold for all genus-two curves or for double isogeny.

The dated certificate retains the supplied scientific assessment, sources and limitations.
