---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Greedily alternating against the sign of each nonzero partial sum keeps the initial and nonfinal sums in [1−m,M]; minimality makes them distinct, bounding length by m+M. For span at most d every mixed-sign term lies between 1−d and d−1. Comparing the length to χ on its own support is a necessary test for strictness on any containing support. The subset-sum test on all but the last term is exact, since a proper zero-sum subset containing that term has a nonempty zero-sum complement. The fresh bounded run gives candidate counts 1,3,9,25,79,245,809,2703 and only the two sign-related strict sequences at nine. The five listed atoms on X*=(-6,-1,2,3) are reproduced. A containing support of diameter nine lies within [-6,3]. Adjoining −5,−4,−3,−2,1 produces respectively an opposite-sign pair of primitive length 7,7,5,5,7 (pair with 2,3,2,3,−6, respectively), so none can preserve strictness for the only candidate witness, of length five. Zero only adds its singleton atom. This confirms the mathematical theorem, including the exact rigidity statement.

## originality

FAIL

The complete mathematical finding is a routine projection of Matthias Köppe's public precomputed primitive-partition-identity table ppi17.dat. Inspection of the actual binary rows, not just the table description, recovers the only strict atom up to sign at span at most nine and exactly the five claimed nonzero atoms on X*. The supporting restrictions on additional points and zero are immediate pair checks. The exact cutoff need not have been printed in Davenport terminology for this prior table to cover it. This is demonstrated coverage, not a failure to establish priority because a paper was unavailable.

## value

FAIL

Comparing the primitive two-value bound with arbitrary integer atoms is mathematically motivated, and a first-gap classification could be valuable in the absence of coverage. Here the cutoff, witness, rigidity and small atom list require only a mechanical projection of a prior complete table and elementary extra-point checks. The fresh enumeration is useful corroboration, not a distinct substantive invariant or structural explanation. No surviving valuable new claim was identified for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
