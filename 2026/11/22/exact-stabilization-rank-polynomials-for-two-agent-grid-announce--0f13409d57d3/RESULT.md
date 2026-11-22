# Exact stabilization-rank polynomials for two-agent grid announcements

## Finding

Fix positive integers \(m,n\). On the full \(m\)-by-\(n\) epistemic grid, let agent 1 distinguish rows, agent 2 distinguish columns, and let \(p\) be a Boolean valuation. Repeatedly announce
\[
\varphi=\Diamond_1 p\wedge\Diamond_2\neg p,
\]
using ordinary public announcement (world deletion) and retaining the original truth values on surviving worlds. Let \(\rho(p)\) be the least \(t\ge0\) for which the models after \(t\) and \(t+1\) announcements coincide, and define the exact rank polynomial
\[
F_{m,n}(z)=\sum_{p\in\{0,1\}^{m\times n}}z^{\rho(p)}.
\]
This polynomial is determined for *every* pair \(m,n\ge1\) by the following finite, triangular recurrences. Put
\[
I_{m,n}=(2^n-1)^m+(2^m-1)^n-2^{mn}\quad(m,n\ge1),
\]
\[
A_{0,n}(z)=1,\qquad B_{m,0}(z)=1\quad(m,n\ge0),
\]
and for positive \(m,n\), define
\[
\begin{aligned}
 A_{m,n}(z)&=I_{m,n}+z\sum_{c=1}^n\binom nc B_{m,n-c}(z),\\
 B_{m,n}(z)&=I_{m,n}+z\sum_{r=1}^m\binom mr A_{m-r,n}(z),\\
 F_{m,n}(z)&=A_{m,n}(z)+B_{m,n}(z)-I_{m,n}.
\end{aligned}
\]
Only the boundary values with one dimension zero shown above are used. The coefficients of the resulting polynomial are the exact labelled-valuation counts, and the recursion terminates for all positive dimensions.

The sharp maximum rank and the exact number of valuations attaining it are
\[
\max_p\rho(p)=\begin{cases}2m-1,&m=n,\\2\min(m,n),&m\ne n,\end{cases}
\]
\[
\#\{p:\rho(p)=\max\rho\}=\begin{cases}
2(m!)^2,&m=n,\\
k!(k+1)!\,\left\{\begin{smallmatrix}\ell\\k+1\end{smallmatrix}\right\},&k=\min(m,n)<\ell=\max(m,n),
\end{cases}
\]
where braces denote Stirling numbers of the second kind. All these extremal counts are nonzero.

A further closed formula gives the entire rank distribution with two rows: write \(Q_j(n)=j!\left\{\begin{smallmatrix}n\\j\end{smallmatrix}\right\}\) and set \(Q_j(n)=0\) for \(j>n\). Then the coefficients of \(F_{2,n}\) in degrees \(0,1,2,3,4\) are, respectively,
\[
Q_2+Q_3,\quad2Q_1+Q_3+Q_4,\quad2Q_1+Q_2,\quad4Q_2,\quad2Q_3.
\]
There are no higher-degree terms. In particular, the exact rank-zero probability for a uniform random valuation on the general grid is
\[
\Pr(\rho=0)=(1-2^{-n})^m+(1-2^{-m})^n-1.
\]

## Assumptions and scope

There are exactly \(mn\) distinct worlds \((i,j)\), with \(1\le i\le m\) and \(1\le j\le n\). Agent 1's accessibility classes are the rows (fixed \(i\)), agent 2's classes the columns (fixed \(j\)). Both are equivalence relations, and the sole propositional letter \(p\) is arbitrary on the grid. The modalities \(\Diamond_i\) have the usual existential Kripke meaning on the *current restricted model*. The empty model is allowed as the outcome of an announcement and is fixed thereafter. Rank zero means the first announcement changes nothing. The formulas concern labelled valuations, not row/column-isomorphism classes, and ordinary state-eliminating public announcements, not arrow-only updates.

## Proof

**1. Rectangular invariant and sink-pruning correspondence.** Let \(R_t\subseteq[m]\), \(C_t\subseteq[n]\), initially both full. Suppose the current worlds equal \(R_t\times C_t\). At a world \((i,j)\), the first conjunct holds exactly when its row contains a surviving \(p\)-world, and the second exactly when its column contains a surviving \(\neg p\)-world. Hence the next world set is \(R_{t+1}\times C_{t+1}\), with
\[
R_{t+1}=\{i\in R_t:\exists j\in C_t\ p(i,j)=1\},\quad
C_{t+1}=\{j\in C_t:\exists i\in R_t\ p(i,j)=0\}.
\]
Direct every edge of the complete bipartite graph on row and column vertices from row \(i\) to column \(j\) when \(p(i,j)=1\), and in the opposite direction when \(p(i,j)=0\). The update deletes all vertices with zero current outdegree, simultaneously. Its surviving worlds are exactly the Cartesian product of the surviving two shores. In particular, an initially empty shore never occurs, and once a shore is empty the updated model is empty and fixed.

**2. Exact rank polynomial.** Call a row *zero* if all its entries are zero; call a column *one* if all its entries are one. Such a row and column cannot coexist because their intersection would be both zero and one. A valuation is fixed at rank zero precisely when it has no zero row and no one column. There are \((2^n-1)^m\) valuations without zero rows and \((2^m-1)^n\) without one columns, so the number with neither forbidden feature is \(I_{m,n}\) by inclusion-exclusion and the impossibility of simultaneous features.

