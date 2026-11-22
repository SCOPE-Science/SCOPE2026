# A degree-marked Poisson process for common edges of independent random labeled trees

## Finding

Let \(T_n^{(1)}\) and \(T_n^{(2)}\) be independent, uniformly distributed labeled trees on \([n]=\{1,\ldots,n\}\). For each common edge \(\{u,v\}\), written \(u<v\), record its rescaled ordered endpoints \((u/n,v/n)\) and its four endpoint degrees
\[
M_{uv}=\bigl(d_{T_n^{(1)}}(u),d_{T_n^{(1)}}(v),d_{T_n^{(2)}}(u),d_{T_n^{(2)}}(v)\bigr).
\]
The random point measure
\[
\Xi_n=\sum_{\{u,v\}\in E(T_n^{(1)})\cap E(T_n^{(2)}),\,u<v}\delta_{(u/n,v/n,M_{uv})}
\]
converges in distribution to a Poisson point process on \(\{0<x<y<1\}\times\mathbb N_{\ge1}^{4}\) with intensity
\[
4\,dx\,dy\,\mu(da,db)\,\mu(dc,dd),
\qquad
\mu=\mathcal L\bigl(1+P+B,\,2+Q-B\bigr),
\]
where \(P,Q\) are independent \(\operatorname{Poisson}(1)\) random variables and \(B\) is an independent fair Bernoulli variable. Thus, conditional on the number of limiting common edges, their rescaled locations are independent uniform points of the upper triangle, and their four-degree marks are independent across edges, with the two-tree mark factors also independent. The degrees *within* each tree at the two ends of one common edge are not independent.

For the finite-size structural statement, fix \(1\le r\le\lfloor n/2\rfloor\) vertex-disjoint prescribed edges \(\{u_i,v_i\}\) with \(u_i<v_i\), and condition one uniform tree on containing all these edges. For \(n\ge r+2\), its exact conditional degree probability-generating function is
\[
\mathbb E\left[\prod_{i=1}^r s_i^{d(u_i)-1}t_i^{d(v_i)-1}\ \middle|\ \{u_i,v_i\}\in E(T_n)\ \forall i\right]
=\prod_{i=1}^r\frac{s_i+t_i}{2}\left(1+\frac{\sum_{i=1}^r(s_i+t_i-2)}{n}\right)^{n-r-2}.
\tag{1}
\]
The corresponding inclusion probability is exactly \((2/n)^r\). Formula (1) tends, for fixed \(r\), to \(\prod_i[(s_i+t_i)/2]\exp[\sum_i(s_i+t_i-2)]\), the product of \(r\) copies of the degree law \(\mu\). For a single prescribed edge in a finite tree with \(n\ge3\), the endpoint degrees have the exact strictly negative conditional covariance
\[
\operatorname{Cov}(d_T(u),d_T(v)\mid\{u,v\}\in E(T))=-\frac14-\frac{n-3}{n^2}.
\tag{1a}
\]

A leaf-level consequence is a complete nine-class Poisson law. At a common edge, mark each tree by \(L\) if its lower-labeled endpoint is a leaf, by \(R\) if its higher-labeled endpoint is a leaf, and by \(0\) otherwise. Let \(q_L=q_R=(2e)^{-1}\) and \(q_0=1-e^{-1}\). The nine counts of types \((a,b)\in\{0,L,R\}^2\) converge jointly to independent Poisson random variables of means \(2q_aq_b\). In particular, the number of common edges pendant at the *same endpoint* in both trees converges to \(\operatorname{Poisson}(e^{-2})\), and the number pendant at *opposite endpoints* in the two trees has another independent \(\operatorname{Poisson}(e^{-2})\) limit. For \(n\ge3\), each of these two counts has the exact expectation
\[
\frac{n-1}{n}\left(1-\frac1n\right)^{2(n-3)}.
\tag{2}
\]
Consequently, the probability of at least one common edge pendant at the same endpoint in both trees converges to \(1-\exp(-e^{-2})\).

