# A sharp signed leaf-dependence classification for uniform spanning trees of crown graphs

## Finding

Let \(n\ge5\) and let \(G_n=K_{n,n}\setminus M\) be the graph obtained from complete bipartite \(K_{n,n}\) by removing a fixed perfect matching \(M\). Let \(T\) be uniformly distributed over all spanning trees of \(G_n\). For a vertex \(v\) put \(I_v=\mathbf1_{\{\deg_T(v)=1\}}\). Every vertex has the same leaf probability \(p_n\). There are exactly three unordered pair types: an adjacent cross-part pair, a matched nonedge across parts, and a pair within one part. With \(B=n(n-2)\), \(c=n^2-3n+1\), \(x=(n-1)(n-3)\), \(y=n^2-4n+2\), and \(D=(n-1)n^{n-2}(n-2)^{n-1}\), their joint leaf probabilities are

\[
p_n=(c/B)^{n-2},\qquad
P_{\mathrm{adj}}=\frac{(n-2)^2c\,x^{n-3}}{D},\qquad
P_{\mathrm{matched}}=\frac{(n-1)^2(n-2)(n-3)x^{n-3}}{D},\qquad
P_{\mathrm{same}}=\frac{(n-1)^2(n-2)(n-3)y^{n-3}}{D}.
\]

For all \(n\ge5\),
\[
P_{\mathrm{adj}}>p_n^2>P_{\mathrm{matched}}>P_{\mathrm{same}}.
\]
Hence *adjacent* vertex leaf indicators are strictly positively correlated, while both nonadjacent pair classes are strictly negatively correlated. The same strict ordering holds at \(n=4\). At the boundary \(n=3\), \(G_3\) is a six-cycle, \(P_{\mathrm{adj}}=1/6\), \(p_3=1/3\), and the last two joint probabilities are both zero. The all-order sign result for \(n\ge5\), not these small covered examples, is the contribution.

## Assumptions and scope

All graphs are finite, undirected, simple, unweighted and connected. The sampled tree is uniform over *all* spanning trees, not a uniform labeled tree independent of the graph, and leaf means degree one in the sampled spanning tree. The perfect matching removed from \(K_{n,n}\) has \(n\) edges. Pair types and equality cases are exhaustive by automorphisms. No assertion concerns edge-indicator covariances or conditional multivertex leaf events.

## Proof

**1. Counting a prescribed leaf set.** For one or two specified vertices \(S\), with \(G_n-S\) connected and at least two vertices, every spanning tree in which all \(S\) are leaves arises uniquely by choosing a spanning tree of \(G_n-S\) and one edge from each \(v\in S\) to the complement. If two vertices in \(S\) are joined by an edge, that edge cannot belong to a tree with both endpoints leaves when the tree has more than two vertices. Consequently
\[
\Pr(S\subseteq L(T))=\frac{\tau(G_n-S)}{\tau(G_n)}\prod_{v\in S}d_{G_n-S}(v),
\]
where \(\tau\) denotes the spanning-tree count and \(d_{G_n-S}(v)\) counts neighbors of \(v\) outside \(S\). A disconnected complement yields zero, in agreement with the formula.

**2. A matching-deletion determinant.** Write \(H_{a,b,t}=K_{a,b}\setminus M_t\), where \(M_t\) is a matching of \(t\) edges, \(1\le t\le\min(a,b)\). The \(t\times t\) transfer-current matrix of those matching edges in the uniform spanning tree on \(K_{a,b}\) has diagonal entries \((a+b-1)/(ab)\) and off-diagonal entries \(-1/(ab)\), after all edges are oriented from the \(a\)-part to the \(b\)-part. These entries follow directly by solving the Kirchhoff equations for a unit current across an edge: the diagonal is its effective resistance and the disjoint-edge voltage drop is \(-1/(ab)\). The spanning-tree deletion determinant, or equivalently the matrix-tree lemma applied to removing these \(t\) conductances, gives
\[
\tau(H_{a,b,t})=a^{b-1}b^{a-1}\det(I_t-K_t)
= a^{b-1}b^{a-1}\frac{(ab-a-b)^{t-1}(ab-a-b+t)}{(ab)^t}.
\]
This identity remains correct when the deletion disconnects the graph (the right-hand side is zero). It specializes to \(\tau(G_n)=D\). Removing a single vertex leaves \(H_{n-1,n,n-1}\) and gives \(\tau(G_n-v)=(n-2)c^{n-2}\). Removing two vertices gives respectively
\[
\begin{aligned}
\tau(G_n-\{u,v\})&=c\,x^{n-3}&&\text{for adjacent cross-part vertices},\\
&=(n-2)(n-3)x^{n-3}&&\text{for a deleted matched pair},\\
&=(n-2)(n-3)y^{n-3}&&\text{for vertices in one part}.
\end{aligned}
\]
The attachment degrees are \(n-2\) for the adjacent cross-part pair, and \(n-1\) otherwise. Substitution in Step 1 yields exactly the four probabilities claimed.

