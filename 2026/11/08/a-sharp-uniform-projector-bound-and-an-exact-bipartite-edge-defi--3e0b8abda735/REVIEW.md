# Review of the graph-spline projector theorem

## Correctness: PASS

On every positive-mass edge, the two nodal hats have mass moments \(w/3,w/6,w/2\). With \(A=\operatorname{diag}(\alpha+d/3)\), \(C=W/6\), both \(M=A+C\) and \(B=A-C\) are invertible because the nonnegative matrix \(A^{-1}C\) has row sums at most \(1/2\). The Neumann series establishes \(|M^{-1}|\leq B^{-1}\), whose entries are all strictly positive by connectivity. Since \(q=3B\mathbf1-2\alpha\), every projector evaluation norm is at most \(3-2(B^{-1}\alpha)_v\). For atom-free nonbipartite graphs, odd closed walks make cancellation strict in the alternating Neumann series. For bipartite graphs, vertex-sign conjugation gives \(M^{-1}=SB^{-1}S\); integration of each opposite-sign linear edge profile yields the strictly positive edge-deficit formula. The geometric path limit follows from a finite lower-triangular limit system. This proves the universal and bipartite statements, including all quantifiers and strictness; the exact rational checker supplies independent finite consistency tests of the derived identities, not the infinite proof.

## Originality: PASS (qualified)

The sharp bound three for degree-one spline least-squares projectors on an interval and its interval sharpness are established work attributed to Ciesielski and Oskolkov in Kayumov's accessible 2004 preprint. Oswald's accessible 2006 preprint shows that degree-one projection bounds can be unbounded for degenerate planar triangulations; this does not imply a sharp constant for branched and cyclic one-dimensional graph domains. Hangelbroek–Narcowich–Sun–Ward's 2010 result covers smooth-manifold kernel bases under quasiuniformity conditions, not the specified graph hat-function basis with arbitrary edge-mass ratios. Earlier special-graph exact formulas concern isolated graph families, not the general comparison theorem or a unified bipartite edge penalty. Targeted published-result and literature searches found no identified covering statement. Boman's 2006 weighted finite-element paper remained abstract-only, creating a concrete possible-coverage risk; the corresponding originality assessment is best-knowledge rather than a uniqueness certificate.

## Value: PASS

Uniform projector stability over arbitrary finite metric graph topology and arbitrarily graded edge masses is a meaningful extension of the classical interval question because the 2-dimensional finite-element counterpart can be unbounded. The exact bipartite formula identifies independent vertex-atom and edge-cancellation mechanisms, predicts norming evaluation points, and gives a computable graph-specific stability margin. A constructive path family proves global sharpness of the universal constant; the content is neither a single test graph nor only a recomputation of the known interval constant.

## Scope and outstanding limitations

Only real edgewise-affine least-squares projection with positive edgewise constant densities is covered. A closed nonbipartite graph-specific constant, nonuniform edge densities, higher-degree splines, and independent mathematical audit remain outside the proved claim. The full text of Boman's paper and any equivalent unindexed network formulation remain originality risks. The finite checker is supporting evidence, not proof of the general quantifiers.

Self-review: passed. Independent audit: not yet performed.
