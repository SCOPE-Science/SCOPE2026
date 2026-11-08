# Sharp total-variation Cayley-core approximation for split-graph spanning trees

## Finding

**Theorem (exact geometric approximation and its sharp threshold).** Let \(a\ge2\) and \(b\ge a-1\) be integers. Write \(G_{a,b}=K_a\vee\overline K_b\), with a distinguished labeled clique \(C\) of order \(a\) and labeled independent set \(B\) of order \(b\), and let \(P_{a,b}\) be the uniform law on spanning trees of \(G_{a,b}\). Define \(Q_{a,b}\) by the following exact constructive law:

1. Choose a uniform labeled Cayley tree \(S\) on \(C\).
2. Injectively assign \(a-1\) distinct labels from \(B\), uniformly, to the edges of \(S\). Subdivide each edge of \(S\) once with its assigned vertex.
3. Attach each remaining label of \(B\) as a leaf to an independent uniform vertex of \(C\).

Let \(E_{a,b}\) be the event that a spanning tree has no edge within \(C\) and every vertex of \(B\) has degree at most two. Then \(Q_{a,b}=P_{a,b}(\,\cdot\mid E_{a,b})\) exactly and

\[
\boxed{d_{\mathrm{TV}}(P_{a,b},Q_{a,b})=1-\frac{(b)_{a-1}}{(a+b)^{a-1}}},\qquad
(b)_k:=b(b-1)\cdots(b-k+1).
\]

Thus for integers \(a\to\infty\), \(b\ge a-1\), with \(a^2/b\to\lambda\in[0,\infty]\), this total-variation distance tends to \(1-e^{-3\lambda/2}\), with value \(1\) at \(\lambda=\infty\). In particular, \(Q_{a,b}\) is asymptotically exact **if and only if** \(a^2/b\to0\), and the transition occurs at \(b\asymp a^2\).

There is an explicit two-defect description at this transition. Let \(K\) be the number of clique-to-clique edges of a uniform tree, and let

\[
R=\sum_{u\in B}\binom{\deg_T(u)-1}{2}.
\]

If \(a\to\infty\) with \(a^2/b\to\lambda<\infty\), then \((K,R)\) converges jointly to **independent** Poisson variables of means \(\lambda\) and \(\lambda/2\), respectively. The event \(E_{a,b}\) is exactly \(\{K=R=0\}\) when \(b\ge a-1\).

As a geometric consequence, if \(a\to\infty\) and \(b/a^2\to\infty\), then for any two distinct marked clique vertices \(u,v\), their distance in \(T\sim P_{a,b}\) satisfies

\[
\frac{d_T(u,v)}{2\sqrt a}\ \Longrightarrow\ Z,
\qquad \Pr(Z>x)=e^{-x^2/2}\quad(x\ge0).
\]

Here \(Z\) has the Rayleigh distribution with unit scale.

## Assumptions and scope

All graphs are finite, labeled, simple, unweighted, connected and undirected. The join \(K_a\vee\overline K_b\) contains every clique edge, every edge between \(C\) and \(B\), and no edge between two vertices of \(B\). Uniform means every spanning tree has the same probability. The total-variation distance is \(\sup_A |P(A)-Q(A)|\) on labeled spanning trees. The exact degree law below holds for \(a\ge2,b\ge1\), including \(b<a-1\); the decorated-tree model requires \(b\ge a-1\). The Poisson and Rayleigh statements require the growth conditions explicitly given above. No edge-weighted sampling or unlabelled-tree measure is intended.

## Proof

**1. An exact multivariate degree polynomial (known enumerator, specialized explicitly).** Put formal weight \(t\) on every edge inside \(C\); give each edge incident to independent vertex \(u_j\in B\) formal weight \(y_j\). Write \(S=y_1+\cdots+y_b\). By the weighted matrix-tree theorem, the spanning-tree partition function is a Laplacian cofactor. After deleting one clique row and column, eliminate the diagonal block \(\operatorname{diag}(a y_1,\ldots,a y_b)\) by a Schur complement. The remaining \((a-1)\times(a-1)\) matrix is

\[
(a t+S) I_{a-1}-(t+S/a)J_{a-1}.
\]

Its determinant is \((a t+S)^{a-1}/a\), because the all-ones eigenvalue is \((a t+S)/a\) and the other \(a-2\) eigenvalues are \(a t+S\). Consequently the exact polynomial is

