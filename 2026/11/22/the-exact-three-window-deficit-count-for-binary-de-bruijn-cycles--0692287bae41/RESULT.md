# The exact three-window deficit count for binary de Bruijn cycles

## Finding

Fix any integer \(n\geq3\). Let \(T_n\) be the number of oriented binary circular words of length \(2^n-3\), modulo **rotation only**, whose \(2^n-3\) cyclic length-\(n\) factors are pairwise distinct. Put
\[
 B_n=2^{\,2^{n-1}-n},\quad m=n-1,\quad z=2^{-m},\quad
 s_m=\begin{cases}0&m\equiv0\pmod3,\\1&m\equiv1\pmod3,\\-1&m\equiv2\pmod3.\end{cases}
\]
Then the exact number for **every** \(n\ge3\) is
\[
 \boxed{T_n=2B_n\left(\frac{1+2(-1/2)^m}{3}
            +\frac{1+2s_mz-8z^2}{7}\right).}
\]
There are precisely four possible triples of *missing* length-\(n\) factors before a connectivity test. For each of the two triples comprising a constant word and the two alternating period-two words, exactly
\[
 L_n=B_n\frac{1+2(-1/2)^m}{3}
\]
cycles occur. For each of the two triples comprising the cyclic rotations of one primitive binary period-three word, exactly
\[
 C_n=B_n\frac{1+2s_mz-8z^2}{7}
\]
cycles occur. The latter number vanishes at \(n=3\) and is positive for every \(n\ge4\). For \(n=3,4,5,6\), the resulting totals are \(2,12,2176,59768832\). The total-to-full-de-Bruijn ratio tends to \(20/21\), while constant-plus-alternating and period-three types tend to fractions \(7/10\) and \(3/10\) of the three-defect total.

## Assumptions and scope

The alphabet \(\{0,1\}\) is labeled. A length-\(L\) *oriented circular word* has one factor at every cyclic starting position, each factor allowed to wrap around. Quotient by rotations, but **not** reversal or bit complementation. In this result \(L=2^n-3\); all length-\(n\) factors at different starting positions must be different, not necessarily all possible words. The omitted factor set therefore has size exactly three. The statement is for \(n\ge3\) (not \(n=1,2\)). All derived rational expressions are integers after multiplication by \(B_n\). It does not enumerate three missing windows over larger alphabets or arbitrary different shortfalls.

## Proof

**1. Exact four-set classification.** Set \(m=n-1\). Let \(D_m\) be the binary de Bruijn directed graph with the \(2^m\) binary length-\(m\) words as vertices, and one edge for every binary length-\(n\) word from its length-\(m\) prefix to its length-\(m\) suffix. Each vertex has in- and outdegree two, and edges have distinguishable word labels. A circular word with pairwise distinct length-\(n\) windows corresponds bijectively to a cyclic Euler tour after precisely its three omitted edges are deleted. Since the remaining graph is balanced, the deleted three edges form a balanced subgraph. Every nonempty balanced digraph with three edges is a disjoint union of directed cycles. Here there are only two loops (the constant words \(0^n,1^n\)), exactly one directed two-cycle (the alternating words), and exactly two directed three-cycles (the rotations of \(001\) and of \(011\)). A balanced three-edge deletion is therefore a loop plus the two-cycle (two choices), or one of the three-cycles (two choices). The four sets are distinct. Conversely a positive in-arborescence count of the remaining balanced graph produces an Euler tour. Distinct edge labels mean such a tour has no nontrivial rotational stabilizer.

**2. BEST theorem and normalization.** For a finite balanced digraph whose edges are individually labeled, the number of cyclic Euler tours is the directed in-arborescence count at a vertex times \(\prod_v(d_v^+-1)!\), provided a tour exists; the product is taken over its active vertices. All residual outdegrees equal one or two, so the factorial product equals one. The full graph has \(B_n=2^{2^m-(m+1)}\) in-arborescences per root by the classical binary de Bruijn count and BEST. Equivalently, this follows from its binary shift-register transition operator described below. Thus, for each missing set, the count is \(B_n\) times the ratio of the directed Laplacian cofactors before and after deletion. This also treats a disconnected residual graph correctly by giving zero.

