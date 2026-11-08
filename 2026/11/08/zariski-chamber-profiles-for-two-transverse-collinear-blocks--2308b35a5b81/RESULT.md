# Zariski-chamber profiles for two transverse collinear blocks

## Finding

Let \(n,m\ge 3\). Blow up \(\mathbb P^2_{\mathbb C}\) at \(n\) distinct points of one line \(A_0\) and \(m\) distinct points of a second line \(B_0\), neither block containing their intersection. Call the resulting smooth surface \(X_{n,m}\). Define \(Z_{n,m}(t;u,v)\) to count Zariski chambers in the big cone by the size of the negative support (variable \(t\)), with \(u\) and \(v\) marking inclusion of the strict transforms \(A\) and \(B\).

For \(N,h\ge0\), define the truncated binomial polynomial
\[
B_{N,h}(t)=\sum_{k=0}^{\min(N,h)}\binom Nk t^k,
\]
with \(\binom Nk=0\) when \(k\notin\{0,\dots,N\}\). For \(0\le a\le n\) and \(0\le b\le m\), put \(N=n-a\), \(M=m-b\), and
\[
\begin{aligned}
P_{a,b}(t;u,v)={}&(1+t)^{N+M}
+ut\, B_{N,n-2}(t)(1+t)^M \\
&+vt\,(1+t)^N B_{M,m-2}(t) \\
&+uvt^2\bigl[B_{N,n-2}(t)B_{M,m-2}(t)
-\binom N{n-2}\binom M{m-2}t^{n+m-4}\bigr].
\end{aligned}
\]
Then the *complete three-variable negative-support enumerator* is
\[
\boxed{\begin{aligned}
Z_{n,m}(t;u,v)={}&P_{0,0}(t;u,v)+nm t P_{1,1}(t;u,v)\\
&+n\sum_{r=2}^{m}\binom mr t^r P_{1,r}(t;u,v)\\
&+m\sum_{r=2}^{n}\binom nr t^r P_{r,1}(t;u,v).
\end{aligned}}
\]
Here the constant coefficient is the nef chamber; evaluating \(u=v=1\) gives the ordinary support-size polynomial. In particular, setting \(z(n,m)=Z_{n,m}(1;1,1)\), one obtains the closed formula
\[
\begin{aligned}
z(n,m)={}&(2^{n+1}-n-1)(2^{m+1}-m-1)-\binom n2\binom m2\\
&+nm\big[(2^n-1)(2^m-1)-(n-1)(m-1)\big]\\
&+n\big[(2^n-1)(2\cdot3^m-(m+2)2^m)-(n-1)\binom m2\big]\\
&+m\big[(2^m-1)(2\cdot3^n-(n+2)2^n)-(m-1)\binom n2\big].
\end{aligned}
\]
The largest possible negative support has \(n+m\) components. The number of such maximal supports is exactly
\[
\begin{aligned}
c(n,m)={}&1+n(2^m-m-1)+m(2^n-n-1)\\
&+n(n-1)\big(2^m-1-m-\binom m2\big)\\
&+m(m-1)\big(2^n-1-n-\binom n2\big).
\end{aligned}
\]
For \((n,m)=(3,4)\), the polynomial \(Z_{3,4}(t;1,1)\) has coefficients \((1,21,150,529,1047,1170,638,92)\), so there are exactly \(3648\) chambers. At \((4,4)\), the count is \(11925\) and the maximal-support count is \(209\).

## Assumptions and scope

The ground field is \(\mathbb C\). The center of each blow-up consists of distinct proper points, with exactly the specified two collinear blocks and with the intersection of \(A_0\) and \(B_0\) unblown. Every \(n,m\ge3\) is included, with no bounded Picard-number hypothesis. A chamber is counted once for its (necessarily negative-definite) reduced negative support, using the standard Zariski-chamber correspondence. It is the smooth blow-up, not any contracted singular model, that is considered.

## Proof

**1. Negative curves are exhausted.** Let \(H\) be the pullback of a plane line, and \(E_i\), \(F_j\) the exceptional curves. Apart from these, the proposed negative curves are
\[
A=H-\sum_{i=1}^{n}E_i,\quad B=H-\sum_{j=1}^{m}F_j,\quad L_{ij}=H-E_i-F_j.
\]
Any irreducible curve \(C\) not equal to \(A\), \(B\) or an exceptional curve is the transform of an irreducible plane curve of degree \(d\ge1\), with multiplicities \(\alpha_i\), \(\beta_j\). Bézout against the two distinct lines gives \(\sum_i\alpha_i\le d\) and \(\sum_j\beta_j\le d\). Hence \(-K_{X_{n,m}}\cdot C=3d-\sum_i\alpha_i-\sum_j\beta_j\ge d\). Adjunction yields \(C^2=2p_a(C)-2+(-K_{X_{n,m}}\cdot C)\ge d-2\); this is nonnegative for \(d\ge2\). If \(d=1\), negativity requires the line to pass through two marked points. Besides \(A_0\) and \(B_0\), these are precisely the cross-block joining lines. Thus the listed \(n+m+nm+2\) curves are exhaustive.

**2. Their intersection pattern.** Every exceptional curve and every \(L_{ij}\) has square \(-1\); \(A^2=1-n\), \(B^2=1-m\), \(A\cdot B=1\). Two distinct cross curves have intersection \(1\) exactly when both their indices differ, and otherwise intersection \(0\). The only positive intersections involving the exceptional curves are \(E_i\cdot A=1\), \(F_j\cdot B=1\), \(E_i\cdot L_{ij}=1\), and \(F_j\cdot L_{ij}=1\). Each cross curve is orthogonal to \(A\) and \(B\).

