# Quarter-rank discrete-Gaussian law for matrix-ring Vieta two-cycles

## Finding
For \(n\ge2\) and a prime power \(q\), consider the *matrix Vieta map* on ordered pairs of matrices over \(\mathbb F_q\):
\[
T(A,B)=(A+B,AB),\qquad A,B\in M_n(\mathbb F_q).
\]
The exact rank-refined two-cycle census and its four-phase rank limit are
\[
C_{n,r}(q)={n\brack r}_q{n-r\brack r}_q|\operatorname{GL}_r(q)|q^{n(n-r)},
\qquad 1\le r\le\lfloor n/2\rfloor,
\]
where \(C_{n,r}(q)\) counts **points**, not unoriented cycles; each directed two-cycle has two points, both with the same rank of \(B\). Thus the number of directed two-cycles equals \(\tfrac12\sum_r C_{n,r}(q)\).

For each fixed prime power \(q\) and residue \(s\in\{0,1,2,3\}\), take \(n=4m+s\to\infty\). Conditional on a uniformly chosen two-cycle point, for every fixed integer \(k\) the rank \(r=m+k\) has limiting probability
\[
\lim_{m\to\infty}\mathbb P(r=m+k\mid T^2(A,B)=(A,B),\ T(A,B)\ne(A,B))
=\frac{q^{-2(k-s/4)^2}}{\Theta_{q,s}},\quad
\Theta_{q,s}=\sum_{j\in\mathbb Z}q^{-2(j-s/4)^2}.
\]
The full total-cycle asymptotic is
\[
\#\{\text{directed two-cycles}\}
\sim\frac{q^{9n^2/8}}{2P_q}\Theta_{q,s},
\qquad P_q=\prod_{j=1}^\infty(1-q^{-j})>0.
\]
This produces four distinct shifted discrete-Gaussian laws indexed by \(n\bmod4\); the typical square-zero matrix has rank near one quarter of the dimension, not half.

## Assumptions and scope
The matrix algebra is unital and associative; \(q\) is any finite prime power, including even characteristic. The operation uses ordered multiplication \(AB\), not \(BA\). The graph's vertices are all \(|M_n(\mathbb F_q)|^2\) ordered pairs. An exact period-two *point* means \(T^2(A,B)=(A,B)\) but \(T(A,B)\ne(A,B)\). A two-cycle is a two-point orbit, hence counts half as many. There are no exact two-cycles for \(n=1\). The asymptotic is at fixed \(q\), with \(n\) increasing along one of the four residue classes; it is not claimed uniformly for \(q\to\infty\).

## Proof
1. A direct (noncommutative) calculation gives \(T^2(A,B)=(A+B+AB,(A+B)AB)\). Equating the first coordinate to \(A\) forces \(AB=-B\). The second then equals \(-(A+B)B=B-B^2\); therefore the two-periodic condition is precisely \(AB=-B\) and \(B^2=0\). The period is exactly two if and only if \(B\ne0\), since the first coordinate of one step is \(A+B\).
2. A square-zero rank-\(r\) map \(B:V\to V\) has image \(U\) of dimension \(r\) contained in its kernel \(K\) of dimension \(n-r\). First choose \(U\) in \({n\brack r}_q\) ways, then choose \(K\supset U\) in \({n-r\brack r}_q\) ways; the induced isomorphism \(V/K\to U\) has \(|\operatorname{GL}_r(q)|\) choices. This proves the square-zero matrix count and \(r\le\lfloor n/2\rfloor\).
3. The equation \(AB=-B\) says exactly that \(A\) restricts to \(-\operatorname{id}\) on \(U=\operatorname{im}B\). An arbitrary extension of this forced map from an \(r\)-subspace to \(V\) has \(q^{n(n-r)}\) choices. Multiplying gives the displayed \(C_{n,r}(q)\). The second coordinate of a two-cycle is \(-B\), which has the same rank, so each count is even and half gives its two-cycle count.
4. Write \(\genfrac{[}{]}{0pt}{}{n}{r}_q\) for the Gaussian binomial. Expanding its elementary product and the order of \(\operatorname{GL}_r(q)\), we obtain
\[
C_{n,r}(q)=q^{n^2+nr-2r^2}H_{n,r}(q),\quad
H_{n,r}(q)=
\frac{\prod_{j=0}^{r-1}(1-q^{j-n})(1-q^{j-(n-r)})}{\prod_{i=1}^r(1-q^{-i})}.
\]
For fixed \(q\), \(0<H_{n,r}(q)\le P_q^{-1}\). If \(n=4m+s\) and \(r=m+k\) with fixed integer \(k\), numerator factors converge to \(1\) and the denominator to \(P_q\), so \(H_{n,m+k}(q)\to P_q^{-1}\). Completing the square gives
\[
n^2+nr-2r^2=\frac98n^2-2(r-n/4)^2.
\]
Therefore \(q^{-9n^2/8}C_{n,m+k}(q)\to P_q^{-1}q^{-2(k-s/4)^2}\). The uniform upper bound by \(P_q^{-1}q^{-2(k-s/4)^2}\), extended by zero for inadmissible ranks, is summable over \(k\in\mathbb Z\). Dominated convergence for series proves both the theta asymptotic of the sum and the normalized discrete-Gaussian probability law.

