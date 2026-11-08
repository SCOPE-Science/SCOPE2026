# Simultaneous idempotent spectra of split basic algebras and an inverse random-cluster invariant

## Finding
Let \(A\) be any finite-dimensional unital split basic associative algebra over a field \(k\), with Jacobson radical \(J\) and \(A/J\cong k^n\). Choose a complete orthogonal family \(e_1,\ldots,e_n\) of primitive idempotents lifting the standard coordinates. For every integer \(r\ge1\), the ordered pairwise-commuting idempotent tuples \((p_1,\ldots,p_r)\) have precisely \(2^{rn}\) simultaneous conjugacy classes under \(1+J\), indexed by colorings \(c:\{1,\ldots,n\}\to\{0,1\}^r\).

Write \(m_{ih}=\dim_k e_iJe_h+\dim_k e_hJe_i\) for \(i<h\), \(\ell_i=\dim_k e_iA\), and \(\rho_i=\dim_k Ae_i\). Define
\[
D(c)=\sum_{i<h}m_{ih}{\mathbf 1}_{c(i)\ne c(h)},\qquad
L_j(c)=\sum_i\ell_i c_j(i),\qquad R_j(c)=\sum_i\rho_i c_j(i).
\]
For a finite field \(k=\mathbb F_q\), the complete labeled joint left/right regular-rank polynomial is
\[
\mathcal F_{A,r,q}(\mathbf X,\mathbf Y)=\sum_c q^{D(c)}\prod_{j=1}^r X_j^{L_j(c)}Y_j^{R_j(c)}.
\]
Thus each color pattern occurs with exactly \(q^{D(c)}\) distinct tuples, not just one automorphism orbit. The reduced simultaneous-idempotent locus has exactly \(2^{rn}\) smooth geometrically irreducible components; the component indexed by \(c\) has dimension \(D(c)\). In fact the defining equation scheme is smooth and reduced over \(k\).

Construct the loopless undirected multigraph \(G_A\) on \(n\) vertices with \(m_{ih}\) parallel edges between \(i\) and \(h\), and put \(W=\sum_{i<h}m_{ih}\). Then, writing the Fortuin--Kasteleyn random-cluster polynomial as \(Z_G(Q,v)=\sum_{F\subseteq E(G)}Q^{k(F)}v^{|F|}\), the unweighted total number is exactly
\[
\#\{(p_1,\ldots,p_r):p_i^2=p_i,\ p_ip_j=p_jp_i\}
=q^W Z_{G_A}(2^r,q^{-1}-1).
\]
Conversely, the family of total-count functions for all \(r\ge1\) and all finite field orders \(q\) determines \(Z_{G_A}(Q,v)\) exactly, and the polynomial determines those functions. The refined bi-rank polynomial sees the separate row and column sizes of the Peirce decomposition, which total tuple counts forget.

## Assumptions and scope
The algebra is finite-dimensional, associative, unital, and split basic, so \(A/J\cong k^n\), and its Jacobson radical \(J\) is nilpotent. This does not require \(A\) to be a path or incidence algebra, or a restriction on characteristic. The same statements hold with zero-dimensional Peirce blocks. All idempotent tuples are ordered and labeled and must commute pairwise. The variables \(X_j,Y_j\) mark the ranks of multiplication \(a\mapsto p_ja\) and \(a\mapsto ap_j\) on the full vector space \(A\), respectively. The graph \(G_A\) is an associated *multigraph* and may be disconnected. The empty edge set is allowed. The result counts actual tuples over the indicated field, not only automorphism orbits.

## Proof
**Step 1: spectral idempotents.** For a commuting idempotent tuple define, for \(\gamma\in\{0,1\}^r\),
\[
f_\gamma=\prod_{j:\gamma_j=1}p_j\prod_{j:\gamma_j=0}(1-p_j).
\]
The \(f_\gamma\) are pairwise orthogonal idempotents whose sum is \(1\), and \(p_j=\sum_{\gamma:\gamma_j=1}f_\gamma\). Modulo \(J\), each coordinate of \(p_j\) is a scalar idempotent and is therefore \(0\) or \(1\). This defines a unique coloring \(c\). Put \(d_\gamma=\sum_{i:c(i)=\gamma}e_i\) and \(d_j=\sum_{i:c_j(i)=1}e_i\).

