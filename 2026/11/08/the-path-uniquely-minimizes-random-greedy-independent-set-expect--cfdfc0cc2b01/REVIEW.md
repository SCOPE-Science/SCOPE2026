# Scientific review

## Correctness (C): PASS

The proof states the finite-tree uniform-priority process, the path expectation \(\alpha_k\), the shattering functional \(\nu\), and the correct definition of proper KC moves. Its novel step is strictness of the alternating mixed difference \(F_j\): the explicit second-difference kernel is positive, strictly decreasing and strictly convex in its index; the associated first decrement is also strictly convex. A two-dimensional checkerboard partition and an alternating-series pairing prove strictness for bare paths of at least two edges. For adjacent KC endpoints, a neighbor on one side witnesses a strict gain through the inequality \(1+\alpha_b>\alpha_{b+1}\). The published off-path comparison and path decomposition then establish strict \(\nu\)-monotonicity. The known proper-KC tree poset and exact first-vertex recursion imply unique minimization. All 30,741 packaged finite exact-arithmetic checks passed; these test but do not replace the all-order proof.

## Originality (O): PASS, with residual priority risk

Krivelevich, Mészáros, Michaeli and Shikhelman [1] prove only \(m(P_n)\le m(T)\) and explicitly state that their proof does not establish uniqueness; their Theorem 8.3 only gives \(\nu(T')\ge\nu(T)\). The new strict checkerboard argument and separate length-one splitting case together prove \(\nu(T')>\nu(T)\), leading to the equality classification. The 2020 version [3] gives the older non-strict minimum. Other graph-family random-greedy output-law results are not stronger theorems on this tree extremality problem. A known example of a proper KC move reducing the greedy expectation does not contradict the result, which does not assert monotonicity of \(m\). There remains a risk that an unindexed paper proves the same equality characterization by another method.

## Value (V): PASS

Uniqueness is an expressly identified missing step in the main tree-extremality theorem for random greedy maximal independent sets. Establishing strictness of the auxiliary tree-shattering functional gives a structural equality case for every finite order, not a numerical improvement or arbitrary finite slice. It also identifies why direct expectation monotonicity is unnecessary and demonstrates an explicit, all-parameter strictness mechanism for KC transformations.

## Scientific limits

The proof is conditional on the established first-vertex formula, \(\alpha\)-subadditivity, KC decomposition and KC-poset reachability from [1, 2]; the new strictness argument and its boundary case are written out here. No quantitative stability constant, nonuniform-priority extension, or new result for general graphs is claimed. Historical-priority review is best-knowledge rather than exhaustive bibliographic certification.

Self-review: passed. Independent audit: not yet performed.
