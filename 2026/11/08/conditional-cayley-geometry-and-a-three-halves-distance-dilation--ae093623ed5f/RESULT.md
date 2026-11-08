# Conditional Cayley geometry and a three-halves distance dilation for perfectly matchable bipartite spanning trees

## Finding
Let \(T_n\) be a uniformly selected spanning tree of the complete bipartite graph \(K_{n,n}\), with labeled sides \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), and let \(\mathcal P_n\) be the event that \(T_n\) has a perfect matching. For every integer \(n\ge2\),
\[
\Pr(\mathcal P_n)=\frac{2^{n-1}n!}{n^n}.
\]
Conditional on \(\mathcal P_n\), its unique perfect matching \(M_n\) is uniform over the \(n!\) bipartite perfect matchings. Given \(M_n\), contract its edges and label each contracted vertex by the index of its \(A\)-endpoint. The resulting graph \(C_n\) is a **uniform Cayley tree** on \(n\) labels, independent of \(M_n\). Conditional on \((M_n,C_n)\), each edge \(\{i,j\}\) of \(C_n\) is independently lifted, with probability \(1/2\) each, to either \(a_i b_{\sigma(j)}\) or \(a_j b_{\sigma(i)}\), where \(M_n=\{a_i b_{\sigma(i)}:1\le i\le n\}\); the matching edges are then restored.

For distinct \(i,j\), write \(L=d_{C_n}(i,j)\). With \(H\sim\operatorname{Bin}(L-1,1/2)\) and an independent fair sign \(\xi\in\{-1,1\}\), the *exact* conditional distance law is
\[
d_{T_n}(a_i,a_j)\ \stackrel{d}{=}\ 2L-H+\xi\,\mathbf 1_{\{H\text{ odd}\}}.
\]
In particular, \(\mathbb E[d_{T_n}(a_i,a_j)\mid C_n,M_n]=(3L+1)/2\). For \(L\ge2\), its conditional variance is \((L+1)/4\); for \(L=1\) it is zero.

Let \(U_n,V_n\) be two uniformly chosen distinct vertices of \(T_n\), independent of the sampled tree. Under the conditional law given \(\mathcal P_n\),
\[
\frac{d_{T_n}(U_n,V_n)}{\sqrt n}\ \Longrightarrow\ \frac32 R,
\qquad \Pr(R>x)=e^{-x^2/2}\quad(x\ge0).
\]
The factor \(3/2\) holds for the whole metric space: if \(\mathcal C\) denotes the standard \(n^{-1/2}\)-rescaled uniform Cayley-tree measured-metric limit, then the conditional measured spaces \((V(T_n),n^{-1/2}d_{T_n},\mathrm{Unif}(V(T_n)))\) converge in distribution in Gromov–Hausdorff–Prokhorov topology to \((3/2)\mathcal C\), with the same mass measure. Here \(\mathcal C\) is the Brownian continuum random tree in the normalization inherited from unit-edge Cayley trees. The exact probability above is a known consequence of spanning-forest counting; the conditional metric dilation is the focus of this result.

## Assumptions and scope
The ambient graph is unweighted, simple, labeled, and balanced complete bipartite; \(n\ge2\). The tree is sampled uniformly from all \(n^{2n-2}\) spanning trees, then conditioned on \(\mathcal P_n\). All independent edge-lift coins are fair. Distances count graph edges, and \(\operatorname{Bin}(0,1/2)\) is identically zero. The continuum limit is taken as \(n\to\infty\), only under the stated conditional law. The one- and two-point finite assertions are exact for every listed \(n\).

## Proof
**1. Exact conditional construction.** Two distinct perfect matchings of a tree would have a symmetric difference containing an even cycle, so every tree has at most one perfect matching. Fix \(M=\{a_i b_{\sigma(i)}\}\). Contract its \(n\) edges. Between every distinct pair of contracted vertices \(i,j\) there are exactly two possible original edges, \(a_i b_{\sigma(j)}\) and \(a_j b_{\sigma(i)}\). Thus the contracted multigraph is the complete graph with two parallel edges per pair, and spanning trees containing \(M\) correspond bijectively to a Cayley tree on \(n\) vertices plus one of two edge lifts independently chosen for each of its \(n-1\) edges. The number is \(2^{n-1}n^{n-2}\) for each matching. There are \(n!\) choices of \(M\), and \(K_{n,n}\) has \(n^{2n-2}\) spanning trees. These facts give the probability and the exact product conditional law.

**2. Exact distance distribution.** Orient the contracted path from \(i\) to \(j\), with \(L\) edges. For its \(t\)-th edge, let \(c_t=1\) if the lift leaves the preceding pair from its \(A\)-vertex, and \(c_t=0\) otherwise. The \(c_t\) are independent fair bits. At the starting pair, the path from \(a_i\) contributes an extra matching edge iff \(c_1=0\); at the ending pair, it contributes one iff \(c_L=1\). At each interior pair, the two adjacent lifted edges meet different endpoints iff \(c_t=c_{t+1}\). Hence
\[
 d_{T_n}(a_i,a_j)=L+(1-c_1)+c_L+\sum_{t=1}^{L-1}\mathbf1_{\{c_t=c_{t+1}\}}
 =2L-H-c_1+c_L,
\]
where \(H=\sum_{t=1}^{L-1}\mathbf1_{\{c_t\ne c_{t+1}\}}\). The map from \((c_1,\ldots,c_L)\) to the initial bit and the \(L-1\) successive change bits is bijective, so \(H\sim\operatorname{Bin}(L-1,1/2)\). The endpoint difference is zero for even \(H\), and has a fair independent sign for odd \(H\). This proves the law, mean and variance (including the \(L=1\) boundary).

