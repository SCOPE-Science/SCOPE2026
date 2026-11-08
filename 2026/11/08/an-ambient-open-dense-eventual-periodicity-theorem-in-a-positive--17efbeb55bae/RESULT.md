# An ambient open-dense eventual-periodicity theorem in a positive-entropy planar absolute-value map

## Finding
For \(F:\mathbb R^2\to\mathbb R^2\) defined by
\[
F(x,y)=(|x|-y-1,\ x-|y|+3/2),
\]
let \(\operatorname{Per}(F)\) denote all points belonging to finite periodic orbits, and let
\[
E=\bigcup_{n\ge0}F^{-n}(\operatorname{Per}(F)).
\]
**The Euclidean interior of \(E\) is dense in \(\mathbb R^2\).** There is an explicit open dense subset all of whose points are eventually periodic with one of at most three distinct periodic omega-limit sets, even though \(F\) has positive topological entropy on its invariant graph.

More precisely, let \(\Gamma\) be the canonical compact invariant polygonal graph from [1], and \(\mathcal W\) the union of the relative interiors of its collapsed (plateau) edges. Let
\[
P=\{(-7/2,-1),(7/2,-3),(11/2,2),(5/2,5)\},
\quad B=\bigcup_{n\ge0}F^{-n}(\mathcal W\cup P).
\]
Then \(\operatorname{int}_{\mathbb R^2}(B)\) is dense, \(B\subseteq E\), and every point of \(B\) has an omega-limit in the finite collection of at most three periodic plateau omega-limits from [1].

## Assumptions and scope
The phase space is the **entire Euclidean plane**, with no bounded initial-condition restriction. The parameters are exactly \(a=-1\), \(b=3/2\); the positive-entropy statement for \(1<b<2\) is a prior result, not part of the proof of ambient density. We use the graph \(\Gamma\), finite graph entrance, and plateau-preimage density established in [1]. A plateau is an edge interior on which \(F\) is constant. When an iterate of \(F\) is said to be affine on an open cell, the open cell is chosen to avoid all nonidentically-zero coordinate switching equations for all iterates under consideration.

## Proof
**1. Published graph dynamics.** In [1, Theorem B and Proposition 18], \(\Gamma\) is compact and forward invariant, every planar orbit enters \(\Gamma\) in finite time, and, with \(Q_1=\{x>0,y>0\}\) and \(Q_3=\{x<0,y<0\}\),
\[
F^{11}(Q_1\cup Q_3)\subseteq\Gamma.
\]
In [1, Proposition 23 and Theorem C], \(\mathcal U_\Gamma=\bigcup_{j\ge0}(F|_\Gamma)^{-j}(\mathcal W)\) is open and dense **relative to \(\Gamma\)**, and the omega-limits of its points are among at most three plateau omega-limits. Because \(b=3/2\) is rational, these limits are periodic orbits. In particular \(\mathcal W\subset E\). The source explicitly leaves the extension of open-density from \(\Gamma\) to the ambient plane as a future problem.

**2. Baire reduction to an affine cell.** Fix any nonempty open disk \(D\subset\mathbb R^2\). The sets \(D\cap F^{-n}(\Gamma)\), \(n\ge0\), are relatively closed in \(D\), and their union is \(D\). By the Baire category theorem, for some \(n\) a nonempty open disk \(V\subset D\) satisfies \(F^n(V)\subset\Gamma\). Since \(F\) is piecewise affine with only finitely many switching lines through time \(n\), shrink \(V\) to a nonempty open affine itinerary cell. Its affine image is contained in the finite one-dimensional graph, so its linear part has rank \(0\) or \(1\).

If the rank is \(1\), shrink \(V\) again so that its image is a nondegenerate relatively open subinterval of a single graph edge. This interval intersects the dense relatively open set \(\mathcal U_\Gamma\). Its inverse image contains a nonempty open \(V'\subset V\) whose orbits eventually enter \(\mathcal W\), hence \(V'\subset B\).