\[
\sum_{T}\,t^{K(T)}\prod_{j=1}^b y_j^{\deg_T(u_j)}
=a^{b-1}\left(\prod_{j=1}^b y_j\right)
\left(a t+\sum_{j=1}^b y_j\right)^{a-1}.
\tag{1}
\]

The identity is polynomial, so the temporary inversion of the diagonal block is justified on the open set where all \(y_j\ne0\), and then algebraically everywhere. At \(t=y_j=1\), the spanning-tree count is \(a^{b-1}(a+b)^{a-1}\). Dividing (1) by this count proves that the vector

\[
\big(K,\deg_T(u_1)-1,\ldots,\deg_T(u_b)-1\big)
\sim\mathrm{Multinomial}\left(a-1;\frac a{a+b},\underbrace{\frac1{a+b},\ldots,\frac1{a+b}}_{b\text{ categories}}\right).
\tag{2}
\]

This forward enumerator is not asserted as new: it is a specialization of classical weighted multipartite spanning-tree enumeration.

**2. The geometric event and exact conditional law.** Since all \(b\) independent vertices have degree at least one, the number of extra incidences \(\sum_{u\in B}(\deg_T(u)-1)\) equals \(a-1-K\). Thus \(K=0\) and \(R=0\) mean that exactly \(a-1\) vertices in \(B\) have degree two, and all remaining vertices in \(B\) have degree one. In any tree meeting this condition, contracting each degree-two independent vertex leaves a connected acyclic graph on \(C\) with exactly \(a-1\) edges, necessarily a labeled Cayley tree. The contractions uniquely recover the distinct subdividing labels; all other independent vertices are attached leaves. Conversely, the three-stage construction always produces a tree in \(E_{a,b}\) and has a unique inverse. Every favorable labeled spanning tree receives the same probability under the construction, since all Cayley trees, injective edge-to-vertex assignments, and remaining leaf attachments are sampled uniformly.

