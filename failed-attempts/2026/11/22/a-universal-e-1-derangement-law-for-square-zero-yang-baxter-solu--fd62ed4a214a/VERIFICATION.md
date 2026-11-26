---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Substitution with a²=0 gives the inverse and the stated braid triple. The preservation identity first factors af through a, then forces the resulting map on W to be additive and injective by translation equivariance. On each W-coset the lift is affine with that same linear part and an arbitrary translation; βτ=φβ gives equal-sized fibers and the split action (on translation functions, b maps to φ∘b∘τ⁻¹). For a uniform lift over φ only the u fixed outer fibers matter. In each, a fixed inner coset contributes u points precisely when its independent translation lies in im(I−φ), an event of probability 1/u. The falling-factorial moments of the number of fixed symbols of S_s are one through order s, giving the exact conditional PGF. For fixed p,r, compact convergence of the PGFs gives convergence of finite coefficients, and the unit mean gives tightness and then total variation; averaging pushes forward to the stated mixture. At zero, the truncated exponential remainder is at most u⁻ˢ⁻¹/(s+1)!, and taking the u-th power costs at most u, yielding the stated uniform error including s=1. Arbitrary translations/inner permutations and the two GL orbits on W give exactly the two automorphism orbits. The supplied checker was inspected, not run; the decision rests on these exact arguments.

## originality

FAIL

The construction and full permutation action are a direct instance of the published 2-reductive isomorphism theorem, not merely a resemblance of abstract groups. After inserting its orbit groups and constants, the exact PGF is the usual fixed-point substitution for independent inner permutations applied to the affine coset with linear part φ. Its input PGF for the normalized affine-coset count is 1+(t−1)/u. This derives the claimed finite law directly from the published action and elementary permutation moments, including the normalization, not just a qualitative Poisson analogy. The finite remainder and limit then follow by the ordinary exponential series. This is a mechanical consequence, not a claim that an older paper printed the displayed formula verbatim.

## value

FAIL

Fixed-point counts in this natural action are legitimate objects, and the formula makes a useful worked example. As an asserted independent finding, however, the exact formula and its error are mechanical consequences of the already-classified action, fixed-subset counting in S_s and the exponential remainder. No distinct structural or probabilistic ingredient remains beyond this calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
