# Scientific review: covariance tomography for vertex-threshold random subgraphs

## Correctness — PASS

Independent uniform vertex labels create edge indicators with covariance determined by whether two host edges coincide, share exactly one endpoint, or are disjoint. Piecewise polynomial integration supplies the complete pair-moment parameters for every interior threshold. The unsigned incidence matrix gives the exact covariance polynomial in the signless Laplacian; spectral positivity supplies the inverse; a Sylvester integral establishes the operator-norm stability needed for the Hoeffding-based finite-sample decoder. Boundary thresholds and bipartite nullspaces are handled explicitly. The packaged rational checker passed 11,215 assertions, including all labelled graphs through five vertices, but the infinite statements rest on the analytic arguments.

## Originality — PASS, with historical-priority qualifications

The direct model source is Fox, Luo and Pham, *On random irregular subgraphs* (arXiv:2207.13651, first public date 2022-07-27). Its inspected results concern degree-bin frequencies and concentration, not the covariance of the numerical labelled degree vector. Alon and Wei (arXiv:2108.02685) prove one-vertex marginal uniformity, not joint covariance identifiability. McGregor and Sengupta (ICALP 2022, Article 96) reconstruct from random adjacency submatrices under a different sampling mechanism. Standard signless-Laplacian facts and degree-covariance reconstruction for independent bond percolation are not presented as new. The accessible full text of the 2002 originating article was not obtained; a broader latent-network moment identity could predate this calculation. The reported originality is qualified best-knowledge, not certification of worldwide priority.

## Value — PASS

Repeated degrees alone are coarser observations than the sampled edge sets, and the edge indicators are dependent. Recovering every unknown host on all interior thresholds via an exact invertible quadratic spectral transform addresses a motivated inverse problem; the explicit finite-sample algorithm and exact covariance-nullity interpretation make the calculation reusable. There is no assertion of optimal sample complexity, graph reconstruction from anonymous degree multisets, or novelty of its elementary constituent lemmas.

## Limitations and closest literature

The theorem needs known threshold, common vertex labels across independent observations, and independent resampling. The supplied sample bound is intentionally conservative and becomes weak near deterministic threshold endpoints. Relevant literature and material-read boundaries are recorded in `AUDIT.json`; the accessible full theorem and proof statements of the closest primary papers were compared. Independent audit and definitive historical-priority confirmation remain open.

Self-review: passed. Independent audit: not yet performed.