**3. Enumerating possible cross curves.** A negative-definite support cannot contain two distinct \((-1)\)-curves intersecting once: their two-by-two principal matrix is singular. Consequently any chosen \(L_{ij}\)'s must have pairwise intersecting index-pairs (edges of a complete bipartite graph). A nonempty pairwise intersecting family of edges of a bipartite graph is a star. The possibilities are: one edge with multiplicity \(nm\) and endpoint counts \((a,b)=(1,1)\); a star with \(r\ge2\) edges centered in the first block with multiplicity \(n\binom mr\) and endpoint counts \((1,r)\); or a star centered in the second block with multiplicity \(m\binom nr\) and endpoint counts \((r,1)\). The empty family is one case with \((a,b)=(0,0)\). If a star uses \(a\) first-block and \(b\) second-block endpoints, exactly \(N=n-a\) and \(M=m-b\) exceptional curves remain eligible.

**4. The two-line Schur complement.** Choose \(k\) of the eligible \(E\)'s and \(\ell\) of the eligible \(F\)'s, independently. Their intersection block is minus an identity matrix. Eliminating it changes the diagonal entries of \(A\) and \(B\) to \(-(n-1-k)\) and \(-(m-1-\ell)\). If only \(A\) occurs, negative definiteness holds exactly when \(k\le n-2\); if only \(B\) occurs, exactly when \(\ell\le m-2\). If both occur, their remaining block is
\[
\begin{pmatrix}-(n-1-k)&1\\1&-(m-1-\ell)\end{pmatrix},
\]
which is negative definite exactly when both inequalities hold and \((n-1-k)(m-1-\ell)>1\). As the two factors are positive integers, this means excluding only \((k,\ell)=(n-2,m-2)\). This argument also proves all permitted supports negative definite: all remaining cross curves contribute independent \((-1)\)-blocks.

**5. Generating functions.** For a fixed cross-family footprint \((a,b)\), the four choices of whether \(A\) and \(B\) occur generate exactly \(P_{a,b}(t;u,v)\). The correction monomial removes the unique forbidden exceptional-cardinality pair when both line transforms occur; its binomial coefficient is zero if the cardinalities are unavailable. Summing over the empty family, one-edge families, and the two kinds of nontrivial stars proves the boxed three-variable identity. Setting \(t=u=v=1\) and using the binomial theorem gives the displayed closed chamber-count formula.

**6. Largest supports.** The Picard number of the blow-up is \(n+m+1\), and the Hodge index theorem bounds negative-definite support size by \(n+m\). The set of all \(n+m\) exceptional curves attains it. Reading the highest coefficient from the star cases gives \(c(n,m)\): its terms count the all-exceptional support; single distinguished-line supports with nontrivial stars on the opposite side; and both-distinguished-line supports with stars of at least three edges, respectively.

## Verification

The standalone file `verify.cpp` exactly constructs the full integral intersection matrix, enumerates **all** subsets of negative curves, and uses fraction-free integer Bareiss elimination (with exact divisibility checks) to test negative definiteness. A separately coded binomial/star enumeration predicts each of the four distinguished-line profiles. For \((n,m)=(3,3)\) and \((3,4)\), the verifier checks respectively all \(131072\) and \(2097152\) subsets, and the four profiles agree coefficient by coefficient. See `verification_output.txt` for the exact replay output. This is finite corroboration of the independent universal proof, not a proof by extrapolation.

## Relationship to prior work

Bauer–Funke–Neumann (arXiv:0912.0958, Proposition 1.1 and Proposition 1.5) prove the general negative-definite-support correspondence and provide an algorithm for general-position del Pezzo blow-ups. Bauer–Schmitz (arXiv:1204.4373) improve the matrix-enumeration algorithm and apply it to the Segre–Schur quartic. These results supply the counting principle but do not present the two-parameter, distinguished-line generating polynomial here; their general algorithms would still require classifying negative curves and negative-definite supports of this particular unbounded family. Testa–Várilly-Alvarado–Velasco (arXiv:0901.1094) classify big-anticanonical rational surfaces and study Cox-ring finite generation, a different invariant. Failla–Lahyane–Molica Bisci (DOI 10.1478/C1A0601001) study a line-plus-integral-conic family with an effective-monoid aim, not this two-line chamber enumerator. A previously available six-point \((3,3)\) chamber count is recovered as a proper specialization; it does not imply the closed formula for arbitrary \((n,m)\).

## Limitations

The result describes support counts and marked distinguished-line incidence, not volumes of individual chambers or their adjacency. It assumes two distinct blocks of proper points and does not cover infinitely-near points, the case of a marked intersection, or configurations on three or more lines. The published-priority comparison is limited to the primary materials described above and searches for exact formulas and aliases; undiscovered specialist tables may exist. The calculation is independently reproducible, but the mathematical review has not been independently audited.

## References

1. T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958 (first posted 2009-12-04), Proposition 1.1 and Proposition 1.5. https://arxiv.org/abs/0912.0958
2. T. Bauer, D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373 (first posted 2012-04-19). https://arxiv.org/abs/1204.4373
3. D. Testa, A. Várilly-Alvarado, M. Velasco, *Big rational surfaces*, arXiv:0901.1094 (first posted 2009-01-08). https://arxiv.org/abs/0901.1094
4. G. Failla, M. Lahyane, G. Molica Bisci, *On the finite generation of the monoid of effective divisor classes on rational surfaces of type (n,m)*, Atti Accad. Peloritana 84 (2006). https://doi.org/10.1478/C1A0601001
