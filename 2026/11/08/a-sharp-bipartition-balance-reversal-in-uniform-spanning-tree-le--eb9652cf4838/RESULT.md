# A sharp bipartition-balance reversal in uniform-spanning-tree leaf counts under one edge addition

## Finding
Let \(a\geq2\) and \(b\geq1\) be integers. Form \(H_{a,b}\) from the complete bipartite graph \(K_{a,b}\) by adding one edge between two distinct vertices in its part of size \(a\). For a connected finite graph \(G\), let \(L(G)\) be the number of degree-one vertices of a uniformly sampled spanning tree of \(G\). Then
\[
\Delta_{a,b}:=\mathbb E[L(H_{a,b})]-\mathbb E[L(K_{a,b})]
=\frac{2}{b+2}\left[\left(1-\frac1b\right)^{a-2}-\left(1-\frac1a\right)^{b-1}\right].
\]
At the boundary \(b=1,a=2\), the first power is interpreted as \(0^0=1\). The response obeys the complete strict sign classification
\[
\Delta_{a,b}>0\iff b\geq a,\qquad
\Delta_{a,b}=0\iff(a,b)=(2,1),\qquad
\Delta_{a,b}<0\iff b<a\ \text{and}\ (a,b)\neq(2,1).
\]
Thus adding the same natural type of edge can either raise or lower the expected number of leaves, depending exactly on the relative part sizes.

## Assumptions and scope
All graphs are finite, simple and connected. A spanning tree is selected uniformly from all labeled spanning trees; this is not the minimum spanning tree of independently weighted edges. The added edge has endpoints in the size-\(a\) part and did not previously exist. The result holds for every integer pair \(a\ge2,b\ge1\), with no asymptotic conditions. The part sizes are ordered by the location of the added edge, not by their magnitude. The statement concerns the *expectation* of the total leaf count, not stochastic domination of the entire leaf-count distribution.

## Proof
Label the size-\(a\) vertices by \(u_1,\dots,u_a\) and the size-\(b\) vertices by \(v_1,\dots,v_b\). Attach positive vertex indeterminates \(x_1,\dots,x_a\) and \(y_1,\dots,y_b\), and weight every edge between vertices \(i,j\) by the product of their variables. Write \(X=\sum_{i=1}^a x_i\), \(Y=\sum_{j=1}^b y_j\) and \(P=\prod_i x_i\prod_j y_j\). A monomial of the weighted spanning-tree enumerator has the exponent of each vertex variable equal to its degree in the tree.

The established complete-bipartite weighted tree identity is
\[
Z_0(\mathbf x,\mathbf y)=P X^{b-1}Y^{a-1}.
\]
This is the two-part specialization of the complete-multipartite formula attributed to Clark (2003) and treated by Klee and Stamps (2019, Theorem 3); it is background, not a new claim.

We now evaluate the effect of inserting the edge \(u_1u_2\) with weight \(x_1x_2\). On the original weighted bipartite network, set potentials \(\phi(u_1)=1/(x_1Y)\), \(\phi(u_2)=-1/(x_2Y)\), and \(\phi=0\) at all other vertices. Currents from \(u_1\) and to \(u_2\) have magnitude one because the total conductance from \(u_i\) to the other part is \(x_iY\). At every \(v_j\) the net current is zero: its two nonzero contributions cancel because \(x_1\phi(u_1)+x_2\phi(u_2)=0\). Hence the weighted effective resistance between \(u_1,u_2\) is exactly
\[
R_{12}=\phi(u_1)-\phi(u_2)=\frac{1/x_1+1/x_2}{Y}.
\]
By the one-edge matrix-tree update, or equivalently the matrix determinant lemma on a reduced Laplacian, the new weighted tree enumerator is
\[
\begin{aligned}
Z_1&=Z_0(1+x_1x_2R_{12})\\
&=P X^{b-1}Y^{a-2}(Y+x_1+x_2).
\end{aligned}
\]
This identity is polynomial in the vertex variables and remains valid for the edge cases \(a=2\) and \(b=1\).

