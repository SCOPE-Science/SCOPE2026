# The matching-base two-point spectrum of the homogeneous three-valued metric space

## Finding

Let \(\mathbb U_3\) be the countable Fraïssé limit of all finite metric spaces whose positive distances belong to \(\{1,2,3\}\). For every integer \(m\ge1\), fix the individually named \(2m\)-point metric base
\[
A_m=\{a_1,b_1,\ldots,a_m,b_m\},\qquad
d(a_i,b_i)=1,\quad d(u,v)=3\text{ for points in different pairs}.
\]
All these distances satisfy the triangle inequality. The class of all finite \(\{1,2,3\}\)-metrics has strong amalgamation: glue two metrics over a common subspace by shortest-path distance through the overlap, cap distances at three, and use distance three across empty overlaps. Hence its stated Fraïssé limit and its finite-extension property exist. Let \(N_m\) be the number of complete nonalgebraic one-point types over \(A_m\). Let \(T_{m,s}\) be the number of complete types of *ordered* pairs \((x,y)\), with \(x\ne y\) and both coordinates outside \(A_m\), for which \(d(x,y)=s\), where \(s\in\{1,2,3\}\). Then
\[
\boxed{N_m=4^m+3m4^{m-1}}
\]
and the complete distance-resolved two-point spectrum is
\[
\boxed{\begin{aligned}
T_{m,1}&=16^m+19m16^{m-1}+25m(m-1)16^{m-2},\\
T_{m,2}&=16^m+33m16^{m-1}+144m(m-1)16^{m-2},\\
T_{m,3}&=16^m+26m16^{m-1}+144m(m-1)16^{m-2}.
\end{aligned}}
\]
Terms multiplied by \(m(m-1)\) are interpreted as zero for \(m=1\), without evaluating a negative power. In particular, for every \(m\ge1\) the strict order is \(T_{m,1}<T_{m,3}<T_{m,2}\).

Sampling uniformly from these complete ordered pair types (not sampling points of the infinite metric space) gives the limiting mutual-distance law
\[
\boxed{\lim_{m\to\infty}\bigl(\Pr(d(x,y)=1),\Pr(d(x,y)=2),\Pr(d(x,y)=3)\bigr)
=\left(\frac{25}{313},\frac{144}{313},\frac{144}{313}\right).}
\]
With probability tending to one, both new coordinates have a distance-one witness among the old vertices, and their sets of distance-one witnesses occur in two *distinct* old matched pairs. Equivalently, the exact number of these separated-witness pair types is \(313m(m-1)16^{m-2}\). Finally, the mean number of allowed mutual distances between two uniformly chosen nonalgebraic unary types over \(A_m\) tends to \(313/144\).

## Assumptions and scope

The finite language names the symmetric distance predicates \(d=1\), \(d=2\), and \(d=3\). All parameters are individually named; no identification of distinct old matched pairs or quotient by their permutations is made. The new coordinates are ordered, distinct from one another, and distinct from every old point. Complete types in the homogeneous structure are equivalent to labelled finite metric extension diagrams by ultrahomogeneity and the one-point extension property. The probability assertions refer to uniform counting measure on a *finite set of logical types*, not to a probability measure on the infinite space.

## Proof

For every new point \(z\) and old points \(u,v\), a prescribed vector \(f(u)=d(z,u)\) is admissible if and only if
\[
|f(u)-f(v)|\le d(u,v)\le f(u)+f(v).
\]
For an old matched pair at distance one, the permissible assignments \((f(a_i),f(b_i))\) are the seven pairs with coordinate difference at most one. Exactly four use only values \(2,3\), and exactly three contain at least one value \(1\). For any vertices from *different* old pairs at distance three, the only prohibited pair of distances to \(z\) is \((1,1)\). Consequently at most one matched pair contains a value one. Independent choices of the four ordinary states at every other pair give
\(N_m=4^m+3m4^{m-1}\).

For the ordered new pair \((x,y)\), fix the mutual distance \(s\). At each old vertex define its state \((u,v)=(d(x,a),d(y,a))\). The allowed state set is
\[
B_s=\{(u,v)\in\{1,2,3\}^2:|u-v|\le s\le u+v\}.
\]
A matched old pair contributes an ordered pair \(((u,v),(u',v'))\in B_s^2\), constrained by \(|u-u'|\le1\) and \(|v-v'|\le1\). Classify this local assignment by its **support**, the subset of \(\{x,y\}\) whose coordinate has distance one to at least one endpoint of the old matched pair. The four support weights \((w_\varnothing,w_x,w_y,w_{xy})\) are, by finite direct inspection,

| Mutual distance \(s\) | \(w_\varnothing\) | \(w_x\) | \(w_y\) | \(w_{xy}\) |
|---|---:|---:|---:|---:|
| 1 | 16 | 5 | 5 | 9 |
| 2 | 16 | 12 | 12 | 9 |
| 3 | 16 | 12 | 12 | 2 |

