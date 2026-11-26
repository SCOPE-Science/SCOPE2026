# Independent mathematical audit

## correctness

PASS

Write c=1-delta and s=sqrt(1-c^2). For unit reference a and nonzero increment b, put x=|<a,b>|/||b||. Maximizing over the closed cap gives ||b|| for x>=c, and ||b||(cx+s sqrt(1-x^2)) for x<c, by aligning the perpendicular component with the signed perpendicular component of b. Boundary values are limits from the open cap, so the suprema coincide. Concavity on [0,c] gives minimum s at x=0. Since each reference increment is unit for an isometry, taking the supremum over pairs gives the lower index bound without any norm-attainment assumption on f. A rank-two skew J has Ja perpendicular to a. Its plane contains one nonzero reference increment, so ||Jg||_Lip is positive and equals one in the isometric case. For a merely norm-one g and admissible u, the orthogonal component of u relative to a/||a|| has norm at most s because <u,a>/||a||>c. Thus normalized Jg gives the upper bound even without an isometry. For unit a the limiting radius equals the supremum of the longitudinal evaluations, by the uniform estimate ||u-a||<=sqrt(2 epsilon). At finite tolerance the perpendicular term adds at most s||f||_Lip. The same skew witness has zero longitudinal evaluation and finite radius exactly s. In real dimension one with isometric g the matching unit sign evaluates the entire increment in absolute value, giving index 1 and error 0.

## originality

PASS

The supported distinction is the exact positive-tolerance profile and best uniform regularization error on all isometric metric domains in real Hilbert targets. Near-norming definitions, skew maps, and a zero limiting relative index are not novel ingredients.

## value

PASS

The finite near-norming relaxation is a preexisting object, and exact control matters because the real Hilbert limiting index is zero. The theorem quantifies the positive floor introduced by tolerance and the worst bias across all normalized test maps, showing that neither square-root scale nor its leading coefficient can be reduced. The construction works on arbitrary metric subsets without needing attainment, differentiability or compactness. This supplies a uniform benchmark, not just a planar cap calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
