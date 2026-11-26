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

In degree less than two every nonconstant representative is linear and irreducible, so the subgroup criterion is exactly trivial intersection with the scalars. In the irreducible case cyclic intersection has order gcd(d,q−1), giving precisely the eligible divisors of q+1. In split coordinates (u,v/u), an eligible subgroup projects injectively onto a cyclic group of order d dividing q−1; its graphs are in bijection with the d possible images of a generator under the homomorphism to F_q^×. In dual-number coordinates the same projection argument gives a graph over a p-subgroup, with trivial scalar component by coprimality; the number of dimension-j subspaces is the asserted Gaussian binomial. The modulus counts are q(q−1)/2 of each distinct-root type and q repeated-root moduli. For odd q the admissible irreducible-case order is odd and at most (q+1)/2, and the split order is at most q−1; for even q, q+1 is admissible and exceeds both other bounds. This proves the two maxima and equality multiplicities, including q=2. The independent replay `python3 /workspace/branches/6cf518ec-dc68-4638-90a8-23187f126c47/quadratic_slice.py` directly enumerated units and all subgroups of the 13 monic quadratic quotients over F_2 and F_3 and obtained aggregate profiles {1:4,2:2,3:1} and {1:9,2:6,3:3}. This checks only the two prime fields; the arbitrary-field conclusion follows from the proof, not either finite checker. The packaged 109-case result is author-reported, not this replay or a formal certificate.

## originality

PASS

The checked prior work supplies the polynomial convention, question and the F_2 whole-group cases, not the proper-subgroup profiles, arbitrary-field counts or parity-dependent extremal classification. Credit that overlap and the standard group-theoretic ingredients, not priority beyond the checked material.

## value

PASS

This closes the natural first degree of the proposed polynomial analogue at subgroup level. It distinguishes embedded subgroups from whole-group eligibility and gives three genuinely different behaviors, including elementary-abelian subgroups in the nonreduced case and a characteristic switch in the maximizing modulus. The full counts and exact extremizers are usable as a quadratic baseline beyond isolated examples, although the proof uses elementary algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