**3. Negative signs.** Elementary cancellation yields
\[
\frac{P_{\mathrm{matched}}}{p_n}=(x/c)^{n-2},\qquad
\frac{P_{\mathrm{same}}}{P_{\mathrm{matched}}}=(y/x)^{n-3}.
\]
Because \(c^2-Bx=1>0\), one has \(P_{\mathrm{matched}}<p_n^2\). Because \(y=x-1<x\), one has \(P_{\mathrm{same}}<P_{\mathrm{matched}}\) for \(n\ge4\). Both are zero at \(n=3\), which is handled separately.

**4. Strict positive sign for adjacent vertices.** The cancellation in Step 2 gives
\[
\frac{P_{\mathrm{adj}}}{p_n}=\frac{n-2}{n-1}(x/c)^{n-3}.
\]
To prove this strictly exceeds \(p_n\), put \(z=1/n\), \(a=(3+\sqrt5)/2\), \(b=(3-\sqrt5)/2\), and \(L_j=a^j+b^j\). For \(n\ge4\), the logarithm of the quotient \(P_{\mathrm{adj}}/p_n^2\) equals
\[
F(z)=(z^{-1}-1)\log(1-2z)+(z^{-1}-4)\log(1-z)
+(z^{-1}-3)\log(1-3z)+(-2z^{-1}+5)\log(1-3z+z^2).
\]
This is analytic for \(0<z<1/3\). Expanding each logarithm using \(1-3z+z^2=(1-az)(1-bz)\), the constant term and the coefficients of \(z,z^2,z^3\) vanish. For every integer \(j\ge4\), the coefficient of \(z^j\) is \(N_j/[j(j+1)]\), where
\[
N_j=(1-j)2^j+3j+4+3^{j+1}+2jL_{j+1}-(5j+5)L_j.
\]
The recurrence \(L_0=2\), \(L_1=3\), \(L_{j+1}=3L_j-L_{j-1}\) gives for \(j=4,\ldots,21\) the strictly positive integers
\[
20,150,735,2996,11052,38370,128040,415822,1324609,4160520,12931380,39873588,122200556,372739110,1132740195,3432359804,10376670108,31313612550.
\]
For \(j\ge22\), rewrite
\[
N_j=3^{j+1}-(j-1)2^j+3j+4
+((\sqrt5-2)j-5)a^j-((\sqrt5+2)j+5)b^j.
\]
Here \(((\sqrt5-2)j-5)a^j\ge0\) because \(j\ge22\). Also \((j-1)2^j\le3^{j+1}/2\) for \(j\ge22\), as verified at the initial value and preserved since the ratio \((j-1)(2/3)^j\) decreases for \(j\ge4\); and \(((\sqrt5+2)j+5)b^j<1\) for \(j\ge22\), using \(b<2/5\), \(\sqrt5+2<17/4\) and the monotonic decrease of \(((17/4)j+5)(2/5)^j\). Thus \(N_j>0\) for every \(j\ge22\). Consequently \(F(z)>0\) for \(0<z<1/3\), in particular every \(n\ge4\). For \(n=3\), direct substitution gives \(P_{\mathrm{adj}}=1/6>1/9=p_3^2\). This completes the exhaustive strict sign classification.

## Verification

The attached dependency-free Python script `crown_leaf_check.py` independently constructs the original graph Laplacian, computes exact Kirchhoff cofactors using rational elimination for every \(3\le n\le7\), and checks the four closed formulas and sign ordering. It separately checks the exact integer recurrence and positivity of the first eighteen nonzero logarithmic-series coefficients. Run with `python3 crown_leaf_check.py`; the observed result is `VERIFY_OK 51 exact assertions`. The finite checks are ancillary to the all-order determinant and positive-series proofs.

## Relationship to prior work

Nachmias and Peres (2020), Theorems 1.1–1.5, identify universal local limits of USTs on regular high-degree graph sequences, including asymptotic leaf density. They do not provide finite-order pairwise leaf-covariance signs at distinguished nearby vertices; their limit does not imply the strict order-\(n^{-4}\) effect here. Klee and Stamps (2020), Proposition 8, give the exact crown-graph Laplacian characteristic polynomial and hence its known tree count; they do not treat joint leaf events. Previously documented results include both a full sign classification for small circular ladders (whose four-rung case coincides with \(G_4\)) and negative all-leaf inequalities on complete multipartite graphs; those do not imply the all-size crown result for \(n\ge5\). The theorem is a strict finite-graph signed-dependence statement, not merely the known Laplacian or tree-count formula.

## Limitations

The theorem is for unweighted crown graphs and ordinary uniform spanning trees only. It does not assert that the leaf indicator family is globally associated, and it does not give a multivertex sign characterization. Its small \(n=3,4\) examples are not claimed to be independently new. Although prior literature and accessible mathematical records were compared for implications, complete historical priority cannot be guaranteed, and no independent external mathematical audit has taken place.

## References

- A. Nachmias and Y. Peres, *The local limit of uniform spanning trees*, arXiv:2011.08833, first public 17 November 2020, https://arxiv.org/abs/2011.08833.
- S. Klee and M. T. Stamps, *Eigenvalues of graph Laplacians via rank-one perturbations*, arXiv:2008.01669, first public 4 August 2020, https://arxiv.org/abs/2008.01669; see Proposition 8.
- Kirchhoff's matrix-tree theorem and the standard transfer-current deletion identity for finite uniform spanning trees (used with their explicit proof ingredients above).
