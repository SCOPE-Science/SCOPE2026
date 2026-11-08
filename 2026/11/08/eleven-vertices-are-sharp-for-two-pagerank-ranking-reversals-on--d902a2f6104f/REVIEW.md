# Scientific review

## Correctness — PASS
The claim is about exactly one pair-ranking crossing phenomenon, with a fixed stochastic PageRank normalization. The matching-polynomial determinant formula follows from the tree determinant expansion; the adjugate proves polynomiality of score numerators, which the checker confirms through all degrees. The exact root bound uses the substitution \(\alpha=z/(1+z)\) and Descartes’ rule, with exact rational Sturm counts only for exceptional sign patterns. The census generates every nonisomorphic tree through eleven vertices; its 20,398 unordered vertex-pair comparisons exclude two crossings below eleven and establish one minimal isomorphism class. The displayed witness has a directly verified exact factorization and two sign-changing roots. An independent rational matrix inversion reproduces sample score differences. Risk: enumeration completeness inherits the established tree generator, rather than a separate hand-derived classification.

## Originality — PASS within inspected evidence
The analytic dependence of PageRank on damping and nonmonotone ranking in general networks is established in Boldi–Santini–Vigna (2005), Bressan–Peserico (2009/2010), and Son–Christensen–Grassberger–Paczuski (2012). Their inspected statements do not imply a sharp minimum and unique unlabelled-tree/vertex-pair classification, and the model is distinct from adjacency-based Katz centrality. The relevant 2009/2010 comparison paper was inspected at abstract/metadata level only; no unconditional historical-priority assertion is made. Semantic searches also found no matching indexed claim. These absences do not establish novelty by themselves.

## Mathematical value — PASS
The sharp eleven-vertex threshold settles the earliest possible non-single-crossing PageRank behavior on tree social networks. The unique minimal witness compares two leaves with equal degree, so a degree-only comparison cannot detect the two reversals. The finite cutoff and full first-layer isomorphism classification are natural structural information about damping-sensitive centrality, not a convenience-selected graph example.

## Limitations and close antecedents
The statement is not about all graph classes, directed graphs, personalized teleportation, nonuniform edge weights, or adjacency-based Katz scores. Bibliographic antecedents and the limitation of abstract-only inspection of Bressan–Peserico are documented in RESULT.md and AUDIT.json. The embedded checker and its output constitute reproducible mathematical evidence, not independent validation.

Self-review: passed. Independent audit: not yet performed.
