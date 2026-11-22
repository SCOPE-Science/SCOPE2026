# Coefficientwise extremality and mod-six balanced orientations of complete bipartite one-point type bases

## Finding

Let \(\mathcal H\) be the countable homogeneous oriented graph whose age consists of all finite loopless oriented graphs having no *transitive* tournament on three vertices. Directed three-cycles are allowed, and a pair may be a nonedge. Fix \(b\ge1\), and let \(D\) range over all orientations of the induced, individually named complete bipartite graph \(K_{3,b}\), with three vertices in the first shore and \(b\) in the second shore. Define \(P_D(z)\) to count complete nonalgebraic singleton types over this named base by the number of old vertices adjacent to the new vertex.

Write \(b=6q+r\), \(0\le r<6\), \(h=\lfloor b/2\rfloor\), and \(H=\lceil b/2\rceil\). For every \(D\), the following two *coefficientwise* inequalities hold:

\[
P_{\min,b}(z)\preceq P_D(z)\preceq P_{\max,b}(z),
\]
where coefficientwise order compares every coefficient separately, and

\[
\begin{aligned}
P_{\min,b}(z)={}&(1+2z)^3+(1+2z)^b-1\\
&+3z\big((1+z)^h+(1+z)^H-2\big)\\
&+z^2\big((6-r)((1+z)^q-1)+r((1+z)^{q+1}-1)\big),\\
P_{\max,b}(z)={}&(1+2z)^3+(1+2z)^b-1\\
&+\big((1+z)^3-1\big)\big((1+z)^b-1\big).
\end{aligned}
\]

For the maximum there are exactly two labeled extremizers: all cross edges point from the first shore to the second, or all point in the opposite direction. For the minimum, encode the three directions incident to any second-shore vertex by a binary column \(\epsilon\in\{0,1\}^3\) (bit zero means first-shore to second-shore). The minimizers are *exactly* those matrices satisfying all three conditions:

1. Neither constant column \(000\) nor \(111\) occurs.
2. Each of the other six binary columns occurs \(q\) or \(q+1\) times, with exactly \(r\) columns occurring \(q+1\) times.
3. Each of the three rows has either \(h\) or \(H\) entries equal to one.

Such minimizers exist for every \(b\ge1\); the number of labeled minimizing orientations is
\[
S_r\,\frac{b!}{(q!)^{6-r}((q+1)!)^r},\qquad
(S_0,S_1,S_2,S_3,S_4,S_5)=(1,6,3,14,3,6).
\]

The extremal total type counts are
\[
\begin{aligned}
P_{\min,b}(1)&=3^b+14+3(2^h+2^H)+(6+r)2^q,\\
P_{\max,b}(1)&=3^b+7\cdot 2^b+19.
\end{aligned}
\]
Subtracting the types whose selected neighbors lie entirely within one shore gives the mixed-shore counts \(R_{\min,b}\) and \(R_{\max,b}\). Their ratio grows as \(\Theta(2^{b/2})\), even though all these bases have the same underlying unoriented graph.

## Assumptions and scope

An *oriented graph* here has at most one directed edge per unordered pair (and may have nonedges). Forbidden triangles are only the transitively oriented *complete* triples. A nonalgebraic singleton type means the new point is distinct from every named parameter; adjacency counts an old vertex joined to the new point by an arc in either direction. The Fraïssé extension property ensures that every permitted finite one-point pattern is realized and yields precisely one complete type because the structure is homogeneous. Individual naming means that no automorphism-orbit quotient is used. All formulas hold for every integer \(b\ge1\), including all small remainder cases.

For a subset \(R\subseteq\{1,2,3\}\) of rows and direction bit \(c\in\{0,1\}\), write \(m_{R,c}\) for the number of second-shore vertices whose direction bits all equal \(c\) on \(R\). Write \(f_m(z)=(1+z)^m-1\), with \(f_0(z)=0\).

## Proof

**1. Type-support correspondence.** Each named old vertex is either unrelated to the new point, receives an arc from the new point, or sends an arc to the new point. If a selected old arc points \(u\to v\), then among the four oriented configurations of the new point with \(u,v\), exactly one avoids creating a transitive tournament: the cyclic configuration \(x\to u\to v\to x\). Thus, whenever selected neighbors meet both old shores, their cross-edges must all point consistently in one direction. Conversely, any nonempty pair of selected shores spanning a monochromatically oriented complete sub-biclique has one admissible choice of all new arcs; selected neighbors contained entirely in just one shore have two independently chosen arc directions apiece. This proves the *exact* support identity
\[
P_D(z)=(1+2z)^3+(1+2z)^b-1+
\sum_{\emptyset\ne R\subseteq[3]} z^{|R|}\sum_{c=0}^{1}f_{m_{R,c}}(z).
\tag{1}
\]
No other triangles can arise because each old shore is independent.

**2. Coefficientwise minimum.** The polynomials \(f_m\) are increasing and discretely convex coefficientwise: whenever \(a\ge c+2\),
\[
f_a+f_c-f_{a-1}-f_{c+1}=z((1+z)^{a-1}-(1+z)^c)\succeq0.\tag{2}\]
For singleton row subsets \(R\), the two complementary counts sum to \(b\). Balancing them at \(h,H\) therefore yields the claimed lower bound \(3z(f_h+f_H)\).

