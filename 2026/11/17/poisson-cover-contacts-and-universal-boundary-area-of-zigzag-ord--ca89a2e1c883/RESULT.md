# Poisson cover contacts and universal boundary area of zigzag order polytopes

## Finding
Let \(Z_n\) be the fence poset on \(z_1,\ldots,z_n\), with covers \(z_1>z_2<z_3>z_4<\cdots\). Write \(P_n\subset\mathbb R^n\) for its standard Euclidean order polytope, with \(0\le x_i\le1\) and \(x_i\ge x_{i+1}\) for odd \(i\), \(x_i\le x_{i+1}\) for even \(i\). Given a uniformly chosen linear extension \(L_n\), let \(X_n\) count those \(n-1\) cover pairs \(\{z_i,z_{i+1}\}\) whose elements occur in consecutive positions in \(L_n\). For every \(n\ge2\):

\[
\mathbb E X_n=1,\qquad
\frac{\operatorname{Area}_{n-1}(\partial P_n)}{\operatorname{Vol}_n(P_n)}=n(2+\sqrt2).
\]

Moreover, for every fixed nonnegative integer \(k\), the falling-factorial moments satisfy
\[
\lim_{n\to\infty}\mathbb E[(X_n)_k]=1,
\qquad X_n\xrightarrow{\mathrm d}\operatorname{Poisson}(1).
\]
Here \((x)_k=x(x-1)\cdots(x-k+1)\) and \((x)_0=1\). Equivalently, \(\Pr(X_n=j)\to e^{-1}/j!\) for every fixed integer \(j\ge0\). The exact mean and boundary-area identity extend to the order polytope of *every* nonempty finite height-two poset in which each element lies on a cover, with \(n\) denoting its cardinality. The Poisson assertion is specific to the growing fence family.

## Assumptions and scope
All polytopes use the unscaled standard coordinate Euclidean metric, not normalized lattice area. A linear extension lists elements from minimal to maximal. A cover contact is the event that the endpoints of a specified cover occupy consecutive positions (a *bump*), not the number of neighboring incomparable pairs or a descent statistic of an alternating permutation. If \(e(Q)\) counts the linear extensions of a poset \(Q\), then \(\operatorname{Vol}_n(\mathcal O(Q))=e(Q)/n!\). The statement for general height-two posets assumes no isolated element, including the two-element-chain case. No independence of individual contacts at finite \(n\) is asserted.

## Proof

### 1. Euclidean boundary flux and the exact contact mean
Consider a height-two poset \(Q\) with \(n\ge2\), no isolated elements, minimal set \(B\), maximal set \(T\), and covers \(E\). The full-dimensional order polytope \(\mathcal O(Q)\) has three kinds of facets: \(x_b=0\) for \(b\in B\), \(x_t=1\) for \(t\in T\), and \(x_b=x_t\) for \((b,t)\in E\). Set \(V=\operatorname{Vol}_n(\mathcal O(Q))\).

Use the vector field \(F_i(x)=x_i\) at minimal vertices and \(F_i(x)=x_i-1\) at maximal vertices. Its divergence is \(n\). Its normal flux vanishes on every coordinate facet; on every cover facet the outward unit normal is \((e_b-e_t)/\sqrt2\), and \(F\cdot\nu=1/\sqrt2\). The divergence theorem therefore gives
\[
\sum_{e\in E}\operatorname{Area}_{n-1}(F_e)=\sqrt2\,nV.\tag{1}
\]
A second vector field \(G_i(x)=x_i-1/2\) has divergence \(n\), flux \(1/2\) on each coordinate facet, and zero on every cover facet. Therefore the sum of all coordinate-facet areas is \(2nV\). Adding (1) proves the exact boundary-area formula.

Fix a cover \(e=(b,t)\). Identifying its equal coordinates yields the contracted poset \(Q/e\) on \(n-1\) elements. The induced Euclidean measure on the hyperplane \(x_b=x_t\) is \(\sqrt2\) times standard coordinate Lebesgue measure after omitting the duplicated coordinate. The canonical unimodular triangulation gives
\[
\operatorname{Area}_{n-1}(F_e)=\sqrt2\,\frac{e(Q/e)}{(n-1)!}.
\]
The event that the endpoints of \(e\) occur consecutively in a linear extension of \(Q\) has probability \(e(Q/e)/e(Q)\), since contracting and subsequently expanding the oriented adjacent pair is a bijection. Sum this identity over covers and apply (1) and \(V=e(Q)/n!\). The sum of these probabilities is \(1\). In particular, \(\mathbb E X_n=1\) exactly.

