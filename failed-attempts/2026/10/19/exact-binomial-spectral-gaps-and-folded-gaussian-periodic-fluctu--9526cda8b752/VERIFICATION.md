---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Off the all-left fixed face, inverse branches ((x−1)/2,y) and (y,(1−x)/2) contract both labels once the inverse word includes two right branches, so the square of any non-all-left word's inverse composition has a unique fixed point, also fixed by the composition. The closed branches do not introduce periodic switching points: if x_i denotes successive pre-right x values and ℓ_i the intervening left count, then x_(i−1)=1−(1+x_(i+1))/2^(ℓ_i+1), forcing all pre-right values below 1 and then strictly above 0. A left step from 0 would produce 1, also excluded. Thus the coded words count points, including smaller prime periods, not primitive orbits. At step j the doubled input label is 1 exactly for s_j=+1. At even parity the signed diagonal exponent difference is 1 plus n−1 free signs; the all-left word subtracts only the all-positive case. Odd parity gives anti-diagonal determinant 2^n and eigenvalues ±i 2^(n/2), hence equal moduli. The ordinary sign CLT, removal of one word, and the limiting parity weights give the stated folded mixture. Even n can have real-spectrum ties at finite n, and n=1 has no real-class conditioning; neither changes the limit. The supplied checker was inspected and not run; the all-n verification is analytic.

## originality

FAIL

The published catalogue contains a distinct theorem and proof that cover the claimed law, not just the parity marginal: the exact real absolute-gap multiplicities are explicit, the proof's stretch variable recovers the signed count by 2A−n on the real class, and the stronger joint gap limit projects to the claimed mixture. The catalogue date of this match is later than the frozen result's; this establishes equivalent coverage in the examined corpus, not earlier publication priority or derivation from that record.

## value

PASS

As a mathematical target, the gap distribution is more informative than counting real and nonreal spectra: it quantifies the separation between typical n^(-1/2) normalized fluctuations in the real class and order-one exceptional normalized gaps, and identifies the persistent atom from nonreal returns. This is a natural fluctuation invariant of a canonical example, although the reviewed record supplies no distinct result beyond the coverage above.

The dated certificate retains the supplied scientific assessment, sources and limitations.