**Step 2: explicit simultaneous conjugator.** Set \(g=\sum_\gamma f_\gamma d_\gamma\). Its image in \(A/J\) is \(1\); hence \(g\in1+J\), which consists of units because \(J\) is nilpotent. Orthogonality gives \(f_\gamma g=f_\gamma d_\gamma=g d_\gamma\), so \(p_j=gd_jg^{-1}\) for every \(j\). Conversely, conjugation of each canonical tuple by \(1+J\) produces a commuting idempotent tuple with the same coloring. Two different colorings have different images in \(A/J\) and cannot be conjugate. This also proves every coloring occurs.

**Step 3: orbit size.** The common stabilizer of \((d_j)_j\) inside \(1+J\) is \(1+W_c\), where
\[
W_c=\bigoplus_{i,h:\ c(i)=c(h)}e_iJe_h.
\]
Indeed, a Peirce block \(e_iJe_h\) commutes with all \(d_j\) exactly when its two endpoint colors agree. The complementary vector-space dimension is \(\dim J-\dim W_c=D(c)\); note that diagonal Peirce blocks cancel. Over \(\mathbb F_q\), \(1+J\) and \(1+W_c\) have \(q^{\dim J}\) and \(q^{\dim W_c}\) elements, giving \(q^{D(c)}\) tuples.

**Step 4: individual regular ranks.** For \(p_j=gd_jg^{-1}\), the image of left multiplication is \(p_j A=g d_j A\), with dimension \(\sum_{i:c_j(i)=1}\dim e_i A=L_j(c)\). The image of right multiplication is \(A p_j=A d_jg^{-1}\), with dimension \(R_j(c)\). Grouping the tuple counts by the coloring gives the displayed multivariate polynomial.

