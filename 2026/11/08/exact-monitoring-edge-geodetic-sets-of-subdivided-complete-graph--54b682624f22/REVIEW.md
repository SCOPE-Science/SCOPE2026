# Scientific review

## Correctness — PASS

The domain is exactly the one-subdivision \(\Sigma_n\) of the labelled complete graph \(K_n\) for \(n\ge3\). The proof separates the four possible types of vertex pairs and explicitly classifies all geodesics. For every subdivided half-edge, every monitoring witness uses at least one endpoint, proving the previously unavailable necessity of vertex-cover membership. The converse is proved constructively and also follows from the published girth/minimum-degree theorem. The forced/optional subdivision vertices give the exact all-set and inclusion-minimal polynomials. The cardinality extreme follows from the exact difference \(f(k)-f(k+1)=k-1\). There are no unproved limiting steps. A standalone BFS-after-edge-deletion checker exhaustively verifies orders \(3,4,5\) and independently samples order \(6\). Finite checks are corroboration only.

## Originality — PASS (provisional publication priority)

The closest prior implication is Foucaud et al., *Bounds and extremal graphs for monitoring edge-geodetic sets in graphs* (arXiv:2403.09122), Theorem 6.3: every vertex cover is an MEG-set when minimum degree is at least two and girth at least five. This includes \(\Sigma_n\) and completely covers the **sufficiency** half. That theorem does not assert that an MEG-set must be a vertex cover. Its Theorem 7.2 gives quantitative bounds for subdivisions inserting at least two vertices per original edge; it does not provide this converse for one-subdivisions. The original Dev et al. paper (arXiv:2210.03774) defines monitoring and determines minimum sizes on other graph families; the inspected source does not supply this exact set-system equivalence or polynomials. The literature on products and later structured classes also does not directly cover the result. Relevant searchable research-record claims concern geodetic or strong-edge-geodetic sets of complete multipartite graphs, not monitoring sets of the incidence graph of a complete graph. The earlier result that original vertices form an MEG-set, the vertex-cover sufficiency, and elementary vertex-cover polynomial algebra are not treated as new. The remaining risk is an equivalent characterization under incidence-graph or subdivision terminology in unindexed literature.

## Value — PASS

Monitoring a network edge through distance-change probes is a motivated graph problem. The complete-graph incidence network is a natural, connected, sparse, minimum-degree-two family. Establishing equality of its monitoring family with its vertex-cover family is a sharp converse to a known general one-way theorem, not a mere restatement of the known optimal value. It yields every permissible probe deployment, all inclusion-minimal deployments, exact cardinality distributions, a unique optimum except at order three, and a quadratic largest-minimal size compared with the linear optimum. The unbounded gaps between possible inclusion-minimal sizes quantify a real structural diversity of irredundant deployments. The enumerators themselves are straightforward once the key equivalence is proved; that limitation is explicitly acknowledged.

## Scientific limitations

Full formal peer review and independent audit are not performed. Priority is provisional, not a claim that every possible source has been excluded. The verifier is finite and does not establish the result for all orders. The theorem does not extend by its present proof to arbitrary subdivisions of arbitrary graphs.

Self-review: passed. Independent audit: not yet performed.
