# Scientific review: centroidal-core chord interception in triangles

## Correctness — PASS
The event and its boundary conventions are explicit. Conditional on distinct sides, the affine coordinates \(u,v\) are independent uniform numbers, and the chord meets the scaled centroidal triangle precisely on the two integration regions derived in RESULT.md. The integrals evaluate to the displayed universal function; the endpoint atom and strict shape bounds follow from side-choice probabilities and the triangle inequality. The exact argument covers every nondegenerate triangle and every \(0<r<1\). A separate segment-clipping implementation checked 975000 randomly generated chords, and direct barycentric sampling provided a separate numerical check. These computations support, but do not establish, the infinite-dimensional claim.

## Originality — PASS (historical priority provisional)
Searches for homothetic triangle-core hitting by random boundary chords in mathematical literature and indexed results identified no statement implying the entire law. The closest 2016 triangle-cut preprint addresses segment length thresholds, the 2013 triangular-lattice preprint concerns hitting across a random lattice, and established triangle line-picking formulas concern interior endpoints. An accessible previous rectangular boundary-chord interception result concerns rectangles and a different conditional pair geometry, while previous triangle chord moments/intersections do not give nested-core interception. A specialist full-text source remains inaccessible; residual historical risk is explicitly retained.

## Mathematical value — PASS
The result gives the complete distribution of a natural minimal target-scale statistic, not just a single hit probability. The logarithmic conditional law is universal across triangle shapes and arbitrary independent side-selection weights. Its endpoint atom separates same-side chords from transverse chords, while its shape factor gives a unique fixed-perimeter equilateral maximizer and an optimal degenerating lower bound. The statistic reveals precisely one symmetric function of the side proportions and is therefore useful both as a comparison invariant and as a negative shape-identification example. The scope is intentionally restricted to centroidal homothetic triangular targets.

Self-review: passed. Independent audit: not yet performed.