## Verification
The accompanying dependency-free Python checker independently computes the map \(T\) on all ordered pairs in \(M_2(\mathbb F_2)\), \(M_2(\mathbb F_3)\), and \(M_3(\mathbb F_2)\), separates exact two-cycles by rank, and compares them with the Gaussian formula. It independently enumerates all square-zero matrices in \(M_4(\mathbb F_2)\) and verifies each rank stratum. It also compares the finite rank probabilities against their four predicted theta limits at \(n\in\{64,65,66,67\}\), \(q\in\{2,3\}\). The checker prints `MATRIX_VIETA2_OK` on success. Finite tests corroborate, but do not replace, the general proof.

## Relationship to prior work
Chernev and Chernev (submitted November 5, 2026) extended ring structure graphs to noncommutative rings and used a known qualitative two-cycle/nilpotence criterion; their treatment did not enumerate noncommutative matrix-ring two-cycle rank strata or an asymptotic rank law. Lipkovski (2012), Proposition 3.3, gives a two-loop characterization for commutative rings; it does not specialize to the full matrix algebras considered here. Bounds (2020) studies multiplication of moduli and cycle lower bounds, rather than the exact noncommutative matrix distribution. The square-zero matrix flag count is standard and has also appeared in work on matrix zero-divisor graphs. The contribution is therefore **not** the flag count or the two-periodic equation alone, but their exact dynamic rank-refined combination and the four-phase fixed-field discrete-Gaussian limit. An unrelated published discrete-Gaussian law concerns **zero-product** matrix pairs \(AB=0\); it does not impose \(B^2=0\) and \(AB=-B\) and does not imply the present quarter-rank distribution as stated.

## Limitations
Only exact cycles of length two are enumerated. No count of longer cycles, no classification of all connected components, and no extension to arbitrary nonmatrix rings is asserted. The first elementary characterization is a simple implication of the map; the novel part must be assessed as the evaluated rank census plus limiting law. Search results do not establish exhaustive historical priority. No independent mathematical audit has been performed.

## References
- A. M. Chernev and N. A. Chernev, *On the Connected Components of Structure Graphs of Associative Rings*, arXiv:2611.07521v1 (first submitted 2026-11-05), https://arxiv.org/abs/2611.07521.
- A. T. Lipkovski, *Digraphs associated with finite rings*, Publ. Inst. Math. 92 (2012), 35–41, https://doi.org/10.2298/PIM1206035L.
- M. Bounds, *New Theorems for the Digraphs of Commutative Rings*, Rose-Hulman Undergraduate Mathematics Journal 21 (2020), https://scholar.rose-hulman.edu/rhumj/vol21/iss1/4/.
- *Degree strata recover rank and square-zero type in matrix zero-divisor graphs*, published result (2026-10-13), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-degree-strata-recover-rank-and-square-zero-type-in-matrix-zero-d--bcab65bc9423.
- *Discrete-Gaussian ranks and exponentially rare homology among zero-product matrix pairs*, published result (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-discrete-gaussian-ranks-and-exponentially-rare-homology-among-ze--55b0cf94c8d7.
