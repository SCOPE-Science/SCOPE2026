# Matching-pattern correlations in uniform interconnection trees

## Finding

**Theorem (projected matching-event law).** Fix an integer \(k\ge3\) and integers \(n_1,\ldots,n_k\ge1\). Let \(G=K_{n_1,\ldots,n_k}\) be the complete multipartite graph with named parts \(V_1,\ldots,V_k\), and suppose \(N=\sum_i n_i\ge2(k-1)\). Choose uniformly at random an **interconnection tree** \(T\): a matching of \(k-1\) edges in \(G\) whose projection \(S\) onto the part indices \(\{1,\ldots,k\}\) is a spanning tree. Put

\[
a_i=n_i-1,\qquad M=\sum_{i=1}^k a_i=N-k,\qquad w_{ij}=a_i+a_j=n_i+n_j-2.
\]

For every matching \(F\) of \(r\) unordered pairs of **distinct part indices**, where \(1\le r\le\lfloor k/2\rfloor\), one has the exact joint inclusion law

\[
\boxed{\displaystyle
\Pr\!\left(F\subseteq E(S)\right)
=\frac{\prod_{\{i,j\}\in F}(n_i+n_j-2)}{(M)_{\underline r}}\,,\qquad
(M)_{\underline r}=M(M-1)\cdots(M-r+1).}
\]

In particular, every pair of vertex-disjoint possible projected links \(e=\{i,j\}\), \(f=\{u,v\}\), with \(w_e,w_f>0\), is **strictly positively correlated**:

\[
\boxed{\displaystyle
\operatorname{Cov}\!\left(\mathbf 1_{e\in S},\mathbf 1_{f\in S}\right)
=\frac{w_e w_f}{M^2(M-1)}>0.}
\]

If either \(w_e\) or \(w_f\) vanishes, the corresponding projected link is impossible and its covariance is zero. When \(F\) has positive probability and \(e\) is disjoint from all pairs of \(F\), the formula also gives \(\Pr(e\in S\mid F\subseteq E(S))=w_e/(M-|F|)\). This is a statement about *quotient-tree links*, not about specified physical edges of \(G\).

## Assumptions and scope

All graphs are finite and simple. The \(k\) parts are individually distinguished, and physical vertices are distinguished within parts. The random choice is uniform among all physical interconnection-tree edge sets, rather than uniform among quotient spanning trees. The size condition \(N\ge2(k-1)\), equivalent to \(M\ge k-2\), guarantees existence of physical matchings with \(k-1\) edges. A matching \(F\) in the statement consists of pairwise vertex-disjoint *part-index pairs*. It need not be a matching of physical vertices, as each chosen index pair represents a possible type of physical edge. Since \(k\ge3\), any quotient spanning tree has positive degree at every index. Falling factorials \((b)_{\underline m}\) are interpreted as \(b(b-1)\cdots(b-m+1)\) for nonnegative integers \(b,m\), with \((b)_{\underline0}=1\) and \((b)_{\underline m}=0\) when \(m>b\).

## Proof

**1. Physical realizations of a fixed quotient spanning tree.** Let \(S\) be any labeled spanning tree on the part indices, and let \(d_i=\deg_S(i)\). To realize \(S\) as a physical matching, assign a distinct vertex in \(V_i\) to each of the \(d_i\) incident quotient edges; these choices determine all physical edges without further constraints because \(G\) is complete multipartite. Thus the number of realizations is

\[
\prod_{i=1}^k(n_i)_{\underline {d_i}}
=\left(\prod_{i=1}^k n_i\right)
\prod_{i=1}^k(a_i)_{\underline {d_i-1}}.
\]

This fixed-quotient count is already part of the enumeration method of Demange and Strozecki [1]; it is not claimed to be new.

**2. A forest-restricted Prüfer polynomial.** For formal commuting indeterminates \(x_1,\ldots,x_k\), define

\[
P_F(\mathbf x)=\sum_{S\supseteq F}\prod_{i=1}^k x_i^{\deg_S(i)-1},
\]

where the sum is over labeled spanning trees of \(K_k\) containing the part-index matching \(F\). If \(|F|=r\), contracting the edges of \(F\) gives \(c=k-r\) components: \(r\) two-index components and \(k-2r\) singletons. Write \(X_C=\sum_{i\in C}x_i\). For a spanning tree \(U\) on the \(c\) components, summing the weights of the possible endpoints of each intercomponent edge contributes \(X_CX_D\) for each \(\{C,D\}\in U\). The weighted Cayley identity, an immediate Prüfer-sequence consequence, is

\[
\sum_U\prod_{\{C,D\}\in U}X_CX_D
=\left(\sum_C X_C\right)^{c-2}\prod_C X_C.
\]

Before adding intercomponent edges, the exponent of \(x_i\) is \(\deg_F(i)-1\). Multiplying by this base weight cancels each singleton component's factor \(x_i\), while each two-index component contributes \(x_i+x_j\). Consequently

\[
\boxed{\displaystyle
P_F(\mathbf x)=
\left(\sum_{i=1}^k x_i\right)^{k-r-2}
\prod_{\{i,j\}\in F}(x_i+x_j).}
\]

The exponent \(k-r-2\) is nonnegative for every admissible \(r\). The unrestricted case is the ordinary Prüfer identity \(P_{\varnothing}(\mathbf x)=(\sum_i x_i)^{k-2}\).

**3. Evaluation by falling-factorial moments.** Define a linear map on monomials by

\[
\mathcal L\!\left(\prod_i x_i^{m_i}\right)
=\prod_i(a_i)_{\underline {m_i}}.
\]

