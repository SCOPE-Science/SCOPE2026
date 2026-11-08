# Review of sharp one-deletion outdegree of binary necklaces

## Correctness — PASS
The claim is unambiguous: count distinct rotation classes of length-one-shorter words reachable from a binary source necklace by exactly one symbol deletion. The proof establishes the general cyclic-run upper bound, separates alternating from nonalternating even sources, proves two independent collisions in the unique near-alternating odd case for all odd lengths at least nine, and constructs an infinite family in which all run deletions are distinct. The exceptional lengths are evaluated directly. All constructions and the universal upper bound were independently cross-checked by literal enumeration for all 4,807 necklaces up to length fifteen; construction witnesses were additionally checked to length 300. The argument is infinite; the code only checks finite cases.

## Originality — PASS, qualified
The closest mathematical starting point is the ordinary linear one-deletion ball formula in Sloane's survey, which counts ordinary (noncyclic) runs and maximizes at the alternating word; its output strings are not identified under rotation. Liron–Langberg give run-dependent extremizers for linear deletion subsequences, again without a circular quotient on both source and output. Burudgunte–Valiant–Wang treat probabilistic circular trace recovery with many possible deletions, rather than the cardinality of the exact-one-deletion support. Published research search comparisons around single-deletion graph enumeration and reconstruction identified no theorem implying the sharp \(n-2\)/\(n-3\) binary necklace maximum. In particular, an exact count of edges or triangles in a linear confusability graph does not imply the maximum outdegree of the necklace deletion graph. Relevant unindexed literature on the necklace subsequence poset remains a historical-priority risk.

## Mathematical value — PASS
The maximal number of possible one-symbol-deletion observations is the natural maximum outdegree in the single-deletion graph on binary necklaces, directly relevant to circular error and trace models. The result gives a complete, sharp answer at every length and detects a structural odd-length obstruction that does not appear for linear words. Neither correctness nor novelty alone establishes this motivation; it comes from determining a natural channel-support invariant without arbitrary restrictions on input words.

## Limitations
This is not a result about exact probabilities of random traces, multi-deletion supports, higher alphabet sizes, minimum outdegree, optimal error-correcting code cardinalities, or reversal-identification. Historical originality is qualified, and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
