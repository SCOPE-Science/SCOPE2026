# Pairwise source–sink attraction and aggregate repulsion in uniformly oriented Cayley trees

## Finding
Choose uniformly one of the \(n^{n-2}\) labeled trees on \([n]\), for each integer \(n\ge2\), and independently orient each of its \(n-1\) edges with a fair coin. Let \(A_i\) indicate that vertex \(i\) is a source (indegree zero), let \(B_i\) indicate that it is a sink (outdegree zero), and put \(S_n=\sum_i A_i\), \(K_n=\sum_i B_i\). Define
\[
c_n=\left(1-\frac1n\right)^{n-2},\qquad d_n=\left(1-\frac1{2n}\right)^{n-2}.
\]
The complete source–sink pairwise covariance profile is
\[
\operatorname{Cov}(A_i,B_j)=
\begin{cases}
-\dfrac{d_n^2}{4},&i=j,\\[2mm]
\dfrac14\left(\dfrac{n}{n-1}c_n-d_n^2\right),&i\ne j.
\end{cases}
\]
Every off-diagonal covariance is **strictly positive** for \(n\ge2\), although
\[
\boxed{\operatorname{Cov}(S_n,K_n)=\frac{n^2}{4}(c_n-d_n^2)<0\quad(n\ge3).}
\]
The two counts are constant, both equal to one, when \(n=2\). Their exact common mean and variance are
\[
\mathbb E S_n=\mathbb E K_n=\frac n2d_n,\qquad
\operatorname{Var}(S_n)=\operatorname{Var}(K_n)=\frac{n^2}{4}(c_n-d_n^2)+\frac n2(d_n-c_n).
\]
In particular, the aggregate repulsion persists at the linear scale:
\[
\frac1n\operatorname{Cov}(S_n,K_n)\longrightarrow-\frac1{16e},\qquad
\frac1n\operatorname{Var}(S_n)\longrightarrow\frac1{2\sqrt e}-\frac9{16e},
\qquad \operatorname{Corr}(S_n,K_n)\longrightarrow-\frac1{8\sqrt e-9}.
\]
Thus positive source–sink association between every *distinct* pair of vertices coexists with strictly negative association between their total counts. Unlike the random-tree average, the fair orientation of a fixed path has positive source–sink count covariance at every order at least five.

## Assumptions and scope
The underlying graph is sampled uniformly from simple undirected labeled spanning trees of the complete graph on \([n]\). All edges are then oriented independently and equiprobably, without using vertex labels to determine directions. The orientation is always acyclic. No isolated vertices occur for \(n\ge2\). All expectations and covariances above average over **both** the randomly sampled tree and its independent orientations. The result is not about conditioned trees, label-increasing orientations, or random directed Erdős–Rényi graphs. All formulas hold for every integer \(n\ge2\), with the explicit strict-sign boundary given above.

## Proof
**1. The weighted Cayley identities.** Let \(d_i(T)\) denote the degree of label \(i\) in a labeled tree \(T\), and let \(x_i>0\), \(s=\sum_i x_i\). Prüfer coding gives
\[
P(x):=\sum_T\prod_{i=1}^n x_i^{d_i(T)-1}=s^{n-2}.
\]
For distinct \(i,j\), the corresponding edge-restricted sum is
\[
P_{ij}(x):=\sum_{T:\,ij\in E(T)}\prod_{v=1}^n x_v^{d_v(T)-1}
=(x_i+x_j)s^{n-3}.
\]
Here is an independent verification of the edge-restricted identity, which is needed below. Give edge \(ij\) conductance \(x_ix_j\). A tree's product of its edge conductances is \((\prod_v x_v)\prod_v x_v^{d_v(T)-1}\), so \(P_{ij}/P\) is precisely the probability of including \(ij\) in the associated weighted spanning tree. The graph Laplacian is \(L=s\operatorname{diag}(x)-xx^{\mathsf T}\). The vector with entries \(1/(sx_i)\) at \(i\), \(-1/(sx_j)\) at \(j\), and zero elsewhere solves \(L\phi=e_i-e_j\), since \(\sum_vx_v\phi_v=0\). Its potential difference is \((x_i^{-1}+x_j^{-1})/s\), the effective resistance \(R_{ij}\). By differentiating a matrix-tree cofactor with respect to the edge conductance, the weighted edge inclusion probability is \(x_ix_jR_{ij}=(x_i+x_j)/s\). Multiplying by \(P=s^{n-2}\) proves the required identity. It extends to all nonnegative evaluations used below by polynomial continuity.

**2. The exact local joint law.** Write \(q_i(T)=2^{-d_i(T)}\). Given \(T\), the conditional probabilities of \(A_i=1\) and \(B_i=1\) are both \(q_i(T)\). As no vertex is isolated, \(A_iB_i=0\) identically. If \(i\ne j\), the required incident orientations are independent unless \(ij\) is an edge. In that case the shared edge is required to point from source \(i\) to sink \(j\), so the joint probability is twice the product. Hence
\[
\mathbb P(A_i=B_j=1\mid T)=q_i(T)q_j(T)\bigl(1+\mathbf1_{\{ij\in E(T)\}}\bigr)\quad(i\ne j).
\]
The Prüfer-degree polynomial with weights \(x_i=1/2\) and all others one yields
\[
\mathbb E q_i=\frac12 d_n,\qquad
\mathbb E(q_iq_j)=\frac14c_n\quad(i\ne j).
\]
For the edge-restricted term, evaluate the preceding \(P_{ij}\) at \(x_i=x_j=1/2\), all other weights one, and divide by the total tree count \(n^{n-2}\). This gives
\[
\mathbb E\bigl[q_iq_j\mathbf1_{\{ij\in E(T)\}}\bigr]
=\frac{(n-1)^{n-3}}{4n^{n-2}}=\frac{c_n}{4(n-1)}.
\]
Consequently \(\mathbb P(A_i=B_j=1)=nc_n/[4(n-1)]\) whenever \(i\ne j\), while \(\mathbb P(A_i=B_i=1)=0\). Subtracting \(\mathbb E A_i\mathbb E B_j=d_n^2/4\) proves the announced pairwise covariance formulas.

