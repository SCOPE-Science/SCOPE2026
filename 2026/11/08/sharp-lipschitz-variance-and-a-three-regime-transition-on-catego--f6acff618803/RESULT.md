# Sharp Lipschitz variance and a three-regime transition on categorical products of cliques

## Finding

Let \(3\le a\le b\) be integers, \(N=ab\), and let \(G_{a,b}=K_a\times K_b\) denote the **categorical/direct graph product**, not the Cartesian product: its vertices are the \(a\)-by-\(b\) cells \((i,j)\), and distinct cells are adjacent exactly when **both** coordinates differ. Give the \(N\) vertices equal probability. For the real Banach space of functions modulo constants with the graph Lipschitz norm, let \(I\) be its canonical linear map into centered \(L^2\) on the vertices. Its squared operator norm is the graph spread, and is exactly

\[
\|I\|^2=\operatorname{spr}(G_{a,b})=
\frac{1}{N^2}\max\left\{
\left\lfloor\frac{N^2}{4}\right\rfloor,\quad
Nb-(b\bmod2),\quad
N(a+b-1)-(a+b-3)^2
\right\}.
\]

There are **only three possible types** of maximizing potentials, up to translation and change of overall sign; one small exceptional checkerboard type also occurs:

1. **Binary:** values \(0,1\) on an arbitrary nearly equal bipartition of the \(N\) cells.
2. **Full line:** values \(-1,1\) in nearly equal numbers on all \(b\) cells of one row (or any longest line), zero outside it.
3. **Cross star:** value \(-1\) at one cell, value \(1\) at every *other* cell in its row or column, and zero at cells outside that cross.
4. **Checkerboard exception:** only for \(a=b=3\), a \(2\)-by-\(2\) subrectangle with two diagonal \(-1\)'s and the opposite two diagonal \(1\)'s, zero elsewhere.

A type is maximizing exactly when its corresponding numerator in the displayed maximum attains the overall maximum (and the checkerboard type is additionally maximizing at \((a,b)=(3,3)\)). In particular, the complete phase diagram is:

| Parameters | Maximizing configurations |
| --- | --- |
| \(a=3,\ 3\le b\le5\) | cross stars; also checkerboards if \(b=3\) |
| \(a=3,\ b=6\) | cross stars and balanced full rows |
| \(a=3,\ b\ge7\) | balanced full rows |
| \(a=4,\ 4\le b\le9\) | cross stars |
| \(a=4,\ b\ge10\) | balanced binary; also balanced full rows when \(b\) is even |
| \(a=5,\ b\in\{5,6\}\) | cross stars |
| \(a=5,\ b\ge7\), or \(a\ge6\) | balanced binary |

The space can equivalently be viewed as the graph on the edges of \(K_{a,b}\) in which two edges are adjacent when disjoint. This distinguishes it from both the rook graph \(K_a\square K_b\) (whose edges represent intersecting pairs) and the Kneser graph on *all* pairs of a larger complete graph.

## Assumptions and scope

All graphs are undirected, simple, connected and unweighted; \(a,b\ge3\) is necessary for the asserted uniform diameter-two geometry. The Lipschitz seminorm is \(\|f\|_{\mathrm{Lip}}=\max_{uv\in E}|f(u)-f(v)|\). The centered \(L^2\) norm is \(\|f-\bar f\|_2^2=N^{-1}\sum_v(f(v)-\bar f)^2\), where \(\bar f=N^{-1}\sum_v f(v)\). Norming functions have Lipschitz seminorm one; all descriptions are modulo additive constants, not modulo arbitrary scaling.

## Proof

**1. Reduction to integer potentials.** Fix an anchor vertex and give it value zero; the graph Lipschitz unit ball on this affine hyperplane is compact. Variance is a strictly convex quadratic form on the anchored quotient, hence every maximizer is an extreme point. More directly, let the tight-edge subgraph consist of edges on which \(|f(u)-f(v)|=1\). If it is disconnected, shifting the values on one nontrivial tight component by a sufficiently small signed \(\varepsilon\) preserves all edge constraints. With \(p\in(0,1)\) the component's vertex proportion, the resulting variance is a quadratic in \(\varepsilon\) having positive coefficient \(p(1-p)\). Thus zero cannot maximize it on an open interval, a contradiction. The tight-edge graph is therefore connected; walking along its edges from the anchor proves that all maximizing values are integers. This argument also establishes integrality without assuming it from an enumeration.

For \(a,b\ge3\), any two cells in a common row have a common neighbor in a different row and a third column; likewise for cells in a common column. Two cells differing in both coordinates are adjacent. Hence the diameter is exactly two. After translating a nonconstant maximizer to have minimum zero, its values are either \(0,1\) or \(0,1,2\). In the first case, the variance is at most \(\lfloor N^2/4\rfloor/N^2\), with equality precisely on nearly equal binary partitions.

**2. Two separated extreme sets.** For the three-level case, write \(A\) for value zero and \(B\) for value two, with value one elsewhere. Both \(A\) and \(B\) are nonempty. They have no edges between them, so each cell of \(A\) shares a row or column with each cell of \(B\). Put \(s=|A|\), \(t=|B|\). Subtracting one from the potential leaves values \(-1,0,1\), and a direct moment calculation gives

\[
N^2\operatorname{Var}(f)=N(s+t)-(s-t)^2.\tag{1}
\]

