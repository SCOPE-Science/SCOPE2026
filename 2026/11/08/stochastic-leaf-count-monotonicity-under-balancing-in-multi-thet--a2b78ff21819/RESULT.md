# Stochastic leaf-count monotonicity under balancing in multi-theta spanning trees

## Finding
Let \(k\ge3\), and let \(\boldsymbol\ell=(\ell_1,\dots,\ell_k)\) be integers satisfying \(\ell_i\ge2\). Form the simple generalized theta graph \(\Theta(\boldsymbol\ell)\) from two distinct terminals joined by \(k\) internally vertex-disjoint paths having \(\ell_i\) edges. Let \(L_{\boldsymbol\ell}\) be the number of degree-one vertices (leaves) in a uniformly sampled spanning tree.

**Balancing theorem.** Fix distinct indices \(a,b\) with \(\ell_a\ge\ell_b+2\), and replace their lengths by \(\ell_a-1\) and \(\ell_b+1\), leaving the others unchanged. If \(\boldsymbol\ell'\) is the new length vector, then
\[
L_{\boldsymbol\ell}\le_{\mathrm{st}}L_{\boldsymbol\ell'},
\]
where stochastic ordering means \(\Pr(L_{\boldsymbol\ell}\ge t)\le\Pr(L_{\boldsymbol\ell'}\ge t)\) for **every real** \(t\). The two laws are different, and in particular \(\mathbb E L_{\boldsymbol\ell}<\mathbb E L_{\boldsymbol\ell'}\). Thus, among all integer length vectors with fixed \(k\ge3\), fixed sum \(s\ge2k\), and each length at least two, the (nearly) equal vector, whose entries differ by at most one, uniquely maximizes the leaf count in stochastic order up to path permutations. The vector \((s-2(k-1),2,\ldots,2)\) uniquely minimizes it, up to permutations. If the two extreme vectors coincide up to permutation, these extremum statements refer to the same law.

The complete finite generating polynomial is also explicit. Set
\[
\tau(\boldsymbol\ell)=\sum_{i=1}^{k}\prod_{j\ne i}\ell_j,
\qquad A_i(z)=2+(\ell_i-2)z.
\]
Then, for all complex \(z\),
\[
\mathbb E[z^{L_{\boldsymbol\ell}}]
=\frac{z^{k-1}}{\tau(\boldsymbol\ell)}
\left[\sum_{i=1}^{k}\prod_{j\ne i}A_j(z)+2k(z-1)\right].
\]
In particular, writing \(e_{k-2}(\boldsymbol\ell)\) for the elementary symmetric polynomial of degree \(k-2\),
\[
\mathbb E L_{\boldsymbol\ell}
=2(k-1)-\frac{4e_{k-2}(\boldsymbol\ell)-2k}{\tau(\boldsymbol\ell)}.
\]

## Assumptions and scope
All graphs are finite, undirected, simple and unweighted. Every length is at least two, so the internally disjoint paths have disjoint internal vertices and share only the two terminals. Uniform means each distinct spanning-tree edge set has probability \(1/\tau(\boldsymbol\ell)\). Trees include all vertices, and a leaf has tree degree exactly one. The vector dimension \(k\) and total edge count \(s\) are fixed in the extremal comparison. The theorem is about the entire leaf-count distribution, not only its expectation or the maximum possible number of leaves in an individual spanning tree.

## Proof
**1. Tree decomposition.** The graph has \(s\) edges and \(s-k+2\) vertices, so every spanning tree deletes exactly \(k-1\) edges. At least one entire terminal-to-terminal path must survive for terminal connectivity; two complete paths cannot survive, since they form a cycle. Consequently precisely one path \(i\) is intact and precisely one edge is deleted from every other path. Conversely every such choice is a spanning tree. The number of trees with intact path \(i\) is \(w_i=\prod_{j\ne i}\ell_j\), and the total number is \(\tau=\sum_i w_i\). Conditional on \(i\), the deleted edge on each other path is uniformly and independently chosen among that path's edges.

**2. Leaf polynomial.** A deleted edge internal to a nonintact path contributes two internal leaves; deleting its first or last edge contributes one internal leaf. Each path of length \(\ell_j\ge2\) has exactly two terminal-adjacent deletion choices and \(\ell_j-2\) internal choices. The resulting internal-leaf enumerator for a deleted edge is \(2z+(\ell_j-2)z^2=zA_j(z)\). There is an additional terminal leaf exactly if all \(k-1\) deleted edges touch the same one of the two terminals. Each intact path has exactly two such deletion patterns. In the internal-leaf product these patterns contribute \(z^{k-1}\), whereas their true leaf count is \(k\). Summing the correction \(2k(z^k-z^{k-1})\) over intact paths proves the polynomial displayed in the Finding. Evaluating at \(z=1\) gives one; differentiating and observing that \(\sum_i\sum_{j\ne i}\prod_{h\notin\{i,j\}}\ell_h=2e_{k-2}(\boldsymbol\ell)\) gives the expectation formula.

**3. One balancing step is an explicit probability mixture.** Write \(p=\ell_a\), \(q=\ell_b\), \(p\ge q+2\), \(\delta=p-q-1>0\), and let \(S=\{1,\ldots,k\}\setminus\{a,b\}\) (nonempty because \(k\ge3\)). Put
\[
B(z)=\prod_{j\in S}A_j(z),\quad
Q(z)=\sum_{h\in S}\prod_{j\in S\setminus\{h\}}A_j(z),\quad
R=Q(1)>0.
\]
The unnormalized bracket in the leaf polynomial is
\[
N(z)=(A_a(z)+A_b(z))B(z)+A_a(z)A_b(z)Q(z)+2k(z-1).
\]
Balancing leaves \(A_a+A_b\) unchanged, increases \(A_aA_b\) by \(\delta z^2\), and increases \(\tau=N(1)\) by \(\delta R\). Define an auxiliary integer-valued random variable \(H\) by the probability-generating function
\[
\mathbb E[z^H]=\frac{z^{k+1}Q(z)}{R}.
\]
This is a probability polynomial: choose \(h\in S\) with probability \(w_h^S/R\), where \(w_h^S=\prod_{j\in S\setminus\{h\}}\ell_j\); for each \(j\in S\setminus\{h\}\), independently select a uniform path edge, add two if it is internal and one if it meets a terminal, then add four. Algebra now gives the **exact convex-mixture identity**
\[
\mathcal L(L_{\boldsymbol\ell'})
=\frac{\tau}{\tau+\delta R}\mathcal L(L_{\boldsymbol\ell})
+\frac{\delta R}{\tau+\delta R}\mathcal L(H).
\]
Here \(\mathcal L\) denotes a probability law, and the equality of laws follows by equality of their generating polynomials.

**4. Coupling that proves \(H\ge L_{\boldsymbol\ell}\) almost surely.** Generate the original tree by selecting its intact path \(I\) with probabilities \(w_i/\tau\) and then generating all its uniform deleted edges. If \(I\in S\), set \(h=I\); if \(I=a\) or \(I=b\), independently choose \(h\in S\) with probability \(w_h^S/R\). In each case, retain the original deleted-edge choices on all paths of \(S\setminus\{h\}\). Define \(H\) by counting these paths' internal leaves and **two additional internal leaves on each of paths \(a,b\)** (four altogether). This artificial count has the claimed generating polynomial. Indeed
\[
\Pr(h=j)=\frac{pq w_j^S}{\tau}
+\frac{(p+q)\prod_{u\in S}\ell_u}{\tau}\frac{w_j^S}{R}
=\frac{w_j^S}{R},\qquad j\in S,
\]
and, conditional on \(h\), all retained edge cuts on \(S\setminus\{h\}\) remain independent and uniform.

Let \(E_j\) indicate that the deleted edge on path \(j\) meets a terminal, and let \(J\) indicate that **all** deleted edges in the original tree meet the same terminal. If \(I=h\in S\), subtracting the original leaf count from \(H\) gives \(E_a+E_b-J\ge0\). If \(I=a\), the difference is \(E_b+E_h-J\ge0\); if \(I=b\), it is \(E_a+E_h-J\ge0\). Each inequality holds because \(J=1\) forces each indicated pair of deleted edges to meet terminals. Thus \(H\ge L_{\boldsymbol\ell}\) almost surely. This is a non-asymptotic coupling for every admissible parameter vector.

The domination is strict in distribution: with positive probability \(I\in S\) and the cuts on paths \(a\) and \(b\) occur at opposite terminals, giving \(J=0\) and \(H-L_{\boldsymbol\ell}=2\). The mixture has strictly positive weight \(\delta R/(\tau+\delta R)\), hence \(L_{\boldsymbol\ell}\le_{\mathrm{st}}L_{\boldsymbol\ell'}\) with different distributions. All first-order stochastic inequalities and strict inequality of means follow.

**5. Global extrema.** Every integer vector of length \(k\) and sum \(s\) with entries at least two can be transformed to its unique nearly equal vector (up to permutation) by finitely many transfers of one unit from a longer entry to a shorter entry whenever the difference is at least two. Conversely the uniquely most unequal vector \((s-2(k-1),2,\ldots,2)\) majorizes every admissible vector and can be transformed into any vector by a sequence of such balancing transfers. Transitivity of first-order stochastic dominance and strictness at each nontrivial transfer prove both claimed extremizers and their uniqueness up to permutation.

## Verification
The standalone Python 3 program `verify.py` uses only the standard library. It independently constructs the finite graph, exhaustively enumerates \((|V|-1)\)-edge subsets on selected small instances, checks connectedness and acyclicity by a disjoint-set routine, and counts their leaves. It compares this independent census with the generating-polynomial coefficients. It also evaluates the exact rational CDF inequalities for every balancing transfer among nondecreasing length vectors with \(3\le k\le5\) and entries in \(\{2,3,4,5\}\). Command: `python3 verify.py`. Observed output ends with `VERIFY_OK 3272 exact assertions`. These finite checks are supplemental; Step 4 is the infinite-parameter proof.

## Relationship to prior work
The UST degree-field framework of Rapoport (first posted 2023-12-22) provides general joint degree probability expressions on finite graphs; they can in principle be evaluated to calculate leaf-count laws. The current result is the explicit all-\(k\) generalized-theta polynomial together with the strictly monotone **cross-graph stochastic ordering under integral path-length balancing**, supplied by an exact probability-mixture/coupling proof. Neither the graph-specific stochastic order nor the extremal classification is stated in the inspected Rapoport source. Nachmias and Peres (first posted 2020-11-17) concern local limits of UST on large-degree regular graph sequences and do not address this fixed-cycle-rank finite subdivision problem. Noguchi and Zamfirescu (first posted 2023-12-21) establish which leaf counts can occur in a connected graph, not a comparison of uniform probabilities when its path lengths change. Classical spanning-tree counts and the existence of many-leaf spanning trees are not claimed as original.

## Limitations
The result is restricted to **uniform** spanning trees of generalized-theta networks with every arm length at least two, and it compares length vectors of the same dimension and total length. It does not prove monotonicity for arbitrary series-parallel graphs or arbitrary edge conductances. A general finite-graph degree formula is known, and a comprehensive historical priority determination is not claimed; published results on specific theta-graph leaf polynomials or stochastic orders outside the material inspected could affect originality. No independent audit has been performed.

## References
1. A. Rapoport, *Correlations in uniform spanning trees: a fermionic approach*, arXiv:2312.14992v1, posted 2023-12-22, https://arxiv.org/html/2312.14992v1 .
2. A. Nachmias and Y. Peres, *The local limit of uniform spanning trees*, arXiv:2011.08833, posted 2020-11-17, https://arxiv.org/abs/2011.08833 .
3. K. Noguchi and C. T. Zamfirescu, *Spanning trees for many different numbers of leaves*, arXiv:2312.13674, posted 2023-12-21, https://arxiv.org/abs/2312.13674 .
4. D. J. Aldous, *The random walk construction of uniform spanning trees and uniform labelled trees*, SIAM J. Discrete Math. 3 (1990), 450–465, https://escholarship.org/uc/item/4gc8v9f6 .
