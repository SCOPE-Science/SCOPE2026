# Scientific review

## Correctness — PASS

The claim quantifies over all integers \(k\ge3\) and positive shore sizes \(a,b\). A star decomposition is equivalent to an orientation with each outdegree in the two-generator semigroup \(H_k\); repeated centers and one-size-only decompositions are allowed. The Euclidean quotient/remainder lemma proves the conductor \(k(k-1)\) and its preceding gap. In the hard case \(a,b\notin H_k\), the assumptions force \(a\ge k+2\), \(1\le q<r\), and an integer budget \(T=b(a-k)\) beyond the conductor. The exact inequalities \(0\le J\le L\le aq\) and \(d_i\le b\) ensure a realizable prescribed row sequence. Gale--Ryser applies because the opposite columns all have degree \(a-k\), and all its subset inequalities follow from the individual upper bounds and total. Every row outdegree is representable and every opposite outdegree is exactly \(k\). The obstruction uses the exact Frobenius gap, so no smaller uniform threshold works. The standalone checker performs independent exhaustive finite tests and direct construction tests; it does not substitute for the all-parameter proof.

## Originality — PASS (qualified historical priority)

Hajebi--Javadi, arXiv:2411.13348v1 (2024-11-20), defining mixed-length star decomposition through orientation and proving computational complexity of fixed multiplicities. Its complete accessible text, including the biclique hardness reduction and the expansion sufficient criterion, was examined. The present universal **unprescribed** two-consecutive-length threshold is a structurally different statement, not obtained by their hardness or fixed-multiplicity results. Harangi's 2025 orientation work addresses uniform-length decompositions in random regular graphs. The later Lee paper arXiv:2611.24973v1 (2026-11-17) was inspected as a direct adjacent comparison; its multipartite \(k=3\) bound and higher-\(k\) questions do not include this biclique all-\(k\) exact threshold. Single-length star design and path-plus-star literature also differ. Actual semantic-index searches yielded no same-statement or stronger biclique result. Priority is not a mathematical uniqueness certification: inaccessible early design articles and unindexed work remain residual risks.

## Value — PASS

The sharp threshold \(k^2-1\) holds simultaneously for all shore imbalances, including stars and near-Frobenius obstructions. It solves a natural extremal existence problem for a heterogeneous two-star palette, with a sharp infinite obstruction family and a constructive proof; the threshold is not an arbitrary finite computation or a routine substitution from the established complete-multipartite \(k=3\) result. The semigroup/degree-realization argument isolates why two successive allowed star sizes change the obstruction. It does not settle prescribed multiplicities or more-than-two-part multipartite graphs.

## Closest sources and limitations

The main comparisons are Hajebi--Javadi (arXiv:2411.13348v1), Harangi (arXiv:2506.05194v1), Lee (arXiv:2611.24973v1, contemporary supporting comparison), Shyu's path/star biclique designs (2013), and Cameron--Horsley's general multigraph criteria (arXiv:1807.10738). The result requires both shores nonempty, admits a choice of star multiplicities, and assumes no constraints on the centers. Its originality remains a best-knowledge judgement rather than an independent literature certification.

Self-review: passed. Independent audit: not yet performed.