**3. Why local signs oppose the global sign.** The diagonal covariances are negative. For distinct labels, observe that
\[
\frac{c_n}{d_n^2}=\left(1-\frac1{(2n-1)^2}\right)^{n-2}.
\]
Bernoulli's inequality gives a lower bound \(1-(n-2)/(2n-1)^2\), which exceeds \((n-1)/n\) for every \(n\ge2\). Hence \(nc_n/(n-1)>d_n^2\) and every distinct-vertex covariance is strictly positive. Summing over all ordered pairs \((i,j)\), including the \(n\) diagonal pairs, gives
\[
\operatorname{Cov}(S_n,K_n)
=-\frac{nd_n^2}{4}+n(n-1)\frac14\left(\frac n{n-1}c_n-d_n^2\right)
=\frac{n^2}{4}(c_n-d_n^2).
\]
The displayed ratio is strictly less than one for \(n\ge3\), making the total covariance negative; at \(n=2\) it is zero.

**4. Marginal variance and asymptotic correlation.** Two distinct vertices cannot both be sources when adjacent; otherwise their source events use disjoint edges. Therefore the same degree and edge enumerators yield
\[
\mathbb P(A_i=A_j=1)=\frac14c_n-\frac{c_n}{4(n-1)}=\frac{(n-2)c_n}{4(n-1)},\quad i\ne j.
\]
It follows that
\[
\operatorname{Var}(S_n)=\mathbb ES_n+n(n-1)\mathbb P(A_1=A_2=1)-(\mathbb ES_n)^2
=\frac n2d_n+\frac{n(n-2)}4c_n-\frac{n^2}4d_n^2.
\]
Algebra gives the stated equivalent variance formula; the sink variance is identical by global edge reversal. Finally,
\[
c_n=e^{-1}\left(1+\frac{3}{2n}+O(n^{-2})\right),\qquad
 d_n^2=e^{-1}\left(1+\frac{7}{4n}+O(n^{-2})\right),\qquad
 d_n=e^{-1/2}\left(1+\frac{7}{8n}+O(n^{-2})\right).
\]
Substituting gives the covariance and variance limits. Since \(8\sqrt e-9>0\), their quotient gives the asserted strictly negative correlation limit. This proof establishes all \(n\) analytically; the computations below only check the formulas on finite cases.

## Verification
`verify.py` is a standalone Python 3 exact-arithmetic verifier, with no nonstandard dependencies. It iterates over every Prüfer sequence and every independent edge orientation for all \(2\le n\le6\). It compares exact rational means, source–sink covariance, marginal variance and two marked source–sink joint probabilities with the formulas in this document. It also checks the exact strict sign inequalities over an additional finite integer range as diagnostics, not as a proof of their infinite validity. Execute `python verify.py` from the directory containing the two files. The full infinite-size proof is Sections 1–4.

## Relationship to prior work
Bernardi and Morales give the classical Cayley multidegree enumerator, and a broader multitype enumeration framework, but do not orient the edges independently or analyze the joint source–sink variables. A previously published fixed-tree analysis of fair random orientations proves the identity \(\operatorname{Cov}(S,K\mid T)=2\sum_{ij\in E(T)}2^{-d_i(T)-d_j(T)}-\sum_i4^{-d_i(T)}\), and gives sharp path/star extrema. That theorem holds for every deterministic tree and is acknowledged as the closest result: it does not by itself state the signed distinct-label pairwise law after averaging uniformly over Cayley trees, the opposite sign of the total covariance, or the limiting correlation. The new statement is obtained by combining the shared-edge term with exact weighted Cayley enumeration, not by treating the fixed-tree covariance as a new fact. Okoth's source/sink enumeration for locally oriented trees directs edges by the ordering of labels, which is a different measure on directed trees.

## Limitations
The statements concern a uniformly sampled labeled tree and independent **fair** orientations only. In particular, they do not assert independence between source and sink counts, a joint central limit theorem, or the same signs for other tree distributions. The precise finite identities can be deduced from known weighted-tree and local orientation ingredients after performing the extra marked-pair calculation; determining whether an earlier source has already made this complete calculation remains a historical-priority risk. Computational enumeration through six vertices does not certify novelty or the infinite-family proof. Independent mathematical audit has not been performed.

## References
- O. Bernardi and A. H. Morales, *Counting trees using symmetries*, arXiv:1206.0598, first posted 4 June 2012, published in Journal of Combinatorial Theory, Series A 123 (2014), 104–122. https://arxiv.org/abs/1206.0598
- *Sharp path–star bounds for source–sink covariance in randomly oriented trees*, published mathematical research record, 27 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/27/SCOPE-sharp-path-star-bounds-for-source-sink-covariance-in-randomly-or--db5fdb9d6d6f
- I. O. Okoth, *Combinatorics of oriented trees and tree-like structures*, doctoral dissertation, Stellenbosch University, March 2015, Chapters 3 and 7. https://www.academia.edu/69407610/Combinatorics_of_oriented_trees_and_tree_like_structures
