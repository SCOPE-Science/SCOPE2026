# Graph-independent outer spheres and cubical contact rigidity for regular-rim discotopes

## Finding

Let \(n\ge4\), and let \(H\) be **any simple \(d\)-regular graph** on the labeled vertex set \(\{1,\ldots,n\}\), where \(1\le d\le n-2\). Connectedness and vertex transitivity of \(H\) are **not** assumed. Let \(G\) be its graph cone: join a new hub vertex \(0\) to every rim vertex. For each graph edge \(\{i,j\}\), let \(D_{ij}=\{s e_i+t e_j:s^2+t^2\le1\}\) be the filled unit disk in that coordinate plane, and define the standard Euclidean graphical discotope
\[
K_G=\sum_{\{i,j\}\in E(G)} D_{ij}\subset\mathbb R^{n+1}.
\]

**Theorem (outer-sphere invariance).** The unique minimum enclosing Euclidean ball of \(K_G\) is centered at the origin and has squared radius
\[
\boxed{R_{n,d}^2=n^2\left(1+\frac{d^2}{2(n-1)}\right).}
\]
Its **entire** sphere-contact set is the following signed rectangular cubical constellation:
\[
\boxed{K_G\cap R_{n,d}S^n
=\left\{\left(\varepsilon_0 n\sqrt{1-\frac{d^2}{2(n-1)^2}},
\frac{nd}{\sqrt2(n-1)}(\varepsilon_1,\ldots,\varepsilon_n)\right):
\varepsilon_i\in\{-1,1\}\right\}.}
\]
There are exactly \(2^{n+1}\) contacts. The Euclidean diameter is \(2R_{n,d}\), and all diametral pairs are the \(2^n\) antipodal pairs of these contacts. In particular, *both the outer radius and the actual coordinate positions of every contact* are independent of the arrangement of rim edges: **any two nonisomorphic regular rim graphs with the same \(n,d\) yield exactly the same outer-sphere contact set**, not merely isometric contact configurations.

**Converse rigidity.** For an arbitrary finite simple rim graph \(H\), if an outer-support maximizing unit normal for the cone discotope has nonzero hub coordinate and rim coordinates all of the same strictly positive absolute value, then \(H\) is regular. Thus the flat-rim extremal support pattern characterizes regularity without any transitivity hypothesis.

## Assumptions and scope

All Euclidean distances use the fixed standard coordinate metric, not a graph metric and not an arbitrary affine transform. Each summand is a **filled, radius-one coordinate-plane disk**, not a segment or a coordinate diamond. The formula for the graph-independent contact set requires \(n\ge4\) and positive rim degree \(1\le d\le n-2\); the upper bound excludes the already-regular complete-cone graph, although its formulas follow by the same argument. The graph cone is connected and nonregular, and has a triangle, whenever the stated hypotheses hold. The rim graph itself may be disconnected. The converse is conditional on a maximizing normal with all indicated coordinates nonzero; it makes no assertion about other maximizers for irregular rim graphs.

## Proof

**1. Exact support and a universal two-class bound.** For a unit vector \(u=(u_0,u_1,\ldots,u_n)\), write \(x_i=u_i^2\), so \(x_i\ge0\) and \(\sum_{i=0}^n x_i=1\). Support-function additivity for filled coordinate disks gives
\[
h_{K_G}(u)=\sum_{i=1}^n\sqrt{x_0+x_i}
+\sum_{\{i,j\}\in E(H)}\sqrt{x_i+x_j}.
\tag{1}
\]
Set \(b=n^{-1}\sum_{i=1}^n x_i\) and \(a=x_0=1-nb\), where \(0\le b\le1/n\). The strict concavity of the square root and Jensen's inequality on the \(n\) hub edges yield
\[
\sum_i\sqrt{a+x_i}\le n\sqrt{a+b}=n\sqrt{1-(n-1)b}.
\tag{2}
\]
Since \(H\) is \(d\)-regular, it has \(nd/2\) edges and \(\sum_{\{i,j\}\in E(H)}(x_i+x_j)=dnb\). Jensen on its rim edges yields
\[
\sum_{\{i,j\}\in E(H)}\sqrt{x_i+x_j}
\le\frac{nd}{2}\sqrt{2b}=\frac{nd}{\sqrt2}\sqrt b.
\tag{3}
\]
Both inequalities are equalities when all rim squares equal \(b\). Therefore maximizing \(h_{K_G}\) over *all* unit directions is **exactly** maximizing
\[
F(b)=n\left(\sqrt{1-(n-1)b}+\frac d{\sqrt2}\sqrt b\right),
\qquad 0\le b\le1/n.
\tag{4}
\]