## Assumptions and scope

All trees are unrooted, simple, uniformly labeled spanning trees of the complete graph on \([n]\). The two trees are independent. A common edge means the same unordered labeled vertex pair appears in both trees. Endpoint order is numerical labeling only; it is not a tree orientation. The finite generating function requires \(r\) vertex-disjoint specified edges and \(n\ge r+2\). All limit assertions keep any tested number of specified edges, spatial windows, and degree marks fixed while \(n\to\infty\). Spatial point-process convergence can be read as joint convergence of counts in finitely many disjoint, boundary-null subsets of the upper triangle, with any finitely many exact degree-mark classes; the total number of points is tight, and marks are also tight.

## Proof

**Exact forest probability.** For a prescribed forest \(F\) on \([n]\) with component sizes \(c_1,\ldots,c_j\), the weighted Cayley forest formula gives exactly \(n^{j-2}\prod_i c_i\) labeled trees containing \(F\). Its probability under a uniform labeled tree is \(n^{-(n-j)}\prod_i c_i\). If \(F\) comprises \(r\) disjoint edges, there are \(r\) components of size two and \(n-2r\) singleton components, so the probability is \((2/n)^r\).

**Conditional degree generating function.** Condition on the \(r\) disjoint edges. Contract each to a supervertex of weight two; the other \(n-2r\) vertices have weight one. Every quotient tree edge between component weights \(a,b\) has \(ab\) different endpoint lifts. Hence the induced probability for a quotient tree \(Q\) is proportional to \(\prod_w c_w^{\deg_Q(w)}\), where the total component weight equals \(n\). In the weighted Prüfer code of \(Q\), the \(n-r-2\) independent code letters select supervertex \(w\) with probability \(c_w/n\). Conditional on \(Q\), every incidence at a weight-two supervertex selects either original endpoint independently and fairly. Each supervertex has exactly one more incidence than its count of occurrences in the Prüfer word. This gives one mandatory fair choice contributing the factor \((s_i+t_i)/2\), and each remaining code letter contributes either \((s_i+t_i)/n\) for a doubled component or \(1/n\) for a singleton. Summing these choices produces (1). This argument supplies an explicit weighted-code construction; no asymptotic independence is assumed.

For fixed \(r\), let \(n\to\infty\) in (1). The exponentiated bracket converges to \(\exp(\sum_i(s_i+t_i-2))\). For one pair, the limiting bivariate degree-excess pgf is
\[
\frac{s+t}{2}\exp(s+t-2),
\]
which is the pgf of \((P+B,Q+1-B)\), with \(P,Q\) independent unit-rate Poisson and \(B\) independent fair Bernoulli. The finite conditional covariance in (1a) follows because the one obligatory fair incidence contributes \(-1/4\) to covariance and the two exclusive categories in each of the \(n-3\) other weighted code draws contribute \(-(n-3)/n^2\). The factorization for any fixed matching proves that all such conditioned degree-pair marks become independent. For two independent trees, their two sets of degree marks are independent even before taking the limit.

**Factorial moments of the marked overlap field.** Take a fixed \(h\ge1\) and any ordered \(h\)-tuple of distinct potential edges. The contribution of vertex-disjoint choices is computed with the exact probability \((2/n)^{2h}\) that every edge lies in both trees. Their conditional marks converge to independent copies of \(\mu\otimes\mu\) by (1), uniformly in which disjoint labels were chosen. The lattice sums of rescaled ordered endpoints converge to area integrals; each potential edge contributes intensity \(4/n^2\), and the limiting spatial intensity is \(4\,dx\,dy\) on \(x<y\).

