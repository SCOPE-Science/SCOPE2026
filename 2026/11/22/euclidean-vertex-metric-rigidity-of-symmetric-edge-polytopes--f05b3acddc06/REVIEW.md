# Scientific review

## Correctness — PASS

Every signed edge-incidence root is an extreme point since all distinct roots lie on the same Euclidean sphere. The squared-distance identity \(\|r-s\|^2=4-2\langle r,s\rangle\) gives the exact shells \(2,4,6,8\). Opposites are unique at \(8\), incident edges give cross-shells \(\{2,6\}\), disjoint edges give \(\{4\}\). Whitney's classical line-graph theorem leaves one exceptional connected pair, and the intrinsic rank of its associated six-point configurations is exactly \(2\) versus \(3\). Each converse and the universal error bound follows without extrapolating from a finite check. The standard-library checker covered \(1694\) graph masks and the triangle/claw exception; a separate graph-atlas calculation covered \(1245\) cases. The proof holds for arbitrary finite simple graphs with edges and deletes invisible isolates explicitly.

## Originality — PASS, historical priority provisional

The nearest direct result is D'Alì, Juhnke-Kubitzke and Koch (arXiv:2307.04933v1), Theorem 4.6: **unimodular equivalence** is equivalent to isomorphism of graphic matroids, and graph isomorphism is characterized only under three-connectivity in their Corollary 4.7. The same paper exhibits a nonisomorphic two-connected pair with unimodularly equivalent polytopes, so those results do not imply canonical Euclidean congruence for all graphs. D'Alì, Delucchi and Michałek (arXiv:1910.05193) develop combinatorial and metric-space connections; the inspected definitions and results do not state full Euclidean vertex-metric inversion. Winter's polytope edge-graph rigidity (arXiv:2302.14194) assumes different reconstruction input, and Rembado's type-A root-subsystem classification (arXiv:2206.03779) has a closure hypothesis absent here. Whitney's line-graph theorem is acknowledged rather than presented as original. Targeted published-record and literature searches revealed related but not statement-covering records. Residual risk: a different terminology or unindexed source could contain this inverse observation.

## Mathematical value — PASS

The theorem completely classifies intrinsic Euclidean congruence for the canonical symmetric edge polytopes of **all** finite simple graphs, thereby separating Euclidean geometry from the much coarser matroidal/unimodular equivalence class. It supplies an explicit coordinate-free inverse and a dimension-independent deterministic noise guarantee. Even all trees of fixed size have equivalent matroidal/combinatorial polytopes but, by this theorem, nonisomorphic trees have different Euclidean vertex metrics. These are structural consequences for a natural and actively studied polytope construction, not a finite table or arbitrary parameter slice. The proof's reliance on the classical Whitney theorem and the simple shell identity is acknowledged; this is a concise reconstruction theorem, not a claim of a new line-graph theorem.

## Source comparison and limits

Relevant primary results inspected: arXiv:2307.04933v1 (full article, especially pages 1, 10--13 and Theorem 4.6); *Many faces of symmetric edge polytopes* (definitions, Sections 2 and 4, targeted reconstruction and equivalence terms); arXiv:2302.14194 (abstract, Sections 1 and 4 topic); arXiv:2206.03779 (introduction and type-A/root-subsystem setup). Unindexed mathematical priority and potential alternative nomenclature remain possible. The result requires full Euclidean squared-distance tables for the unweighted canonical realization; it does not reconstruct isolated vertices or extend to arbitrary affine re-embeddings.

Self-review: passed. Independent audit: not yet performed.