**2. Exact maximizer and strict equality case.** Let \(t=\sqrt{(n-1)b}\) and \(c=d/\sqrt{2(n-1)}\). The objective becomes
\[
F(b)=n\left(\sqrt{1-t^2}+ct\right),
\qquad 0\le t\le\sqrt{(n-1)/n}.
\tag{5}
\]
By planar Cauchy–Schwarz it is at most \(n\sqrt{1+c^2}\), with unique maximizer \(t=c/\sqrt{1+c^2}\). This point is strictly inside the permitted interval because \(d\le n-2\) implies \(d^2<2(n-1)^2\). Explicitly,
\[
b_*=\frac{d^2}{(n-1)(d^2+2(n-1))},\qquad
a_*=1-nb_*=\frac{2(n-1)^2-d^2}{(n-1)(d^2+2(n-1))}>0.
\tag{6}
\]
Consequently \(\max_{\|u\|=1}h_{K_G}(u)=R_{n,d}\) with the displayed squared radius. In (2), strict concavity forces \(x_1=\cdots=x_n=b_*\) at **every** maximizing unit direction. Conversely, for every independent choice of signs \(\varepsilon_i\in\{-1,1\}\), the unit vector
\[
u_\varepsilon=(\varepsilon_0\sqrt{a_*},\varepsilon_1\sqrt{b_*},\ldots,\varepsilon_n\sqrt{b_*})
\tag{7}
\]
achieves equality in (2)–(5). Thus (7) is a complete classification of maximizing unit normals, and there are precisely \(2^{n+1}\) of them.

**3. Exact contacts, with no hidden arcs or faces.** At any vector (7), the orthogonal projection onto every constituent disk's plane is nonzero; each disk therefore has a **unique** supporting point, namely that normalized projection. Summing exposed points produces
\[
z_0=\varepsilon_0\,n\sqrt{\frac{a_*}{a_*+b_*}},\qquad
z_i=\varepsilon_i\left(\frac d{\sqrt2}+\sqrt{\frac{b_*}{a_*+b_*}}\right)\quad(1\le i\le n).
\tag{8}
\]
The ratios simplify to
\[
\frac{b_*}{a_*+b_*}=\frac{d^2}{2(n-1)^2},
\qquad \frac{a_*}{a_*+b_*}=1-\frac{d^2}{2(n-1)^2},
\tag{9}
\]
which gives the claimed contact coordinates. Direct substitution shows \(\|z\|_2^2=R_{n,d}^2\) and \(z=R_{n,d}u_\varepsilon\).

For any compact convex body \(K\), \(\max_{z\in K}\|z\|_2=\max_{\|u\|_2=1}h_K(u)\). Hence \(R_{n,d}\) is its exact origin-centered outer radius. If an arbitrary point \(z\in K_G\) lies on this sphere, then its normal \(u=z/R_{n,d}\) satisfies \(h(u)\ge u\cdot z=R_{n,d}\), hence \(h(u)=R_{n,d}\). Section 2 forces \(u=u_\varepsilon\), and its unique exposed point is (8). Therefore the displayed \(2^{n+1}\) points exhaust the contact set. Their coordinates are all nonzero, so they are distinct.

As \(K_G\) is centrally symmetric, each listed contact comes with its negative. Any Euclidean ball containing this antipodal pair has radius at least \(R_{n,d}\); equality forces its center to be their midpoint \(0\). Thus the enclosing ball is unique. Moreover, \(\|p-q\|_2\le\|p\|_2+\|q\|_2\le2R_{n,d}\), and equality holds exactly for antipodal outer contacts, establishing the complete diametral-pair classification.

