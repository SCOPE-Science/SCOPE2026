# Scientific review

## Correctness — PASS
The claim fixes the standard synchronous four-neighbour update on the triangular graph. For an absent root edge the number of active line-graph neighbours equals the sum of endpoint degrees. With four initial edges, a first activation forces all four edges to meet one of the endpoints of a missing edge; the complete star/double-star case split leaves exactly \(P_5\) and \(P_3\sqcup P_3\). Both fill the root complete graph in three or four parallel rounds, giving the exact size classification. Path and block counting proves the formula. Local edge-swap enumeration proves both reconfiguration degrees, and path reversals plus support changes prove connectivity. Separately implemented verifiers reproduce the classification and exchange counts. Risk: proof and tests use the stipulated simple-graph, fixed-four-neighbour convention; they do not assert other models.

## Originality — PASS, with priority risk
The 2014 full-text paper on minimal contagious sets in random regular graphs motivates optimization with time constraints but not this specific host graph. Bidgoli, Mohammadian and Tayfeh-Rezaie (2021) already explicitly determine \(m(L(K_n),r)\), so the numeric minimum \(m(L(K_n),4)=4\) is not presented as new. The proposed new result is the necessary-and-sufficient shape census, exact multiplicities and completion times, and connected nonregular replacement graph. Searches of mathematical-result records under degree-sum, percolation, optimizer shapes, and exchange aliases found no implication covering that joint claim. A pertinent same-object article's full text was inaccessible; its abstract only describes the minimum cardinality, not the complete optimizer/reconfiguration geometry, so priority uncertainty must remain explicit.

## Value — PASS
A naturally defined extremal problem on the line graph of a complete graph has a surprisingly small but nonunique optimal motif list and an exact all-order configuration count. The result contrasts two optimal root-forest shapes, identifies the only fast three-round exceptions, and proves that all optimal seed sets are mutually reachable by one-seed exchanges even while their exchange degrees differ. It supplies an exact structural and temporal benchmark, not a mere restatement of the known minimum.

Self-review: passed. Independent audit: not yet performed.
