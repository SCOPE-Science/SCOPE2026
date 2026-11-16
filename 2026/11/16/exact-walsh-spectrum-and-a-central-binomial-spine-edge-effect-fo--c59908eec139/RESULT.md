# Exact Walsh spectrum and a central-binomial spine-edge effect for triangular-book spanning trees

## Finding
Let \(n\ge1\) and let \(B_n=K_{1,1,n}\) have two distinguished vertices \(u,v\), their common edge \(e=uv\), and leaves \(w_1,\ldots,w_n\) adjacent to both distinguished vertices. This is the triangular-book, or thagomizer, graph. On \(H_n=\mathbb F_2^{2n+1}\), indexed by its edges, let \(f_n\) indicate the spanning-tree edge-incidence vectors. Its unnormalized Walsh transform is

\[
W_n(\omega)=\sum_{T\text{ spanning tree of }B_n}(-1)^{\langle\omega,\mathbf1_T\rangle}.
\]

Write \(c=(-1)^{\omega_e}\), \(a_i=(-1)^{\omega_{uw_i}}\), \(b_i=(-1)^{\omega_{vw_i}}\), and let \(d=|\{i:a_i\ne b_i\}|\). The **complete Walsh spectrum**, valid at every frequency, is

\[
W_n(\omega)=
\begin{cases}
0,&d\ge2,\\
-2^{n-1}\prod_{i\ne j}a_i,&d=1\text{ with discordant index }j,\\
2^{n-1}\left(\prod_{i=1}^n a_i\right)\left(2c+\sum_{i=1}^na_i\right),&d=0.
\end{cases}
\]

Convolution by \(f_n\) on \(H_n\) has exact Fourier rank

\[
\operatorname{rank}(f_n*)=2^{n+1}(n+1)-\mathbf1_{2\mid n}\,2\binom n{n/2-1}.
\]

Its smallest positive singular value is \(2^{n-1}\), its largest singular value is \(2^{n-1}(n+2)\), and the Moore--Penrose inverse has \(\ell^2\)-norm \(2^{1-n}\). In particular the nonzero spectral condition number is exactly \(n+2\). The convolution operator is invertible only when \(n=1\).

For the *different operator* \(P_n\), the Fourier projection on the frequencies indexed by the spanning-tree incidence vectors of \(B_n\), the sharp endpoint norm is

\[
\|P_n\|_{\ell^1\to\ell^1}=\|P_n\|_{\ell^\infty\to\ell^\infty}
=\frac n2+\frac{n}{2^n}\binom{n-1}{\lfloor(n-1)/2\rfloor}+\frac1{2^n}\binom n{\lfloor n/2\rfloor}.
\]

Removing just the spine edge gives the complete bipartite graph \(K_{2,n}\); the sharp spanning-tree-frequency projection norm changes by exactly

\[
\|P_{B_n}\|-\|P_{K_{2,n}}\|=2^{-n}\binom n{\lfloor n/2\rfloor}
\sim\sqrt{\frac2{\pi n}}.
\]

## Assumptions and scope
All graphs are finite, simple, labelled, connected, and undirected; \(n\) is any integer at least one. The binary pairing is the coordinate dot product and the unnormalized Walsh transform is used. Convolution and Fourier projection act on complex functions on \(H_n\), with counting measure for \(\ell^1\) and \(\ell^\infty\) and the standard \(\ell^2\) norm; the Fourier projection is normalized by \(2^{-(2n+1)}\). The inverse in the singular case means Moore--Penrose pseudoinverse on the orthogonal complement of the kernel. The projection frequency set \(A_n\) and nonzero Walsh support of its indicator are distinct sets, so these two operators should not be conflated.

## Proof
First classify spanning trees: if the edge \(uv\) belongs to the tree, each leaf must contribute exactly one edge, independently, giving \(2^n\) possibilities. If \(uv\) is absent, precisely one leaf must attach to both hubs, and every other leaf must attach to exactly one hub, giving \(n2^{n-1}\) possibilities. There are \((n+2)2^{n-1}\) trees. Multiplying their edge signs gives the exact polynomial identity

\[
W_n(\omega)=c\prod_{i=1}^n(a_i+b_i)+\sum_{j=1}^na_jb_j\prod_{i\ne j}(a_i+b_i).
\]

If at least two signed pairs disagree, every product has a zero factor. If exactly one pair disagrees, its sole surviving term has \(a_jb_j=-1\) and value \(-2^{n-1}\prod_{i\ne j}a_i\). If none disagree, write \(a_i=b_i=z_i\), factor \(2^{n-1}\prod_i z_i\), and obtain \(2c+\sum_i z_i\). These three disjoint cases prove the stated complete transform.

