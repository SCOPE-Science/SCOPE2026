# A parity law for generic projectivity in cyclic radical-square-zero module spaces

## Finding

For every integer \(n\ge2\), every \(d\ge1\), and every prime power \(q\), let \(Q_n\) be the consistently oriented cycle on vertices \(\mathbb Z/n\mathbb Z\), and let \(A=\mathbb F_qQ_n/J^2\), where \(J\) is the arrow ideal. A labeled \(A\)-module with dimension \(d\) at each vertex is an \(n\)-tuple of maps \(D_i:\mathbb F_q^d\to\mathbb F_q^d\) satisfying \(D_iD_{i-1}=0\) (indices modulo \(n\)). All such tuples are counted with equal weight.

For nonnegative integers \(r_i\le d\), set \(s_i=d-r_{i-1}-r_i\). The number of tuples with \(\operatorname{rank}D_i=r_i\) for every \(i\) is zero unless every \(s_i\ge0\), and otherwise equals
\[
N_{n,d,q}(\mathbf r)=\prod_{i\in\mathbb Z/n\mathbb Z}{d\brack r_{i-1}}_q{d-r_{i-1}\brack r_i}_q\,|\operatorname{GL}_{r_i}(\mathbb F_q)|.
\]
Every such module is isomorphic to \(\bigoplus_iP_i^{r_i}\oplus\bigoplus_iS_i^{s_i}\), where \(P_i\) is the indecomposable projective supported by the arrow \(i\to i+1\) and \(S_i\) the simple at vertex \(i\). Its projective dimension is zero if all \(s_i=0\), and infinite otherwise.

The degree of the polynomial \(N_{n,d,q}(\mathbf r)\) in \(q\), with leading coefficient one, is
\[
E(\mathbf r)=\frac{nd^2-\sum_i s_i^2}{2}.
\]
Consequently, as \(q\to\infty\) through prime powers, with \(n,d\) fixed, the uniform distribution on these labeled modules satisfies the following sharp parity trichotomy, with all error probabilities \(O_{n,d}(q^{-1})\).

* **Even \(n\)**: the module is projective with probability \(1-O_{n,d}(q^{-1})\). The \(d+1\) alternating projective rank profiles \((a,d-a,a,d-a,\dots)\), for \(0\le a\le d\), have limiting probabilities \(1/(d+1)\) each.
* **Odd \(n\), even \(d\)**: the module is projective with probability \(1-O_{n,d}(q^{-1})\); its unique dominant rank profile is \(r_i=d/2\) at every vertex.
* **Odd \(n\), odd \(d\)**: no such module is projective. With probability \(1-O_{n,d}(q^{-1})\), its nonprojective part consists of exactly one simple \(S_j\). Every \(j\) occurs with limiting probability \(1/n\); these modules have infinite, periodic projective resolutions.

This shows that the generic homological behavior alternates with the parities of the cycle length and the common vertex dimension: a uniform mixture of projective types, a single projective type, or necessarily one residual simple.

## Assumptions and scope

Here \({a\brack b}_q=\prod_{j=0}^{b-1}(q^{a-j}-1)/(q^{b-j}-1)\) for \(0\le b\le a\), and zero otherwise; \(|\operatorname{GL}_0(\mathbb F_q)|=1\). All asymptotic statements concern **labeled** quiver representations, rather than choosing isomorphism classes uniformly. The algebra has \(n\) vertices and exactly one arrow from \(i\) to \(i+1\) (for \(n=2\), the two opposite directed arrows are distinct). There is no field-characteristic restriction. The dimension \(d\) and the number of vertices \(n\) remain fixed in the limit.

## Proof

**Stratum count.** At the vertex \(i\), put \(I_i=\operatorname{im}D_{i-1}\) and \(K_i=\ker D_i\). The relations require \(I_i\subseteq K_i\), with \(\dim I_i=r_{i-1}\), \(\dim K_i=d-r_i\), and hence \(s_i\ge0\). Choose the subspace \(I_i\) in \({d\brack r_{i-1}}_q\) ways, then \(K_i\supseteq I_i\) in \({d-r_{i-1}\brack r_i}_q\) ways. After these choices, \(D_i\) is equivalent to an isomorphism \(\mathbb F_q^d/K_i\to I_{i+1}\), with \(|\operatorname{GL}_{r_i}(\mathbb F_q)|\) possibilities. The choices for distinct vertices are independent, so multiplication yields the exact formula without overcounting.

**Module decomposition and homology.** Split each vertex space as \(I_i\oplus U_i\oplus T_i\), where \(I_i\oplus U_i=K_i\) and \(\dim U_i=s_i\), \(\dim T_i=r_i\). Via the induced isomorphisms \(T_i\to I_{i+1}\), matched basis vectors form \(r_i\) copies of the length-two projective \(P_i\); the remaining basis vectors form \(s_i\) copies of \(S_i\). This is an explicit direct-sum decomposition, not merely a dimension count. The kernel of the projective cover of \(S_i\) is the nonzero simple \(S_{i+1}\). Thus successive syzygies cycle among the \(n\) simples; a module has finite projective dimension exactly when every \(s_i\) vanishes, in which case it is already projective.

