# The first positive local-selector correlation in binary de Bruijn cycles

## Finding
Let \(n\ge2\), put \(m=n-1\), and sample a binary de Bruijn cycle of order \(n\) uniformly from its rotation classes. At each binary length-\(m\) word \(v\), its two incoming length-\(n\) words are \(0v\) and \(1v\), and its outgoing words are \(v0\) and \(v1\). Their consecutive occurrences in the cycle define one of two bijections. Write \(X_v=1\) for the crossed bijection \(0v\mapsto v1\) (equivalently \(1v\mapsto v0\)), and \(X_v=0\) for the straight bijection.

**Sharp threshold theorem.** For orders \(2\le n\le4\), every pair of distinct local selectors has nonpositive covariance. For every \(n\ge5\), the two distinct words
\[
 v=0^{n-3}10,\qquad w=10^{n-3}1
\]
have strictly positive covariance
\[
 \boxed{\operatorname{Cov}(X_v,X_w)=2^{-n}.}
\]
In particular order five is the first binary de Bruijn order permitting positively correlated local successor choices. The displayed family supplies positive correlation at every higher order; it does not classify all correlations at those orders.

For the displayed pair, additionally,
\[
 \Pr(X_v=1)=\tfrac12,\quad
 \Pr(X_w=1)=\tfrac12+2^{-(n-2)},\quad
 \Pr(X_v=X_w=1)=\tfrac14+3\cdot2^{-n}.
\]

## Assumptions and scope
A binary order-\(n\) de Bruijn cycle is a cyclic binary word of length \(2^n\) in which all \(n\)-bit factors appear exactly once. Rotation, but not bit complementation or reversal, is quotiented. Each length-\(n\) factor represents one directed arc in the binary shift-register graph with length-\(m\) vertices. The cyclic order of its arcs supplies exactly one successor bijection at every vertex; the conjunction of those bijections is a single cyclic orbit on the \(2^n\) arcs. Each cyclic de Bruijn word has exactly one resulting selector table, and each selector table defining a single orbit corresponds to exactly one such word. Thus uniform sampling of cycles is uniform sampling from valid selector tables. The covariance refers to these Bernoulli indicators; the statements concern distinct vertices \(v,w\), not the input bits of a uniformly random unrestricted string.

## Proof
**1. Finite orders.** Exhaust all \(2^{2^{n-1}}\) binary selector tables for each \(n\in\{2,3,4\}\): from the length-\(n\) arc whose first bit is \(a\) and remaining \(m\) bits are \(v\), its prescribed next arc is \(v\,(a\oplus X_v)\). Retain a table if iteration from arc \(0^n\) visits every one of the \(2^n\) arcs exactly once and returns to \(0^n\). This is a complete (not sampled) decision procedure for a single cycle. It retains exactly \(1,2,16\) tables at orders \(2,3,4\), respectively. At order two all off-diagonal covariances vanish; at order three the sole negative pair is \((v,w)=(01,10)\), with covariance \(-1/4\). At order four, with vertices interpreted as three-bit integers, the only nonzero off-diagonal covariances are \(-1/8\) at \((1,4),(3,6)\), and \(-1/16\) at \((2,5)\). Every other pair is zero. The exhaustive algorithm and its full finite arithmetic are independently reproducible from `verify.py`; the preceding enumeration and explicit finite lists constitute a finite proof of the nonpositivity half.

**2. Contraction identity for two prescribed turns.** For \(n\ge5\), set \(m=n-1\) and encode length-\(m\) words by binary integers. The event \(X_v=1\) is equivalent to the presence of the specific length-\(n+1\) cyclic factor \(0v1\), because once the incoming arc \(0v\) is followed by \(v1\), the second transition at \(v\) is forced. Likewise for \(w\).

The two prescribed transitions use four distinct length-\(n\) arcs when \(n\ge5\). Contract each specified two-arc path into a single shortcut arc. The original Eulerian graph has outdegree two at every vertex. In the contracted graph exactly the two intermediate vertices have outdegree one, all others still two. Directed BEST counting therefore cancels every factorial factor, so the joint event probability equals the ratio of directed rooted spanning-in-tree counts of the contracted and original graphs. Individual event probabilities arise from one contraction in the same way.

