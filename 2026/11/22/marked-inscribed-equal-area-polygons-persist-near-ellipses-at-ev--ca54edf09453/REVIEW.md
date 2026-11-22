# Scientific review

## Correctness — PASS

The fixed-mark Jacobian of the \(n-1\) independent signed consecutive-triangle-area differences is exactly \(c_n(u_{j+2}-u_j-u_1+u_{n-1})\), with \(c_n=\cos(2\pi/n)-\cos(4\pi/n)>0\). A kernel vector has \(u_{j+2}=u_j\), hence for odd \(n\) is constant and, with \(u_0=0\), vanishes. Therefore the finite-dimensional Jacobian is bijective. The Banach-parameter implicit function theorem for \(C^2\) radial graphs proves existence and local uniqueness, uniformly for prescribed angle on a compact circle. Positivity of the radial curvature numerator and the circular triangle determinant gives strict convexity and positive common area. A direct determinant expansion gives the first-order recurrence; for even \(n\), its alternating cokernel supplies the precise differentiable-branch obstruction. All quantifiers and local limitations are explicit. The standalone checker passed 278 numerical diagnostics; the proof does not rely on numerical exhaustiveness.

## Originality — PASS, with residual historical risk

The explicitly posed 2011 Craizer–Teixeira–da Silva Section 3.3 question asks for *inscribed*, fixed-order equal-area polygons with prescribed first vertex, and says its own approximation is not necessarily inscribed. The present theorem supplies a nontrivial local affirmative instance for all fixed odd orders, an all-marked-point local uniqueness statement, and an explicit inverse deformation law. Harel–Rabin 2003 classify abstract equal-area polygons and do not impose their vertices on a separately specified near-ellipse curve. Both primary texts were inspected, rather than inferred from titles. Searches for inscribed equal-area polygons, odd-order marked vertices, convex-curve perturbations, and local implicit-function results did not identify a covering result. An independent comprehensive historical-priority search is not claimed; a specialized older local theorem could overlap.

## Value — PASS

The article motivating this work singled out exact marked inscription (as opposed to merely approximating the oval) as a meaningful open geometric condition. The result provides an all-marked-point persistence theorem and uniqueness along a nonconic Banach neighborhood, not merely a classification of polygons already known to exist. Its derivative explicitly distinguishes odd and even cyclic geometry, offering a concrete local mechanism and a boundary on smooth continuation. This is a motivated structural local theorem, not a claim of a global solution or significant numerical improvement.

## Closest literature and limits

Harel–Rabin, *Amer. Math. Monthly* 110 (2003), 606–619, derives affine classification; Craizer–Teixeira–da Silva, arXiv:1103.2722 Section 3.3 (2011), gives an approximate noninscribed construction and asks the exact marked-inscription question. The authors' educational webpage repeats that question. Comparisons with other published equal-area polygon moduli results found no implication of this near-ellipse marked existence theorem. The proof works for each fixed odd \(n\) and ovals sufficiently \(C^2\)-close to ellipses; historical priority has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
