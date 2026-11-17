# Assessment of the Euclidean pentasm classification

## Correctness — PASS

The domain is explicit: standard Euclidean \(\mathbb R^d\), all integers \(d\ge3\), and all real \(t>0\). The proof derives the purported center and common radius from the equal-distance and strictly positive barycentric equations for \(d\) affinely independent contacts. It then independently checks every polytope vertex by direct squared-distance expansion. Three noncontact vertex types have strictly positive clearance; the segment endpoint omitted from the vertex list also has positive clearance. The weighted-variance identity supplies a genuine global lower bound on the radius at **every** proposed center, proving optimality and uniqueness, not merely local stationarity. Direct type-by-type pair enumeration proves the diameter formula and that no other pair is diametral. An exact rational verifier passed 220 parameter configurations and 110220 comparisons, with 15 external convex-hull configurations confirming the vertex count. Computations alone do not cover all real parameters; the written algebra does.

## Originality — PASS, with historical priority qualified

The exact coordinate realization of the pentasm at unit displacement, the definition by Minkowski addition, and the extremal face-count significance are already in Pineda-Villavicencio, Ugon and Yost (arXiv:1509.08218, Section 4). The newer Wang–Yost (arXiv:2611.07472v1, Sections 1–3) classifies related few-vertex decomposable polytopes and explicitly treats pentasms as background. Their inspected statements concern combinatorial decomposability, facets and edges; searches of both full texts for terms associated with Euclidean minimum spheres and diameters did not find a covering metric classification. Earlier exact minimum-ball work on weighted terminal simplices applies to a **simplex** rather than this simplex-plus-segment Minkowski sum. Stellohedra and lineup polytopes are different Minkowski-sum families. Published mathematical-record searches for pentasms, oblique simplex-plus-segment sums, circumspheres, screening, and bipartite diameter graphs yielded no dominating result. The new claim is the complete **parameterized metric classification** including all contacts and diametral pairs; it does not claim the existence or combinatorics of pentasms as new.

Residual risk: a general, possibly differently indexed formula for minimum balls of simplex-plus-segment sums could specialize to the present family. Search failure is not proof of historical uniqueness. A generic minimum-ball solver can of course compute particular finite instances, but does not by itself present the all-dimensional equality classification.

## Mathematical value — PASS

Pentasms are a distinguished, extremal family of decomposable polytopes with only \(2d+1\) vertices. For the canonical orthonormal realization with an adjustable length of the segment summand, the theorem determines the exact enclosing radius, its sole center, **every** contact point, the strictly positive noncontact clearances, the diameter, and the entire diameter graph, for all dimensions and all positive parameters. The persistent loss of \(d+1\) possible sphere contacts despite changes in segment length, and the precise \(K_{2,d-2}\) diametral structure, are structural and naturally motivated geometry facts; neither follows from the extremal face-count classification. They provide an explicit test family for Euclidean extremal geometry of sparse Minkowski-decomposable polytopes. The scope is narrower than arbitrary affine pentasms and no broader general theorem is claimed.

## Scientific and verification limitations

The conclusion is conditional on the stated orthonormal coordinates and positive parameter. The singular endpoint \(t=0\) is not covered. Exact rational computations test finitely many parameter values only, and a numerical convex hull test covers small dimensions only. Historical priority is provisional, and an independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