**4. Converse: a uniform extremal rim forces regularity.** Now take an arbitrary simple \(H\), not assumed regular, and suppose a maximizing unit normal has \(x_0=a>0\) and \(x_i=b>0\) for every rim vertex. In the positive interior of the simplex \(\sum_{i=0}^n x_i=1\), the right-hand side of (1) is differentiable. Its partial derivative with respect to a rim variable, evaluated at this point, is
\[
\frac{\partial h}{\partial x_i}
=\frac{1}{2\sqrt{a+b}}+\frac{\deg_H(i)}{2\sqrt{2b}}.
\tag{10}
\]
At an interior constrained maximum all rim partial derivatives agree (vary one rim variable upward and another downward while fixing \(a\)). Equation (10) therefore implies \(\deg_H(i)=\deg_H(j)\) for every \(i,j\), so \(H\) is regular. This converse does not require or assert uniqueness of outer support for irregular graphs.

## Verification

The standalone Python 3 standard-library script `verify.py` constructs 32 valid regular rim graphs, including both cycles and disconnected unions of cycles, and performs 8,000 independently generated unit-direction support checks together with all 28,032 explicit sign-pattern contact checks across its tested cases. It also verifies the claimed radius and contact-coordinate identities using exact rational arithmetic before numerical substitution. Invocation: `python verify.py`. The observed output is:

`REGULAR_CONE_DISCOTOPE_PASS graph_cases=32 random_support_checks=8000 explicit_contacts=28032`

These computations are **finite corroboration**, not a proof that untested graphs satisfy the theorem. The all-dimensional claims follow from (1)–(10); the script also directly reconstructs exposed points from the disks instead of trusting the proposed contact coordinates.

## Relationship to prior work

Gesmundo and Meroni's *The Geometry of Discotopes* (arXiv:2111.01241, first public version 1 November 2021), notably Sections 2–3, establishes the Minkowski-sum class and studies exposed faces and algebraic boundary geometry, but not the circumsphere and contact set of graph cones with regular rims. Mathis and Meroni's *Fiber Convex Bodies* (arXiv:2105.12406, first submitted 26 May 2021), Sections 1 and 5, studies a different operation on related disk sums.

A subsequent classification of regular graphical discotopes determines their Euclidean extremal ellipsoids and sphere-contact topology. Its regularity hypothesis applies to the **entire graph**: in the present theorem, the apex degree is \(n\), whereas every rim degree is \(d+1<n\), so these graph cones are nonregular. Another classification handles Löwner ellipsoids of biregular bipartite graphical discotopes; the present cones have triangles and are not bipartite. A prior weighted complete-split discotope calculation concerns cliques joined to independent vertex classes, not arbitrary regular rim graphs. Graphical zonotope cone formulas concern *line-segment* summands and cannot be used for disk sums. The present result is therefore a distinct complete description of a nonregular family's **outer Euclidean sphere and all contacts**, plus its converse degree-rigidity criterion.

## Limitations

No minimal-volume enclosing ellipsoid, maximal inscribed ellipsoid, full boundary classification, or volume of these cone discotopes is claimed. The graph-independent outer geometry is specific to **unit disk sums** and regular rim graphs; arbitrary edge weights or irregular rims are not covered by the formula. The converse only rules out uniform-rim maximizing normals for irregular rims; it does not classify their maximal directions. Although the cited work and related indexed results were compared by implication, an unindexed equivalent formulation in wider zonoid theory cannot be ruled out. Independent mathematical audit has not been performed.

## References

1. F. Gesmundo and C. Meroni, *The Geometry of Discotopes*, arXiv:2111.01241, first public 2021-11-01. https://arxiv.org/abs/2111.01241
2. L. Mathis and C. Meroni, *Fiber Convex Bodies*, arXiv:2105.12406, first public 2021-05-26. https://arxiv.org/abs/2105.12406
3. *Spherical extremal ellipsoids and bipartite outer-contact topology of regular graphical discotopes*, published result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-spherical-extremal-ellipsoids-and-bipartite-outer-contact-topolo--29a07695a757
4. *Degree-ellipsoid rigidity and complete contact graphs of bipartite graphical discotopes*, published result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-degree-ellipsoid-rigidity-and-complete-contact-graphs-of-biparti--5cadf5d3fdbb
5. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed., 2014, background on support functions.
