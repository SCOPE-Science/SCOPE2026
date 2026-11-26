# Independent mathematical audit

## correctness

PASS

The original mathematics is correct, including the removed exchange claim. A fresh implementation (not either uploaded verifier) checked all 65,536 placements and independently ran BFS from all 320 minimum triples. It reproduced failed counts 1,16,120,240,60 and none above size four, exact equality of failures with subsets of induced 2K2s, unique extension for every failed triple, and at most one wave after initial observation for every success. It also reproduced degree 21, 3360 edges and shells (1,21,126,172) at all 320 roots for the original graph. Replay: /workspace/branches/42a07edb-32ce-4794-99f4-9daa907203a4/reproduce_record2.py and its reproduction_subsets.json and reproduction_exchange.json. For the repaired claim I independently checked the written proof: wave monotonicity follows because a forcer remains observed and an unobserved target remains unique in the larger observed state. The three triple orbits use a translated vertex of the appropriate type; the XOR representatives have the listed initial unseen sets and wave behavior. For an edge represented by ∅,{i}, the six nonneighbors of both endpoints induce three pairs of complementary two-subsets of the other four coordinates. This supplies the unique completion and the count 40·3/2. For the failed representative {0,1,6}, adding its partner 7 leaves the observed set unchanged, so the completed set is stalled. Every pair extends to a failed triple; a four-set with one edge in every triple is a matching by counting twice per edge, and such a five-set would require 3e=10. The complete failure classification and polynomial follow, without an exchange enumeration. Repaired RESULT.md, SLOGAN.txt and scientific body of VERIFICATION.md were checked for consistency; the verification-status front matter is unchanged.

## originality

PASS

Originality of the combined original claim FAILS the distinct-claim requirement: an independently indexed same-day result gives the same minimum-triple classification and exact token-jump graph, including all claimed distance layers. This is demonstrable overlap, not a finding that either record has chronological priority or that the frozen theorem is false. The repaired finding removes the entire reconfiguration claim and credits the three-set input. PASS applies only to the surviving new content: the exact maximal failed family, unique failed-triple extension, and all-placement classification and polynomial. A narrowed search and statement-level comparison support that distinct content, with the risks below.

## value

PASS

The repaired finding is an exact structural classification on a canonical strongly regular graph, not a recomputation of minimum size or jump distances. It identifies all maximal ways to fail, gives a unique completion rule for each failing triple and specifies the success enumerator at every sensor budget. Those are distinct useful finite facts for reasoning about robustness of placements. The proof explains why the induced matchings stall, beyond simply listing the configurations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
