# Exact minimum enclosing spheres and diametral rigidity of Euclidean pentasms

## Finding

**Theorem (complete Euclidean outer geometry of a scalar-stretched pentasm).** Fix any integer \(d\ge3\) and any real \(t>0\). Put \(m=d-2\), let \(e_1,\ldots,e_d\) be the standard orthonormal basis of \(\mathbb R^d\), and define
\[
\Delta_d=\operatorname{conv}\{0,e_1,\ldots,e_d\},\qquad
P_{d,t}=\Delta_d+[0,t(e_1+e_2)].
\]
Write
\[
D=m(2t+1)^2+2,\qquad
A=\frac{(2t+1)(mt(t+1)+1)}D,\qquad
B=\frac{2t^2+2t+1}{D}.
\]
The unique minimum enclosing **Euclidean** ball of \(P_{d,t}\) has center
\[
c=(A,A,\underbrace{B,\ldots,B}_{m\text{ entries}})
\]
and squared radius
\[
\boxed{\quad R^2(P_{d,t})=\frac{2mt^4+4mt^3+6mt^2+4mt+m+1}{m(2t+1)^2+2}.\quad}
\]
Of the polytope's exactly \(2d+1\) vertices, **precisely \(d\)** are on the optimal sphere: they are
\[
\boxed{\quad e_3,\ldots,e_d,\quad e_1+t(e_1+e_2),\quad e_2+t(e_1+e_2).\quad}
\]
These \(d\) contact vertices form an affinely independent simplex of dimension \(d-1\), with the ball center in its relative interior. Every other vertex has strictly positive squared-distance clearance from that sphere. The Euclidean diameter and its complete equality classification are
\[
\boxed{\quad\operatorname{diam}_2(P_{d,t})^2=2t^2+2t+2,\quad}
\]
with **exactly \(2(d-2)\) unordered diametral pairs**,
\[
\boxed{\quad\{e_j,\ e_i+t(e_1+e_2)\}:\quad 3\le j\le d,\ i\in\{1,2\}.\quad}
\]
Consequently the nonisolated component of the Euclidean diameter graph is \(K_{2,d-2}\); its other \(d+1\) vertices are isolated. In particular, *all and only* the minimum-sphere contacts are endpoints of diameters.

For the traditional unit displacement \(t=1\),
\[
\boxed{\quad R^2(P_{d,1})=\frac{17d-33}{9d-16},\qquad
\operatorname{diam}_2(P_{d,1})^2=6.\quad}
\]

## Assumptions and scope

The parameter \(t\) is arbitrary and strictly positive. The Euclidean scalar product is the standard one in \(\mathbb R^d\); these formulas do **not** claim affine invariance or apply to arbitrary skew realizations of the same combinatorial polytope. The case \(t=0\) is excluded because the polytope collapses to a simplex and its contact and diameter classes change. The construction is full-dimensional for \(d\ge3\).

As a Minkowski sum of a simplex and a non-edge-parallel segment in a two-face direction, \(P_{d,t}\) is a pentasm. Its vertex set is
\[
\{0\}\ \cup\ \{e_i:1\le i\le d\}\ \cup\
\{e_i+t(e_1+e_2):1\le i\le d\}.
\]
The remaining potential Minkowski endpoint \(t(e_1+e_2)\) is not a vertex: it is the strict convex combination of \(0\) and the two special translated vertices with weights \(1/(2t+1),\ t/(2t+1),\ t/(2t+1)\). All listed points are exposed vertices: for the untranslated basis points, choose a linear objective selecting that basis point while making the sum of its first two coefficients negative; for translated basis points, reverse the sign of that sum while selecting the desired basis point. The origin is exposed by a strictly negative objective. Thus there are exactly \(2d+1\) vertices.

## Proof

**1. Candidate sphere from its support simplex.** Abbreviate \(v=e_1+e_2\). The candidate contact points are the two distinguished translated vertices \(p_1=e_1+tv\), \(p_2=e_2+tv\), together with \(q_j=e_j\) for \(3\le j\le d\). Seek a center with first coordinates \(A,A\) and remaining coordinates \(B\). Equality of their squared distances requires
\[
2t(t+1)-2(2t+1)A+2B=0,
\qquad B=(2t+1)A-t(t+1).
\]
Require simultaneously that the center be a convex combination of these contacts, with equal weights on the two distinguished points and on each of the \(m\) remaining ones. The proposed coefficients are
\[
w(p_1)=w(p_2)=\frac{A}{2t+1}=\frac{mt(t+1)+1}{D},
\qquad w(q_j)=B=\frac{2t^2+2t+1}{D}.
\]
They are strictly positive, sum to one because \(2A/(2t+1)+mB=1\), and have weighted barycenter exactly \(c\). In particular, all contact points are at one common distance from \(c\). Direct expansion gives the displayed \(R^2\). Their coordinate columns are linearly independent (the first two coordinates of \(p_1,p_2\) have determinant \(2t+1>0\)), so they are affinely independent as claimed.

**2. Global containment and strict contact screening.** Define the squared clearance of a point \(z\) to be \(\gamma(z)=R^2-\lVert z-c\rVert_2^2\). Computing it for every vertex type gives
\[
\begin{aligned}
\gamma(q_j)&=\gamma(p_1)=\gamma(p_2)=0,\\
\gamma(0)&=\frac{m+4(m-1)t(t+1)}{D},\\
\gamma(e_1)&=\gamma(e_2)
=\frac{2t(2mt^2+3mt+m-2t)}{D},\\
\gamma(e_j+tv)&=\frac{2t(2mt^2+mt+2t+2)}{D}\quad(3\le j\le d).
\end{aligned}
\]
Every displayed nonzero clearance is strictly positive: \(m\ge1\), \(t>0\), and \(2mt^2+3mt+m-2t\ge2t^2+t+1>0\). For completeness, the omitted nonvertex Minkowski endpoint has clearance \(\gamma(tv)=m(2t+1)(2t^2+2t+1)/D>0\). The entire finite endpoint set, and therefore its convex hull \(P_{d,t}\), lies in the closed sphere ball. Since squared distance from a fixed point is strictly convex, no nonvertex convex combination of the contact points can also lie on the sphere. Hence these and only these \(d\) vertices are contact points of the full polytope.