For reproducibility, each entry equals the explicit finite sum
\[
w_J(s)=\sum_{p,q\in B_s}\mathbf1_{\{|p_1-q_1|\le1,\,|p_2-q_2|\le1\}}\,\mathbf1_{\{\operatorname{supp}(p,q)=J\}},
\]
where the support is formed by including \(x\) when \(1\in\{p_1,q_1\}\) and \(y\) when \(1\in\{p_2,q_2\}\). There are at most \(9^2=81\) summands to check for each row. In particular the support-free block has four choices at each endpoint, hence weight sixteen for all three distances.

The cross-block old distances all equal three. Their metric triangle inequalities impose *exactly* the restriction that each of \(x\) and \(y\) may belong to the support of at most one block: two ones in the same new coordinate at old points in different blocks would force \(3\le1+1\), which fails. There are therefore only three mutually exclusive possibilities: no supported block, one supported block carrying either one or both new coordinates, or two distinct blocks carrying the disjoint singleton supports \(\{x\}\) and \(\{y\}\). Counting the possibilities gives the identity
\[
T_{m,s}=16^m+m(w_x+w_y+w_{xy})16^{m-1}
+m(m-1)w_xw_y16^{m-2}.
\]
Substituting the support table proves the exact formulas. No further restrictions exist: every triangle among old points is already metric, all new-old-old triangles were enforced, and all new-new-old triangles are enforced by membership in \(B_s\). Every admissible resulting finite metric extension is realized in \(\mathbb U_3\).

Subtracting the formulas yields
\[
T_{m,2}-T_{m,3}=7m16^{m-1},\qquad
T_{m,3}-T_{m,1}=7m16^{m-1}+119m(m-1)16^{m-2},
\]
which are strictly positive. Summing the three formulas gives
\[
T_m=3\cdot16^m+78m16^{m-1}+313m(m-1)16^{m-2}.
\]
The separated-witness cases are precisely the last terms, with coefficient \(25+144+144=313\), hence their proportion tends to one. Dividing each channel by \(T_m\) and comparing leading quadratic terms proves the distance law. For uniformly chosen unary types, the expected number of feasible mutual distances is \(T_m/N_m^2\); its leading-term ratio is \(313/144\). These limits are consequences of exact polynomials and not extrapolations from finite tests.

## Verification

The standalone `artifacts/verify.py` exhaustively derives the local support-weight table from all allowable pairs of old-vertex states, without relying on the stated weight entries. In an independent calculation it enumerates every admissible unary distance vector for old matching bases with \(m=0,1,2,3\), checks every old-new and new-new triangle for each possible mutual distance, and compares its direct counts with the closed formulas. The observed \((T_{m,1},T_{m,2},T_{m,3})\) are \((1,1,1)\) at \(m=0\) (empty-base auxiliary check), \((35,49,42)\) at \(m=1\), \((914,1600,1376)\) at \(m=2\), and \((21088,43264,37888)\) at \(m=3\). It also checks strict channel ordering through \(m=16\) and the limiting rational identities. The recorded output ends in `ALL_CHECKS_PASS`. The proof for arbitrary \(m\) is the preceding block-support counting argument, not the finite tests.

## Relationship to prior work

Mubayi and Terry's *Discrete metric spaces: structure, enumeration, and 0–1 laws* (first arXiv release 2015-02-04, arXiv:1502.01212) studies global asymptotic counts of labelled finite integer metrics. Its Section 7 explicitly uses a matching of short-distance-one edges, with all other distances at least two, as a construction for a lower bound when the distance alphabet has odd size. That construction motivates the present matching-base question, but their argument counts the ambient labelled metrics, not the three numbers of ordered, two-coordinate extensions over one fixed metric matching base. They do not assert this conditional distance law.

The published note *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space* identifies nonalgebraic **one-point** type counts for certain three-valued metric parameter spaces with a graph homomorphism polynomial. Its one-point invariant does not determine which two unary types can coexist at a prescribed mutual distance, and its graph-metric slice has old distances one or two, whereas the present base has long cross-pair distance three. A separate earlier equilateral-base two-point spectrum in the same metric structure yields limiting distance law \((1/9,4/9,4/9)\); its all-equal old-distance hypothesis does not hold for the matching base. The different limiting fractions display the contribution of the old short-pair geometry.

## Limitations

The theorem applies to the specified matched-pair bases and ordered pairs of fresh points, not arbitrary finite metric parameter bases, unrestricted tuple arities, or samples drawn from the infinite space. It does not make assertions about global random metrics uniformly sampled on growing sets. Although targeted prior-results and literature checks found no implication or tabulated equivalent, earlier unpublished or differently named conditional metric-extension enumerations remain a historical-priority risk. Independent mathematical audit has not been performed.

## References

1. D. Mubayi and C. Terry, *Discrete metric spaces: structure, enumeration, and 0–1 laws*, arXiv:1502.01212 (initial version 2015-02-04), Section 1 and Section 7. https://arxiv.org/abs/1502.01212
2. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, published research note, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989
3. D. Amato, G. Cherlin, and H. D. Macpherson, *Metrically homogeneous graphs of diameter 3*, Journal of Mathematical Logic 21 (2021), article 2050020. https://doi.org/10.1142/S0219061320500208
