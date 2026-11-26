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

The diagonal idempotent entries split the scheme into open-and-closed color fibers. Over any commutative base algebra the products of the commuting idempotents and their complements give orthogonal joint projectors. Taking the x-column of the appropriate projector gives a unipotent simultaneous conjugator. The stabilizer has exactly same-color entries, because any differing bit gives coefficient +1 or −1. The product of the different-color affine section with the stabilizer has a polynomial inverse by recursion on strict intervals, proving the scheme isomorphism including over nonreduced rings. Expanding q+(1−q)[colors equal] over edges gives the FK transform; interpolation over infinitely many q and Q=2^r recovers the bivariate polynomial, whose q-degree is m. For connected graphs the standard Tutte conversion works, and the converse gives every dimension multiplicity. Rooting a tree gives the displayed binomial multiplicities. The two four-point trees have different undirected cover graphs; the semisimple quotient acting on the height-one radical bimodule recovers those graphs even up to opposite algebra. A connected height-one poset of smaller size is unique at each size up to duality.

## originality

FAIL

The core affine-fiber decomposition, FK counts and recovery of the Tutte polynomial are covered by a distinct earlier indexed result, d6c6054e5969. Its explicit polynomial forward and inverse maps apply over arbitrary commutative base algebras: the proof uses orthogonal projectors, coordinate projections and finite geometric-series inverses, so the all-ring wording is not a new theorem beyond that proof. The star/path example and the four-point cutoff follow directly from the covered invariant and the first two distinct trees on the same number of vertices. This is coverage, not an inference about historical priority from metadata alone.

## value

FAIL

The structural relationship is useful, but the frozen finding does not add a substantive advance over the earlier explicit affine and FK result. In particular the illustrative four-point cutoff is a routine consequence of equal tree Tutte polynomials and the classification of smaller height-one connected posets. It does not warrant a separate repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
