# Sharp Euclidean contact screening in two-part composition polytopes

## Finding

For every pair of positive integers \(p,q\), put \(n=p+q\) and consider the two-part composition polytope
\[
Q_{p,q}=\left\{x\in\mathbb R_{\ge0}^{n}:\ 
\sum_{i=1}^{p}x_i\le p,\quad \sum_{i=1}^{n}x_i\le n\right\}.
\]
Its unique smallest enclosing Euclidean ball, its exact radius, and **all** contact points are as follows. Set
\[
K=p^2+3pq+q^2,\quad F=(q-2)(p+q)^2-qp^2,\quad
\alpha=\max\left\{0,-\frac{F}{2K}\right\},\quad
\beta=\frac{n(1-\alpha)}q.
\]
The unique center is \(c=(\alpha\mathbf1_p,\beta\mathbf1_q)\) and the squared radius is
\[
\boxed{R^2=\frac{n^2(q-1)}q+\frac Kq\alpha^2.}
\]
All \(q\) vertices \(B_j=ne_{p+j}\) contact this sphere. The \(p\) vertices \(A_i=pe_i\) contact it exactly when \(F<0\). The origin additionally contacts it exactly when \(p=q=1\). No other point of the polytope contacts the sphere; in particular none of the \(pq\) mixed vertices \(C_{ij}=pe_i+qe_{p+j}\) does.

There is **no integer boundary case** \(F=0\). For \(q=1,2\), always \(F<0\). For \(q\ge3\), the two-orbit contact regime occurs precisely when
\[
\boxed{p>p_*(q):=\frac q2\left(q-2+\sqrt{q(q-2)}\right)};
\]
when \(p<p_*(q)\), only the final-block vertices contact the sphere. The threshold is irrational for all integral \(q\ge3\). Hence the number of contacts is \(p+q+\mathbf1_{(p,q)=(1,1)}\) on the first side and exactly \(q\) on the second side. Except for \((p,q)=(1,1)\), their affine span changes from dimension \(p+q-1\) to dimension \(q-1\).

For example, at \(p=10\), the case \(q=4\) has fourteen contacts, center blocks \(\alpha=1/59\) and \(\beta=203/59\), and squared radius \(8674/59\). Increasing \(q\) to five leaves only five contacts, with center blocks \(0\) and \(3\), and squared radius \(180\).

## Assumptions and scope

All assertions hold for **all positive integers** \(p,q\), using the standard coordinate Euclidean metric in \(\mathbb R^{p+q}\). Each coordinate block has the specified order and scale; arbitrary affine transformations do not preserve the metric statement. A contact point means a point of the **whole polytope**, not merely a combinatorial vertex, at distance exactly \(R\) from \(c\). The polytope has full affine dimension \(p+q\).

## Proof

**1. Exact vertex set.** Besides the origin, the vertices are exactly
\[
A_i=pe_i\ (1\le i\le p),\quad
B_j=ne_{p+j}\ (1\le j\le q),\quad
C_{ij}=pe_i+qe_{p+j}.
\]
To see completeness, write \(s=\sum_{i\le p}x_i\) and \(\theta=s/p\in[0,1]\). For \(0<\theta<1\), the first block is a convex combination of vertices in \(p\Delta_{p-1}\), and the last block, of coordinate sum at most \(n-s=(1-\theta)n+\theta q\), splits between \(n\Delta_q\) at \(\theta=0\) and \(q\Delta_q\) at \(\theta=1\). Here \(\Delta_{p-1}\) denotes the probability simplex on the first \(p\) coordinates, and \(\Delta_q=\operatorname{conv}\{0,e_1,\ldots,e_q\}\) denotes the simplex in the last \(q\) coordinates. More explicitly, with \(x=(u,v)\), define \(u_1=u/\theta\), \(v_0=nv/(n-s)\), and \(v_1=qv/(n-s)\); then \(x=(1-\theta)(0,v_0)+\theta(u_1,v_1)\), with \(v_0\in n\Delta_q\) and \((u_1,v_1)\in(p\Delta_{p-1})\times(q\Delta_q)\). Endpoint values follow directly. The four listed types are all extreme by the nonnegative coordinate supports and the equality faces for the two sum bounds.

**2. Four squared-distance classes.** For a block-constant candidate center \(c=(a\mathbf1_p,b\mathbf1_q)\), put \(D_0=pa^2+qb^2\). Squared distances to the four vertex classes are
\[
D_A=D_0+p^2-2pa,\quad D_B=D_0+n^2-2nb,\quad
D_C=D_0+p^2+q^2-2pa-2qb,\quad D_0.
\]
The proposed \(a=\alpha\), \(b=\beta=n(1-a)/q\) makes \(D_B=n^2(q-1)/q+(K/q)a^2=R^2\). With \(a_0=-F/(2K)\), direct simplification gives
\[
D_A-D_B=\frac{2K}{q}(a_0-a),\qquad
D_B-D_C=2p(q+a-b).
\]
For \(F<0\), \(a=a_0>0\), and
\[
1-a_0=\frac{q(2pq+2p+q^2)}{2K}>0,\qquad
b-a-q=-\frac{q(pq+2p+2q)}{2K}<0.
\]
Hence \(D_A=D_B>D_C\). For \(F>0\), \(a=0\), \(D_A<D_B\). This latter case requires \(q\ge3\) and \(p<q(q-1)\): indeed \(F=-2p^2+2q(q-2)p+q^2(q-2)\) has a single positive root and \(F(q(q-1))=-q^3<0\). Thus \(b=n/q<q\), so \(D_C<D_B\) also in this case.

