# Scientific assessment: rooted-forest chain-polytope moment theorem

## Correctness — PASS
For every finite rooted forest, the triangular stick-breaking map bijects the open parameter cube and the chain-polytope interior. Its Jacobian is exactly the product of \((1-b_v)^{s_v-1}\), so normalized volume is a product of \(\operatorname{Beta}(1,s_v)\) laws and the mixed-moment product follows from elementary beta integrals. The covariance ratios reduce to shared-ancestor factors \(F(s)>1\) and one comparable-node factor \(G(s)<1\). The strict upper bound obtained by telescoping \(\prod_{j=1}^{h}F(s_v+j)\) proves every ancestor–descendant covariance negative; the same-component incomparable and disconnected cases follow without exceptions. An independently structured canonical-simplex calculation checked exact first/second moments for 873 small rooted forests. No extrapolation from finite tests is used in the theorem.

## Originality — PASS, historical priority provisional
The inspected Okada–Tsuchiya full text (arXiv:2003.12271) contains Stanley's standard transfer map and enriched constructions but no all-degree rooted-forest volume-moment or covariance-sign formula. Ohsugi–Tsuchiya (arXiv:1812.02097) treats enriched chain polytopes and toric/Ehrhart questions; von Bell and coauthors (arXiv:2102.11306) analyze generalized-snake order-polytope triangulations and volumes. Search comparisons against related mathematical records did not identify a statement implying the full moment factorization and strict three-way covariance sign law. The classical hook-length volume product and transfer map are premises and are not claimed as new. The earlier complete-multipartite stable-set moment identity covers only overlapping special posets, not arbitrary rooted forests. A possible unlocated equivalent in probabilistic tree-labeling terminology remains a risk; negative searches alone are not proof of novelty.

## Mathematical value — PASS
The theorem determines every interior polynomial moment, supports exact volume-uniform sampling and rational covariance evaluation, and extracts the rooted-forest comparability relation and component partition from strict covariance signs. Its negative-versus-positive sign separation is structural rather than a low-degree numeric coincidence and works with arbitrary branching and tree sizes. The full distribution law and sign recovery are more informative than the classical hook-volume formula alone.

## Literature and limits
Closest foundations: Stanley (1986); Okada–Tsuchiya (2020 arXiv submission); Ohsugi–Tsuchiya (2018 arXiv submission); von Bell et al. (2021 arXiv submission). Special-case overlap exists with complete multipartite stable-set-polytope moment formulas. The theorem does not assert the same law for general Hasse diagrams with multiple parents, and historical priority has not received independent verification.

Self-review: passed. Independent audit: not yet performed.