**Degree calculation.** Both Gaussian binomials are monic polynomials in \(q\), of degrees \(r_{i-1}(d-r_{i-1})\) and \(r_i(d-r_{i-1}-r_i)\), respectively; \(|\operatorname{GL}_{r_i}(\mathbb F_q)|\) is monic of degree \(r_i^2\). Summing degrees over the cycle and substituting \(s_i=d-r_{i-1}-r_i\) gives \(E(\mathbf r)=(nd^2-\sum_i s_i^2)/2\). Every feasible profile therefore contributes a monic polynomial. There are finitely many profiles for fixed \(n,d\), so asymptotic probabilities are determined by those minimizing \(\sum_i s_i^2\).

**Parity minimization.** Summing the defining equalities yields \(\sum_i s_i=nd-2\sum_i r_i\); hence \(\sum_i s_i\equiv nd\pmod2\). If \(n\) is even, \(s_i=0\) for all \(i\) is feasible and forces exactly the \(d+1\) alternating rank profiles. If \(n\) is odd and \(d\) even, all \(s_i=0\) is feasible and uniquely forces \(r_i=d/2\). If both \(n,d\) are odd, the all-zero vector \(\mathbf s\) is impossible, but for each vertex \(j\) the choice \(s_j=1\), \(s_i=0\) otherwise determines a feasible unique cyclic rank solution, alternating between \((d-1)/2\) and \((d+1)/2\). These are exactly the \(n\) profiles with minimum square sum one. Any non-dominant feasible profile has a strictly smaller **integer** polynomial degree and contributes a relative \(O_{n,d}(q^{-1})\). Every dominant profile has leading coefficient one, so its conditional limiting mass is uniform among the dominant profiles, as claimed.

## Verification

The included standalone \(\texttt{verify.py}\) implements the Gaussian-binomial formula, enumerates all matrices and their consecutive-zero products directly over the prime fields of orders two and three in ten small configurations, and verifies the rank-profile counts. It also checks the complete list of dominant profiles for all \(2\le n\le7\), with \(1\le d\le5\) when \(n\le4\) and \(1\le d\le3\) otherwise. Execution prints \(\texttt{VERIFY\_OK}\). These checks are finite consistency tests; the proof above, not enumeration, establishes the unrestricted theorem.

## Relationship to prior work

Vaso's 2021 treatment of radical-square-zero bound quiver algebras (primary MSC 16G20) supplies the relevant Nakayama representation-theoretic setting; it concerns cluster-tilting subcategories, rather than finite-field counts of fixed labeled dimension vectors. Deng and Hua (2021) develop finite-field quiver counting under nilpotent relations, emphasizing indecomposable isomorphism classes; their formulas do not explicitly give the cyclic radical-square-zero rank-stratum law and parity-dependent generic projectivity distribution stated here. Jonsson and Stroiński (2021) consider higher representations over radical-square-zero Nakayama algebras, a different invariant. Darmajid and Jensen's earlier work on fixed-rank varieties of complexes supplies important geometric context, but its main theorem concerns complexes of projective modules over algebras of global dimension at most two; it does not directly specialize to finite-field cyclic square-zero Nakayama module counts and the three limiting probabilities. The underlying classification of Nakayama indecomposables and Gaussian subspace counts are standard facts, not asserted to be original.

## Limitations

The result concerns equal vertex dimension, a single consistently oriented cycle, and the radical-square-zero relation. The limits do not describe fixed-field large-dimension behavior or uniformly sampled isomorphism classes. An equivalent rank-profile count could exist in cyclic-complex or Hall-polynomial literature; inspected sources did not establish that coverage, but the literature comparison does not prove global publication priority. No independent mathematical audit has been performed.

## References

1. B. Deng and J. Hua, *Counting Representations of Quivers Respecting Nilpotent Relations over Finite Fields*, arXiv:2103.00636, first posted 2021-02-28, https://arxiv.org/abs/2103.00636.
2. L. Vaso, *n-cluster tilting subcategories for radical square zero algebras*, arXiv:2105.05830, first posted 2021-05-12, https://arxiv.org/abs/2105.05830.
3. H. Jonsson and M. Stroiński, *Simple transitive 2-representations of bimodules over radical square zero Nakayama algebras via localization*, arXiv:2112.09590, first posted 2021-12-17, https://arxiv.org/abs/2112.09590.
4. Darmajid and B. T. Jensen, *Varieties of Complexes of Fixed Rank*, arXiv:1312.2058, https://arxiv.org/abs/1312.2058.
