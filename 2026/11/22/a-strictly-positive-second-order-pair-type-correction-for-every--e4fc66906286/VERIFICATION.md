---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Every admissible finite ordered two-new-point diagram is realized over the base by the free-amalgamation Fraïssé limit and determines a complete type by homogeneity. The four-sets with one new point yield exactly the two decreasing link predicates; a four-set with both new points excludes state (1,1) on an old pair in S. Counting the empty-core possibilities yields independent allowed pair states given S and weight proportional to (3/4)^(choose(|S|,2)). At one restricted coordinate the change from four states to three is ((u0-u1)(v0+v1)+2u1(v0-v1))/12 for decreasing nonnegative u,v, so replacing coordinates in sequence proves the exact finite lower bound. If abc is an old edge, take S={a,b}, set X_ac=X_bc=1 and the other non-ab link bits to zero, and take the second link's other bits all zero. This gives a positive-probability strict witness. With no edges equality holds for every n, including n=0,1 where applicable. On a two-vertex core intersection the gain is (a_p^2+2a_pb_p)/3-((a_p+b_p)/2)^2, the stated d_p. Changing the event that p is included to the event that p is the exact intersection loses at most (k-2)pi_3 and all intersections of size at least three have probability at most choose(k,3)pi_3. Adjacent weights have ratio (n-s)(3/4)^s/(s+1); the mode inequalities give first m=O(log n), then m=(log n-log log n+O(1))/log(4/3). The ratios fall by a factor at most 3/4, giving both tails at distance j bounded by (3/4)^(j(j-1)/2), hence the claimed factorial moments and remainder for fixed H. For two old edges sharing ab, conditional probabilities are (1,9/16) on ab, (7/8,11/16) on each of four side pairs and equal on the unused pair. This gives f_H=25/32 and D_H=865/3072; one edge gives D_H=13/64. In a fresh finite check at n=4, exhaustive assignments to all triples containing one or both new vertices, rejecting any complete four-set, gave counts 46553, 37011, 30378, 25275 for old cores with 0, 1, 2, 3 edges respectively. The bundled verifier, protocol and output were read, not executed. The expansion is not an exact two-term finite identity.

## originality

PASS

Distinct contribution: the strict finite comparison and explicit second-order invariant for arbitrary fixed cores, in particular overlapping triples. The closest distinct same-date result covers the leading coefficient on disjoint-triple cores and obtains growing-core uniformity there. Credit that coverage without inferring priority from the shared date. No novelty is credited for the matching-core specialization, scalar normalizer, or one-point count.

## value

PASS

This quantifies a genuine interaction between the two added vertices: forbidding a shared link state counters the independent single-vertex obstruction by a strictly positive gain, with a local influence formula that works for overlapping old clauses. The exact finite sign and leading computable coefficient distinguish arbitrary cores using their link predicates; they are not just a new estimate for the old normalization or one checked small core.

The dated certificate retains the supplied scientific assessment, sources and limitations.
