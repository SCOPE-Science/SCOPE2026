---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

FAIL

The Finding attributes independent 2+Geom(1/2) complete-arch lengths to the finite uniform length-n word. Literally these are stopped by the observation horizon: for n=3, conditional on having a complete arch its length is 3 with probability one, not 1/2. The proof's intended interpretation is correct: in an infinite chain, an arch first sees two distinct symbols in two draws, then discovers the third with conditional probability 1/2 at each draw. The law at each boundary is independent of the boundary letter by symmetry, yielding iid durations on the infinite chain; I_n counts their partial sums at most n. Greedy arches characterize fixed-alphabet universality by the last-first-appearance obstruction, explaining why omitted symbols yield index zero. The binomial tail is the probability of at least k successes in n−2k fair trials. Using A(x)=x³/(2−x), the probability GF is (1−A)/[(1−x)(1−uA)], which gives F after converting prefix probabilities to counts. The renewal CLT gives variance rate 2/4³ and the LLN gives 1/4. Independent principal-part calculations for the mean and second factorial-moment GFs at t=1−x give 1/(4t²)−9/(16t) and 1/(8t³)−9/(16t²)+115/(128t); the other poles are at modulus sqrt(2). This confirms −5/16, 13/256 and both error terms. Thus the distribution and limit formulas are correct under the intended coupling; the as-stated law of finite completed arches is not. No supplied script was executed.

## originality

FAIL

A distinct indexed arbitrary-alphabet theorem explicitly gives the identical ternary enumerator, the infinite-prefix renewal structure and stronger LLN, and the same CLT. The binomial tail and second-order moments are not quoted there, but they follow directly from that theorem's geometric-duration model and exact generating function, respectively. The November 8 UTC record is dated later than the frozen October 27 UTC record; the overlap verifies existing coverage and does not establish an earlier discovery date or dependence.

## value

FAIL

The renewal structure for this natural constrained language is useful, but as a distinct narrow contribution it is covered by the exact all-alphabet theorem. The residual binomial rewriting and partial-fraction offset calculations are mechanical consequences and do not isolate a fresh worthwhile claim. Clarifying the finite-prefix wording would correct the statement but would not address that substantive issue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