### 2. Contact multipoint integrals
On \(L^2([0,1])\) define bounded Volterra operators
\[
(Uf)(t)=\int_0^t f(s)\,ds,\qquad
(Df)(t)=\int_t^1 f(s)\,ds=U^*f(t).
\]
For the fence, integrate its inequalities in the path order. With \(U,D\) alternating and starting with \(U\), one obtains the exactly normalized volume
\[
V_n=\langle\mathbf 1,UDU\cdots\mathbf1\rangle,
\]
where there are \(n-1\) operator factors. Let \(S\subseteq\{1,\ldots,n-1\}\) be a set of edge indices with pairwise disjoint endpoints, equivalently no two consecutive integers in \(S\). Define \(J_n(S)\) by replacing every \(U\) or \(D\) at a position belonging to \(S\) with the identity operator \(I\). The identity is integration against the diagonal delta kernel, so it enforces equality of the corresponding adjacent coordinates and removes one integration variable. All selected pairs are disjoint, and contracted pairs are compatible; the remaining order-polytope triangulation yields
\[
J_n(S)=\frac{e(Z_n/S)}{(n-|S|)!},\qquad
\Pr(S\text{ all contact})=\frac{J_n(S)}{(n)_{|S|}V_n}.\tag{2}
\]
Adjacent cover indices cannot both contact in one linear extension, because the common vertex is respectively below or above *both* other vertices and cannot be immediately next to both in a total order. Thus (2) encompasses every nonzero joint contact event.

### 3. Spectral mixing and a uniform majorant
The positive self-adjoint compact operator \(K=UD\) has integral kernel \(K(t,s)=\min(t,s)\), leading eigenvalue \(\lambda=4/\pi^2\), normalized strictly positive eigenfunction \(\varphi(t)=\sqrt2\sin(\pi t/2)\), and remaining eigenvalues \(\lambda/(2j+1)^2\) for integers \(j\ge1\). Put \(u=2/\pi\). Then \(\|U\|=\|D\|=u\), \(\lambda=u^2\), and
\[
\left\|\lambda^{-h}K^h-\Pi_{\varphi}\right\|\le9^{-h},\qquad
\langle\varphi,U\varphi\rangle
=\langle\varphi,D\varphi\rangle=\lambda.\tag{3}
\]
If \(n=2m+1\), then \(V_n=\langle\mathbf1,K^m\mathbf1\rangle\); if \(n=2m\), then \(V_n=\langle\mathbf1,K^{m-1}U\mathbf1\rangle\). There exists an absolute \(c>0\), for example \(c=1/2\), with \(V_n\ge c u^{n-1}\) for every \(n\ge2\). For odd \(n\), this follows from the top spectral projection: \(\langle\mathbf1,\varphi\rangle^2=8/\pi^2>1/2\). For even \(n\), use positivity of the kernel and the pointwise inequality \(t=(U\mathbf1)(t)\ge(\sqrt2/\pi)\varphi(t)\), giving \(V_n\ge u^n\ge(1/2)u^{n-1}\). By Cauchy–Schwarz and \(\|I\|=1\),
\[
0\le\frac{J_n(S)}{V_n}\le2u^{-|S|}.\tag{4}
\]

