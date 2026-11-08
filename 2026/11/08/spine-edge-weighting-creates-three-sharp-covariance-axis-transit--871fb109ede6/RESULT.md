# Spine-edge weighting creates three sharp covariance-axis transitions in book-graph zonotopes

## Finding
Let \(q\ge2\) be an integer and \(t\ge0\) be real. The centered edge-weighted graphical zonotope of the triangular book graph with \(q\) pages, spine weight \(t\), and unit page edges has an exact uniform-volume covariance spectrum. Write
\[
D=t+\frac q2,\qquad
c_j=\frac{e_A+e_B}{2}-e_j,\qquad
d=e_A-e_B.
\]
For a uniform intrinsic-volume point \(X\) in the zonotope,
\[
\boxed{\operatorname{Cov}(X)=a\sum_{j=1}^q c_jc_j^{\mathsf T}+b dd^{\mathsf T}},\qquad
\boxed{a=\frac{4t+2q-1}{12t+6q}},
\]
\[
\boxed{b=\frac{t^3+\frac32 qt^2+\frac14q(3q+1)t+\frac18q^2(q+1)}{12D}}.
\]
The exact intrinsic Euclidean volume and covariance eigenvalues are
\[
\boxed{\operatorname{Vol}_{q+1}=2^q D\sqrt{q+2}},\qquad
\boxed{\lambda_{\mathrm{leaf}}=a\ \ (q-1\text{ times}),\quad
\lambda_{\mathrm{collective}}=\frac{q+2}{2}a,\quad
\lambda_{\mathrm{hub}}=2b.}
\]
The leaf-contrast eigenvalue is always strictly smaller than the collective eigenvalue. Put
\[
F_q(t)=4t^3+6qt^2+(3q^2-3q-8)t+\frac{q^3-3q^2-6q+4}{2}.
\]
Then the exact competition is
\[
\boxed{\lambda_{\mathrm{hub}}-\lambda_{\mathrm{collective}}
=\frac{F_q(t)}{24D}.}
\]
For each \(q\in\{2,3,4\}\) the cubic \(F_q\) has exactly one positive root \(t_q\). For \(t<t_q\) the unique principal direction is the aggregate hub-versus-leaf axis; for \(t>t_q\) it is the hub-difference axis; at equality the top eigenspace is two-dimensional. The three thresholds are
\[
t_2=\frac1{\sqrt2},\qquad t_3\approx0.3948095099,\qquad t_4\approx0.0674814602.
\]
For \(q\ge5\), \(F_q(t)>0\) for every \(t\ge0\), so the hub-difference axis is the unique principal direction throughout. **In particular**, the ordinary triangular book graphical zonotope, with unit spine weight \(t=1\), always has the hub-difference principal axis for every \(q\ge2\). The unit-spine variance parameters simplify to
\[
a=\frac{2q+3}{6(q+2)},\quad b=\frac{(q+1)(q+4)}{48},\quad
\operatorname{Vol}_{q+1}=2^{q-1}(q+2)^{3/2}.
\]

## Assumptions and scope
The graph has hubs \(A,B\), leaves \(j=1,\ldots,q\), and edges \(\{A,j\}\), \(\{B,j\}\), and \(\{A,B\}\). We assign weight one to each page edge and nonnegative weight \(t\) to the spine. With the standard Euclidean basis of \(\mathbb R^{q+2}\), define precisely
\[
Z_{q,t}=\sum_{j=1}^q\left(
[-(e_A-e_j)/2,(e_A-e_j)/2]+[-(e_B-e_j)/2,(e_B-e_j)/2]\right)
+[-t(e_A-e_B)/2,t(e_A-e_B)/2].
\]
At \(t=0\) the last segment is the origin and the graph effectively is \(K_{2,q}\). For positive \(t\), the support graph is the complete tripartite graph \(K_{1,1,q}\), also called a triangular book. All covariance matrices, volumes, and principal axes use the intrinsic \((q+1)\)-dimensional Euclidean structure of the zero-sum hyperplane, with points drawn uniformly by volume. The covariance is that of all interior points, not of the finite vertex set and not the pushforward of the uniform distribution on the coefficient cube.

