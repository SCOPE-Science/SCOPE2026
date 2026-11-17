# Euclidean facet shells and incenter parity for three-edge generalized theta spaces \(\Theta_{3,m}\)

## Finding
Let \(m\ge3\) be an integer. Form the graph \(G_m\) from two distinct terminals \(A,B\) joined by \(m\) internally vertex-disjoint paths \(A-u_i-v_i-B\), each having three unit edges. Give the vertex set its shortest-path metric. Let \(K_m\) be the real Lipschitz-free unit ball in the canonical zero-sum Euclidean space
\[
H_m=\left\{x\in\mathbb R^{2m+2}:\sum_{v\in V(G_m)}x_v=0\right\},\qquad
K_m=\operatorname{conv}\{e_v-e_w:\{v,w\}\in E(G_m)\}.
\]
The following completely specifies the multiset of Euclidean distances from the origin to the facets of \(K_m\). For every triple of nonnegative integers \(a,b,c\) with \(a+b+c=m\), include
\[
2\frac{m!}{a!b!c!}\quad\text{copies of}\quad
\left[\frac{m+1}{2}+2(a+c)-\frac{2(c-a)^2}{m+1}\right]^{-1/2}.
\]
Include two further copies of \(\sqrt{2/(m+9)}\). Equal distances from distinct triples are to be combined by adding multiplicities. The total multiplicity is \(2(3^m+1)\), agreeing with the known facet count.

Put \(\varepsilon_m=0\) for even \(m\), and \(\varepsilon_m=1\) for odd \(m\). The exact **global** largest Euclidean ball contained in \(K_m\) has radius
\[
\boxed{\displaystyle \rho_m=\left(\frac{5m+1}{2}-\frac{2\varepsilon_m}{m+1}\right)^{-1/2}.}
\]
The origin is an optimal center. Exactly
\[
\boxed{\displaystyle T_m=\begin{cases}
2\binom{m}{m/2},&m\text{ even},\\[3pt]
4\binom{m}{(m-1)/2},&m\text{ odd}
\end{cases}}
\]
facets are tangent to the origin-centered optimal Euclidean ball. If \(\mathcal C_m\subset H_m\) denotes the **entire** set of centers of balls of radius \(\rho_m\) contained in \(K_m\), then
\[
\boxed{\displaystyle \dim\operatorname{aff}(\mathcal C_m)=
\begin{cases}m+1,&m\text{ even},\\m,&m\text{ odd}.\end{cases}}
\]
In particular, this center is never unique for \(m\ge3\), but the center-locus codimension jumps by one with parity.

## Assumptions and scope
All edges have length one; the number of parallel terminal paths is an integer \(m\ge3\). The graph is simple and connected. The Euclidean structure is the one inherited from the coordinate hyperplane \(H_m\), not an arbitrary Banach-space isomorphism or a John-ellipsoid normalization. Every distance and tangent-facet count concerns the polytope \(K_m\), not its polar. A tangent facet count is for the ball centered at the origin; other maximal-radius centers can acquire additional tangent facets.

For any real function \(f\) on the vertices write \(\bar f=(2m+2)^{-1}\sum_v f(v)\) and \(\widehat f=f-\bar f\mathbf1\). The polar ball of \(K_m\) is the set of edgewise \(1\)-Lipschitz functions modulo constants, with Euclidean facet normal \(\widehat f\). A facet given by \(\langle\widehat f,x\rangle\le1\) lies at Euclidean distance \(1/\|\widehat f\|_2\) from the origin.

## Proof
**1. Full facet enumeration.** A potential \(f\), normalized by \(f(A)=0\), is an extreme point of the polar ball precisely when its tight-edge graph (edges satisfying \(|f(v)-f(w)|=1\)) is connected and spanning. Indeed, a spanning tight tree uniquely fixes all potentials, whereas a disconnected tight graph admits a nonzero sufficiently small componentwise-constant perturbation preserving every strict inequality. Propagation along a tight spanning tree shows that extreme potentials are integer-valued.

The graph \(G_m\) is bipartite. In a connected tight-edge graph, integer potentials have opposite parities on the two bipartition classes. Consequently, **every** original edge has an odd potential difference and hence a saturated difference of absolute value one. This also follows from the established bipartite facet description in the cited literature. Each path therefore has three signed unit gradients, and all path sums coincide with \(f(B)\). They must equal either \(1,-1,3\) or \(-3\).

For \(f(B)=1\), the three possible pairs of internal values \((f(u_i),f(v_i))\) are \((-1,0)\), \((1,0)\), and \((1,2)\), here called \(X,Y,Z\). Every word in these three states defines a facet. The \(f(B)=-1\) facets are their negatives. For \(f(B)=3\), the sole potential has every pair equal to \((1,2)\), and for \(f(B)=-3\) there is its negative. This proves the total count \(2(3^m+1)\), already known from the general facet-count theorem of Braun and Bruegge; it is an input to the Euclidean analysis, not claimed as a new count.

**2. Exact Euclidean shells.** Suppose a word of \(m\) path states has \(a\) copies of \(X\), \(b\) of \(Y\), and \(c\) of \(Z\). Its uncentered coordinate sum is \(m+1+2(c-a)\), and its sum of squares is \(m+1+4c\). Since \(|V(G_m)|=2(m+1)\), subtracting the squared mean gives
\[
\|\widehat f\|_2^2
=\frac{m+1}{2}+2(a+c)-\frac{2(c-a)^2}{m+1}.
\]
There are \(m!/(a!b!c!)\) such words and the same number of negatives. For the terminal difference \(3\), the potential is \((0,3,1,\dots,1,2,\dots,2)\), with centered squared norm \((m+9)/2\), and there is one negative. These observations establish the entire multiset asserted above.

