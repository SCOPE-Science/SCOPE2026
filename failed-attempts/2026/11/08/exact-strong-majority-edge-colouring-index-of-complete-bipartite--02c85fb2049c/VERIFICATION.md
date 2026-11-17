---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The precise edge-neighbour cap is floor((m+n-2)/2), with the current colour subtracted twice in row-plus-column counts. A binary two-colouring forces r_i+s_j-2x_ij=(m+n-2)/2 and additive-minor rigidity; only two-vertex shores with even opposite shore allow balanced monochromatic stripes (K_2,2 has four named solutions). The i+j mod 3 construction and finite exceptions (3,4),(4,4),(4,5),(4,7) cover all m,n>=3; four displayed matrices checked independently. The supplied column-canonical search for K_3,4 and K_4,5 is sound because violation in an assigned prefix cannot be repaired by appended rows. An earlier complete analytic proof independently establishes both exceptional non-3-colourability statements. C PASS for m,n>=2, no general bipartite claim.

## originality

FAIL

The complete 2/3/4 index formula was published on 2026-10-12 and again 2026-10-25 for identical edge-neighbourhood semantics. The earlier October 12 proof already forces balanced whole columns in every two-colour optimum. Counting which n/2 labelled columns have colour 1 gives binom(n,n/2) (and four stripes at K_2,2) immediately; the submitted named two-colouring count is a routine coefficient, not an uncovered independent theorem. O FAIL based on full actual earlier theorem and its implication, not from absent search results.

## value

FAIL

The graph family and strong-majority edge-index problem are natural, but the whole classification was already completely proved. The only extra labelled-optimum statistic is a direct choice of n/2 columns after previously published stripe rigidity, not a nontrivial new structural enumeration. V FAIL for the final package despite correct code and explicit matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