There are \(a^{a-2}\) Cayley core trees, \((b)_{a-1}\) injective connector assignments, and \(a^{b-a+1}\) leaf attachment choices. Hence \(\#E_{a,b}=a^{b-1}(b)_{a-1}\), giving

\[
P_{a,b}(E_{a,b})=\frac{(b)_{a-1}}{(a+b)^{a-1}}.
\tag{3}
\]

Because \(Q=P(\,\cdot\mid E)\) and \(Q(E)=1\), their total variation distance is exactly \(1-P(E)\), not just bounded by it.

**3. The sharp transition.** For \(a^2/b\to\lambda<\infty\) and \(a\to\infty\), necessarily \(a/b\to0\). Taking logarithms of (3),

\[
\log P(E)=\sum_{i=0}^{a-2}\log\left(1-\frac i b\right)-(a-1)\log\left(1+\frac a b\right)
=-\frac{(a-1)(3a-2)}{2b}+O\left(\frac{a^3}{b^2}\right),
\tag{4}
\]

where the remainder is uniform when \(a/b\) is sufficiently small. It tends to \(-3\lambda/2\). If \(a^2/b\to\infty\), the bound \(P(E)\le[b/(a+b)]^{a-1}\le\exp(-a(a-1)/(a+b))\) tends to zero (since \(a\to\infty\) and \(b\ge a-1\)). More generally, if the total-variation distance tends to zero, the same bound implies \(a(a-1)/(a+b)\to0\), which forces \(a^2/b\to0\) for \(a\to\infty\). This proves the asserted necessary and sufficient condition without assuming that \(a^2/b\) already converges.

**4. The two independent Poisson defect mechanisms.** Identity (2) has a sampling interpretation: throw \(a-1\) independent tokens, choosing a special clique-edge category with probability \(a/(a+b)\), and otherwise selecting any of the \(b\) independent-vertex categories with equal probability \(1/(a+b)\). Then \(K\sim\mathrm{Bin}(a-1,a/(a+b))\), hence \(K\Rightarrow\mathrm{Pois}(\lambda)\) when \(a^2/b\to\lambda<\infty\). Given \(K=k\), the remaining \(L=a-1-k\) tokens are independent and uniform among \(b\) categories. The number \(R\) is precisely their number of colliding unordered pairs. For \(L/\sqrt b\to\sqrt\lambda\), the factorial-moment expansion of this pair count has a leading contribution from \(r\) vertex-disjoint colliding pairs, tending to \((\lambda/2)^r\), while every configuration containing a collision cluster of at least three tokens is \(o(1)\). Thus \(R\Rightarrow\mathrm{Pois}(\lambda/2)\). Since \(K\) is tight and the conditional limit for \(R\) is unchanged when \(k\) varies over any fixed finite set, these two limiting variables are independent. For \(\lambda=0\), both converge to zero, also by first moments. The zero-defect limit agrees with (4).

**5. The geometric distance limit.** In a uniform Cayley tree on \(a\) vertices, for two distinct fixed vertices let \(D_a\) be their graph distance. Counting the ordered internal vertices on the unique path and rooted forests attached to that path gives, for \(1\le d\le a-1\),

\[
\Pr(D_a=d)=\frac{(d+1)(a-2)_{d-1}}{a^d},
\qquad \Pr(D_a>d)=\frac{(a-2)_d}{a^d}.
\tag{5}
\]

For \(d=\lfloor x\sqrt a\rfloor\) the latter product converges to \(e^{-x^2/2}\). Under the decorated law \(Q\), the distance between the same two clique vertices is exactly \(2D_a\). If \(b/a^2\to\infty\), (3) shows \(d_{\mathrm{TV}}(P,Q)\to0\); therefore the distance law under \(P\) has the same Rayleigh limit.

## Verification

The standalone `verify.py` independently enumerates all spanning trees of the nine labeled split graphs with \(2\le a\le4\), \(1\le b\le3\), checking the total count, **every** vector of clique-edge count and independent-vertex degree surplus against the exact multinomial coefficient, the favorable-event count, and a separate symbolic Kirchhoff determinant. It additionally enumerates Cayley trees via Prüfer sequences for \(2\le a\le7\), checking every two-vertex distance probability in (5). Run `python verify.py` with Python 3 and SymPy. The script is a finite corroboration; the determinant, bijection, asymptotic expansions and factorial-moment proof establish the all-order theorem.

## Relationship to prior work

The weighted matrix-tree and complete multipartite enumerators in Klee and Stamps (2019), originating in Clark's earlier weighted formula, already imply the forward degree generating identity (1); it is included as a proof tool, **not a new result**. Dong and Ge (2021) calculate spanning-tree counts containing fixed forests in complete bipartite graphs. Egecioglu and Remmel (1994) developed multipartite-tree bijections and asymptotic leaf statistics; their full text was not recovered for this comparison. Nachmias and Peres (2020) establish universal local limits on regular or high-degree almost-regular graphs, which do not apply to the strongly imbalanced split graphs in the stated scaling. The assessed contribution is the exact **geometric** conditional-law identification and optimal total-variation formula, the independent two-defect critical limit with coefficient \(3/2\), and the resulting clique-distance law. These statements concern whole-tree geometry and a singular joint-growth regime rather than only the already-known weighted enumerator.

## Limitations

Novelty is assessed against the cited material and searchable records, not guaranteed historical uniqueness. The 1994 multipartite bijection paper and the body of Li–Chen–Yan (2023) were not available in full text in the accessible sources; both present residual historical-priority risks. No claim is made that (1), elementary Cayley enumeration, or classical birthday Poisson convergence is new. The exact coupling is for complete split graphs with labeled vertices; its Rayleigh conclusion requires \(b\gg a^2\). The result does not address a different split graph with missing cross edges, weighted trees, or arbitrary multipartite growth. The finite checker is not an independent infinite proof.

## References

- A. Nachmias and Y. Peres, *The local limit of uniform spanning trees*, arXiv:2011.08833v1, first public 2020-11-17, https://arxiv.org/html/2011.08833v1.
- S. Klee and M. T. Stamps, *Linear algebraic techniques for weighted spanning tree enumeration*, arXiv:1903.03575, first public 2019-02-27, https://arxiv.org/abs/1903.03575.
- F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294v1, first public 2021-03-09, https://arxiv.org/html/2103.05294v2.
- O. Egecioglu and J. B. Remmel, *A bijection for spanning trees of complete multipartite graphs*, Congressus Numerantium 100 (1994), 225–243, abstract https://sites.cs.ucsb.edu/~omer/personal/abstracts/multipartite.html.
- D. Li, W. Chen, and W. Yan, *Enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest*, J. Graph Theory 104 (2023), 160–170, DOI:10.1002/jgt.22954.