Classify every pair of nonempty, disjoint cell sets with this cross-separation property. If either set is a singleton at \((i,j)\), the other lies in the union of row \(i\) and column \(j\), with at most \(a+b-2\) cells. Otherwise suppose \(A\) contains two cells in different rows and columns, say \((i,j),(k,l)\). Then every \(B\)-cell must be one of the two opposite corners \((i,l),(k,j)\). If \(B\) has at least two cells, symmetry forces \(A\) to consist of the original two corners: an alternating checkerboard. In the remaining case, \(B\) is a singleton. Finally, if \(A\) contains no pair differing in both coordinates and \(|A|\ge2\), all of \(A\) lies in one row or column. Every \(B\)-cell must then lie in the same line. This proves the exhaustive three-type structural classification.

**3. Exact optimization.** In a line of length at most \(b\), with both signs present, formula (1) is maximized by using all \(b\) positions and balancing the signs. Its numerator is \(Nb-(b\bmod2)\). For a singleton against \(k\) other cells in its row/column, formula (1) becomes

\[
F(k)=N(k+1)-(k-1)^2,\qquad 1\le k\le a+b-2.
\]

Since \(F(k+1)-F(k)=N-2k+1>0\) throughout that range (as \(N-2(a+b-2)+1=(a-2)(b-2)+1>0\)), the entire cross must be used. This yields \(N(a+b-1)-(a+b-3)^2\). The checkerboard yields \(4N\). With \(q=a+b\), the cross-star score minus \(4N\) is

\[
N(q-5)-(q-3)^2\ \ge\ 3(q-3)(q-5)-(q-3)^2
=2(q-3)(q-6)\ge0,
\]

where \(ab\ge3(a+b-3)\); equality holds only at \(a=b=3\). Together with the binary case this proves the displayed maximum. All candidates described above attain their proposed scores and satisfy the Lipschitz constraints, so no unproved feasibility requirement remains. The strict inequalities in the preceding steps give the full equality classification.

**4. Phase analysis.** Write \(a\le b\). For \(a=3\), the full-row score exceeds the binary score, and cross-star minus full-row is \(b(6-b)+(b\bmod2)\); this changes sign exactly at \(b=6\). For \(a=4\), the binary score is \(4b^2\), the full-row score is \(4b^2-(b\bmod2)\), and cross-star minus binary is \(-b^2+10b-1\); the crossing lies between \(b=9\) and \(b=10\). For \(a=5\), the row score is strictly below binary, and four times cross-star minus binary equals \(-9b^2+64b-16+(b\bmod2)\); its last positive integer case is \(b=6\). For \(a\ge6\), put \(u=1/a\), \(v=1/b\). The normalized cross-star score is

\[
H(u,v)=u+v-uv-(u+v-3uv)^2.
\]

On \(0<u,v\le1/6\), both partial derivatives are positive: for instance \(\partial_u H=1-v-2(u+v-3uv)(1-3v)>5/6-2/3>0\). Thus \(H(u,v)\le H(1/6,1/6)=35/144\), whereas binary gives at least \(1/4-1/(4N^2)>35/144\). The full-row score is also smaller than binary for \(a\ge5\). All asserted parameter regimes and ties follow.

## Verification

Run the standalone `checker.py` using Python 3, without third-party dependencies. It independently enumerates every integral Lipschitz assignment on grids \(3\)-by-\(3\) and \(3\)-by-\(4\); exhaustively enumerates pairs of cross-separated extreme sets on six small grids; and checks all phase/tie identities for \(3\le a\le b<300\). The reported finite checks corroborate, but are not used in place of, the universal structural proof. Source text and checker are self-contained in this package.

## Relationship to prior work

The graph-spread invariant and the integral-extremizer principle are prior work: Alon, Boppana and Spencer (1998), especially their Theorem 2.1. Their Theorem 3.6 concerns products equipped with the **sum metric**, not the categorical graph product defined here. Its known Cartesian tensorization does imply the numerical \(3\)-by-\(3\) case via the small self-complementary rook graph, but does not determine the general rectangular family or its optimizer phases. Addario-Berry, Janson and McDiarmid (arXiv:0902.1156, first posted February 6, 2009) focus on random graph spread, not this exact deterministic classification. Yancey's later study (arXiv:1705.09725) analyzes the Cartesian product and concentration extremizers, not this categorical-product formula. These previously known structural principles are used as motivation and context; they are not asserted as new.

The novelty claim is restricted to the exact three-envelope formula, the parameter-by-parameter phase diagram, and the complete norming-function classification for this categorical family. Exact equivalent treatments in unindexed sources cannot be ruled out.

## Limitations

The theorem assumes \(a,b\ge3\), unit edges, equal vertex masses, and real functions with quadratic variance. It does not cover the disconnected or different-diameter small products, weighted vertex probabilities, arbitrary factors in a direct graph product, or nonlinear target norms. The finite checker only tests specified finite parameter ranges; the infinite family is handled by proof. Originality is an evidence-based comparison, not an exhaustive guarantee. Independent mathematical validation has not been conducted.

## References

1. N. Alon, R. Boppana, J. Spencer, *An Asymptotic Isoperimetric Inequality*, Geometric and Functional Analysis **8** (1998), 411–436; DOI `10.1007/s000390050062`. Author-hosted full text: `https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf` (especially Theorems 2.1 and 3.6).
2. L. Addario-Berry, S. Janson, C. McDiarmid, *On the Spread of Random Graphs*, first arXiv version February 6, 2009, `arXiv:0902.1156`; `https://arxiv.org/abs/0902.1156`.
3. M. P. Yancey, *Probabilistic and Geometrical Applications to Graph Theory*, first arXiv version May 26, 2017, `arXiv:1705.09725`; `https://arxiv.org/abs/1705.09725`.
