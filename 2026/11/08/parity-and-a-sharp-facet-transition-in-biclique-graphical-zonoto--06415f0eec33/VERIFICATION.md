---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

PASS

Re-audited the narrowed theorem in repairs/3/RESULT.md. With the intrinsic projected cut normal, containment at the known radius is equivalent to twice the absolute cut sum being at most d(S)-p sqrt(s(N-s)/(N-1)). The Laplacian-gap bound gives strictly positive slack at the origin for 2<=s<=N-2. The smaller-part singleton bounds are the box constraints; larger-part singletons force x_B=0. For a<p/2 the relevant uniform bound follows by squaring ap+(p-2a)b>=p sqrt(a+b): all coefficients are nonnegative except possibly when p=2a+1 and a>=2, where the quadratic discriminant is negative. The strict norm comparison for s>1 handles every nonsingleton or noncomplement cut in that range. Balanced cuts have constant boundary count and largest normal norm at the nearest integer to N/2. Comparison with the attainable middle sum (p/2)delta gives equality at p^2-1 and strict truncation starting at p^2; the squared threshold expression increases across the parity changes. Each oriented middle subset then has an equality witness strictly inside every other bound, giving exactly one new facet. Independent exact boundary replay at (p,q)=(4,11),(4,12),(6,29),(6,30) is included in the repaired result. The frozen verification notes are recorded finite tests, not formal/external evidence; uploaded code was not run.

## originality

PASS

The frozen priority framing fails insofar as it claims the complete all-center locus, radius, uniqueness in the square case or dimension as uncovered: the October 18 record already gives these, including an exact finite inequality description for all rectangular cases in scope. The replacement claims only a uniform strict redundancy theorem for the nonmiddle cuts and its sharp parity-dependent truncation and facet consequence. Prior cardinality-wise minimizations determine the polytope but do not give or mechanically prove that those bounds are uniformly redundant on the entire singleton box. The proof supplies that estimate before computing the middle-bound crossover. No earlier statement of that surviving theorem was found in the sources examined.

## value

PASS

The repaired theorem answers which inequalities actually matter in the earlier exact but unsimplified biclique description. Strict redundancy collapses all odd cases to a box section and explains the full even phase change, including how many facet orientations appear. This is usable geometric information not supplied by merely evaluating the known radius or listing all cut inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
