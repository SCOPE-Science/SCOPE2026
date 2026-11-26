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

The convolution is diagonalized by the group characters. For a nonzero character, cyclotomic irreducibility makes the multiplier zero exactly when the five affine fiber populations agree; the nontrivial frequencies vanish in packets of four. The constant frequency is nonzero except for the empty mask. For weight 5h, a pencil is balanced exactly when its within-fiber unordered collision count is the minimum 5 binom(h,2): transferring a point from a fiber at least two larger than another strictly decreases the collision count. I independently enumerated all 53,130 weight-five and 3,268,760 weight-ten supports by combinations, counting equal projections of point pairs rather than line populations. The histograms in order k=0,…,6 are (36000,15600,1500,0,0,30,0) and (2697000,545700,24000,2000,0,60,0). Complementation and the cyclotomic criterion handle all other weights; the global totals exactly match the frozen record. In the submitted proof, sharp three-transitivity implies transitivity on every set of directions by complementation, the 2-regular bipartite count splits into 10-cycles and disjoint 6- and 4-cycles, and binomial inversion gives the stated counts. The numerical check corroborates those identities, not their novelty.

## originality

FAIL

The complete table, not just its missing rank nine, follows mechanically from the published special-direction classification plus two elementary moments. Let F_k be the number of weight-w masks with k balanced pencils. The relation rank=25−4k identifies Kiss–Somlai special directions with the 6−k unbalanced pencils. Their §2 gives F_4=0 and F_5=6 binom(5,w/5). For a proper nonempty mask F_6=0 by Fourier inversion. Their Theorem 4.1 gives F_3=0 at weight five and one affine orbit at weight ten, with representative S={(a,b): b<a}. In affine coordinates u=b, v=4−a, t=a−b−1, this triangle is the triples of nonnegative representatives summing to 3, on u+v+t=3 over F5. The three coordinate pencils are exactly its special directions, with distinct fiber counts 4,3,2,1,0. Any stabilizer permutes these pencils; one fixing each must fix every line in each and hence is the identity. All six coordinate permutations are affine and preserve S, so the orbit size is 12000/6=2000. The known exceptional classes therefore determine all other entries: F_2=15N_2−3F_3−10F_5, F_1=6N_1−2F_2−3F_3−5F_5, F_0=binom(25,w)−F_1−F_2−F_3−F_5. Here N_1=binom(5,w/5)^5; N_2 is 5!=120 for w=5, and 5!4!/2+binom(5,2)^2·6=2040 for w=10 by the two cycle decompositions of a 2-regular bipartite graph. This yields every displayed entry, including the large rank-17, rank-21 and full-rank populations, without the submitted three-pencil enumeration. It also gives the two triple intersection counts from 20N_3=F_3+10F_5. Complementation and the basic cyclotomic criterion finish all weights. The exact table need not have appeared verbatim to be covered at this standard.

## value

FAIL

The rank-by-weight statistic is natural, and the manuscript is a useful exact reproduction. But under the value standard for a narrow invariant, it must supply a distinct fact beyond a routine consequence of existing work. Here the rare cells are forced by known structural theorems and the remainder by elementary one-/two-pencil counts. The triple-pencil enumeration merely recovers an already forced finite specialization. No separate valuable new claim is asserted that can be retained by narrowing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