## Proof
**1. Exact fibers and Euclidean Jacobian.** Write the two page-edge coefficients as \(\alpha_j,\beta_j\in[-1/2,1/2]\), and the spine coefficient as \(\gamma\in[-t/2,t/2]\). Set
\[
s_j=\alpha_j+\beta_j,\qquad \delta_j=\alpha_j-\beta_j,\qquad h=\frac12\sum_j\delta_j+\gamma.
\]
Every zonotope point is \(x=\sum_j s_jc_j+hd\). Since \(s_j\in[-1,1]\), the exact coefficient constraints at fixed \(s_j\) are \(|\delta_j|\le 1-|s_j|\). The Minkowski sum of these centered scalar intervals and the spine interval gives the **entire** fiber
\[
-\frac{\ell(s)}2\le h\le\frac{\ell(s)}2,\qquad
\ell(s)=t+\sum_{j=1}^q(1-|s_j|).
\]
This is a one-to-one parametrization of \(Z_{q,t}\) up to a null boundary set: the leaf coordinates of \(x\) equal \(-s_j\), so \(s\) and then \(h\) are recovered uniquely. The vectors \(c_j\) have Gram matrix \(I_q+J_q/2\), are orthogonal to \(d\), and \(\|d\|^2=2\). Hence the Jacobian is
\[
\sqrt{\det(I_q+J_q/2)\,\|d\|^2}=\sqrt{q+2}.
\]
In particular, writing expectation under independent uniform \(S_j\in[-1,1]\) as \(\mathbb E_0\),
\[
\operatorname{Vol}_{q+1}(Z_{q,t})=2^q\sqrt{q+2}\,\mathbb E_0\ell(S)
=2^q\sqrt{q+2}\left(t+\frac q2\right).
\]

**2. Uniform-volume covariance, not cube-pushforward covariance.** Under the uniform-volume law, the joint density of \(s\) is proportional to \(\ell(s)\). Conditional on \(s\), the variable \(h\) is uniform on its symmetric interval, so \(\mathbb E(h\mid s)=0\) and \(\mathbb E(h^2\mid s)=\ell(s)^2/12\). Signed-coordinate symmetries give \(\mathbb E s_j=0\), \(\mathbb E s_is_j=0\) when \(i\ne j\), and \(\mathbb E s_jh=0\). For \(S\) uniform on \([-1,1]\),
\[
\mathbb E S^2=\frac13,\qquad \mathbb E(1-|S|)=\frac12,\qquad
\mathbb E[S^2(1-|S|)]=\frac1{12}.
\]
Thus
\[
\mathbb E_0[S_j^2\ell(S)]=\frac t3+\frac{2q-1}{12},
\quad
\frac{\mathbb E_0[S_j^2\ell(S)]}{\mathbb E_0\ell(S)}=a.
\]
For \(V_j=1-|S_j|\), the variables \(V_j\) are independent uniforms on \([0,1]\). Let \(Y=\sum_jV_j\). Elementary expansions give
\[
\mathbb E Y=\frac q2,\qquad
\mathbb E Y^2=\frac{q(3q+1)}{12},\qquad
\mathbb E Y^3=\frac{q^2(q+1)}8.
\]
It follows that
\[
\mathbb E_0\ell(S)^3=t^3+\frac{3q}2t^2
+\frac{q(3q+1)}4t+\frac{q^2(q+1)}8.
\]
Since the uniform-volume expectation \(\mathbb E h^2\) equals \(\mathbb E_0\ell^3/(12\mathbb E_0\ell)\), this is precisely \(b\). The asserted tensor identity now follows by expanding \(x=\sum_j s_jc_j+hd\), with no omitted cross terms.

**3. Complete spectral decomposition.** On \(\operatorname{span}\{c_j\}\), the operator \(\sum c_jc_j^{\mathsf T}\) has eigenvalue one on the \((q-1)\)-dimensional leaf-contrast subspace and eigenvalue \((q+2)/2\) on the line spanned by \(\sum_j c_j\). The perpendicular hub-difference line is spanned by \(d\) and has eigenvalue \(2b\). The collective eigenvalue is larger than the leaf-contrast eigenvalue because \(q\ge2\) and \(a>0\).

