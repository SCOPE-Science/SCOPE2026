# Sharp moment-order thresholds for ranking phylogenetic conservation interventions

## Finding
For each integer \(k\geq 1\), joint extinction probabilities through order \(k\) suffice to determine the ranking of all equal-cost, single-species, certain-survival interventions on every rooted phylogenetic tree with at most \(k+1\) species. This bound is sharp in a strong decision-theoretic sense: on \(n=k+2\) species there exist one rooted full-binary tree with **strictly positive** branch lengths and two exchangeable extinction laws with identical joint extinction probabilities for every group of at most \(k\) species, as well as identical probability that all \(n\) species go extinct, yet with different **unique** best species to protect. All laws in the construction assign positive probability to every extinction subset.

In particular, among four taxa, **pairwise extinction data, all single-species extinction probabilities, and even the four-way extinction probability do not determine the optimal conservation priority**. The discrepancy is created solely by a three-species joint-extinction probability invisible to pairwise data.

The explicit four-species witness has a root split \(\{a,b,c\}\mid\{d\}\), with the three-species side split as \(\{a,b\}\mid\{c\}\). Edge lengths are \(8\) for the \(\{a,b,c\}\)-clade, \(1\) for the \(\{a,b\}\)-clade, and pendant lengths \(3,1/8,1/8,11/2\) for \(a,b,c,d\), respectively. For the exchangeable distributions of the number \(K\) of extinct species
\[
\mathbb P_{-}(K=j)=\frac{(3,5,15,7,2)_j}{32},\qquad
\mathbb P_{+}(K=j)=\frac{(1,11,9,9,2)_j}{32},\qquad 0\leq j\leq4,
\]
where the extinct subset is uniform among all \(\binom4j\) subsets conditional on \(K=j\), the protected-species gains in expected rooted phylogenetic diversity are
\[
(G_a,G_b,G_c,G_d)_{-}=\left(\frac{43}{16},\frac54,1,\frac{11}4\right),\qquad
(G_a,G_b,G_c,G_d)_{+}=\left(\frac{45}{16},\frac{11}{8},\frac98,\frac{11}4\right).
\]
Thus under \(\mathbb P_-\) only \(d\) is optimal, while under \(\mathbb P_+\) only \(a\) is optimal. The two laws both have \(q_1=1/2\), \(q_2=1/4\), and \(q_4=1/16\), whereas \(q_3=15/128\) versus \(17/128\).

## Assumptions and scope
Let \(T\) be any finite rooted phylogenetic tree with \(n\geq1\) labeled leaves and nonnegative edge lengths (strictly positive lengths in the sharpness witnesses). For each edge \(e\), let \(C_e\) be the set of descendant leaves and \(\ell_e\) its length. Rooted phylogenetic diversity of a survivor set \(S\subseteq[n]\) is \(\operatorname{PD}_T(S)=\sum_e\ell_e\mathbf1\{S\cap C_e\ne\varnothing\}\). If a root stem above all leaves is included, it is allowed; its conservation gain is common to every candidate and does not affect rankings.

Let \(E\subseteq[n]\) be an arbitrarily distributed set of species that go extinct before a fixed future horizon. Write \(q_U=\mathbb P(U\subseteq E)\) for the **joint extinction probability** of \(U\). Protecting species \(i\) means changing the realized survivor set \(E^c\) to \(E^c\cup\{i\}\), leaving all other extinction outcomes unchanged (no causal rescues or secondary ecological effects). Define \(G_i=\mathbb E[\operatorname{PD}_T(E^c\cup\{i\})-\operatorname{PD}_T(E^c)]\). The comparison concerns full rankings, including ties, of these gains at equal intervention costs. No independence of species extinctions is assumed.

