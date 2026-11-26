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

Restricting the EPPF to the named labels, adjacent all-one pairs require one triple block; disjoint all-one pairs allow one block of four or the specified two doubletons. Their difference is (1-alpha)(theta+alpha)/[(theta+1)(theta+2)(theta+3)] > 0, also for admissible negative theta. Thus all edge pairs must have the same incidence type. A pairwise-intersecting simple edge family is a star or triangle (an edge avoiding the common end of two incident edges must complete their triangle, after which no fourth edge is possible). A disjoint family is a matching, including the single-edge case. Vertex relabelings realize every edge permutation in all three cases. The sampling-consistent infinite partition on a countable star or matching gives the first two infinite extensions. In a triangle the masses are A at 111, B at each singleton-one word, C at 000, and zero at every two-one word. A uniform k-subset of N gives positive mass to a fixed two-one word exactly when 2 <= k <= N-1, forcing total one count in {0,1,N}. The weights at these three counts are uniquely C-(N-3)B, NB, A; these reproduce all eight words, and the first weight is nonnegative exactly when N <= 3+C/B = (theta+3-alpha)/(1-alpha). This includes equality, N=3, and excludes infinite extension by restriction. The proof holds for all stated real parameters; check.py is a finite corroboration of probabilities, extension weights and small graph shapes, inspected but not executed.

## originality

PASS

The partition law, generic exchangeability and extension machinery, and star/triangle incidence characterization are inputs. The inspected sources do not already resolve the combined graph classification and evaluated sharp finite horizon with uniqueness for this family. The closest catalogue results have substantial overlap in observables or extension question but do not establish the same fact.

## value

PASS

This determines when graph-indexed partition observations may be treated as exchangeable Bernoulli coordinates and shows that an infinitely exchangeable vertex partition can give an edge vector with only finite extendibility. The cutoff and unique marginal-compatible extension laws identify exactly how many exchangeable copies a triangular observation permits, including the sharp integer boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
