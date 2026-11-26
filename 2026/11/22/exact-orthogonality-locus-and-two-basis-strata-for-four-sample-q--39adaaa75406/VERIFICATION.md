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

For samples 0 through 3 the entries are (1,r,rt,t^3); r and t are recovered from entries 1 and 2 (with entry 0 equal to 1). The phase map is onto, with kernel {(0,0),(π,π)}. Factoring the coherence as (1+t)(r+t²−t+1) proves that t=−1 gives an entire circle; otherwise the unit-modulus condition is |2 cos(arg t)−1|=1, giving precisely the three listed quotient points. The equation α+3β=π mod 2π parametrizes a single circle by β; each isolated quotient point has two lifts. For any orthogonal set, its second coordinates lie in one rotated fourth-root set. A repeated second coordinate forces opposite first coordinates and excludes both adjacent fourth-root values: an adjacent value would require the same ratio r/t to each member of the repeated class. Four points therefore consist of two antipodal second-coordinate values, each with two opposite first coordinates, yielding A(z). With no repeats, all four fourth-root values occur, and all adjacent pairs force r/t to be constant, yielding B. These conditions also suffice by the ratio test. Translation preserves the multiplicities that distinguish the two types, and column length is 2. Verified for the unrestricted phase torus only. The source checker was inspected, not executed; its reported grid figures can be recovered independently as a 16-vertex degree-7 Cayley graph (56 edges) and two A choices plus one B choice through the identity (8 and 4 cliques, respectively, by double counting).

## originality

PASS

The supported distinct contribution is the full continuous zero locus and exhaustive inverse-image classification under chirp-preserving equivalences. The isolated Fourier example and the abstract order-four Hadamard family are established objects, not new configurations in the ambient Hadamard classification. An exact same-day overlap on the ordinary-character case is credited without assigning priority from the date.

## value

PASS

Four consecutive samples are the first size where, after fixing the initial entry to one, the quadratic chirp imposes a constraint on the remaining phase entries: two noninitial entries already determine both torus coordinates. At this cutoff the result gives exact exceptional coherence differences and all orthogonal bases under the natural phase equivalence, including a rigorous obstruction to using three distinct combined phases. This is useful as a complete finite benchmark, not a claim about physically feasible arrays or a new abstract Hadamard family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