By step 1, the number of physical interconnection trees whose quotient contains \(F\) equals \((\prod_i n_i)\mathcal L(P_F)\). Let \(s=k-r-2\). In each term obtained by expanding \(\prod_{\{i,j\}\in F}(x_i+x_j)\), one selects one endpoint of each pair. These selected \(r\) indices are distinct. For any such set \(J\) of size \(r\), the falling-factorial identity \((a)_{\underline{m+1}}=a(a-1)_{\underline m}\), followed by the multinomial form of Vandermonde's identity, gives

\[
\mathcal L\!\left[\left(\sum_i x_i\right)^s\prod_{j\in J}x_j\right]
=s!\binom{M-r}{s}\prod_{j\in J}a_j.
\]

If some selected \(a_j=0\), both sides vanish, so this calculation also covers singleton parts. Summing over the independent endpoint choices within the \(r\) pairs yields

\[
\mathcal L(P_F)
=s!\binom{M-r}{s}\prod_{\{i,j\}\in F}(a_i+a_j).
\]

The corresponding unrestricted count is

\[
\mathcal L(P_{\varnothing})
=(k-2)!\binom M{k-2}.
\]

Since \(s=k-r-2\), the ratio of the scalar factors simplifies exactly to

\[
\frac{s!\binom{M-r}{s}}{(k-2)!\binom M{k-2}}
=\frac{(M-r)!}{M!}=\frac1{(M)_{\underline r}}.
\]

Dividing the restricted count by the unrestricted count proves the claimed joint probability, with no asymptotic or probabilistic approximation.

**4. Dependence.** For one projected link \(e\), the law gives \(\Pr(e\in S)=w_e/M\). For disjoint links \(e,f\), it gives \(\Pr(e,f\in S)=w_ew_f/[M(M-1)]\). The difference from the product of marginals is precisely \(w_ew_f/[M^2(M-1)]\). The denominator is positive because disjoint links require \(k\ge4\), and the size condition then gives \(M\ge k-2\ge2\). Strict positivity holds if and only if both links have positive weight. The conditional identity follows by dividing the \((r+1)\)-edge probability by the \(r\)-edge probability when the conditioning event has positive probability. This completes the proof.

## Verification

The standalone `verify.py` program uses exact integer and rational arithmetic, with no third-party packages. One check enumerates every labeled quotient tree via Prüfer sequences, weights it by independently computed physical realization factors \(\prod_i(n_i)_{\underline{\deg_S(i)}}\), and checks the displayed probability for **6,312** pairs of part profiles and index-edge matchings: all admissible \(k=3,4,5\), all part sizes from \(\{1,2,3\}\), and all nonempty disjoint index-pair matchings. A separate edge-subset enumeration, using no Prüfer encoding, reconstructs the actual physical matchings in six selected profiles and tests the same identity. Both checks pass under `python verify.py`. These finite checks support, but do not replace, the proof for arbitrary integers.

For a concrete strict-dependence example, take \((n_1,n_2,n_3,n_4)=(2,2,1,1)\) and the disjoint quotient edges \(e=\{1,3\}\), \(f=\{2,4\}\). Then \(M=2\), \(w_e=w_f=1\), so the marginals are \(1/2\), the joint probability is \(1/2\), and the covariance is \(1/4\). Direct enumeration finds eight physical interconnection trees and exactly four containing both quotient links. As another consistency check, summing \(\Pr(\{i,j\}\in S)=w_{ij}/M\) over all quotient edges yields \(k-1\), the number of edges in every quotient spanning tree.

## Relationship to prior work

Demange and Strozecki [1] introduced interconnection trees, proved the existence criterion for complete multipartite graphs, and obtained both the fixed-quotient weighted count and the total count \((k-2)!\binom M{k-2}\prod_i n_i\) (their Theorem 11). The present result does **not** claim either enumeration as new. The contribution is the exact probability for simultaneously prescribed pairwise disjoint quotient links, its all-orders conditional formula, and the strict positive covariance for two possible disjoint links. These conclusions require the forest-restricted weighted Prüfer evaluation carried out above; they are not stated in [1].

For comparison, disjoint edge-presence events are independent in a uniformly sampled ordinary Cayley tree on a complete graph, as recorded in the Lu–Mohr–Székely lemma quoted in Vondrák's notes [2]. The physical matching constraint changes the law on quotient trees and reverses the zero-covariance phenomenon. This contrast concerns two different probability spaces and does not assert independence or positivity for individual physical edges.

## Limitations

The exact product law is proved only when the required **projected** links are pairwise vertex-disjoint; projected links sharing part indices need not obey this product formula. The graph must be complete multipartite, and sampling must be uniform over physical interconnection trees. We do not claim a corresponding formula for incomplete multipartite graphs, for prescribed actual physical edges, for arbitrary projected forests, or for general weighted sampling. The total counting theorem and fixed-projection weights used in the proof are previously published. A possibility remains that an unindexed treatment of capacity-weighted Cayley trees contains an equivalent event formula; mathematical novelty is not a claim of exhaustive bibliographic uniqueness. No independent external validation has been performed.

## References

[1] Noé Demange and Yann Strozecki, *Complexity of Finding and Enumerating Interconnection Trees*, arXiv:2605.18125, first posted 2026-05-18, especially Definition 3, Theorem 11 and its proof, and Section 5. https://arxiv.org/abs/2605.18125 . A lawful public full text was inspected at https://www.researchgate.net/publication/404996733_Complexity_of_Finding_and_Enumerating_Interconnection_Trees .

[2] Jan Vondrák, *Math 233, Lecture 4: The Lopsided Lovász Local Lemma*, Stanford University, 2016-04-04, Lemmas 4.11–4.12 (attributing the disjoint-edge independence lemma to Lu, Mohr and Székely, 2012). https://theory.stanford.edu/~jvondrak/MATH233-2016/Math233-lec04.pdf .