Let \(P\) be the transition matrix of the unbiased binary shift on length-\(m\) words: \(P(x,y)=1/2\) when \(y\) results from shifting \(x\) left and appending a bit. After \(m\) transitions its distribution is uniform, hence \(P^m=J\), the uniform averaging matrix. For \(0\le t<m\),
\[
 P^t(x,y)=2^{-t}H_t(x,y),\quad
 H_t(x,y)=\mathbf 1\{\operatorname{suf}_{m-t}(x)=\operatorname{pre}_{m-t}(y)\}.
\]
The original graph Laplacian is \(L=2(I-P)\). On the zero-sum subspace, its inverse is the finite kernel
\[
 K(x,y)=\sum_{t=0}^{m-1}2^{-(t+1)}H_t(x,y),
\]
since \((I-P)\sum_{t=0}^{m-1}P^t=I-J\). A shortcut replacing arcs \(a\to b\to c\) changes the Laplacian by the rank-one term \((e_a-e_b)(e_b-e_c)^\mathsf T\). Both factors have zero coordinate sum. The directed Matrix-Tree theorem, together with the determinant lemma on the zero-sum subspace, therefore gives the ratio of in-tree counts as \(\det M\), where for two contractions \((a_i,b_i,c_i)\),
\[
 M_{ij}=\delta_{ij}+K(b_i,a_j)-K(b_i,b_j)-K(c_i,a_j)+K(c_i,b_j).
\]
For one contraction this expression is the corresponding diagonal entry. This derivation does not assume independent local selectors.

**3. Explicit finite overlap calculation valid at every higher order.** For \(v=0^{m-2}10\) and \(w=10^{m-2}1\), the two contracted length-\(m\) vertex paths, in integer encoding, are
\[
 (a_1,b_1,c_1)=(1,2,5),\qquad
 (a_2,b_2,c_2)=(2^{m-2},2^{m-1}+1,3).
\]
These vertices give two disjoint prescribed two-arc paths for every \(m\ge4\). To make the kernel evaluation explicit, write \(d_{ij}(t)=H_t(b_i,a_j)-H_t(b_i,b_j)-H_t(c_i,a_j)+H_t(c_i,b_j)\). Checking the equality of the indicated suffixes and prefixes yields the following **complete lists of nonzero terms** for all integers \(m\ge4\):
\[
\begin{array}{c|l}
(i,j)&(t,d_{ij}(t))\\\hline
(1,1)&(0,-1)\\
(1,2)&(m-3,1),(m-2,-2),(m-1,2)\\
(2,1)&(1,-1)\\
(2,2)&(0,-1),(m-2,1)
\end{array}
\]
The conditions \(m\ge4\) ensure that the listed exponents in each row are distinct. Inserting these terms into the finite geometric kernel gives
\[
 \boxed{M=\begin{pmatrix}\frac12&2^{1-m}\\-\frac14&\frac12+2^{1-m}\end{pmatrix}.}
\]
Consequently the two marginals are its diagonal entries, their joint probability is
\[
 \det M=\frac14+\frac32\,2^{1-m}=\frac14+3\cdot2^{-(m+1)},
\]
and their covariance is
\[
 \det M-M_{11}M_{22}=-M_{12}M_{21}=2^{-(m+1)}=2^{-n}>0.
\]
This proves the family and the sharp first-order threshold. \(\square\)

## Verification
The standalone Python 3 standard-library program `verify.py` reproduces every selector table at orders two through five and verifies the complete signed covariance histogram, including all nonpositive cases through four and the first positive cases at five. Independently it evaluates the path-contraction kernel at each order from five through sixteen and confirms the exact matrix and covariance formula against rational arithmetic. The program also directly compares the determinant formula to the empirical joint probability at order five. Finite checks support, but do not replace, the all-order overlap evaluation and determinant proof.

## Relationship to prior work
Rødland's 2006 *Exact Distribution of Word Counts in Shuffled Sequences* (Theorems 1 and 3) gives a general Eulerian path-contraction method for joint factor counts. Its general method already implies the **unreduced joint-probability determinant**, which is therefore not claimed as new here. The known 2013 framework for de Bruijn cycles provides standard existence and Eulerian encodings. An earlier published study of local length-three factor correlations in order-two de Bruijn cycles with alphabet size at least three gives a different sharp **alphabet-size** sign threshold; it does not cover the binary alphabet with variable word order. The contribution here is the exact **binary order threshold**, including a persistent explicitly computable positive-correlation family and the complete small-order exclusion. Numerical coincidences or formal algebraic specializations of general moment formulae are not themselves claimed as new. Indexed and primary-literature comparisons did not reveal an earlier statement of the same binary-order sign transition; absence from searched material is not a uniqueness proof.

## Limitations
The theorem does not classify all selector-pair covariances at orders five and above; only one explicit family is asserted. The proof uses exact uniform distribution on cyclic de Bruijn rotation classes, not on arbitrary Eulerian multisets. It establishes pairwise covariance, not stochastic association or higher-order independence. The finite table enumeration is exhaustive only at the indicated orders, while the infinite family is proved separately. Independent mathematical review has not been performed.

## References
1. E. A. Rødland, *Exact Distribution of Word Counts in Shuffled Sequences*, Advances in Applied Probability **38** (2006), 116–133, DOI: 10.1239/aap/1143936143, https://doi.org/10.1239/aap/1143936143.
2. A. Campbell, A. Godbole and B. Kay, *Contributions to the Theory of de Bruijn Cycles*, arXiv:1304.2820 (first posted 2013-04-10), https://arxiv.org/abs/1304.2820.
3. BEST theorem and directed Matrix-Tree theorem (standard Euler tour and arborescence counting identities).
