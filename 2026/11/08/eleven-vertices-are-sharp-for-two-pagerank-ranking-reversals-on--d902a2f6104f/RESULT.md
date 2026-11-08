# Eleven vertices are sharp for two PageRank ranking reversals on trees

## Finding
For every finite, connected, undirected tree with at most ten vertices, the standard uniform-teleportation PageRank scores of any two vertices can reverse their strict order at most once as the damping parameter \(\alpha\) increases through \((0,1)\). At eleven vertices two reversals first occur. Among the 235 nonisomorphic eleven-vertex trees there is exactly one tree–unordered-vertex-pair isomorphism class exhibiting at least two such reversals.

An explicit witness has vertex set \(\{0,1,\ldots,10\}\), edge set
\[
\{\{0,7\},\{0,1\},\{1,2\},\{1,6\},\{2,3\},\{2,4\},\{2,5\},\{7,8\},\{7,10\},\{8,9\}\},
\]
and compares leaves \(3\) and \(10\). Their PageRank difference has the exact form
\[
\operatorname{PR}_{3}(\alpha)-\operatorname{PR}_{10}(\alpha)
=\frac{\alpha(1-\alpha)F(\alpha)}{22(1+\alpha)(72-108\alpha^2+47\alpha^4-6\alpha^6)},
\]
where
\[
F(\alpha)=3\alpha^6+4\alpha^5-18\alpha^4-16\alpha^3+26\alpha^2+12\alpha-12.
\]
The two distinct roots in \((0,1)\) are approximately \(0.661953279218271\) and \(0.933109836094827\). The same unordered-pair class has the three representatives \(\{3,10\}\), \(\{4,10\}\) and \(\{5,10\}\), owing to automorphisms permuting the leaves \(3,4,5\).

## Assumptions and scope
A graph is finite, simple, undirected, connected, and acyclic, with \(n\ge2\) vertices. Let \(A\) be its adjacency matrix and \(D\) the diagonal matrix of positive vertex degrees. For every real \(0<\alpha<1\), define the column-stochastic random-walk matrix \(W=AD^{-1}\) and the unique PageRank column vector
\[
\mathbf r(\alpha)=\frac{1-\alpha}{n}(I-\alpha W)^{-1}\mathbf1.
\]
A strict ranking reversal means the sign of \(r_u-r_v\) changes between two points in \((0,1)\). A pair has *two reversals* when its difference changes sign at least twice at successive distinct interior crossings. Identically tied pairs have no strict reversals. The theorem does not concern directed networks, nonuniform teleportation, personalized PageRank, weighted edges, or adjacency-based Katz scores.

## Proof
Write \(H(\alpha)=\det(I-\alpha W)\). Since \(W\) is similar to the symmetric matrix \(D^{-1/2}AD^{-1/2}\), its eigenvalues lie in \([-1,1]\), so \(H(\alpha)>0\) for \(0<\alpha<1\). For each vertex \(u\), write
\[
N_u(\alpha)=H(\alpha)\big[(I-\alpha W)^{-1}\mathbf1\big]_u.
\]
The adjugate identity shows that \(N_u\) is a polynomial of degree at most \(n-1\). Consequently the PageRank difference has the sign of \(P_{uv}=N_u-N_v\).

For a tree, only transpositions along disjoint edges contribute to the determinant expansion. Thus the determinant is the **weighted matching polynomial**
\[
H(\alpha)=\sum_{M\text{ a matching}}(-\alpha^2)^{|M|}
\prod_{\{i,j\}\in M}\frac{1}{d_i d_j}.
\]
Let \(y_u^{(k)}=[W^k\mathbf1]_u\). Starting with \(y_u^{(0)}=1\), compute exact rational values by
\[
y_u^{(k+1)}=\sum_{v\sim u}\frac{y_v^{(k)}}{d_v}.
\]
If \(H(\alpha)=\sum_{j=0}^{n}h_j\alpha^j\), its product with the Neumann series determines each coefficient of the numerator polynomial:
\[
[\alpha^k]N_u=\sum_{j=0}^{k}h_j y_u^{(k-j)},\qquad 0\le k<n.
\]
An exact independent polynomial identity check verifies \((I-\alpha W)\mathbf N=H\mathbf1\) in degrees \(0\) through \(n\) for every enumerated tree.