**3. Rank-zero branches, including pre-graph collapse.** If the affine image is a point, choose the *first* iterate at which the affine derivative on the itinerary cell becomes zero. On quadrants \(Q_2\) and \(Q_4\), the affine branch matrices are invertible (determinant of absolute value \(2\)); on quadrants \(Q_1\) and \(Q_3\), the branch maps have rank \(1\). Thus the first rank loss from \(2\) to \(1\) occurs upon entering \(Q_1\) or \(Q_3\). After that visit, the full first-image lines may be parametrized respectively as
\[
(X,Y)=(t,t+5/2),\quad t\in\mathbb R,
\qquad
(X,Y)=(-t-1,t+3/2),\quad t<0.
\]
A ten-iteration exhaustive rational affine-cell split, reproduced by the included standalone checker, determines **every constant open-cell image on both rays before graph entrance**. It returns exactly
\[
C=\{(-7/2,-1),\ (-3/2,1),\ (5/2,-2)\}.
\]
For reproducibility, if \((X,Y)=(\alpha t+\beta,\gamma t+\delta)\), split the current parameter interval at each root of \(X\) or \(Y\). On each open subinterval with signs \(s_x,s_y\in\{-1,1\}\), the updated coefficients are
\[
(\alpha',\beta',\gamma',\delta')
=(s_x\alpha-\gamma,\ s_x\beta-\delta-1,\ \alpha-s_y\gamma,\ \beta-s_y\delta+3/2).
\]
Whenever both new slopes vanish, the output is constant and recorded. After the first ten steps from the first-image ray, the numbers of surviving nonconstant cells are respectively
\[
(2,3,3,4,4,5,7,8,10,11)
\quad\text{and}\quad
(3,5,6,9,10,13,15,17,22,26).
\]
Every recorded constant value belongs to \(C\), and each point of \(C\) enters the displayed four-cycle \(P\): the entrance delays are \(0,8,3\), respectively. The cycle \(P\) is a plateau omega-limit by [1, Section 5.6], since \(F\) collapses the edge \(\overline{P_4S}\) onto \(P_1=(-7/2,-1)\).

For a rank-zero branch whose first collapse occurs *after* the first eleven iterates following the visit to \(Q_1\) or \(Q_3\), its still-rank-one image by that time is contained in \(\Gamma\) by Proposition 18. Shrink its itinerary cell so this image is an open interval of a single graph edge, away from vertices. Its first subsequent rank-zero collapse necessarily takes place on a plateau edge of \(\Gamma\), and therefore the entire shrunk open cell eventually enters \(\mathcal W\). This covers the remaining possibility. Thus **every rank-zero case gives a nonempty open subdisk contained in \(B\)**.

**4. Conclusion.** Every initial disk \(D\) contains an open subdisk in \(B\). Therefore \(\operatorname{int}_{\mathbb R^2}(B)\) is open and dense. The published plateau conclusions imply eventual periodicity with at most three omega-limit sets for its points. By [1, Proposition 36], \(h(F|_\Gamma)>0\) at \(b=3/2\), which is compatible with the open-dense eventual-periodic planar subset.

## Verification
Run `python3 certify_ambient.py` using standard Python 3. The checker represents all finite endpoints, coefficients, and orbit coordinates as exact rational fractions. For the two infinite ray tails it uses a rational interior test point, which determines the constant signs of the affine coordinates on each unsplit open cell. It asserts the ten-step alive-cell vectors, all distinct constant images, and eventual capture of each such image by \(P\). An exact split of linear functions on open intervals is exhaustive; no floating-point trajectory scan establishes the claim. The count concerns open two-dimensional itinerary cells. Switching boundaries need not be captured, because the theorem asserts existence of an open dense subset, not capture of every point.

## Relationship to prior work
The complete finite polygonal graph, finite entrance, dense plateau-preimage subset **within the graph**, and positive entropy are due to Cima, Gasull, Mañosa and Mañosas [1]. They expressly identify open density in the **whole plane** as a problem for future research. The 2025 follow-up [2] proves full arclength measure on invariant graphs for certain parameter regions but does not establish this particular ambient-plane claim. The present contribution is a Baire lift that handles the otherwise problematic rank-zero planar cells, with an exhaustive exact parameter-ray certificate. The special parameter \(b=3/2\) lies in the positive-entropy window, so ambient topological genericity and chaotic graph dynamics coexist.

## Limitations
This statement is **topological**, not an assertion of full two-dimensional Lebesgue measure, nor a classification of every planar orbit. It is proved for the indicated parameter only; arbitrary rational \(b\), boundary itineraries, and higher-dimensional perturbations are not treated. Source theorems are taken as established results. The exhaustive finite certificate is restricted to the eleven iterates before graph entrance; the graph theorem and plateau geometry address all subsequent times. An equivalent result in independently unindexed literature remains possible, and independent validation has not been undertaken.

## References
[1] A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052 (first available 2024-10-01); *Qualitative Theory of Dynamical Systems* 24 (2025), article 70, DOI: 10.1007/s12346-025-01221-1. Full open text: https://link.springer.com/article/10.1007/s12346-025-01221-1.

[2] A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Entropy and omega-limit sets on invariant graphs for a class of planar piecewise linear maps*, arXiv:2503.02411 (2025), https://arxiv.org/abs/2503.02411.