For the three choices of two-element row subsets and the two direction bits, there are six counts \(m_{R,c}\). Every nonconstant binary column has exactly one monochromatic two-row restriction, and every constant column has three. If \(t\) is the number of constant columns, these six counts sum to \(b+2t\). By (2), monotonicity and balancing, their contribution is at least \((6-r)f_q+r f_{q+1}\), *coefficientwise*, without needing to presume \(t=0\). The three-row contribution is nonnegative. Combining these independent inequalities with (1) proves \(P_{\min,b}\preceq P_D\).

All inequalities are attained simultaneously. Take \(q\) copies of each nonconstant column, and distribute the remaining \(r\) copies according to one of these balanced choices: for \(r=0\), none; for \(r=1\), any singleton; for \(r=2\), a pair of complementary columns; for \(r=3\), the three columns \(001,010,100\); for \(r=4\), the complement (within the six columns) of any complementary pair; for \(r=5\), all except any one. Every row then has \(h\) or \(H\) ones.

Equality at \(z=1\) is rigid: the strictly convex sequence \(2^m-1\) forces each row's two group counts to be balanced. It also forces the six pair-group counts to be balanced *at their smallest possible sum*, hence \(t=0\). The three-row summands must vanish, consistently with \(t=0\). Because nonconstant columns correspond bijectively to the six two-row monochromatic group labels, exactly the stated multiplicity and row-balance conditions result. They suffice for equality of polynomials. To count equality matrices, choose which \(r\) of the six patterns are at frequency \(q+1\), then permute the resulting multiset of columns. For \(r=0,1,2,3,4,5\), the counts of balanced pattern selections are \(1,6,3,14,3,6\), respectively: at sizes two and four they are complementary pairs and their complements; at size three only six of the \(\binom63=20\) sets have an entirely constant row and are excluded. This proves the full equality classification and labeled formula.

**3. Coefficientwise maximum and equality.** In (1), every mixed support \((R,C)\) contributes zero or one admissible type, according to whether its old induced complete bipartite subgraph is monochromatically oriented. Ignoring this restriction gives exactly \(((1+z)^3-1)((1+z)^b-1)\); all-one-direction matrices attain it. Conversely, equality of totals would require every nonempty mixed sub-biclique to be monochromatically oriented. Already choosing one column and two first-shore vertices forces all three bits of that column to agree; choosing one row and two columns forces the constant bits of every two columns to agree. Thus the only maximum matrices are the two constant matrices.

**4. Numerical and asymptotic consequences.** Substituting \(z=1\) into the two exact extremal polynomials gives the displayed total counts. The total one-shore contribution, independent of orientation, is \(3^b+26\). Consequently
\[
\begin{aligned}
R_{\max,b}&=7(2^b-1),\\
R_{\min,b}&=3(2^h+2^H-2)+(6+r)2^q-6.
\end{aligned}
\]
Since \(h,H=b/2+O(1)\) and \(q=b/6+O(1)\), the minimum is \(\Theta(2^{b/2})\) and the maximum is \(\Theta(2^b)\), proving the ratio assertion.

## Verification

The standalone Python 3 checker `CHECKER.py` independently enumerates all \(8^b\) orientations for every \(1\le b\le6\). It compares every coefficient with both closed polynomials, checks all equality cases against the exact balanced-signature criterion, and checks the predicted labeled extremizer counts. It also directly enumerates all ternary one-point adjacency assignments for every orientation through \(b=3\), testing the type-support characterization independently. Its recorded output is `CHECKER_OUTPUT.txt`, ending in `VERIFY_OK`. These finite checks support the all-order symbolic proof but do not replace it.

## Relationship to prior work

Kühn, Osthus, Townsend and Zhao (original arXiv posting 2014-04-24) establish global typical structure of oriented graphs forbidding transitive tournaments; their Theorem 1.2 concerns asymptotic multipartiteness of almost all large forbidden-tournament-free oriented graphs, not finite-base one-point spectra or extremal orientations of a fixed biclique. Conant's 2015 work provides a broad model-theoretic free-amalgamation setting but not this all-coefficient enumeration or mod-six equality classification. Lang and Stein's 2015 work on locally coloured complete bipartite graphs studies monochromatic path/cycle partitions; that extremal covering question does not imply the coefficientwise enumeration of *all* monochromatic sub-bicliques. Standard convex balancing is an elementary ingredient, not claimed as novel. Historical priority against unindexed biclique submatrix enumerations and equivalent matrix partition functions remains an explicit risk.

## Limitations

The extremal result is proved for exactly three individually named vertices in one shore, arbitrary positive size in the other shore, and the one-sorted generic oriented structure forbidding *transitive* triangles. It does not classify general \(K_{a,b}\) with \(a\ge4\), arbitrary oriented parameter graphs, or higher-arity types. A self-contained proof and finite verifier are supplied; independent mathematical audit and exhaustive historical-priority validation have not been performed.

## References

- D. Kühn, D. Osthus, T. Townsend, Y. Zhao, *On the structure of oriented graphs and digraphs with forbidden tournaments or cycles*, arXiv:1404.6178 (first posted 2014-04-24), https://arxiv.org/abs/1404.6178 .
- G. Conant, *An axiomatic approach to free amalgamation*, arXiv:1505.00762 (first posted 2015-05-04), https://arxiv.org/abs/1505.00762 .
- R. Lang, M. Stein, *Local colourings and monochromatic partitions in complete bipartite graphs*, arXiv:1501.05619 (first posted 2015-01-22), https://arxiv.org/abs/1501.05619 .
