# A modulo-four rigidity law for majority equilibria on two-subset Kneser graphs

## Finding
For each integer \(n\ge5\) satisfying \(n\equiv0\) or \(1\pmod4\), let \(G_n=KG(n,2)\). Its vertices are the unordered two-element subsets of \([n]\), with two vertices adjacent precisely when the subsets are disjoint. Each vertex carries a bit, and at each synchronous update it adopts the strict majority bit among its open neighbors, retaining its bit on a tie.

**Theorem.** If \(n\equiv0\pmod4\), the only fixed configurations are the two unanimous configurations. If \(n\equiv1\pmod4\), every nonunanimous fixed configuration is exactly the indicator of a labelled simple \((n-1)/2\)-regular graph on \([n]\), and every such graph supplies a fixed configuration. Therefore, writing \(f_n\) for the number of *labelled, one-step fixed* configurations,
\[
f_n=\begin{cases}
2,&n\equiv0\pmod4,\[2mm]
2+[x_1^{(n-1)/2}\cdots x_n^{(n-1)/2}]
\displaystyle\prod_{1\le i<j\le n}(1+x_i x_j),&n\equiv1\pmod4.
\end{cases}
\]
The coefficient counts the regular graphs with the given labelled vertex set. At \(n=5\) it equals \(12\), so \(f_5=14\). At \(n=8\), \(f_8=2\). At every \(n\equiv1\pmod4\) there are nonunanimous fixed configurations.

## Assumptions and scope
All graph vertices and ground-set elements are labelled; no quotient by graph automorphisms is taken. The graph is finite, simple and undirected. Let \(m=\binom n2\) denote the number of Kneser vertices, and \(D=\binom{n-2}2\) their common degree. For the two stipulated residue classes, \(D\) is odd, so ties never occur; the stated tie rule is then immaterial. The assertion concerns \(F(x)=x\), not the full recurrent set \(F^2(x)=x\), attraction times or the other two residue classes.

Associate to a binary Kneser configuration the set \(E\subseteq\binom{[n]}2\) of active pairs. Write \(T=|E|\), and let \(d_i\) be the degree of \(i\) in the ordinary graph \(([n],E)\). The Kneser-neighbor count at the pair \(\{i,j\}\) is exactly
\[
N_{ij}=T-d_i-d_j+\mathbf1_{\{i,j\}\in E}.
\]

## Proof
First note that \(D\) is odd when \(n\equiv0,1\pmod4\). Let \(h=(D+1)/2\) and \(k=h-1=(D-1)/2=(n-1)(n-4)/4\). Suppose \(E\) is a fixed configuration other than the empty one or the complete one. At every active pair \(\{i,j\}\in E\), the majority requirement and the exact neighbor count give
\[
T-d_i-d_j+1\ge h,
\qquad d_i+d_j\le T-k.
\]
Summing over all active pairs yields the important identity and inequality
\[
\sum_{i=1}^{n}d_i^2
=\sum_{\{i,j\}\in E}(d_i+d_j)
\le T(T-k).
\]
Since \(\sum_i d_i=2T\), Cauchy--Schwarz implies
\[
\frac{4T^2}{n}\le \sum_i d_i^2\le T(T-k).
\]
As \(T>0\) and \(n>4\), dividing by \(T\) and rearranging gives
\[
T\ge\frac{nk}{n-4}=\frac{n(n-1)}4=\frac m2.
\]
Because every vertex of \(G_n\) has odd degree, bitwise complementation commutes with the majority update. The complement of \(E\) is also a nonempty fixed configuration, so applying the same bound to it gives \(m-T\ge m/2\). Thus \(T=m/2\).

Equality must hold throughout the Cauchy--Schwarz chain. Equality in Cauchy--Schwarz forces all the ordinary degrees to agree:
\[
d_1=\cdots=d_n=\frac{2T}{n}=\frac{n-1}{2}.
\]
When \(n\equiv0\pmod4\), the last quantity is a half-integer, impossible for graph degrees. Accordingly only the two unanimous configurations remain.