Define \(A_{m,n}\) to count rank-weighted valuations **without zero rows**, and \(B_{m,n}\) those **without one columns**. A valuation counted by \(A\) either is fixed (\(I_{m,n}\) possibilities) or has a uniquely specified nonempty set of \(c\) one columns. The first announcement deletes exactly these columns; the remaining \(m\)-by-\((n-c)\) valuation has no one columns and retains exactly its own subsequent rank. This proves the \(A\) recurrence, including \(c=n\) by the boundary value \(B_{m,0}=1\). The symmetric zero-row argument proves the \(B\) recurrence, including \(r=m\). As no valuation has both a zero row and a one column, the universe is the union of the two counted classes, whose overlap consists of exactly \(I_{m,n}\) fixed valuations. Hence \(F=A+B-I\). Both recurrences decrease one positive dimension, establishing uniqueness and termination.

**3. Sharp bound and extremal census.** While both shores are nonempty, sinks cannot occur in both shores at once: the edge joining any proposed opposite-shore sinks would contradict at least one sink condition. After deleting all current sinks of one shore, every remaining vertex of that shore still has an outgoing neighbor in the unchanged opposite shore; therefore the next strict deletion, if any, is from the other shore. Nonempty sink-removal batches alternate shores. If \(m=n=k\), at most \(2k-1\) batches can occur before a shore empties; if \(k=\min(m,n)<\ell\), at most \(2k\) can occur. Both are realizable by arranging row and column vertices in an alternating order and orienting every edge toward earlier vertices. In the balanced case equality forces all \(2k\) consecutive alternating blocks to be singletons: there are \(2(k!)^2\) assignments of their row/column labels. In the unbalanced case equality forces the \(k\) vertices of the smaller shore to be singleton blocks, interleaved with \(k+1\) ordered nonempty blocks partitioning the larger shore; this gives \(k!(k+1)!\left\{\begin{smallmatrix}\ell\\k+1\end{smallmatrix}\right\}\) valuations. In both cases the alternating block order uniquely determines the orientation and vice versa.

**4. Two-row closed spectrum.** Each column is one of the four binary types \(00,01,10,11\). The dynamic rank depends only on which types occur, not their multiplicities. Listing the \(15\) nonempty subsets of these types and applying the two-shore update gives, by rank: for rank \(0\), one two-type and one three-type subset; for rank \(1\), two one-type subsets, one three-type subset and the four-type subset; for rank \(2\), two one-type subsets and one two-type subset; for rank \(3\), four two-type subsets; for rank \(4\), two three-type subsets. The number of length-\(n\) column sequences using exactly any prescribed \(j\) types is the surjection count \(Q_j(n)\). Summation proves the five coefficients stated above. The rank-zero probability follows from the exact count \(I_{m,n}\) by division by \(2^{mn}\).

## Verification

The accompanying `verify.py` performs independent direct world-elimination and a separate two-shore peeling recurrence for every Boolean valuation in \(19\) small rectangular dimensions, totaling \(92{,}314\) valuations. It checks equality of their stabilization ranks, the recurrence coefficients, the rank-zero formula, the claimed maximum and its multiplicity, and the explicit two-row spectrum. It independently tests that the surviving terminal world set is nonempty precisely when the valuation contains a two-by-two alternating checkerboard. It prints `VERIFY_OK` when every assertion succeeds. These finite computations support the proof and do not replace the all-size arguments.

## Relationship to prior work

Eiji Yamada, *Properties of Public Announcements as Operators* (2026), provides general announcement algebra, fixed-point theory, stabilization-rank statements and a finite-model bound by the total number of worlds. The present claim restricts to one specified positive existential epistemic formula on full two-agent grids and determines its *exact entire rank distribution* at all grid dimensions. It is not a claim to improve universal bounds for arbitrary formulas.

Sink elimination and directed-walk survival on bipartite tournaments predate this work: see Eoh, Kim and Yoon (2020) and Jung, Kim and Yoon (2020, especially sink sequences and Theorem 2.4). Cameron, Glass, Rekvényi and Schumacher (2014/2022), Theorem 3.1, already enumerate all acyclic orientations of complete bipartite graphs by alternating blocks. Those background results explain the extremal orientation structure and are **not** being claimed as new in isolation. The separately quantified public-announcement rank polynomial, its coupled all-dimension recurrence, and the full two-row rank census are the primary results here. They include cyclic orientations and epistemic semantics, not just the total acyclic-orientation count.

## Limitations

This theorem is specific to a full Cartesian two-agent grid with a single Boolean letter and the stated conjunction of two existential modalities. It does not classify arbitrary S5 frames, multi-letter formulas, arrow-only updates, or arbitrary interleaved announcements. Extant work on sink sequences and lonesum matrices may furnish alternative reductions or streamline parts of the enumeration; a full historical-priority audit has not been conducted. The results are supported by an internal mathematical review, not independent validation.

## References

- E. Yamada, *Properties of Public Announcements as Operators: Commutativity, Monotonicity, Idempotence, Fixed Points, and Stabilization*, arXiv:2611.11911v1, first public 2026-11-09, especially Sections 2 and 4.2. https://arxiv.org/html/2611.11911v1
- J.-H. Jung, S.-R. Kim, H. Yoon, *On competition indices and periods of multipartite tournaments*, arXiv:2012.08147, 2020, especially Definitions and Theorem 2.4. https://arxiv.org/abs/2012.08147
- P. J. Cameron, C. A. Glass, K. Rekvényi, R. U. Schumacher, *Acyclic orientations and poly-Bernoulli numbers*, arXiv:1412.3685, first public 2014-12-11, especially Theorem 3.1 and its alternating-block proof. https://arxiv.org/pdf/1412.3685
- S. Eoh, S.-R. Kim, H. Yoon, *On \(m\)-step competition graphs of bipartite tournaments*, Discrete Applied Mathematics 283 (2020), 199–206. Mentioned for the preceding sink-sequence framework in Jung–Kim–Yoon (2020).