## Proof
**1. Branchwise gain identity.** An edge contributes additional rooted PD after protection of \(i\) exactly when \(i\in C_e\) and every original species in \(C_e\) would have gone extinct. Consequently
\[
G_i=\sum_{e:\,i\in C_e}\ell_e q_{C_e}.
\tag{1}
\]
This follows by subtracting the two edge-indicator sums for each extinction realization and then taking expectations; it is not an independent-extinction approximation.

**2. Information suffices through order \(n-1\).** If two extinction laws agree on \(q_U\) for all \(|U|\leq k\) and \(n\leq k+1\), all terms in (1) with \(|C_e|<n\) agree. An edge with \(|C_e|=n\) has every leaf as descendant, so its term \(\ell_e q_{[n]}\) is common to all \(G_i\). Hence every pairwise difference \(G_i-G_j\), and therefore the entire ranking, is unchanged. This also covers multifurcations, non-binary trees, and a possible root stem.

**3. A moment-separated pair of exchangeable laws.** Fix \(k\geq1\), set \(n=k+2\) and \(\varepsilon=2^{-(n+1)}\), and define, for \(j=0,\ldots,n\),
\[
b_j=2^{-n}\binom nj,\qquad
v_j=\begin{cases}(-1)^{n-1-j}\binom{n-1}j,&0\leq j\leq n-1,\\0,&j=n.\end{cases}
\]
Set \(\mathbb P_{\pm}(K=j)=b_j\pm\varepsilon v_j\), and conditional on \(K=j\), choose the extinct set uniformly among \(j\)-element subsets. Because \(|\varepsilon v_j|/b_j\leq1/2\) for \(j<n\), these are strictly positive distributions. The finite-difference identity
\[
\sum_{j=0}^{n-1}(-1)^{n-1-j}\binom{n-1}j f(j)=0\quad\text{for every polynomial }\deg f\leq n-2
\tag{2}
\]
shows that the falling-factorial moments of \(K\) agree through degree \(n-2=k\). Exchangeability implies that every specified \(r\)-element set has joint extinction probability \(q_r=\mathbb E[(K)_r]/(n)_r\). Thus \(q_r^+=q_r^-\) for \(0\leq r\leq k\). Since \(v_n=0\), also \(q_n^+=q_n^-\). Only the \(j=n-1\) term contributes to the difference in the \((n-1)\)-st moment, so
\[
q_{n-1}^{\pm}=2^{-(n-1)}\pm\frac{\varepsilon}{n},
\qquad q_{n-1}^+-q_{n-1}^-=\frac{2\varepsilon}{n}>0.
\tag{3}
\]

**4. The sharp tree and unique decision reversal.** Give the root one child subtending a clade \(A\) with \(n-1\) leaves and another child the isolated leaf \(d\). The edge leading to \(A\) has length one. Within \(A\), choose any rooted binary refinement and a distinguished leaf \(a\). Give \(a\)'s pendant edge length one, and every other internal/pendant edge within \(A\) the same small positive length \(\delta\). Set the pendant length of \(d\) to \(L_d=G_a^{(0)}/q_1\), where \(G_a^{(0)}\) is the gain at \(a\) under the unperturbed binomial law \((b_j)\); here \(q_1=1/2\), so \(L_d>0\). The base law yields \(G_a^{(0)}=G_d^{(0)}\). Because only \(q_{n-1}\) changes between \(\mathbb P_-\) and \(\mathbb P_+\) among proper clades, (1) and (3) give
\[
G_a^--G_d^-=-\frac{\varepsilon}{n}<0,
\qquad G_a^+-G_d^+=\frac{\varepsilon}{n}>0.
\tag{4}
\]
Every other leaf in \(A\) shares the length-one ancestral edge with \(a\); as \(\delta\downarrow0\), \(a\) has a further gain \(q_1=1/2\) from its length-one pendant edge, whereas each competing leaf has no positive-length edge beyond that shared ancestor. By continuity, choosing a sufficiently small \(\delta>0\) guarantees that \(G_a^{\pm}>G_x^{\pm}\) for every \(x\in A\setminus\{a\}\). Formula (4) then makes \(d\) the unique maximizer under \(\mathbb P_-\) and \(a\) the unique maximizer under \(\mathbb P_+\). All edges are strictly positive, every subset has positive extinction probability, and the two laws are exchangeable. This proves sharpness for every \(k\geq1\).

