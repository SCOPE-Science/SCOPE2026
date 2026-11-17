# Review of the metric-extremal theorem for Marion central polytopes

## Correctness — PASS
The theorem uses the literal ratio-two inequality system \(x_i\le2x_j\) from Kazakov's regular-simplex barycentric construction [1], with intrinsic Euclidean distances measured in the coordinate-sum-one hyperplane. The exhaustive vertex determination is reconstructed from its active constraints. Pair distances reduce to three integer parameters (two set sizes and their intersection), and the intersection coefficient is strictly negative. Strict one-coordinate exchanges rule out all noncomplementary size pairs; the remaining one-variable expression has a unique maximum at the two balanced cardinalities. Strict convexity rules out nonvertex diameter endpoints. Permutation symmetry and uniqueness of the minimum enclosing ball force the centroid, and the exact radial function has a unique maximizing cardinality after checking the two possible nearest integers. Every claimed multiplicity follows from these equality descriptions. The accompanying standard-library checker reproduced 1,756,025 exact assertions, but the proof rather than finite checks supplies all-dimensional validity.

## Originality — PASS (historical priority provisional)
The central polytope, inequalities, volume fraction, and \(2^N-2\) two-level vertex construction are published in Kazakov [1] and are **not** claimed as new. Full mathematical sections and the tetrahedron appendix of that source were inspected. Its metric discussion is limited to face side lengths and face-plane distances in the tetrahedral example; it does not state an exact all-dimensional Euclidean diameter with every maximizer, or the minimum enclosing sphere with its high-coordinate contact layer. Published descriptions of shard polytopes [2] offer combinatorial neighbors; combinatorial equivalence does not transfer distances between Euclidean realizations. Searches for ratio-bounded simplices and Marion-trisection diameter/radial formulas, as well as semantic mathematical-record searches, produced no exact or stronger covering theorem. An unindexed equivalent geometric realization remains a historical-priority risk.

## Mathematical value — PASS
A precise metric invariant of a recently studied infinite polytope family is determined globally, including complete equality cases and multiplicities. The two types of extremal geometry select demonstrably different vertex layers: balanced complementary sets for pairwise diameter and an approximately one-third-sized high-coordinate set for the enclosing sphere. That separation and the sharp scale ratio \(4\sqrt2/3\) are not consequences merely of knowing the volume and number of vertices. These are natural geometric invariants in the canonical Euclidean realization; arbitrary alternative embeddings are explicitly excluded.

## Limits and comparison
The result concerns only the Euclidean regular-simplex embedding with factor-two coordinate constraints and does not generalize unchanged under affine deformation. The 2026 source's all-dimensional volume theorem and vertex count are credited. No claim of formal proof certification or independent mathematical validation is made. Priority is provisional outside the accessible inspected literature.

[1] Yu. V. Kazakov, *Generalization of Marion's Theorem: Volumes of Central Polytopes Obtained by Trisecting the Edges of Simplices*, arXiv:2606.02087 (2026-06-01), https://www.researchgate.net/publication/405683659_Generalization_of_Marion%27s_Theorem_Volumes_of_Central_Polytopes_Obtained_by_Trisecting_the_Edges_of_Simplices.

[2] A. Padrol, V. Pilaud, J. Ritter, *Shard Polytopes*, arXiv:2007.01008.

Self-review: passed. Independent audit: not yet performed.
