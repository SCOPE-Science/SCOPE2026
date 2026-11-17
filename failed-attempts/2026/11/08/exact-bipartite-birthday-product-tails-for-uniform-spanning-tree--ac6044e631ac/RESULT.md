# Exact bipartite birthday-product tails for uniform spanning-tree distances

## Finding
Let \(K_{a,b}\) be the complete bipartite graph with labeled parts \(A,B\) of positive integer sizes \(a,b\), and choose a spanning tree \(T\) uniformly from its \(a^{b-1}b^{a-1}\) spanning trees. For two fixed distinct vertices \(u,v\), let \(D=d_T(u,v)\) count edges on their unique path. Define the falling factorial by \((z)_{\underline{k}}=\prod_{j=0}^{k-1}(z-j)\) for nonnegative integers \(k\), with an empty product equal to one. Then the following are exact for every nonnegative integer \(k\):

* If \(u\in A\), \(v\in B\), then
\[
\Pr(D>2k+1)=\frac{(a-1)_{\underline{k+1}}(b-1)_{\underline{k+1}}}{(ab)^{k+1}}.
\]
* If \(u,v\in A\), so \(a\ge2\), then
\[
\Pr(D>2k)=\frac{(a-2)_{\underline{k}}(b-1)_{\underline{k}}}{(ab)^k}.
\]
* If \(u,v\in B\), interchange \(a,b\) in the second formula.

The products become zero when the path cannot be long enough. The two-point distributions are thus explicitly determined, including the parts of size one. In addition, for any sequence \(a,b\to\infty\), without a bound on their ratio, put \(s_{a,b}=\sqrt{ab/(a+b)}\). For either choice of parts of the two fixed endpoints, with distinct vertices available, one has
\[
\frac{D}{2s_{a,b}}\ \xrightarrow{\mathrm d}\ R,\qquad \Pr(R>x)=e^{-x^2/2}\quad(x\ge0),
\]
where \(R\) is a Rayleigh random variable of scale one. The finite formulas, not the Rayleigh scaling itself, are the principal result.

## Assumptions and scope
All graph edges have unit weight. The random object is a **uniform spanning tree**, not a minimum-weight spanning tree or the complete bipartite host graph itself. The endpoints are deterministic and distinct; the tree distance counts its edges. In the same-part cases that part must contain at least two vertices. There is no restriction on how unbalanced \(a\) and \(b\) may be. The first two exact laws apply to all finite sizes, and the scaling statement requires both part sizes tending to infinity.

## Proof
Write \(r_A,r_B\) for the numbers of vertices in the two parts of a prescribed simple path \(P\), with \(1\le r_A\le a\), \(1\le r_B\le b\). A tree containing every edge of \(P\) is equivalent, by contraction of \(P\), to a spanning tree of a weighted multigraph with one contracted vertex \(w\), \(a-r_A\) other \(A\)-vertices and \(b-r_B\) other \(B\)-vertices. The remaining cross-part edges have weight one; edges from \(w\) to an outside \(A\)-vertex have total weight \(r_B\), and those from \(w\) to an outside \(B\)-vertex have total weight \(r_A\). Removing the row and column for \(w\) from its Laplacian leaves
\[
M=\begin{pmatrix}
 bI_{a-r_A}&-J_{a-r_A,b-r_B}\\
 -J_{b-r_B,a-r_A}&aI_{b-r_B}
\end{pmatrix}.
\]
Here \(J\) denotes an all-one matrix, with the usual empty-block convention. By the matrix-tree theorem and the rank-one determinant lemma,
\[
\det M=b^{a-r_A}a^{b-r_B}
\left(1-\frac{(a-r_A)(b-r_B)}{ab}\right).
\]
This formula remains valid if either block is empty. Since \(K_{a,b}\) itself has \(a^{b-1}b^{a-1}\) spanning trees, division yields
\[
\Pr(P\subseteq T)=\frac{ar_B+br_A-r_Ar_B}{a^{r_B}b^{r_A}}.\tag{1}
\]

For \(u\in A\), \(v\in B\), a simple path of length \(2j+1\) uses \(j+1\) vertices of each part. There are exactly \((a-1)_{\underline j}(b-1)_{\underline j}\) such ordered paths with these fixed endpoints. Every tree has exactly one path between \(u,v\), so these path events are disjoint. Inserting \(r_A=r_B=j+1\) into (1) gives
\[
\Pr(D=2j+1)=\frac{(a-1)_{\underline j}(b-1)_{\underline j}}{(ab)^j}
\frac{(j+1)(a+b-j-1)}{ab},\tag{2}
\]
for all \(j\ge0\), interpreting impossible paths as having probability zero. Set \(F_{-1}=1\) and \(F_j=(a-1)_{\underline{j+1}}(b-1)_{\underline{j+1}}/(ab)^{j+1}\). Direct subtraction yields \(F_{j-1}-F_j\) equal to the right side of (2). The finite sequence terminates at zero, so telescoping proves \(\Pr(D>2k+1)=F_k\).

