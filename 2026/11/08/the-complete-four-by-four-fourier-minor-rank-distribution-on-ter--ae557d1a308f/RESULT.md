# The complete four-by-four Fourier minor rank distribution on ternary affine spaces

## Finding
For each integer \(d\ge3\), write \(Q=3^d\), \(G=\mathbb F_3^d\), and \(\omega=\exp(2\pi i/3)\). Form the \(Q\)-by-\(Q\) Fourier character table \(F_{a,b}=\omega^{a\cdot b}\). For \(j\in\{1,2,3,4\}\), let \(N_j(Q)\) be the number of **ordered pairs** \((A,B)\) of four-element subsets of \(G\) for which the square complex matrix \(F[A,B]\) has rank \(j\). Then the complete rank distribution is
\[
\begin{aligned}
N_1(Q)&=\frac{Q^2(Q-27)(Q-9)(Q-3)(Q-1)(Q^2+54Q+972)}{11337408},\\
N_2(Q)&=\frac{Q^3(Q-9)(Q-3)(Q-1)(133Q^2-540Q+29403)}{5668704},\\
N_3(Q)&=\frac{Q^4(Q-3)(Q-1)(278Q^2-3339Q+16038)}{472392},\\
N_4(Q)&=\frac{Q^5(Q-3)(Q-1)(59Q-342)}{52488}.
\end{aligned}
\]
In particular, on \(\mathbb F_3^3\) these four counts are respectively
\[0,\qquad4{,}359{,}420,\qquad90{,}239{,}994,\qquad213{,}403{,}086.\]
Their sum is exactly \(\binom Q4^2\) for every \(d\ge3\). The theorem counts positional minors, not just attainable ranks or the existence of singular submatrices.

## Assumptions and scope
The group is the ternary elementary abelian group, not the cyclic group of order \(Q\), and the indices in each of \(A,B\) must be four distinct points. The Fourier pairing is the standard nondegenerate dot product; replacing it with an equivalent nondegenerate bilinear pairing only permutes columns. Rank is over \(\mathbb C\). There are no row/column repetitions and no coefficient-support assertions beyond the stated minors. The formulas are asserted for every integer \(d\ge3\), including arbitrarily large dimensions, by an exact finite local classification and a dimension-independent lifting argument.

## Proof
**1. Three affine row types.** Translating \(A\) scales the Fourier columns by nonzero phases, and applying any invertible affine map to \(A\) induces an invertible relabeling of the column indices. Thus the rank-incidence distribution depends only on the affine orbit of \(A\). Every four-point set in a ternary vector space belongs to exactly one of three orbits: a full affine line with one off-line point (type \(L\)); a planar four-cap with no collinear triple (type \(C\)); or an affine three-simplex (type \(S\)). Representatives are, respectively,
\[
\begin{split}
L&=\{(0,0),(1,0),(2,0),(0,1)\},\\
C&=\{(0,0),(1,0),(0,1),(1,1)\},\\
S&=\{(0,0,0),(1,0,0),(0,1,0),(0,0,1)\}.
\end{split}
\]
A planar cap is an affine parallelogram in characteristic three; hence the stated transitivity. The numbers of row sets of the three types, for \(Q=3^d\), are
\[
R_L=\frac{Q(Q-1)(Q-3)}6,\qquad
R_C=\frac{Q(Q-1)(Q-3)}8,\qquad
R_S=\binom Q4-R_L-R_C.
\]
For \(R_L\), choose the unique full line and then the off-line point. For \(R_C\), choose a vertex and two ordered independent edge vectors, dividing by eight descriptions per parallelogram. Remaining four-point sets are simplices.

**2. Exact local Fourier-rank classification.** For each representative of affine dimension \(r\in\{2,3\}\), project every column index onto its first \(r\) coordinates. The four-by-\(t\) Fourier matrix depends only on those coordinates. Let \(h_T(t,j)\) count unordered distinct \(t\)-point projected column sets giving rank \(j\), for type \(T\). The exhaustive exact tables, with entries listed by rank from \(1\) through \(4\), are
\[
\begin{array}{c|rrrr}
T,t&j=1&j=2&j=3&j=4\\\hline
L,1&9&0&0&0\\ L,2&0&36&0&0\\ L,3&0&3&81&0\\ L,4&0&0&45&81\\
C,1&9&0&0&0\\ C,2&0&36&0&0\\ C,3&0&6&78&0\\ C,4&0&0&45&81\\
S,1&27&0&0&0\\ S,2&0&351&0&0\\ S,3&0&63&2862&0\\ S,4&0&0&3213&14337
\end{array}
\]
These counts are proved by deterministic exhaustive exact enumeration of every \(t\)-subset of the \(9\) or \(27\) projected column labels, for \(1\le t\le4\), with a self-contained checker. Each Fourier subdeterminant is evaluated in \(\mathbb Z[\omega]\). Represent \(u+v\omega\) by its integer pair \((u,v)\), and compute a determinant by its Leibniz expansion. The matrix has rank at least \(j\) exactly when one of its \(j\)-minors has nonzero Eisenstein pair. The program exhausts every projected subset and verifies every reported cell, including all \(\binom{27}{4}=17{,}550\) simplex four-column subsets. It also independently checks each rank by Gaussian elimination over a split prime \(1{,}000{,}003\): each \(j\)-minor, \(j\le4\), has Eisenstein coefficients bounded by \(24\) in absolute value, so its nonzero norm is less than \(1{,}000{,}003\), excluding a spurious zero reduction. This is a finite proof of the local table, not a numerical sample or a projected infinite computation.