**3. Exact resolvent of the shift graph.** Let \(P\) be the row-stochastic matrix which shifts an \(m\)-bit vertex left and appends a uniformly random independent bit. Let \(J=\mathbf1\mathbf1^{\mathsf T}/2^m\) and \(L=2(I-P)\) be the out-Laplacian (self-loops cancel). The chain forgets the starting vertex after \(m\) shifts, so \(P^m=J\). On zero-sum vectors, the inverse of \(L+J\) is
\[
 (L+J)^{-1}=J+\frac12\sum_{k=0}^{m-1}(P^k-J).
\]
The equality follows by multiplying by \(2(I-P)+J\) and telescoping \(I-P^m=I-J\). In a balanced graph, the rank-one matrix-tree identity gives the arborescence ratio after any balanced edge deletion as \(\det(L'+J)/\det(L+J)\).

**4. A loop and the two-cycle.** Deleting a self-loop does not change \(L\). Let \(u,v\) be the alternating length-\(m\) vertices and \(w=e_u-e_v\). Deleting their two oppositely oriented connecting edges changes \(L\) to \(L-ww^{\mathsf T}\). Therefore the determinant ratio is \(1-w^{\mathsf T}(L+J)^{-1}w\). For every \(0\le k<m\), the alternating suffix-prefix overlap gives \(w^{\mathsf T}P^kw=2(-1/2)^k\). By the resolvent, the ratio is exactly
\[
 1-\sum_{k=0}^{m-1}(-1/2)^k=\frac{1+2(-1/2)^m}{3}.
\]
This is strictly positive for \(m\ge2\), giving \(L_n\) for either constant-loop choice.

**5. A primitive period-three cycle.** By bit complementation it suffices to delete the three edges of the period-three word \(001001\cdots\). Index its three length-\(m\) vertices \(v_i\) by initial phase \(i=0,1,2\) in the infinite period \(001\). The deleted edge at \(v_i\) points to \(v_{i+1}\), indices mod three. The matrix determinant lemma reduces the cofactor ratio to \(\det K\) where the explicit three-by-three matrix is
\[
 K_{ij}=\delta_{ij}-\frac{Z_{ij}-Z_{i+1,j}}2,
 \qquad Z_{ij}=\sum_{k=0}^{m-1}(P^k)_{v_i,v_j},\quad 0\le i,j\le2.
\]
For \(k<m\), \((P^k)_{v_i,v_j}=2^{-k}\) exactly when the length-\((m-k)\) suffix of \(v_i\) equals the corresponding prefix of \(v_j\), and is zero otherwise. All three cyclic length-two blocks of \(001\), namely \(00,01,10\), are distinct. Hence for \(k\le m-2\) the matching phase is uniquely \(j\equiv i+k\pmod3\). For the final \(k=m-1\) there is only a one-bit equality check. Write \(a_0=a_1=0\), \(a_2=1\), and \(S_d=\sum_{0\le k\le m-2,\,k\equiv d\pmod3}2^{-k}\). Then
\[
 Z_{ij}=S_{(j-i)\bmod3}+2z\,[a_{(i+m-1)\bmod3}=a_j].
\]
The three geometric sums are explicitly, in order \(S_0,S_1,S_2\),
\[
 \begin{array}{c|ccc}
 m\bmod3&S_0&S_1&S_2\\\hline
 0&8(1-z)/7&4(1-z)/7&2(1-8z)/7\\
 1&8(1-2z)/7&4(1-2z)/7&2(1-2z)/7\\
 2&8(1-z/2)/7&4(1-4z)/7&2(1-4z)/7
 \end{array}.
\]
Substituting these into the displayed **explicit** three-by-three determinant and expanding separately for the three residues gives, respectively,
\[
 \det K=\frac{1-8z^2}{7},\quad
 \frac{1+2z-8z^2}{7},\quad
 \frac{1-2z-8z^2}{7}.
\]
This is \((1+2s_mz-8z^2)/7\), establishing \(C_n\) without extrapolating from finite calculations. With \(m=2\) the last determinant is zero; for all \(m\ge3\), the displayed values are positive. Complementation maps the cycle \(001\) to the \(011\) cycle, so both share the same count.

**6. Summation, integrality, and limits.** There are two distinct missing sets of each type and no others. BEST therefore gives \(T_n=2(L_n+C_n)\) exactly. Since the values count labeled-edge Euler tours, their integrality follows combinatorially. Finally \(z\to0\) and \((-1/2)^m\to0\), so \(T_n/B_n\to2(1/3+1/7)=20/21\) and the two type proportions tend to \((1/3)/(1/3+1/7)=7/10\) and \(3/10\).

## Verification

The standalone `verify.py` requires only Python 3's standard library. It reconstructs the de Bruijn edge graph independently of the formulas, computes exact directed Laplacian cofactors by fraction-free integer Bareiss elimination for all four missing triples at \(n=3,4,5,6,7,8\), and compares with the closed forms. A separate memoized, edge-labeled Euler-tour enumeration checks each missing triple at \(n=3,4,5\). It independently enumerates all unordered deletion triples and checks the complete four-pattern balanced classification at \(n=3,4,5\). Finally it checks direct three-vertex suffix-prefix overlap determinants for every \(2\le m\le15\). On the embedded actual script, execution returned `VERIFY_OK exact_tree_orders=3..8 independent_Euler_tours=3..5 complete_balanced_triples=3..5 periodic_overlap_m=2..15 totals=[(3, 2), (4, 12), (5, 2176), (6, 59768832), (7, 140174538401906688), (8, 1257833913980061993011512735753568256)]`. These checks test the theorem but the proof for arbitrary \(n\) is the finite-rank determinant calculation above.

## Relationship to prior work

Champlin, Godbole and Tomlinson (public preprint March 14, 2013) establish universal-cycle existence for complementary classes of words, not this three-exception enumeration. Gabrić, Holub and Shallit (public preprint March 13, 2019) define generalized de Bruijn circular words and **already list** the exact lengths-and-counts \(29\mapsto2176\) (Table 1) and \(61\mapsto59768832\) (Table 4). Those previously published finite numbers are not claimed as new. Their counting section expressly leaves general exact enumeration open, and does not give the present all-order expression or the missing-type breakdown. Chen, Kitaev and Sun (2019 preprint; 2020 open-access paper) analyze existence probabilities after forbidden factors, with exact cycle results for up to two omitted words, not a three-omission cycle count. A separate published result on three forbidden factors determines the number of deletion sets admitting a **linear** Euler trail, not the numbers of cyclic Euler tours or their exact distribution. A published two-defect result supplies a related rank-one calculation, but does not imply the rank-two period-three calculation here. The precise new claim is the unrestricted \(n\)-formula and two exact per-type counts, not known isolated table entries or the general Euler/BEST machinery.

## Limitations

The result is restricted to binary alphabets, precisely three missing length-\(n\) words, and rotation classes of oriented cycles. It does not compute arbitrary deficits or other alphabets. The 2019 finite numerical counts cited above are earlier results, not evidence of formula novelty on their own; these known entries are used as independent checks. The older Fredricksen (1982) survey was not available in full for inspection: later primary literature describes its two-defect formula, but an unlocated older three-defect statement remains a residual originality risk. The mathematical proof and verification are not an independent mathematical audit or a claim of publication priority.

## References

1. Michelle Champlin, Anant Godbole and Beverly Tomlinson, *Universal Cycles of Complementary Classes*, first public March 14, 2013, arXiv:1303.3323. https://arxiv.org/abs/1303.3323
2. Daniel Gabrić, Štěpán Holub and Jeffrey Shallit, *Maximal State Complexity and Generalized de Bruijn Words*, first public March 13, 2019, arXiv:1903.05442, Section 4, Tables 1 and 4. https://arxiv.org/abs/1903.05442
3. H. Z. Q. Chen, S. Kitaev and B. Y. Sun, *On the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, first public August 3, 2019, arXiv:1908.01116; *Mathematics* 8 (2020), 778. https://doi.org/10.3390/math8050778
4. *Exact universal-word probability after three binary factor deletions*, published mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-universal-word-probability-after-three-binary-factor-delet--152536a5a424
5. *Exact two-window-defect enumeration of nonbinary de Bruijn necklaces*, published mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-two-window-defect-enumeration-of-nonbinary-de-bruijn-neckl--91541f51dfe4
6. Harold Fredricksen, *A Survey of Full Length Nonlinear Shift Register Cycle Algorithms*, *SIAM Review* 24 (1982), 195–221, DOI:10.1137/1024041 (original full text not inspected).