There are \(n2^{n+1}\) frequencies with exactly one disagreeing pair, all nonzero, and \(2^{n+1}\) with zero disagreeing pairs. For even \(n\), the latter family vanishes exactly when \(\sum_i z_i=2\) and \(c=-1\), or when \(\sum_i z_i=-2\) and \(c=1\), yielding \(2\binom n{n/2-1}\) more zeros. For odd \(n\), none vanish. Fourier diagonalization of convolution gives the rank formula. All nonzero transform values are integer multiples of \(2^{n-1}\); a one-discordant-pair frequency attains that modulus. At the zero frequency the maximal magnitude is the tree count \((n+2)2^{n-1}\), by the triangle inequality. Thus the positive singular-value endpoints and the pseudoinverse norm follow.

For the frequency projection, its convolution kernel is \(2^{-(2n+1)}W_n(x)\), so both endpoint norms equal the absolute kernel sum divided by \(2^{2n+1}\). The one-discordant-pair terms contribute \(n/2\). Let \(S_n=z_1+\cdots+z_n\) with independent uniform signs. The equal-pair terms contribute \(\tfrac12\mathbb E\max(|S_n|,2)\), because

\[
|s+2|+|s-2|=2\max(|s|,2).
\]

The exact elementary binomial identities \(\mathbb E|S_n|=2n\binom{n-1}{\lfloor(n-1)/2\rfloor}/2^n\) and

\[
\tfrac12\mathbb E(\max(|S_n|,2)-|S_n|)=2^{-n}\binom n{\lfloor n/2\rfloor}
\]

hold separately for odd \(n\) (only \(|S_n|=1\) contributes) and even \(n\) (only \(S_n=0\) contributes). These identities establish the displayed norm. Deleting \(uv\) leaves the \(n/2+\tfrac12\mathbb E|S_n|\) formula by the same signed-tree expansion without the spine term. Their difference is exactly the central-binomial correction; Stirling's asymptotic proves the final equivalence.

## Verification
The included standalone `check_book.py` enumerates the actual spanning-tree incidence supports and calculates the complete integer Walsh transform by a fast Walsh--Hadamard transform for \(1\le n\le8\), including all \(131072\) frequencies for \(n=8\). It compares every coefficient, the nonzero rank, smallest/largest nonzero magnitude, and the endpoint norm against the explicit formulas. Independently, exact signed Laplacian minors are evaluated at 75 reproducible random frequencies at each \(1\le n\le15\). The central-binomial correction is tested arithmetically for all \(1\le n\le100\). All tests pass (`BOOK_WALSH_EXACT_TESTS_PASS`). These are finite consistency checks; the all-dimensional claims rest on the combinatorial proof above.

## Relationship to prior work
Sokal's multivariate Tutte framework encompasses general weighted spanning-tree enumerators, which are used here only as a broad setting and are not claimed as new. The 2015 book-network complexity work concerns ordinary spanning-tree counts. Gedeon's thagomizer-matroid paper studies Kazhdan--Lusztig polynomials and equivariant refinements, not the complete Walsh transform. A related previously published result determines the Walsh spectrum and sharp spanning-tree-frequency projection norm of the graph \(K_{2,n}\) without the spine. The new asserted contribution is the exact Fourier rank and spectrum for the *spine-augmented* graph, together with the quantitative sharp central-binomial perturbation of the endpoint projection norm. An earlier equivalent specialized formula cannot be ruled out by these comparisons.

## Limitations
The result concerns triangular-book graphs, not arbitrary book networks, and does not estimate \(\ell^1\)- or \(\ell^\infty\)-norms of convolution pseudoinverses. The closest comparative published record was available as an indexed summary, not verified by full-text inspection. No independent mathematical audit or exhaustive literature-priority determination has been performed.

## References
- A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, arXiv:math/0503607 (first posted 2005-03-25), https://arxiv.org/abs/math/0503607.
- K. R. Gedeon, *Kazhdan-Lusztig polynomials of thagomizer matroids*, arXiv:1610.05349 (first posted 2016-10-17), https://arxiv.org/abs/1610.05349.
- A. Mokhlissi, M. Lotfi and A. El Marraki, *Combinatorial methods evaluating the complexity of book networks*, Applied Mathematical Sciences 9 (2015), DOI 10.12988/ams.2015.54380.
- *Complete Walsh spectrum and sharp Fourier projection norms for the spanning trees of* \(K_{2,n}\), published comparative research record (2026-11-08), published-finding corpus (this concerns the graph without the spine edge).
