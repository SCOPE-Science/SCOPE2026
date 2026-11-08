# Scientific review: a sharp Pareto area law for random circumscribed polygons

## Correctness — PASS

The proof starts from the exact uniform Dirichlet law of circular spacings and the necessary-and-sufficient boundedness criterion \(\max_iY_i<1/2\). The tangent-polygon area is \(\sum_i\tan(\pi Y_i)\). A one-gap density calculation supplies the leading coefficient, and the translated-simplex two-gap probability \((2\delta)^{n-1}\) eliminates coincident extreme gaps for all \(n\ge3\). The elementary maximum/sum squeeze and tail integration finish the infinite-range statements. The standalone test checks the finite rational identities and numerical consequences; simulations alone are not regarded as proof.

## Originality — PASS (provisional priority)

Xu (2015) studies the same circle-tangency construction and recognizes unbounded magnitudes, and Wang--Li--Xu (2023) supplies the known tangent-score formula and large-sample approximations. Fodor--Hug--Ziebarth (2014) studies clipped random circumscribed polyhedra under different halfspace sampling. Neither the available abstract of Xu (2015) nor the inspected complete 2023 HTML establishes the exact **fixed-sample conditional** \(1/t\) survival coefficient and its sharp moment criterion; indexed records comparing related tangent geometry likewise do not imply them. The 2015 primary full text could not be inspected, leaving an explicit priority risk. Negative searches do not certify uniqueness.

## Mathematical value — PASS

The theorem explains why conditioning away unbounded intersections does not give finite expected area, although bounded polygons occur with positive probability and large-sample approximation theorems exist. Its exact Pareto coefficient and moment cutoff provide a natural, quantitative boundary for the area functional in circumscribed geometric probability, not a restatement of unbounded support.

## Closest literature and limitations

Fodor--Hug--Ziebarth, arXiv:1409.8105 (2014); W.-Q. Xu, Statistics & Probability Letters 106 (2015), 52–57, DOI 10.1016/j.spl.2015.06.026; and Wang--Li--Xu, Journal of Numerical Analysis and Approximation Theory 52 (2023), 273–294, DOI 10.33993/jnaat522-1360. The result has no outer truncation and concerns iid uniform points on the unit circle for fixed integers \(n\ge3\); it makes no claims about nonuniform angular sampling, general smooth convex boundaries, or tail error uniform in \(n\). Priority is provisional because the full Xu article was inaccessible.

Self-review: passed. Independent audit: not yet performed.