All other \(h\)-tuples involve at most \(2h-1\) distinct vertices and number \(O_h(n^{2h-1})\). If their union contains a cycle, their joint inclusion probability is zero. Otherwise it is a forest with \(h\) edges, and the inequality \(c\le2^{c-1}\) for positive integers \(c\) gives an upper bound \((2/n)^h\) for inclusion in one tree, and \((2/n)^{2h}\) for inclusion in both. Their total marked factorial-moment contribution is therefore \(O_h(n^{-1})\). The limiting factorial moment measures equal those of the stated marked Poisson process. The standard factorial-moment/Poisson characterization gives joint finite-dimensional count convergence; the uniform bounded first moment and tight fixed-edge degree distributions supply point-measure tightness and remove truncation of degree marks. This proves the full statement.

**Pendant corollaries and exact means.** Under \(\mu\), the two degree-excess variables are \(P+B\) and \(Q+1-B\). Exactly one may vanish; either vanishes with probability \(\tfrac12e^{-1}\). Independent trees therefore give the nine mark weights \(q_aq_b\), and the spatial mass \(\int_{0<x<y<1}4\,dx\,dy=2\) supplies the nine Poisson means. The two same-endpoint pendant categories \((L,L),(R,R)\) have combined mean \(e^{-2}\), as do the two opposite-endpoint categories. In a finite tree conditional on a specified edge, a given endpoint is a leaf exactly when it receives none of the external stubs, so its probability from (1) is \(\frac12(1-1/n)^{n-3}\). Multiply the square of this conditional probability by the two-tree inclusion probability \((2/n)^2\), the two possible pendant endpoints and the \(\binom n2\) possible edges to obtain (2). Taking the limit completes the proof.

## Verification

The included standalone `verify_marks.py` enumerates every labeled tree through size six for the degree-mark conditioning checks and every ordered pair of labeled trees through size five for the same-endpoint and opposite-endpoint pendant-overlap means. Exact `fractions.Fraction` calculations compare the empirical conditional joint distributions for \((n,r)=(3,1),(4,1),(4,2),(5,1),(5,2),(6,1),(6,2),(6,3)\) against a second constructive calculation from weighted Prüfer letters. They also verify the three displayed finite overlap means for sizes three, four and five. The checker reports 156 exact rational constraints passed. Run using `python3 verify_marks.py`; the script uses only the Python standard library. These bounded exhaustive enumerations check the finite identities, not the infinite Poisson-process convergence, which follows from the analytical proof.

## Relationship to prior work

The unmarked \(\operatorname{Poisson}(2)\) law for common edges is classical and is not asserted as new: Janson (1986), Bender and Canfield (1999), and Bóna and Wagner (2025) treat edge overlaps. In particular, Bóna and Wagner state and prove the exact forest inclusion formula and use it for the unmarked Poisson law. The additional statement here tracks **all four endpoint degrees, their non-product within-edge limiting law, independent degree-mark classes and spatial locations simultaneously**. The unmarked law is obtained by forgetting marks and locations; it does not by itself imply their conditional joint distribution. The weighted Prüfer calculation supplies that extra information.

## Limitations

The conclusion concerns two independent uniform Cayley trees, fixed finite degree classes and labels rescaled in the unit interval; it does not assert the same marks for arbitrary host graphs, correlated trees, or growing prescribed degree values. No convergence rate in total variation is claimed. An independent mathematical audit and exhaustive historical-priority verification have not been performed. The 1986 primary paper was available only through its abstract and publication record in this research, so possible broader statements in its inaccessible full text are a remaining originality uncertainty.

## References

1. S. Janson, *Random trees in a graph and trees in a random graph*, Mathematical Proceedings of the Cambridge Philosophical Society **100** (1986), 319–330, https://doi.org/10.1017/S0305004100066111 .
2. E. A. Bender and E. R. Canfield, *Intersections of Randomly Embedded Sparse Graphs are Poisson*, Electronic Journal of Combinatorics **6** (1999), #R36, https://doi.org/10.37236/1468 .
3. M. Bóna and S. Wagner, *On the intersection of pairs of trees*, https://arxiv.org/abs/2501.18570 (first posted 2025-01-30).