**3. Global radius and contacts.** Put \(h=a+c\le m\). For each fixed \(h\), the squared norm is at most \((m+1)/2+2h\), with equality whenever \(c=a\). If \(h=m\), the smallest possible \(|c-a|\) is \(0\) for even \(m\), and \(1\) for odd \(m\). Therefore the largest squared norm among words with terminal difference \(1\) is
\[
R_m^2=\frac{m+1}{2}+2m-\frac{2\varepsilon_m}{m+1}.
\]
Every word with \(h\le m-1\) has squared norm at most \((m+1)/2+2m-2<R_m^2\), because \(m+1>1\). The exceptional terminal difference \(3\) has squared norm \((m+9)/2<R_m^2\) for all \(m\ge3\), as the difference is \(2m-4-2\varepsilon_m/(m+1)>0\). Thus all maximizing words have \(b=0\) and the two types \(X,Z\) as balanced as possible. Counting the choices gives the displayed \(T_m\).

The facets of \(K_m\) have form \(\langle\widehat f,x\rangle\le1\). Hence the origin-centered inradius is \(1/R_m\). It is also the **globally** largest possible radius: if \(c+\rho B_2^{H_m}\subset K_m\), central symmetry gives \(-c+\rho B_2^{H_m}\subset K_m\), and their Minkowski average gives \(\rho B_2^{H_m}\subset K_m\). This proves the radius formula without presupposing a unique optimal center.

**4. Affine dimension of every optimal center.** Write \(P\) for the orthogonal projection onto \(H_m\), and set \(w_i=P(e_{u_i}+e_{v_i})\). The \(m\) vectors \(w_i\) are linearly independent. Let \(g_0\) be the centered potential with terminal values \(0,1\) and all internal pairs equal to \((1,2)\). For any subset \(S\subseteq\{1,\ldots,m\}\) specifying the paths of type \(X\), the corresponding centered normal is
\[
g_S=g_0-2\sum_{i\in S}w_i.
\]
For each fixed size \(1\le a=|S|\le m-1\), differences of these normals span the \((m-1)\)-dimensional space \(U=\{\sum_i t_iw_i:\sum_i t_i=0\}\). Their span therefore has dimension \(m\): the additional normal is not in \(U\), since its difference between terminal coordinates is \(1\), while every vector in \(U\) has terminal difference zero. If two distinct subset sizes occur, the span dimension increases to \(m+1\), because modulo \(U\) the two normals are \(g_0-(2a/m)\sum_iw_i\) with distinct \(a\), and \(g_0\) is independent of \(\sum_iw_i\) by the terminal difference. Thus contact-normal rank is \(m\) in the even case (one balanced subset size) and \(m+1\) in the odd case (two sizes).

Every optimal center \(c\) must satisfy \(\langle g,c\rangle=0\) for each maximal-norm polar vertex \(g\), because both \(g\) and \(-g\) support facets tangent at the origin. Conversely, all noncontact facet inequalities are strictly slack at \(c=0\); since there are finitely many, a sufficiently small neighborhood of \(0\) inside the common kernel of the contact normals also comprises optimal centers. Thus the affine hull of \(\mathcal C_m\) is exactly that kernel. Its dimension is \((2m+1)-m=m+1\) for even \(m\), or \((2m+1)-(m+1)=m\) for odd \(m\).

## Verification
Run `python3 check_theta_inball.py`. The standalone script uses only Python's standard library and exact rational operations. For \(m=3,4,5\), it independently enumerates all feasible integer potential assignments and checks the connected saturated-edge condition; the resulting \(708\) dual vertices match the expected counts, norms, contact counts and contact-normal ranks. For \(m=3,\ldots,8\), a separate enumeration of all signed full-path potential words checks the exact squared-normal maximizer and contacting-normal rank across \(19,668\) signed possibilities. The computations are **finite corroboration**; the all-integer assertion is proved in the preceding steps.

## Relationship to prior work
Higashitani, Jochemko and Michałek (2018, Theorem 3.1) gave the general tight-edge criterion for symmetric-edge-polytope facets. D'Alì, Delucchi and Michałek (2019, Section 2.3) identified the relationship with Kantorovich–Rubinstein/Lipschitz polytopes. Braun and Bruegge (2022 preprint, Proposition 22 and Corollary 23; journal 2023) obtained the general equal-length theta facet-count formula \(\sum_{j=0}^{3}\binom3j^m=2(3^m+1)\). The present contribution is not a new facet count: it is the exact Euclidean facet-distance multiset, its maximizing shells, the globally optimal radius, and the complete optimal-center affine-dimension parity law in the canonical embedding. The underlying normalization is essential.

## Limitations
This result concerns unit edge lengths, exactly three edges per parallel path and \(m\ge3\), not arbitrary mixed path lengths, edge weights, or other Euclidean models. The facet-distance formula may have coincident shells for different triples; its multiset convention handles their multiplicities. No claim of independent review, historical uniqueness, or a general theta-graph inradius theorem is made. Equivalent formulations through maximum centered Lipschitz variance have not been exhaustively ruled out.

## References
1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, public July 20, 2018, Theorem 3.1. https://arxiv.org/abs/1807.07678
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1, public October 11, 2019, Section 2.3. https://arxiv.org/abs/1910.05193
3. B. Braun, K. Bruegge, *Facets of symmetric edge polytopes for graphs with few edges*, arXiv:2201.13303, first public January 31, 2022, Proposition 22 and Corollary 23; *Journal of Integer Sequences* 26 (2023), 23.7.2. https://arxiv.org/abs/2201.13303