It remains to screen the origin. For \(F<0\), substitution yields
\[
D_B-D_0=\frac{pn^2(n-2)}K\ge0,
\]
with equality if and only if \(n=2\), equivalently \((p,q)=(1,1)\). For \(F>0\),
\[
D_B-D_0=n^2(1-2/q)>0,
\]
because \(q\ge3\). The proposed ball therefore contains every listed vertex and hence all of \(Q_{p,q}\), and its exact contact vertices are as claimed.

**3. Minimality and uniqueness.** In the \(F<0\) regime, \(0<a<1\) and
\[
c=\frac{a}{p}\sum_{i=1}^{p}A_i+\frac{1-a}{q}\sum_{j=1}^{q}B_j.
\]
These are strictly positive weights on contacting vertices. In the \(F>0\) regime, \(a=0\) and \(c=q^{-1}\sum_{j=1}^q B_j\). Thus in either regime the center is a probability-weighted barycenter of points on the proposed sphere. For any other center \(z\), the weighted mean squared distance to those points is exactly \(R^2+\|z-c\|^2\). Therefore every enclosing ball centered at \(z\) has squared radius at least that expression. This proves optimality and uniqueness of \(c\). Strict convexity of squared Euclidean norm implies that a nontrivial convex combination of distinct vertices cannot itself contact a sphere containing all those vertices; hence the vertex list is the **entire** contact set.

**4. Arithmetic phase boundary.** For \(q=1,2\), the formula for \(F\) is strictly negative. For \(q\ge3\), expansion gives \(F=-2p^2+2q(q-2)p+q^2(q-2)\), whose unique positive real root is \(p_*(q)\). As \(q(q-2)=(q-1)^2-1\) lies strictly between consecutive integer squares for \(q\ge3\), \(\sqrt{q(q-2)}\) is irrational. Therefore \(F\neq0\) for all positive integer parameters, and the strict phase classification is complete.

The stated affine contact dimensions follow because \(q\) terminal axis vertices span a \((q-1)\)-simplex, while all \(A_i,B_j\) together span an \((p+q-1)\)-dimensional simplex. The exceptional origin at \((1,1)\) is not in their affine line.

## Verification

The included `check_two_part.py` uses only the Python standard library. It reconstructs the true H-representation vertices by exact rational Gaussian elimination in 26 small instances, then tests the proposed formulas and equality classes for every integer pair \(1\le p,q\le80\) (6,400 pairs). It executes 40,131 exact assertions and compares all individual vertex distances in 1,639 additional instances of vertices in low dimension. Its results were checked against the closed algebraic identities above. Run `python3 check_two_part.py` in the directory containing this document and the checker. Finite computations do not prove the universal claim; the preceding proof does.

## Relationship to prior work

The composition polytopes, their coordinate inequalities, their combinatorial product-of-simplices type and their lattice/Ehrhart properties predate this note. In particular, Athanasiadis (2025 preprint; 2026 journal article) studies their lattice-point enumeration and gamma-positivity; Chapoton introduced the encompassing arbor polytopes; Pitman and Stanley developed a more general family containing the composition polytopes. None of those results implies the metric contact equations merely from combinatorial equivalence: the exact center/radius and sharp equality cases depend on the fixed standard-Euclidean embedding. Related Euclidean sphere results for parking-function polytopes and for partial permutohedra treat other vertex configurations, not the two-part composition constraints. Standard minimum-enclosing-ball barycenter certificates are used, not claimed to be new.

## Limitations

The theorem concerns only length-two compositions and the standard Euclidean metric. It makes no claim about optimal enclosing ellipsoids, arbitrary numbers of composition parts or affine-invariant geometry. Published priority is assessed against identified sources, not independently certified; an unindexed equivalent formulation remains possible. Exact rational testing corroborates but does not certify all infinite parameters. Independent mathematical audit has not been performed.

## References

- Christos A. Athanasiadis, *Lattice point enumeration of polytopes associated to integer compositions*, arXiv:2510.23903 (first public 2025-10-27), *Annals of Combinatorics* (2026), DOI: 10.1007/s00026-026-00812-2.
- Frédéric Chapoton, *On posets and polytopes attached to arbors*, arXiv:2503.04247 (2025).
- Jim Pitman and Richard P. Stanley, *A polytope related to empirical distributions, plane trees, parking functions, and the associahedron*, *Discrete & Computational Geometry* 27 (2002), 603–634.
