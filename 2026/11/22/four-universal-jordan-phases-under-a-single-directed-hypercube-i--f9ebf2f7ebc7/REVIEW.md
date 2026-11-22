# Scientific review: a directed arc toggle on Boolean cubes

## Correctness — PASS

The result is an exact all-dimension classification over every finite field of characteristic two. The proof first establishes that the unedited cube adjacency shifted by dimension parity is square-zero with rank half the vertex count. The directed toggle is rank-one. The single scalar \(e_v^{\mathsf T}(A+\delta I)e_u\) equals one for adjacent distinct vertices and zero for nonadjacent vertices. Independent basis-vector arguments give the full power-rank and projection identities, forcing the four stated Jordan structures. The Fitting decomposition then yields all primitive-period populations, time-to-periodic-entry shells and basin sizes. Both standalone scripts ran without error from their actual files: 27 finite rank-filtration checks and 14 exhaustive dynamical cases, including the full \(\mathbb F_4\) state space for dimension three. These computations are corroboration, not an infinite-size proof.

## Originality — PASS, qualified

The original XOR-network treatment of Ciandrini et al. (arXiv:0809.1526) supplies a general linear-dynamics framework, but not this explicit one-way hypercube defect theorem. Batal's (arXiv:2108.03059) edge-addition/removal theory concerns symmetric closed-neighborhood matrices and nullity, not ordered rank-one toggles or temporal orbit counts. The closely matching published hypercube missing-edge classification treats a *bidirectional* defect; its even-dimensional periodic three-/six-cycles and odd-dimensional four-cycles differ in both operator and conclusions. This result instead supplies a two-distance, two-parity classification of one-way interaction changes. The comparison includes actual indexed-result searches and accessible full primary text. Searches alone cannot exclude inaccessible, unindexed or differently worded equivalent work, including a general rank-one square-zero perturbation theorem possibly containing the classification as a corollary.

## Value — PASS

A single *directed* interaction change is a natural local intervention in a directed regulatory or parity network. The exact response on an infinite family of highly symmetric graphs is a complete four-phase classification rather than a renaming of the unperturbed dynamics. Near-neighbor deletion and far-neighbor insertion give opposite behaviors: reversible four-cycles versus complete four-step extinction in the two dimension parities, with sharp temporal-shell and individual basin laws. Unlike a rank-only calculation, the theorem determines the complete recurrent/transient decomposition and quantifies attraction to every orbit, making the precise invariant meaningful for fault/intervention sensitivity.

## Literature and limitations

- Ciandrini et al., *Feedback topology and XOR-dynamics in Boolean networks with varying input structure*, arXiv:0809.1526 (first posted 2008-09-09), https://arxiv.org/abs/0809.1526 . General linear framework, not this geometric one-arc classification.
- A. Batal, *Effects of edge addition or removal on the nullity of a graph*, arXiv:2108.03059, https://arxiv.org/html/2108.03059v2 . Undirected symmetric matrices and static nullity, not directed or time-dependent.
- *A missing-edge parity transition in hypercube XOR dynamics*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-missing-edge-parity-transition-in-hypercube-xor-dynamics--0ddebf65b6fe . Closest graph perturbation, but toggles both orientations and has different invariant factors.

Only one ordered arc is toggled; the theorem does not cover arbitrary graph defects, different fields or update schedules. The bibliographic review is not a priority certificate, and there has been no independent external validation.

Self-review: passed. Independent audit: not yet performed.