**3. Optimality and uniqueness.** For an arbitrary proposed Euclidean ball center \(z\), the exact weighted-variance identity applied to the strictly positive barycentric weights from step 1 yields
\[
\sum_{u\in\{p_1,p_2,q_3,\ldots,q_d\}}
 w(u)\lVert u-z\rVert_2^2
=R^2+\lVert z-c\rVert_2^2.
\]
Therefore any ball containing the contact points—and a fortiori containing the whole polytope—must have squared radius at least \(R^2+\lVert z-c\rVert_2^2\). The previously exhibited ball attains \(R^2\), and equality forces \(z=c\). Thus the minimum enclosing ball is unique for every allowed \(d,t\).

**4. Diameter and its complete equality cases.** Every diameter of a polytope is realized by a pair of vertices because squared Euclidean distance is convex in each argument. Partition the vertices as \(O=\{0\}\), \(U=\{e_1,e_2\}\), \(V=\{e_j:3\le j\le d\}\), \(U'=\{e_1+tv,e_2+tv\}\), and \(V'=\{e_j+tv:3\le j\le d\}\). Directly subtracting the coordinate vectors gives the following upper bounds for squared distances between distinct vertices in each pair of types:

| Types | Upper bound for squared distance |
|---|---:|
| \(O,U\) or \(O,V\) | \(1\) |
| \(O,U'\) | \(2t^2+2t+1\) |
| \(O,V'\) | \(2t^2+1\) |
| \(U,U\), \(U,V\), \(V,V\), \(U',U'\), \(U',V'\), \(V',V'\) | \(2\) |
| \(U,U'\) | \(2t^2+2\) |
| \(U,V'\) | \(2t^2-2t+2\) |
| \(V,V'\) | \(2t^2+2\) |
| \(V,U'\) | \(2t^2+2t+2\) |

A pair type with fewer than two members has no within-type pair; this does not affect the inequalities. Every bound except the final one is **strictly below** \(2t^2+2t+2\) for \(t>0\). Every cross-type pair in \(V\times U'\) attains the final bound, since
\[\lVert e_j-(e_i+tv)\rVert_2^2=(t+1)^2+t^2+1=2t^2+2t+2.\]
This proves both the exact diameter and the exhaustive pair classification, giving the graph \(K_{2,m}\) plus isolated vertices.

## Verification

A standalone standard-library-only verifier, `check_pentasm.py`, uses exact rational arithmetic. It checked \(220\) parameter instances: every integer \(3\le d\le24\) and ten positive rational values of \(t\), including \(1/29\), \(1\), \(13/5\), and \(57\). It executed \(110220\) exact endpoint/distance comparisons, checked every squared clearance and the barycentric certificate, and exhaustively enumerated all vertex pairs against the asserted diametral set. A second implementation using a convex-hull library verified the \(2d+1\)-vertex census for \(d=3,4,5,6,7\) and \(t=1/5,1,17/10\), totaling \(15\) configurations. Both passed.

The formulas for general real \(t>0\) and arbitrary integer \(d\ge3\) follow from the algebraic proof above, *not* from these finite tests. The exact checker requires only Python 3 and its standard library; run `python check_pentasm.py` from a directory containing the file.

## Relationship to prior work

Wang and Yost [1], first public on November 5, 2026, extend classification results for decomposable polytopes with few vertices and identify pentasms among the relevant segment-sum families. Pineda-Villavicencio, Ugon, and Yost [2] previously defined pentasms as a simplex plus a segment and determined extremal face-count properties. Those works supply the natural polytope object and its combinatorial significance; neither of their inspected discussions establishes the Euclidean enclosing-sphere and diameter classification proved here. General smallest-ball algorithms, such as those discussed in [3], are standard background and not asserted to be new. The originality asserted here is restricted to the **specific all-dimensional, positive-parameter metric formulas and complete equality classifications**, not the existence of minimum balls or pentasm combinatorics.

## Limitations

The result is specific to the **orthonormal-coordinate family** with displacement parallel to \(e_1+e_2\); it does not classify Euclidean metrics for arbitrary affine deformations, general segment directions, or other few-vertex decomposable polytopes. The boundary \(t=0\) is excluded and has a different vertex structure. Although exact symbolic reasoning proves the claim, historical priority remains provisional: alternate terminology or an unpublished general formula for simplex-plus-segment minimum balls might imply it. There has been no independent audit.

## References

1. Jie Wang and David Yost, *Decomposable polytopes with few vertices*, arXiv:2611.07472v1 (first posted November 5, 2026), https://arxiv.org/abs/2611.07472.
2. Guillermo Pineda-Villavicencio, Julien Ugon, and David Yost, *Lower bound theorems for general polytopes*, arXiv:1509.08218 (first posted September 28, 2015), published in *European Journal of Combinatorics* **79** (2019), 27–45, https://arxiv.org/abs/1509.08218.
3. Michael N. Vrahatis, *Towards the methodology for solving the minimum enclosing ball and related problems*, arXiv:2410.11063 (2024), https://arxiv.org/abs/2410.11063.