**3. Rayleigh pair-distance limit.** In a uniformly random labeled Cayley tree, the distance \(L_n\) between two specified distinct labels satisfies, exactly,
\[
 \Pr(L_n>k)=\frac{(n-2)_k}{n^k}\quad(0\le k\le n-1),
\]
where \((u)_k=u(u-1)\cdots(u-k+1)\). To derive it, count the ordered \(k-1\) interior vertices of a path of length \(k\), then apply the standard forest-contraction count \((k+1)n^{n-k-2}\) to each path; telescoping the resulting mass function yields the displayed tail. For \(k=\lfloor x\sqrt n\rfloor\), the logarithm of the product tends to \(-x^2/2\), proving \(L_n/\sqrt n\Rightarrow R\). Conditional on \(L_n\), the lift contributes mean \((L_n+1)/2\) extra edges and variance at most a constant times \(L_n\); by tightness of \(L_n/\sqrt n\), the centered contribution divided by \(\sqrt n\) vanishes in probability. Choosing two random vertices instead of two fixed \(A\)-vertices changes only bounded endpoint matching costs; the two vertices belong to the same matched pair with probability \(1/(2n-1)\). Thus the asserted \((3/2)R\) limit holds.

**4. Entire-space dilation.** Let \(\pi\) send each original vertex to its matched pair. For every two vertices in different pairs at contracted distance \(L\), irrespective of their endpoint types, the expected lifted distance is \((3L+1)/2\), and flipping one lift coin changes the distance by at most two. Bounded-difference concentration therefore gives
\[
 \Pr\!\left(\left|d_{T_n}(u,v)-\mathbb E[d_{T_n}(u,v)\mid C_n,M_n]\right|>t\mid C_n,M_n\right)
 \le 2e^{-t^2/(2L)}.
\]
The diameter of the uniform Cayley tree divided by \(\sqrt n\) is tight, by the classical Cayley-tree continuum-limit theorem. On \(\{\operatorname{diam}(C_n)\le K\sqrt n\}\), use the displayed tail bound with \(t=n^{3/8}\), then union bound over at most \(4n^2\) ordered vertex pairs. It follows that
\[
 \max_{u,v\in V(T_n)}\bigl|d_{T_n}(u,v)-\tfrac32d_{C_n}(\pi u,\pi v)\bigr|=o_{\Pr}(\sqrt n).
\]
For vertices in the same pair the discrepancy is at most one. The projection \(\pi\) pushes the uniform measure on the \(2n\) original vertices exactly to the uniform measure on the \(n\) matched pairs. The correspondence induced by \(\pi\) thus has vanishing rescaled distortion and a measure-preserving coupling; the Gromov–Hausdorff–Prokhorov limit follows from the established Cayley-tree convergence.

## Verification
Run `python3 verify.py` in the same directory (Python standard library only). The checker enumerates all spanning trees of \(K_{n,n}\) for \(n=2,3,4\) independently as edge subsets; verifies unique perfect matchings, exact counts, the uniform Cayley quotient with every edge orientation, and the conditional shortest-path distribution by graph breadth-first search. It separately enumerates Cayley trees by Prüfer sequences for \(2\le n\le6\) to check the exact distance formula. Successful replay reports `VERIFY_OK 943 exact assertions`. These finite checks corroborate the combinatorial lemmas; the Rayleigh and metric-space limits are established by the proof, not by enumeration.

## Relationship to prior work
Bérczi, Király, Kobayashi, Yamaguchi and Yokoi (arXiv:2407.02958; first public July 3, 2024) study algorithmic optimization of spanning trees containing a perfect matching, including complete bipartite graphs; their results do not furnish a conditional random-tree metric limit. Dong and Ge (arXiv:2103.05294; first public March 9, 2021) provide a matching-containing spanning-tree count as a special case of a more general forest formula. Consequently, the displayed exact \(\Pr(\mathcal P_n)\) is **not** asserted to be independently new. The contribution examined here is the conditional Cayley-product law together with its exact lifted-path distribution and the resulting \(3/2\) random-metric dilation. Kargin (arXiv:2310.11530; 2023) studies continuum limits under a *leaf-number* conditioning, not perfect matchability. Classical Aldous Cayley-tree convergence is used as input and not claimed as new.

## Limitations
Historical priority cannot be certified from literature searches alone. In particular, indirect results about rare perfect-matchable trees may already imply some consequences. The proof covers the balanced complete bipartite host with uniform unit edge weights, and does not claim the same dilation for arbitrary bipartite hosts, weighted trees, or other matching constraints. It relies on the established Cayley-tree continuum-limit theorem for the full measured-space convergence; the exact conditional law and pair-distance limit are derived without that external theorem. No external independent mathematical audit has been performed.

## References
1. K. Bérczi, T. Király, Y. Kobayashi, Y. Yamaguchi, Y. Yokoi, *Finding Spanning Trees with Perfect Matchings*, arXiv:2407.02958 (v1, 2024-07-03), https://arxiv.org/abs/2407.02958.
2. F. Dong, J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294 (v1, 2021-03-09), https://arxiv.org/html/2103.05294v2.
3. V. Kargin, *Scaling limits of slim and fat trees*, arXiv:2310.11530 (v1, 2023-10-17), https://arxiv.org/abs/2310.11530.
4. D. Aldous, *The continuum random tree I*, Annals of Probability 19 (1991), 1–28, DOI:10.1214/aop/1176990534.
5. D. Aldous, *The Random Walk Construction of Uniform Spanning Trees and Uniform Labelled Trees*, SIAM J. Discrete Math. 3 (1990), 450–465, DOI:10.1137/0403039.