**Step 5: component smoothness.** Consider the affine equation scheme cut out in \(A^r\) by all \(p_j^2-p_j\) and \(p_ip_j-p_jp_i\). Quotienting by \(J\) maps it to the finite reduced scheme of binary \(rn\)-coordinate patterns, so each coloring is a clopen scheme stratum. On that stratum the orbit morphism \(1+J\to A^r\), \(g\mapsto(gd_jg^{-1})_j\), is surjective on geometric points, and its stabilizer is the smooth affine-space subgroup \(1+W_c\); its image is geometrically irreducible of dimension \(D(c)\). For first-order deformations over \(k'[\varepsilon]/(\varepsilon^2)\), with \(k'\) any algebraic closure extension, the spectral idempotents still reduce modulo \(J\) to the constant pattern (an idempotent in a local dual-number ring is \(0\) or \(1\)). The same formula for \(g\) therefore gives a conjugator in \(1+J\otimes k'[\varepsilon]\). The Zariski tangent space at \((d_j)\) is exactly the image of \(t\in J\mapsto([t,d_j])_j\), of dimension \(D(c)\). This equals the dimension of the geometric orbit. Every geometric point is conjugate to a canonical point, so the equation scheme is smooth, reduced, and has one geometrically irreducible component of dimension \(D(c)\) per coloring.

**Step 6: random-cluster equality and inversion.** If the variables are set to one, the sum is \(F_{A,r}(q)=\sum_cq^{D(c)}\). Each of the \(m_{ih}\) parallel edges contributes \(q\) when the endpoint colors differ and \(1\) when they agree. Expanding \(q^W\prod_{e\in E(G_A)}[1+(q^{-1}-1){\mathbf 1}_{c(u_e)=c(v_e)}]\) and summing over the \(2^r\) color labels proves \(F_{A,r}(q)=q^W Z_{G_A}(2^r,q^{-1}-1)\) by the Fortuin--Kasteleyn identity. Conversely, viewing each known function on prime-power values as its unique integer polynomial in \(q\), its value at \(q=1\) is \((2^r)^n\), determining \(n\). Choose \(r\) with \(2^r\ge n\); an injective coloring has \(D(c)=W\), so the degree in \(q\) is exactly \(W\), determining \(W\). Substitute \(q=(1+v)^{-1}\) into \(q^{-W}F_{A,r}(q)\) to recover \(Z_{G_A}(2^r,v)\). Infinitely many integers \(2^r\) determine each coefficient polynomial in \(Q\), hence the full \(Z_{G_A}(Q,v)\). This is an inverse identity for the random-cluster polynomial, not a claim that it reconstructs the graph itself.

**Step 7: sharp information limits.** For three vertices, the path algebra of \(0\to1\to2\) and the radical-square-zero algebra on arrows \(0\to1\), \(1\to2\), and \(0\to2\) have identical Peirce dimensions and left/right dimensions; hence all these spectra agree despite different \(J^2\). The oppositely oriented two-edge forks \(0\to1,0\to2\) and \(1\to0,2\to0\) have the same \(G_A\) and total counts, but different \(\ell_i\) and \(\rho_i\), and consequently different bi-rank distributions. These examples delimit what the invariant detects.

## Verification
A standalone program, `checker.py`, computes products in the original algebra basis, enumerates idempotents, selects pairwise-commuting tuples and obtains full left/right multiplication ranks by finite-field row reduction. Independently, it evaluates the coloring formula from Peirce dimensions. The accompanying `checker_output.txt` records exact equality for ten settings involving characteristic two or three, one-, two-, and three-tuples, and path, triangle, fork, and reversed-fork algebras. The program also checks equal spectra for algebras with different radical multiplication and orientation sensitivity of bi-rank profiles. Run `python checker.py` from the extracted files. The proof holds for arbitrary fields; finite verification does not prove the infinite-family assertion.

## Relationship to prior work
The joint lifting/conjugation step is consistent with the classical exchange and commuting-idempotent lifting literature. Mazurek--Nielsen--Ziembowski study commuting idempotents and exchange phenomena, but their focus is not the all-arity finite-field, left/right-rank and inverse graph-polynomial census. Berg develops the split-basic algebra framework and related quiver models; Quinn gives quiver/incidence-algebra background. Gargate--Gargate explicitly count fixed-diagonal polynomial-potent matrices in triangular/incidence algebras. When sufficiently many distinct scalar eigenvalues are available, a tuple of commuting idempotents can be encoded as one element with distinct color eigenvalues, so even multiple-idempotent *incidence-algebra* coloring counts may follow from that work by interpolation; no such incidence-only specialization is claimed independently new. Can--Casimiro--Malheiro establish components and conjugacy for the single-idempotent incidence-monoid variety; the corresponding special case of Step 5 is pre-existing. Sokal surveys the random-cluster/Tutte formalism. The contribution assessed here is the combined arbitrary split-basic all-arity bi-rank distribution and exact random-cluster inversion, including the distinguishability and non-distinguishability boundaries. Any broader published theorem implying that complete combination would defeat originality; no such result was established from the inspected materials.

## Limitations
The theorem does not classify algebra isomorphism types, determine the graph uniquely from its random-cluster polynomial, or recover multiplication inside \(J^2\). It does not cover general nonbasic algebras with matrix factors in the semisimple quotient. Small-field checker tests support, but do not independently certify, arbitrary-characteristic or arbitrary-dimensional claims. Historical priority has not been independently certified.

## References
1. Carl Fredrik Berg, “Structure Theorems for Basic Algebras,” arXiv:1102.1100 (first submitted 2011-02-05).
2. David Quinn, “The incidence algebra of posets and acyclic categories,” *Kyushu Journal of Mathematics* **67** (2013), 117–127, DOI: 10.2206/kyushujm.67.117. Public online release verified as 2013-07-25.
3. R. Mazurek, P. P. Nielsen, and M. Ziembowski, “Commuting idempotents, square-free modules, and the exchange property,” *Journal of Algebra* **444** (2015), 52–80, DOI: 10.1016/j.jalgebra.2015.07.015.
4. A. Gargate and G. Gargate, “(k+1)-potent Matrices in triangular matrix Groups and Incidence Algebras of Finite Posets,” arXiv:2009.04243 (2020).
5. M. B. Can, A. Casimiro, and A. Malheiro, “Idempotent Varieties of Incidence Monoids and Bipartite Posets,” arXiv:2208.01073 (2022).
6. A. D. Sokal, “The multivariate Tutte polynomial (alias Potts model) for graphs and matroids,” arXiv:math/0503607 (2005).
