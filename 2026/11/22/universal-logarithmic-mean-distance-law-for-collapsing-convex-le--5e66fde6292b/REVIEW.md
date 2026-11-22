# Scientific review: collapsing-lens boundary mean-distance asymptotic

## Correctness — PASS

The result is restricted to fixed Lipschitz graph pairs with convex lower graph, concave upper graph and coincident endpoints. The arclength-to-horizontal-mixture approximation has total-variation error \(O(\varepsilon^2)\), and perimeter \(4+O(\varepsilon^2)\). Same-branch distances differ from the horizontal Gini mean by \(O(\varepsilon^2)\). The two opposite-branch contributions reduce with error \(O(\varepsilon^2)\) to a single vertical width \(h(x)\). Exact integration of \(\sqrt{s^2+r^2}-s\) establishes the coefficient \(1/32\) after the sampling and perimeter normalizations. This integral has an integrable endpoint remainder because \(h\) is Lipschitz and zero at the tips. Sharp fixed-area bounds follow from Cauchy–Schwarz and the positive mixture representation of concave profiles by area-one tents, including equality and nonattainment. Finite quadrature independently checks three nonidentical lens geometries but is not the proof.

## Originality — PASS, with stated residual priority risks

The motivating paper of Shen establishes the universal \(1/6\) lower bound but not its thin-lens logarithmic correction. The published acute-triangle result for collapsing concave lenses obtains a different three-point probability with coefficient proportional to \(\int h^2\); it already contains the tent/flat envelope, which is **not** claimed as a novel concavity inequality. The thin-parallelogram logarithmic result concerns the boundary-minus-interior mean-distance *gap* for quadrilaterals and not this arbitrary-profile normalized boundary mean. A previously studied stadium asymptotic has a different zero-tip geometry and is only a special shape case. The conclusion is best-knowledge novelty of the two-point observable's full family coefficient, not absolute historical priority. A plausible older work of Tokmachev and Lotnikov's 2026 preprint were not available as inspected full text; this limits the originality assessment without implying coverage.

## Mathematical value — PASS

The theorem quantifies the deficit in a recently proved sharp geometric mean-distance inequality for the natural degenerating class of all Lipschitz convex lenses, rather than a fixed shape. The leading coefficient is exactly observable from the squared width profile and is unaffected by vertical midline shear. Its sharp fixed-area range identifies the triangular-tent maximizer, the unattainable flat-profile infimum, and strictness for each nondegenerate lens. The independent novelty resides in the mean-distance asymptotic; classical one-dimensional concavity bounds are employed rather than represented as discoveries.

## Scope and limitations

This is an analytic leading-order result and fixed-profile \(O(\varepsilon^2)\) estimate. The complete second-order constant and endpoint-unbounded-slope profiles remain untreated. The checked literature and public records do not constitute an exhaustive historic priority search. Numerical code supplies corroborating finite checks only; no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