For each fixed \(k\), consider \(k\) selected edge positions that are each at least \(2h+2\) from both endpoints and are mutually separated by at least \(2h+2\). Each replacement occurs in a distinct block of the pairing \(UD=K\), separated from all other replacements by at least \(h\) unmodified \(K\)-blocks. A modified block is precisely \(D\) if the removed factor was \(U\), and \(U\) if it was \(D\). Repeated insertion of (3) between blocks gives, uniformly over these well-separated choices as \(n\to\infty\), then \(h\to\infty\),
\[
\frac{J_n(S)}{V_n}=\prod_{a=1}^k
\frac{\langle\varphi,T_a\varphi\rangle}{\lambda}
+O_k(9^{-h})+o_n(1)
=1+O_k(9^{-h})+o_n(1),\tag{5}
\]
where every \(T_a\) is either \(U\) or \(D\). The endpoint spectral coefficients cancel against those of \(V_n\); the remainder is uniform because \(k\) is fixed, all operator norms are bounded, and the top eigenspace of \(K\) is simple. For fixed \(h\), at most \(O_k(hn^{k-1})\) ordered distinct \(k\)-tuples of edge indices violate these separation requirements.

### 4. Factorial moments and the Poisson conclusion
Expand \((X_n)_k\) into ordered distinct contact indicators. Pairs sharing a vertex have zero contribution. For the other tuples, apply (2). There are \(n^k+O_k(n^{k-1})\) ordered admissible tuples. Formula (5) applies to all but \(O_k(hn^{k-1})\) of them, while (4) bounds *every* remaining term. Consequently
\[
\mathbb E[(X_n)_k]
=\frac1{(n)_k}\sum_{(i_1,\ldots,i_k)\,\mathrm{admissible}}
\frac{J_n(\{i_1,\ldots,i_k\})}{V_n}
=1+O_k(9^{-h})+O_k(h/n)+o_n(1).
\]
First let \(n\to\infty\) for fixed \(h\), then \(h\to\infty\). Hence every factorial moment tends to \(1\), exactly the sequence of factorial moments of \(\operatorname{Poisson}(1)\). Standard factorial-moment uniqueness (or ordinary moments and the Poisson moment-generating function) implies convergence in distribution, completing the proof.

## Verification
A standalone exact-integer verifier `CHECK.py` enumerates all linear extensions by memoized order-ideal dynamic programming and records the complete contact-count distribution through \(n=17\). It independently checks that the total count matches Euler zigzag numbers, that the mean contact count is exactly one, and that the probability of zero contacts and variance trend toward their Poisson targets. These finite checks corroborate the derivation but do not substitute for the infinite-dimensional spectral argument. The eigenvalue and inner-product identities in (3) are elementary direct integrations; no numerical spectral certificate is assumed.

## Relationship to prior work
Coons and Sullivant (arXiv:1901.07443, first public 2019-01-22) develop triangulations, Ehrhart numerators and a swap statistic for zigzag order polytopes. Petersen and Zhuang (arXiv:2403.07181, first public 2024-03-11) study zigzag Eulerian polynomials and big returns. Their alternating-permutation statistics concern descents, admissible swaps and big returns, not simultaneous contact events between consecutive *poset labels* in a random linear extension. Abramson (1979) studies runs and prescribed ascent patterns of alternating permutations; these do not directly yield the cover-contact Poisson law. The universal area identity is an auxiliary exact metric connection; the substantive contribution is the Poisson law with its multipoint operator proof. Finite linear-extension tables and the known Euler-number volume formula alone do not imply this law.

## Limitations
The Poisson conclusion concerns the alternating path order only; it is not claimed for arbitrary height-two posets. The mean-one and boundary-area formulas are elementary general identities and are not independently represented as a breakthrough. The proof does not give a sharp total-variation convergence rate or a simultaneous local limit for the locations of contacts. Historical priority is provisional: a statistic phrased as adjacent consecutive values in alternating permutations could be indexed under another name. Independent mathematical review has not been performed.

## References
1. J. I. Coons and S. Sullivant, *The \(h^*\)-polynomial of the order polytope of the zig-zag poset*, arXiv:1901.07443v1 (2019-01-22), https://arxiv.org/abs/1901.07443 .
2. T. K. Petersen and Y. Zhuang, *Zig-zag Eulerian polynomials*, arXiv:2403.07181v1 (2024-03-11), https://arxiv.org/abs/2403.07181 .
3. M. Abramson, *Permutations Related to Secant, Tangent and Eulerian Numbers*, Canadian Mathematical Bulletin 22 (1979), 281–291, https://doi.org/10.4153/CMB-1979-034-9 .
4. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, https://doi.org/10.1007/BF02187680 .
