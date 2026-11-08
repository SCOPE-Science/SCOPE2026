# Review of the clique-windmill minimal-alliance classification

## Correctness

**PASS.** The exact defensive inequalities are derived separately for a selected outer vertex and the central vertex. For a central-absent alliance, each occupied clique is itself an alliance and global minimality forces a single clique at the smallest feasible occupancy. For a central-present alliance, any clique occupancy above its peripheral threshold creates a proper defensive subset; all remaining nonzero occupancies are forced to the half-size threshold. The hub inequality, combined with the parity identity for the sum of the floors, permits such a set exactly when at most one petal has odd size. The reverse direction checks **all proper subsets** by whether they contain the hub. The two classes are disjoint, the binomial counts have no duplication, and all boundary sizes (including singleton petals) are covered.

An implementation independent of the structural proof directly checked the defining property and every proper nonempty subset in 495 ordered profiles (1,462,825 candidate vertex subsets). Its complete coefficient dictionaries agree with the formula. This is corroboration rather than an infinite proof.

## Originality

**PASS, with residual priority uncertainty.** The closest primary work is Feng–Fernau–Mann (arXiv:2312.11963), which establishes the importance and distinctions of global and local minimality and develops general enumeration procedures, but does not provide the exact formula for one-point unions of arbitrary cliques. Ibrahim (arXiv:1811.10089) develops a different two-variable connected-set surplus polynomial and characterizes friendship graphs using singleton coefficients; it does not classify globally minimal alliances. Gaikwad–Maity (arXiv:2202.02010) gives optimization and parameterized-complexity results, not an accessible exact enumerator for the claimed family. A complete comparison with that last paper could not be made because its full text was inaccessible; a source with equivalent unindexed coverage remains a risk. Related indexed results on strong defensive alliances of complete multipartite graphs concern a different graph family and a stricter alliance inequality, while friendship-graph dissociation and zero forcing polynomials concern different properties. The actual mathematical implications, not keyword overlap, were compared.

## Mathematical value

**PASS.** Counting *all* inclusion-minimal defensive alliances is a motivated enumeration problem because defensive alliances are not monotone and local and global minimality can differ. The answer covers an unrestricted list of unequal clique petals and isolates a parity obstruction at the hub that is invisible to the minimum defensive alliance number alone. Even the uniform triangular-petal case has exactly two possible globally minimal sizes, separated by an unbounded interval. The exact number of minimal configurations at each size is supplied, not just a minimum or maximum parameter. The result is meaningful as a complete finite-combinatorial classification, without claiming a general-graph algorithm.

## Closest literature and residual risks

The principal comparators are arXiv:2312.11963, arXiv:2202.02010, and arXiv:1811.10089. Full-text evidence was inspected where accessible; one relevant optimization paper was available only through its abstract and excerpts. The independent verification program covers a finite set of profile sizes, and the theorem's unrestricted scope relies on its proof. Priority is provisional pending broader human literature review.

Self-review: passed. Independent audit: not yet performed.