When \(n\equiv1\pmod4\), the degree is an integer. Conversely, let \(E\) be *any* simple graph on \([n]\) of degree \(d=(n-1)/2\) at every vertex, so \(T=nd/2=n(n-1)/4\). Using the displayed neighbor-count identity gives
\[
N_{ij}=\begin{cases}
h,&\{i,j\}\in E,\\
h-1,&\{i,j\}\notin E.
\end{cases}
\]
Thus every active vertex sees a strict active majority and every inactive vertex sees a strict inactive majority. Hence the indicator is fixed. This proves the characterization.

The multivariate coefficient in the theorem selects exactly those simple edge subsets with every vertex incident to \((n-1)/2\) chosen edges, proving the enumeration. For existence at each \(n=4r+1\), take the circulant graph in which \(i\) and \(j\) are joined when their cyclic distance in \(\mathbb Z/n\mathbb Z\) lies in \(\{1,\ldots,r\}\). Each vertex has exactly \(2r=(n-1)/2\) neighbors. In the first case \(n=5\), the regular graphs are the 12 labelled five-cycles.

## Verification
The companion standalone Python 3 program `check_kg_majority.py` implements two different descriptions of each majority update: direct disjoint-pair adjacency and the active-edge-degree identity. It exhausts all \(2^{10}=1024\) configurations at \(n=5\), obtaining 14 fixed states (two unanimous and 12 with five active pairs). It also compares the two update implementations on 7,500 pseudorandom configurations for \(n=5,8,9,12,13\), and checks explicit nonunanimous circulant equilibria for \(n=5,9,13\). Its deterministic output is included as `checks.txt`. Finite checks corroborate but do not replace the all-size argument above.

## Relationship to prior work
Majority-dynamics convergence to a fixed point or two-cycle on finite symmetric networks is classical; it is not claimed as a contribution here. Benjamini, Chan, O'Donnell, Tamuz and Tan (2014) give a framework for majority dynamics on finite and unimodular graphs, but their theorems do not state this Kneser fixed-point classification. Cannings (2009) considers majority and minority models on other regular network families, including complete graphs and hypercubes; an equivalent result hidden in an unavailable part of that paper cannot be excluded.

Some previously published exact computations address the Petersen graph \(KG(5,2)\) individually and therefore cover the 14-state numerical example, which is not claimed as new. Previously published graph-dynamics results for the same two-subset Kneser family use neighbor-XOR or NOR rather than strict majority, and their orbit classifications do not imply the present fixed-point theorem. A general majority result for line graphs concerns the complementary triangular graph \(J(n,2)\), whose neighbor relation is intersection rather than disjointness; the active-neighbor inequalities are different. The contribution is the simultaneous all-size classification in the two odd-degree residue classes and its exact degree-regularity bijection, not the elementary fact that a particular small example has fixed configurations.

## Limitations
This theorem does not classify configurations with primitive temporal period two, nor configurations in the remaining residue classes \(n\equiv2,3\pmod4\), whose Kneser degree is even and requires a tie convention. The regular-graph coefficient formula is exact but does not claim a closed elementary product for the number of labelled regular graphs. Historical priority has been checked against accessible sources, but unindexed or inaccessible general theorems might overlap. No independent external mathematical audit has been performed.

## References
1. Chris Cannings, *The majority and minority models on regular and random graphs*, 1st International Conference on Game Theory for Networks (2009), DOI: 10.1109/GAMENETS.2009.5137464. Public source date: 2009-06-26. https://eudl.eu/doi/10.1109/gamenets.2009.5137464
2. Itai Benjamini, Siu-On Chan, Ryan O'Donnell, Omer Tamuz and Li-Yang Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486 (first posted 2014-05-11). https://arxiv.org/abs/1405.2486
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), DOI: 10.1016/0012-365X(80)90121-1 (general periodicity background, not a Kneser fixed-point enumeration).