Set all vertex variables equal to one and divide the enumerator by its value there. This gives the joint probability-generating polynomial for the tree degree vector. If a vertex variable occurs as a compulsory single factor, the chance that its degree is exactly one is the value obtained by setting that variable to zero in the remaining normalized factor. Thus, in \(K_{a,b}\), each size-\(a\) vertex is a leaf with probability
\[
p_A=\left(1-\frac1a\right)^{b-1},
\]
and each size-\(b\) vertex is a leaf with probability
\[
p_B=\left(1-\frac1b\right)^{a-1}.
\]
In \(H_{a,b}\), each of the two added-edge endpoints has leaf probability \(p_A(b+1)/(b+2)\), each of the other size-\(a\) vertices retains probability \(p_A\), and each size-\(b\) vertex has probability
\[
p_B'=\frac{b+1}{b+2}\left(1-\frac1b\right)^{a-2}.
\]
These formulae include \(a=2,b=1\) by evaluating all zero powers as one. Summing all vertex leaf probabilities and subtracting gives
\[
\begin{aligned}
\Delta_{a,b}
&=2\left(\frac{b+1}{b+2}-1\right)p_A+b(p_B'-p_B)\\
&=-\frac2{b+2}p_A+\frac2{b+2}\left(1-\frac1b\right)^{a-2},
\end{aligned}
\]
which is the asserted expression.

For the sign, first let \(a=2\). At \(b=1\) both powers equal one, while at every \(b\ge2\) the first power is one and the second is strictly below one. Now fix \(a\ge3\). As the positive integer \(b\) increases, \((1-1/b)^{a-2}\) increases strictly, while \((1-1/a)^{b-1}\) decreases strictly. At \(b=a-1\), both exponents are \(a-2\) but the base of the first expression is smaller, so the difference is strictly negative. At \(b=a\), the bases agree and the exponent of the first is one less, so the difference is strictly positive. Monotonicity establishes the claimed sharp classification for all other integers \(b\).

## Verification
The self-contained `verify.py` uses integer, rational and combinatorial arithmetic without third-party packages. Its independent checks are: (1) exact Kirchhoff cofactors of weighted graph Laplacians against both claimed generating polynomials, with nonuniform integer weights; (2) exhaustive small-graph spanning-tree enumeration with actual degree-one counts against the formula; and (3) exact rational sign tests for all \(2\le a\le120\), \(1\le b\le120\). The script outputs `VERIFY_OK 14416 exact assertions`. The universal statements are proved above; finite checks do not replace the all-order argument. To reproduce, run `python3 verify.py` in the directory containing this result.

## Relationship to prior work
The weighted complete-bipartite enumerator \(Z_0\) is classical, explicitly attributed to Clark (2003) by Klee and Stamps (2019, Theorem 3). Their formula does not state the perturbed enumerator for an additional *within-part* edge, nor compare the expected number of leaves before and after that addition. Dong and Ge (2021, Theorem 4) count spanning trees of an unmodified complete bipartite graph subject to a prescribed forest of already-present edges; this does not include a newly introduced within-part edge. General finite-graph degree formulas, including Rapoport (2023), can provide an alternative starting point but do not state the all-parameter edge-addition response or its sign threshold in the inspected material. The contribution here is the exact perturbation response and sharp global balance classification, not a claim that the determinant lemma or the unperturbed weighted enumerator is new.

## Limitations
The result addresses one added edge within a complete-bipartite part, and only the expected number of leaves. It does not assert stochastic monotonicity, characterize several added edges, or give the law of the total leaf count. The formula is derived from established enumeration and rank-one methods, and earlier specialized literature could contain an equivalent evaluation; historical priority remains subject to further literature review. No independent external mathematical audit has been performed.

## References
- S. Klee and M. T. Stamps, *Linear algebraic techniques for weighted spanning tree enumeration*, arXiv:1903.03575v1 (first public 2019-02-27), especially Section 2, Theorem 3. https://arxiv.org/abs/1903.03575
- F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294v1 (2021-03-09), especially Theorem 4. https://arxiv.org/abs/2103.05294
- A. Rapoport, *Correlations in uniform spanning trees: a fermionic approach*, arXiv:2312.14992v1 (2023-12-22), especially finite-graph joint-degree and leaf-event formulas. https://arxiv.org/abs/2312.14992
