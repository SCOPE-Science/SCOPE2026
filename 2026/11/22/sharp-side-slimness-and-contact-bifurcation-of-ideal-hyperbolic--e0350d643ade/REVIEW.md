# Scientific review: sharp ideal-quadrilateral side slimness

## Correctness — PASS

The claimed domain is *all nondegenerate ideal geodesic quadrilaterals* of the curvature-\(-1\) hyperbolic plane; no finite vertices or arbitrary polygons are included. Three-transitivity normalizes the boundary vertices to \((0,1,\lambda,\infty)\). The signed Euclidean circle equation gives the hyperbolic point-to-geodesic distance exactly. The minimum of the three side-distance functions is maximized by separating \(0<x\le1\) from its reciprocal half. Its unique crossover lies inside that interval precisely when \(\lambda>3\). The four side types are reduced using a half-turn and a change to the reciprocal cross-ratio parameter. Their envelope has exactly one maximum, at the nonregular class \(\kappa=3\).

An independent point-to-point/geodesic minimization program (`verify.py`, standard library only) passed 5,335 analytic/direct numerical comparisons and five relabeling tests. Such finite computation does not establish the universal theorem; the exact algebraic and monotonicity arguments in `RESULT.md` do.

## Originality — PASS, with stated priority risk

The closest full-text mathematical comparisons are the 2013 ideal-quadrilateral results of Vuorinen–Wang and their 2019 treatment by Wang–Vuorinen–Zhang. Their variables \(d_1,d_2\) are *infimum distances between opposite-side pairs*. Our invariant has the different quantifier order \(\max_S\sup_{p\in S}\min_{T\ne S}d(p,T)\), including the adjacent sides; the earlier sharp statements do not determine the farthest-point contact law or the nonregular shape achieving the global bound. The November 2026 slim-polygon paper supplies the motivating notion, not this exact profile. A known regular-square side-slimness calculation is one specialization; the work here treats a full one-dimensional shape-moduli space and identifies its sharp, nonregular extremum. No exact equivalent was found in focused title, alias, formula and parameter searches.

The absence of an indexed match is not a proof of novelty. The main residual risk is an unindexed classical ideal-quadrilateral thinness calculation using another convention, or a general theorem implying the result without naming this invariant.

## Mathematical value — PASS

The output is a complete sharp classification of a natural geodesic-polygon invariant, not merely a routine numerical instance: all shapes are treated, the maximizing shape is uniquely nonregular, and the nearest-side contact geometry bifurcates at a single exact cross ratio. It gives a reproducible ideal-quadrilateral benchmark for polygon-slimness questions and distinguishes this observable from familiar opposite-side separation and inradius observables. Neither a new general hyperbolicity criterion nor a theorem for general finite-vertex quadrilaterals is claimed.

## Evidence and limitations

Primary scientific sources: P. Tselekidis, arXiv:2611.05429v1 (2026); G. Wang, M. Vuorinen, X. Zhang, arXiv:1908.10389 (2019); M. Vuorinen and G. Wang, Ann. Acad. Sci. Fenn. Math. 38 (2013), 433–453, Corollary 1.4 and its proof. The proof and standalone numeric test are included in the deliverable. Historical-priority completeness and external correctness validation are not asserted.

Self-review: passed. Independent audit: not yet performed.