**5. Explicit four-leaf instance.** With \(k=2\), the two distributions in the Finding section are obtained by the same perturbation. Directly from (1),
\[
G_a=3q_1+q_2+8q_3,\quad G_b=\tfrac18q_1+q_2+8q_3,\quad G_c=\tfrac18q_1+8q_3,\quad G_d=\tfrac{11}2q_1.
\]
Substituting \(q_1,q_2,q_3\) gives all eight fractions above and proves both unique optimality assertions. This is an exact finite witness, not a numerical simulation.

## Verification
The standalone \(\texttt{check.py}\) uses only Python's standard library. For \(3\leq n\leq10\), it verifies positivity of the two extinction-count laws, normalization, equal marginal moments through degree \(n-2\), equal all-extinct probability and the exact separating moment. For the four-leaf tree it independently enumerates all 16 possible extinction subsets and directly compares the change of rooted phylogenetic diversity under each protective action, then compares that with the branchwise formula. All tests passed. The universal proof for every \(n\geq3\) is equations (1)–(4), **not** the finite code tests.

## Relationship to prior work
Steel–Mimoto–Mooers (2007) develop expected contributions to rooted phylogenetic diversity using independent extinction probabilities, and Faller–Steel (2009) derive expected PD and variance under correlated ecological-network extinctions. Thus the general branchwise event viewpoint and dependence sensitivity are **prior art**. Simianer (2007/2008) explicitly shows that dependent extinctions can reverse conservation priorities under the Weitzman diversity measure and notes the difficulty of estimating higher-order extinction probabilities. Therefore neither correlation-sensitive priorities nor pairwise data limitations in an informal sense are claimed new. The present exact result is specifically the sharp order-versus-tree-size theorem and the all-order exchangeable reversal construction while matching all lower-order joint extinctions and the full-extinction probability on the *same rooted-PD tree*. Ingram–Steel (2010) analyze network-correlated expected rooted PD but do not establish this decision-ranking cutoff in the inspected sections.

## Limitations
The probability laws are mathematical scenarios; they need not arise from a particular ecological dynamics, and exchangeability of extinction does not mean independence. Protecting one species is defined as forcing its presence while leaving the fate of all others unchanged; interactive ecological responses to protection are outside scope. The statement concerns a **single** equal-cost intervention, not multi-species budget allocation, empirical recommendations, or identifiability from noisy estimated probabilities. Historical priority has not been independently verified. The general all-order construction chooses a sufficiently small \(\delta\) existentially, while the four-taxon witness specifies every branch length rationally.

## References
1. Steel, M., Mimoto, A., and Mooers, A. O. (2007). *Hedging our bets: the expected contribution of species to future phylogenetic diversity*. arXiv:0704.2649, first submitted 2007-04-20. https://arxiv.org/abs/0704.2649
2. Faller, B. and Steel, M. (2009). *Trait-dependent extinction leads to greater expected biodiversity loss*. arXiv:0911.3441. https://arxiv.org/abs/0911.3441
3. Simianer, H. (2007/2008). *Accounting for non-independence of extinction probabilities in the derivation of conservation priorities based on Weitzman's diversity concept*. Conservation Genetics. doi:10.1007/s10592-007-9319-x. https://doi.org/10.1007/s10592-007-9319-x
4. Ingram, T. and Steel, M. (2010). *Modelling the unpredictability of future biodiversity in ecological networks*. Journal of Theoretical Biology. https://www.math.canterbury.ac.nz/~m.steel/Non_UC/files/research/ecofob_jtb.pdf