For \(u,v\in A\), a path of length \(2j\), \(j\ge1\), contains \(j+1\) vertices of \(A\), and \(j\) vertices of \(B\). There are \((a-2)_{\underline{j-1}}(b)_{\underline j}\) choices. Formula (1) gives
\[
\Pr(D=2j)=\frac{(a-2)_{\underline{j-1}}(b-1)_{\underline{j-1}}}{(ab)^{j-1}}
\frac{aj+b(j+1)-j(j+1)}{ab}.\tag{3}
\]
Put \(G_0=1\) and \(G_j=(a-2)_{\underline j}(b-1)_{\underline j}/(ab)^j\). Then (3) equals \(G_{j-1}-G_j\), and telescoping proves the claimed same-part tail. The \(B\)-case follows by exchanging parts.

Finally, in the opposite-part case, the survival product may be written
\[
\Pr(D>2k+1)=\prod_{j=1}^{k+1}(1-j/a)(1-j/b),
\]
while in the \(A\)-same-part case it is \(\prod_{j=1}^{k}(1-(j+1)/a)(1-j/b)\). For fixed \(x>0\), take \(k=\lfloor xs_{a,b}\rfloor\). Since \(s_{a,b}\le\sqrt{\min(a,b)}\), every argument of each logarithm tends uniformly to one in the relevant product. The estimate \(\log(1-z)=-z+O(z^2)\), summed over at most \(O(s_{a,b})\) factors, gives
\[
\log\Pr(D>2k+1)=-\tfrac12 k^2(1/a+1/b)+o(1)=-x^2/2+o(1)
\]
for opposite-part endpoints; the same conclusion holds for same-part endpoints and their corresponding even thresholds. Parity changes a threshold by at most one, which vanishes after division by \(2s_{a,b}\). This proves the Rayleigh limit for every sequence with \(\min(a,b)\to\infty\).

## Verification
`verify.py` enumerates connected \((a+b-1)\)-edge subsets of \(K_{a,b}\) for part sizes up to four and total order at most seven, finds the marked distance by independent breadth-first search, and compares exact rational survival probabilities with the stated products. It also checks the weighted contraction cofactor by an independent fraction-free determinant implementation for all \(1\le a,b\le8\), all possible positive path part sizes, and verifies monotonicity and terminal vanishing of the formulas over part sizes through \(29\). Its last execution passed 83,789 exact assertions. This finite test is a consistency check; the all-size statements follow from the determinant and telescoping arguments above.

## Relationship to prior work
Burton and Pemantle's transfer-impedance theorem (1993; open arXiv version dated April 2, 2004) gives general edge-set inclusion probabilities in uniform spanning trees via determinants; its general formula can in principle be specialized to a fixed bipartite path but does not itself state the evaluated parity-resolved falling-factorial distance tails. Alappattu and Pitman (arXiv submitted November 25, 2006) obtain a birthday-law formula for loop-erased random walks and paths in the **complete graph** and uniform rooted forests; that path law is not the same as the alternating two-part walk of \(K_{a,b}\). Archer and Shalev's dense-graph scaling theorem (first published February 27, 2024) includes balanced-asymptotic bipartite examples and supports Rayleigh/CRT behavior there; our Rayleigh conclusion is not claimed as a novel general CRT limit. The finite all-aspect-ratios tail identities and small-part exact boundaries are the intended refinement.

## Limitations
The theorem does not describe joint distances of three or more marked vertices, the tree's diameter or its full metric-measure scaling limit. The Rayleigh limit is derived here only from the exact two-point laws and requires both parts to diverge. General transfer-current methods may make the specialized finite laws derivable without matching their explicit statement; an unlocated earlier bipartite specialization remains a genuine priority risk. Independent external validation has not been performed.

## References
1. R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances*, Annals of Probability 21 (1993), 1329–1371; public preprint https://arxiv.org/abs/math/0404048 (first arXiv posting April 2, 2004).
2. J. Alappattu and J. Pitman, *Colored loop-erased random walk on the complete graph*, https://arxiv.org/abs/math/0611775 (first submitted November 25, 2006), Combinatorics, Probability and Computing 17 (2008), 727–740.
3. E. Archer and M. Shalev, *The GHP scaling limit of uniform spanning trees of dense graphs*, Random Structures & Algorithms 65 (2024), 149–190, https://doi.org/10.1002/rsa.21213 (first published February 27, 2024).