**3. All-dimensional column lifting.** Each projected label for row type \(T\) occurs with multiplicity \(M_T=3^{d-r_T}\), where \(r_L=r_C=2\) and \(r_S=3\). Choosing four distinct actual column points that project to exactly \(t\) distinct specified labels has \(W_t(M)\) possibilities, with
\[
\begin{aligned}
W_1(M)&=\binom M4,\\
W_2(M)&=2M\binom M3+\binom M2^2,\\
W_3(M)&=3M^2\binom M2,\\
W_4(M)&=M^4.
\end{aligned}
\]
These are the four partitions of four distinct original points into projected-label fibers (for \(t=2\), the partitions \(3+1\) and \(2+2\)). Repeated projected columns do not alter rank. Therefore, for every \(j\in\{1,2,3,4\}\), the exact formula is
\[
N_j(Q)=\sum_{T\in\{L,C,S\}}R_T(Q)
\sum_{t=1}^4h_T(t,j)W_t(M_T).
\]
Substituting the displayed local tables, expanding \(M_L=M_C=Q/9\), \(M_S=Q/27\), and simplifying gives precisely the four polynomials stated in the finding. The lifting is exact for every dimension, because all missing ambient coordinates are constant-multiplicity fibers. The four counts sum to \(\binom Q4^2\) as an additional algebraic check.

## Verification
Run `python3 checker.py`. It implements Eisenstein integer determinants exactly; enumerates all projected column sets for each row orbit; compares each rank with an independent modular Gaussian-elimination calculation protected by a proven norm bound; asserts all twelve local histogram rows; and evaluates the all-dimensional count formulas for dimensions three through six. The run prints `TERNARY_FOURIER_RANK_CENSUS_PASS`. The proof of every dimension relies on the exact fiber-lifting identity, not on extrapolation from those four test dimensions.

## Relationship to prior work
Delvaux and Van Barel study ranks and Hamming-number obstructions of Kronecker-product Fourier submatrices; their constructions and uncertainty bounds do not provide this complete positional four-by-four rank distribution. Krahmer, Pfander, and Rashkov provide the finite-abelian time-frequency uncertainty context. Biró and Lev study support-sensitive uncertainty in finite planes rather than the all-dimensional count of all rank classes.

The previously published *The four-by-four Fourier-minor incidence of the ternary affine plane* gives precisely the planar \(t=4\) singular-versus-nonsingular counts, equivalent to the appropriate last rows of the \(L\) and \(C\) local table. Those planar counts are not claimed as new. The previously published *Fourier-support spectrum of a ternary affine 3-simplex* studies attainable Fourier support sizes for fixed four-point simplices, using related evaluation-row rank calculations, but does not provide the simplex four-column rank histogram or all-dimensional positional rank-count polynomials. The contribution here is the **complete four-rank census for all index pairs throughout the full ternary affine hierarchy**, including projection collisions and full affine-simplex incidence. Prior stronger treatments in coding-theoretic or association-scheme language might imply the same result; no such direct coverage was identified in the examined sources.

## Limitations
Only four-by-four minors of ternary elementary abelian Fourier matrices are classified. The formulas do not imply a comparable rank distribution for non-ternary finite fields, cyclic prime-power groups, or other minor orders. The local exact enumeration is a finite certificate with fully specified domain and standalone code, rather than a short closed-form derivation of every local histogram entry. Independent external validation and exhaustive historical-priority adjudication have not been performed.

## References
1. F. Krahmer, G. Pfander, and P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493, first public posting 2006-11-16. https://arxiv.org/abs/math/0611493
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, technical report TW477, dated 2006-11-15 (public release day not independently established). https://www.cs.kuleuven.be/publicaties/rapporten/tw/TW477.abs.html
3. A. Biró and V. F. Lev, *Uncertainty in finite planes*, arXiv:1808.07424, first posting 2018-08-22. https://arxiv.org/abs/1808.07424
4. *The four-by-four Fourier-minor incidence of the ternary affine plane*, publicly available result with full theorem and proof. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-four-by-four-fourier-minor-incidence-of-the-ternary-affine-p--9f007d7c322e
5. *Fourier-support spectrum of a ternary affine 3-simplex*, publicly available result with full theorem and proof. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-fourier-support-spectrum-of-a-ternary-affine-3-simplex--3a5760f6b057
