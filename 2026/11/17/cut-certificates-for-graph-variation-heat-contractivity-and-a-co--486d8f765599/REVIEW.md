# Scientific review

## Correctness — PASS

The linear heat operator preserves constants and its sharp graph-total-variation norm reduces by the discrete coarea decomposition to indicator cuts. First differentiation gives an integer cut statistic: the squared crossing-degree term is cancelled against the absolute differences across uncut edges. The derivative of a finite maximum and the semigroup-product argument prove that nonpositive slopes at time zero are equivalent to contraction for every later time. The bridge cut formula is derived exactly; its degree-sum obstruction excludes every long off-cycle attachment and multiple leaves at one cycle vertex. Explicit cycle-arc cuts exclude all remaining long-cycle and over-leafed-pentagon cases. The 40 residual cases are completely enumerated by a standalone integer checker with 3,064 cuts and an independent derivative calculation, not extrapolated from samples. For the indicated seven-vertex graph, direct Laplacian arithmetic yields positive Lipschitz slope despite nonpositive total-variation slopes.

Critical proof limitations: the general graph cut test is finite but exponential, the full time-dependent operator norms are not calculated, and no weighted/normalized graphs are claimed. The finite certificate proves only its bounded cases; the unrestricted steps have their own mathematical proofs.

## Originality — PASS (qualified)

A fresh comparison was made against semigroup curvature, graph coarea and total-variation flow literature and against accessible mathematical-record searches and historical claim headings. The closest graph-gradient result is Münch–Wojciechowski's equivalence between Ollivier curvature and edge-\(\ell^\infty\) Lipschitz heat contraction, not the cutwise edge-\(\ell^1\) variation test here. An explicit seven-vertex positive-Lipschitz-slope example within the present variation-contractive class prevents that result from implying the new classification. Münch's paper on “total variation of the heat semigroup” means total-variation **distance of measures**, not variation across graph edges. The nonlinear total-variation gradient flow in Giga–van Gennip–Okamoto is governed by a different generator. Previously accessible heat edge-variation work on complete bipartite graphs does not cover general cut geometry or the unicyclic graph class. No stronger equivalent or existing exact unicyclic table was found in inspected material; this is a best-evidence priority assessment, not a proof of historical uniqueness.

Residual risk: an equivalent general semigroup-dissipativity characterization or an implicit treatment of unicyclic edge-\(\ell^1\) contractions could exist in older Banach lattice/graph diffusion studies.

## Mathematical value — PASS

Edgewise total variation is a standard stability functional for graph signals, yet conventional heat-flow estimates typically concern Euclidean, probability-mass, or Lipschitz norms. The cut criterion transforms an all-time analytic contractivity question into finite, exact combinatorial inequalities for arbitrary finite graphs. The unicyclic classification has a genuine cycle-length threshold: no attachments survive beyond a pentagon, even though every bare cycle is stable. A seven-vertex example also demonstrates why a superficially similar known curvature condition cannot replace the new one. These constitute a natural complete structural classification and an obstruction mechanism that extend beyond finite sample enumeration.

## Closest sources and limits

Bauer et al., *Li-Yau inequality on graphs* (arXiv:1306.2561, §§1 and 4); Münch–Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians* (arXiv:1712.00875, Theorem 3.8); Münch, *Non-negative Ollivier curvature on graphs* (arXiv:1907.13514, Theorem 3.1.1); Giga–van Gennip–Okamoto, *Graph gradient flows: From discrete to continuum* (Hokkaido preprint 2022, §4); van Gennip–Budd, *A Prolegomenon to Differential Equations and Variational Methods on Graphs* (2025, §3.2). All involve distinct or broader conceptual settings but none of the inspected statements gives the claimed exact graph-cut certificate and unicyclic classification. Lack of a matching statement is not an exhaustive publication-priority guarantee.

Self-review: passed. Independent audit: not yet performed.