For any polynomial \(P\) of degree \(d\), the substitution \(\alpha=z/(1+z)\) maps the interval \((0,1)\) bijectively to \(z>0\). Therefore the number of interior zeros of \(P\), with multiplicities, is bounded by Descartes' sign-variation count of
\[
Q(z)=(1+z)^d P\big(z/(1+z)\big).
\]
The companion exact-arithmetic enumeration generates one representative of **every unlabelled tree** of orders two through eleven. It computes \(P_{uv}\) for every unordered vertex pair. For all \(n\le10\), every transformed polynomial has at most one sign variation, proving the universal lower bound. At \(n=11\), among 12,925 unordered vertex-pair comparisons across 235 trees, only 30 have at least two variations. Exact rational Sturm sequences, evaluated by one-sided signs at both interval endpoints, show that precisely three pairs have two distinct zeros in \((0,1)\); all three occur in the explicit tree above. These pairs form one orbit under the leaf-permutation automorphisms. This is a complete finite classification, not a numerical sampling claim.

For the witness, the exact computation gives
\[
N_3(\alpha)-N_{10}(\alpha)=\frac{\alpha(1-\alpha)F(\alpha)}{144},
\qquad
H(\alpha)=\frac{(1-\alpha^2)(72-108\alpha^2+47\alpha^4-6\alpha^6)}{72}.
\]
The claimed PageRank formula follows immediately. Furthermore,
\[
(1+z)^6F\big(z/(1+z)\big)
=-z^6+12z^5+30z^4-32z^3-94z^2-60z-12,
\]
which has exactly two coefficient sign changes. Direct exact evaluations show
\[
F(1/2)=-157/64<0,\quad F(2/3)=4/81>0,\quad
F(9/10)=342483/1000000>0,\quad
F(19/20)=-13677637/64000000<0.
\]
Thus there are at least two sign-changing roots; Descartes' bound gives at most two, proving that they are the only two interior roots and that both crossings are strict.

## Verification
Run `python check.py` in the same directory, using the version of NetworkX specified by `requirements.txt` (Python 3.10 or newer). The reproducible script uses Python `fractions.Fraction` for determinant, polynomial, Descartes and Sturm calculations, and verifies polynomial linear-system identities. It regenerates all nonisomorphic trees through eleven vertices, checks 20,398 vertex-pair comparisons across orders two through eleven, tests the witness's exact factorization, and requires the complete classification. It prints `CHECK PASS` only if every assertion succeeds. A separate symbolic linear-system inversion at four rational damping values verified the displayed formula independently of the census.

## Relationship to prior work
Boldi, Santini and Vigna (2005) developed analytic dependence of PageRank on its damping factor, including closed-form derivatives. Bressan and Peserico (2009/2010) showed that flexible orderings can occur on some graphs, without establishing the present minimum within undirected trees. Son, Christensen, Grassberger and Paczuski (2012) studied ranking changes with damping in directed networks. This result isolates a different, precise question: the first undirected tree admitting two strict reversals for one pair, and the classification at its smallest order. A separate adjacency-resolvent centrality comparison is not equivalent because its walk weights are not normalized by degrees.

## Limitations
Historical priority is provisional: one relevant published article was available through abstracts and bibliographic information, not a complete inspected copy; no uniqueness guarantee follows from literature searches. The finite census relies on the completeness of the published NetworkX nonisomorphic-tree generator; all arithmetic for supplied representatives is exact. The theorem covers only the stipulated PageRank normalization and graph family. No independent scientific audit has been performed.

## References
- P. Boldi, M. Santini and S. Vigna, *PageRank as a Function of the Damping Factor*, WWW 2005, 557–566, https://doi.org/10.1145/1060745.1060827 (first publicly dated 2005-05-10); author-hosted version: https://vigna.di.unimi.it/ftp/papers/PageRankAsFunction.pdf.
- M. Bressan and E. Peserico, *Choose the Damping, Choose the Ranking?*, Journal of Discrete Algorithms 8 (2010), 199–213, https://doi.org/10.1016/j.jda.2009.11.001.
- S. W. Son, C. Christensen, P. Grassberger and M. Paczuski, *PageRank and rank-reversal dependence on the damping factor*, https://arxiv.org/abs/1201.4787 (first version 2012-01-23).
- NetworkX documentation, `nonisomorphic_trees`: https://networkx.org/documentation/stable/reference/generated/networkx.generators.nonisomorphic_trees.html.
