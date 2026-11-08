# Scientific review

## Correctness — PASS

The statement is restricted to symmetric aversion-to-enemies games with four specified core agents and two peripheral sets of cardinality \(q\ge2\). The negative valuation \(-n\) makes every coalition with an enemy pair non-IR; any eligible coalition must be a friendship clique. Merging separated portions of either compatible core and merging leftover peripheral-only coalitions strictly raises positive Nash welfare, yielding an exact two/three-coalition reduction. The product becomes \((a+1)^{a+2}(b+1)^{b+2}(r-1)^r\). Convexity of \(s\log(s-1)\) reduces the domain to five polygon vertices, with the mixed vertices dominated by the two-coalition product. The log-ratio of the remaining two products is strictly increasing for \(q>2\), and exact comparisons at \(q=8,9\) establish the threshold. Separate complete set-partition enumeration for \(q=2,3\), plus integer scanning through \(q=80\), agreed with the analytic prediction. The finite scans are explicitly supplementary and do not prove the infinite theorem.

## Originality — PASS, qualified

Pagano and Schlenga (2026), *Nash Welfare in Additively Separable Hedonic Games*, https://arxiv.org/html/2605.19030v1, define the same preference/utility normalization and prove that IR AEG coalitions are friendship cliques. Their Theorem 6.1 and its appendix derive the optimum among partitions with **at most two** coalitions, whereas their Theorem 6.2 gives general hardness for up to three or more coalitions. Neither statement or inspected proof supplies the unconstrained global optimum for the connected bipartite graph family, nor its switch at nine peripherals per side. The paper's known convexity argument for fixed two-coalition sizes is acknowledged rather than claimed new.

Available earlier special-family welfare classifications concern complete multipartite friendship graphs with within-class enemies and interclass friends, not the current deleted-biclique enemy structure; their conclusions do not imply the stated switch. Searches for equivalent formulations and broader coverage did not locate an equivalent classification. An unindexed clique-partition/Nash-welfare result could still anticipate the theorem; this is a residual publication-priority risk. A related 2026 paper on individual rationality with coalition constraints was inspected only at its abstract and cannot support whole-paper novelty exclusion.

## Mathematical value — PASS

The paper's algorithmic result for two-coalition AEGs leaves open what the **unrestricted** optimum does even on simple connected bipartite enemy graphs. The explicit, infinite, structurally motivated family shows a genuine phase transition: in a larger market a two-colouring is still feasible but strictly less Nash-efficient than introducing a third coalition. The theorem identifies the exact cutoff, global product, and all maximizing partitions with an analytic argument. This is a meaningful boundary to a natural extrapolation of a known restricted optimization theorem, without asserting any global smallest-graph claim.

## Limitations and closest literature

The result applies only to the specified four-core/two-peripheral signed complete model and a product objective on nonnegative IR utilities. No robustness, stability, incentive or arbitrary-graph algorithm claim is asserted. The closest inspected literature is the 2026 Pagano–Schlenga preprint, particularly Sections 2, 3, 6.1 and the appendix proof of Theorem 6.1. Open priority risks include unindexed graph-clique-partition work and older specialized social-welfare studies not inspected in full.

Self-review: passed. Independent audit: not yet performed.