**4. Sharp phase diagram.** Direct common-denominator algebra gives
\[
2b-\frac{q+2}{2}a=\frac{F_q(t)}{24(t+q/2)}.
\]
For \(q=2\), \(F_2(t)=2(t+3)(2t^2-1)\), giving \(t_2=1/\sqrt2\). For \(q=3,4\), the coefficients of \(t\), \(t^2\), and \(t^3\) in \(F_q\) are strictly positive, while \(F_q(0)<0\); hence exactly one positive root exists and the sign changes there. For \(q\ge5\), both the constant coefficient and all positive-degree coefficients are positive, hence \(F_q(t)>0\) for all \(t\ge0\). Direct substitution shows \(F_q(1)>0\) for \(q=2,3,4\), and the remaining dimensions were already handled. This proves the full phase diagram and unit-edge corollary.

## Verification
The self-contained `verify.py` uses exact rational three-point tensor cubature on \([0,1]^q\), separately recomputes the width-weighted second and third moments for 36 parameter profiles, checks the rational eigenvalue crossing identity and positivity through 299 page counts, and optionally integrates the actual convex hull in dimensions three and four using SciPy. The latter independent Euclidean hull computation checked eight parameter profiles with spine weights including zero and two. Both checks returned `BOOK_GRAPH_ZONOTOPE_CHECKS_PASSED`. The all-parameter statements rely on the explicit fiber geometry and polynomial sign argument, not on finite enumeration.

## Relationship to prior work
Padrol, Pilaud, and Poullot [1] give the standard graphical zonotope and develop its deformation cones, normal fans, and combinatorial structure; their full arXiv HTML, including Sections 1.3 and 2, concerns those objects and does not compute the uniform interior covariance of this weighted triangular-book family. Chapoton and Pilaud [2] define graph-join shuffles (the graph-join viewpoint explains the natural complete tripartite unit-weight endpoint); their available abstract establishes face and Minkowski descriptions rather than the present interior covariance phase diagram. Grujić [3] counts faces of graphical zonotopes, a different invariant.

The unweighted bipartite endpoint \(t=0\) has an existing exact covariance formula and a discrete page-count transition at five pages; those pre-existing results are **not** asserted to be novel here. The new assertion is the complete continuous spine-weight parameter dependence, the three nontrivial positive transition weights and the fact that the actual triangular-book family at \(t=1\) is already in the hub-axis regime for every \(q\ge2\). Closest identified published mathematical results give complete multipartite **circumspheres**, complete bipartite **minimum enclosing ellipsoids**, and arbitrary weighted graphical zonotope **inradii**, none of which implies the uniform-volume covariance or the three sharp parameter crossings [4–6].

## Limitations
The theorem is specific to uniform page weights and a single spine weight. It does not give the covariance of arbitrary complete multipartite zonotopes or arbitrary independent edge weights. No equivalence from the full matrix formula for arbitrary graphs is claimed. Exact mathematical formulas do not establish historical priority; unindexed volume-moment identities for cube projections or thagomizer zonotopes may exist. The numerical hull integration is deliberately limited to stable low-dimensional cases, and the exact all-dimensional proof is independent of it. No independent external validation has been carried out.

## References
[1] A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422v1, first public 2021-11-24; HTML arXiv:2111.12422v2, https://arxiv.org/html/2111.12422v2.
[2] F. Chapoton, V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896v1, first public 2022-01-18, https://arxiv.org/abs/2201.06896.
[3] V. Grujić, *Counting faces of graphical zonotopes*, arXiv:1604.06931, https://arxiv.org/abs/1604.06931.
[4] *Complete multipartite graphical zonotopes have cubic-moment circumspheres*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-multipartite-graphical-zonotopes-have-cubic-moment-circ--2fc427ff213b.
[5] *Exact Löwner ellipsoid and contact vertices of complete-bipartite graphical zonotopes*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-l-wner-ellipsoid-and-contact-vertices-of-complete-bipartit--3af21ae2f6c8.
[6] *Euclidean inradius of weighted graphical zonotopes is a cut expansion constant*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-euclidean-inradius-of-weighted-graphical-zonotopes-is-a-cut-expa--cb1eceb082ab.
