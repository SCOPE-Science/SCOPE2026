# Three separated weight bands for perfect double Italian domination on complete prisms

## Finding
For every integer \(n\ge4\), let \(G_n=K_n\square K_2\), with two labeled cliques \(A=\{a_1,\dots,a_n\}\) and \(B=\{b_1,\dots,b_n\}\), joined by the perfect matching \(a_ib_i\). Write \(P_n(z)=\sum_f z^{\omega(f)}\), summing once over every perfect double Italian dominating function \(f:V(G_n)\to\{0,1,2,3\}\), and \(\omega(f)=\sum_v f(v)\).

The complete polynomial is
\[
\begin{aligned}
P_n(z)={}&\left(\binom n3^2+n^3\right)z^6+n^2(n-1)z^7+\binom n2 z^8\\
&+2n z^{2n+1}(1+z)^n+n(n+1)z^{2n+2}\\
&+2n z^{2n+3}+2z^{3n}+z^{4n}(1+z)^{2n}.
\end{aligned}
\]
In particular, \(\gamma^p_{dI}(G_n)=6\), and there are exactly \(\binom n3^2+n^3\) minimum-weight functions. Their structure is characterized in the proof. For every \(n\ge5\), the set of attainable weights is precisely the **three disjoint integer intervals**
\[
\{6,7,8\}\ \cup\ [2n+1,3n+1]_{\mathbb Z}\ \cup\ [4n,6n]_{\mathbb Z}.
\]
Thus no weights from \(9\) through \(2n\), or from \(3n+2\) through \(4n-1\), are possible. The endpoints \(n=2,3\) lie outside the theorem; direct checks give minimum weights \(4,5\) and minimum counts \(3,6\), respectively.

## Assumptions and scope
The graph is finite, simple, undirected and has the described exact Cartesian-product adjacency. The two cliques have named vertices; no quotient by automorphisms or exchange of the two layers is made in the polynomial.

The *perfect double Italian* definition here is the closed-neighborhood **interval** convention: a function \(f:V\to\{0,1,2,3\}\) is admissible if and only if every vertex \(v\) with \(f(v)\in\{0,1\}\) satisfies
\[
3\le\sum_{u\in N[v]}f(u)\le4.
\]
Vertices labeled \(2\) or \(3\) have no condition. This is distinct from the later, stricter exact-neighborhood-sum convention called perfect Roman \(\{3\}\)-domination.

Write \(x_i=f(a_i)\), \(y_i=f(b_i)\) and the layer weights \(A_*=\sum_i x_i\), \(B_*=\sum_i y_i\). Then the closed-neighborhood sums at \(a_i\), \(b_i\) are respectively \(A_*+y_i\) and \(B_*+x_i\). Hence feasibility is equivalent to the **two local conditions**
\[
x_i\le1\ \Longrightarrow\ 3\le A_*+y_i\le4,
\qquad
y_i\le1\ \Longrightarrow\ 3\le B_*+x_i\le4.
\tag{1}
\]
There is no positivity or optimality assumption in (1).

## Proof
**1. Light/heavy dichotomy.** Call a layer *heavy* if all its labels belong to \(\{2,3\}\), and *light* otherwise. If layer \(A\) is light, an index with \(x_i\le1\) exists; (1) then implies \(A_*\le4\). Similarly every light layer has total at most \(4\), whereas a heavy layer has total at least \(2n\). Partition all functions uniquely into light/light, heavy/light, light/heavy and heavy/heavy.

**2. Both layers light.** For \(n\ge4\), each light layer has total at least \(3\). Indeed, if \(A_*=0\), each of the \(n\) positions forces \(y_i\ge3\), contrary to \(B_*\le4\). If \(A_*=1\), every position forces \(y_i\ge2\), again contrary to \(B_*\le4\). If \(A_*=2\) and all \(x_i\le1\), every \(y_i\ge1\), so \(B_*\ge n\); equality is possible only for \(n=4\), \(B_*=4\) and all \(y_i=1\), but then the second condition in (1) requires each \(x_i=0\), a contradiction. If instead a unique \(x_j=2\), then \(y_i\ge1\) for \(i\ne j\). Since \(B_*\ge n-1\ge3\), the second condition in (1) would fail at \(j\) unless \(y_j\ge2\). Consequently \(B_*\ge n+1>4\), another contradiction. Interchange layers to also obtain \(B_*\ge3\). Thus \((A_*,B_*)\in\{3,4\}^2\).

For \((A_*,B_*)=(3,3)\), every column is either low/low, with its two digits in \(\{0,1\}\), or high/high, with its two digits in \(\{2,3\}\); mixed columns violate (1). With no high column, choose three positions labeled \(1\) independently in each layer: \(\binom n3^2\) possibilities. If a high column occurs it is unique. At its position the ordered pair may be \((2,2),(2,3),(3,2),(3,3)\); the residual sums on the remaining columns are independently \(1\) or \(0\). This gives
\[
n\bigl((n-1)^2+2(n-1)+1\bigr)=n^3
\]
functions. Thus the weight-six coefficient is \(\binom n3^2+n^3\).

For \((A_*,B_*)=(4,3)\), every positive entry in layer \(B\) must be at least \(2\) and matched to a high entry in \(A\); therefore precisely one \(y_j=3\), with \(x_j=2\) or \(3\). All other \(y_i=0\), and the remaining \(x_i\) are \(0\) or \(1\) with sum \(2\) or \(1\). The number is
\[
n\left(\binom{n-1}{2}+n-1\right)=\frac{n^2(n-1)}{2}.
\]
Interchanging layers doubles this number at weight seven. Finally, for \((A_*,B_*)=(4,4)\), every column is either \((0,0)\) or high/high; the only possibility is exactly two \((2,2)\) columns. There are \(\binom n2\) such weight-eight functions. This completes the light/light contribution.

**3. One heavy layer.** Suppose \(A\) is heavy and \(B\) is light, so \(x_i\in\{2,3\}\) and \(B_*\le4\). For any \(y_i\le1\), (1) gives \(3\le B_*+x_i\le4\), so necessarily \(B_*\le2\). Since at least one such index exists, only \(B_*\in\{0,1,2\}\) is possible.

If \(B_*=0\), then every \(y_i=0\) and all \(x_i=3\); this contributes \(z^{3n}\). If \(B_*=1\), exactly one \(y_j=1\), and the \(n\) entries of the heavy layer can independently be \(2\) or \(3\). The contribution is \(n z^{2n+1}(1+z)^n\).

If \(B_*=2\), either two \(y\)-entries equal \(1\) (forcing every \(x_i=2\)), giving \(\binom n2 z^{2n+2}\); or one \(y_j=2\), which leaves \(x_i=2\) at every \(i\ne j\) while \(x_j\in\{2,3\}\), giving \(n z^{2n+2}(1+z)\). Doubling these three expressions accounts for the orientation in which \(B\) is heavy and \(A\) is light. Simplification yields the four mixed terms in the displayed formula.

**4. Both layers heavy.** The closed-neighborhood restriction is vacuous at every vertex. Every one of the \(2n\) labels is independently \(2\) or \(3\), giving \(z^{4n}(1+z)^{2n}\).

The four cases are disjoint and exhaustive, so summing them proves the polynomial. Its low-degree term proves the stated minimum and optimum count. For \(n\ge5\), the light/light contribution has support exactly \(\{6,7,8\}\), the mixed contribution exactly \([2n+1,3n+1]_{\mathbb Z}\) (the binomial factor alone supplies each integer), and the heavy/heavy contribution exactly \([4n,6n]_{\mathbb Z}\). These intervals are disjoint for \(n\ge5\); their complementary gaps are therefore exact.

## Verification
The accompanying standalone file `verify_prism.cpp` constructs the graph explicitly and checks the defining closed-neighborhood inequalities for **every one** of the \(4^{2n}\) labelings for each \(2\le n\le6\). It matches the complete polynomial for \(4\le n\le6\), not merely the first coefficient. It also verifies the excluded small endpoints directly.

The independently implemented `verify_prism.py` fixes each pair of layer totals, enumerates allowed ordered digit pairs in all \(16\) possibilities and convolves these states over the \(n\) matched columns, never using the four-case proof to count candidates. It agrees with the formula for every \(4\le n\le9\). The certificate programs are finite corroborations; the proof above establishes the formulas for arbitrary integers \(n\ge4\).

For orientation, the first pairs \((n,\gamma^p_{dI}(G_n),\text{minimum count},\text{total valid functions})\) are \((4,6,80,548)\), \((5,6,225,1721)\), \((6,6,616,5731)\), \((7,6,1568,20131)\).

## Relationship to prior work
Hao, Jalilolghadr and Mojdeh introduced the interval-definition perfect double Italian invariant in 2023 and established its values for paths, cycles and complete multipartite graphs, plus general extremal classifications. The inspected full-text portions covering its definition and standard families contain no matching-joined-two-clique or complete-prism polynomial.

“Roman \(\{3\}\)-domination of complete prisms” establishes that the **nonperfect** Roman \(\{3\}\) minimum is \(5\) on \(K_4\square K_2\) and \(6\) for larger orders, with \(\binom{n+2}{3}^2\) minimum functions for \(n\ge6\). Its defining lower-bound inequalities omit the upper bound of four used here, so its minimum-function classification does not imply this much smaller perfect-function census or the separated full weight spectrum. “Perfect double Italian domination of square rook graphs” studies \(K_n\square K_n\), with both Cartesian factors equal and \(n\ge3\), rather than the unequal two-clique prism \(K_n\square K_2\) considered here.

Almulhim's 2024 “Perfect Roman \(\{3\}\)-Domination” concerns a stricter exact-sum condition for labels \(0\) and \(1\), not the interval convention. That paper's inspected family results address paths, cycles and complete multipartite graphs, not this matched-clique product. The present result is neither a simple specialization nor a consequence of those results: the upper endpoint four in (1) is essential to the first weight gap. Priority checks are necessarily provisional for unindexed or differently named literature.

## Limitations
The theorem is for \(K_n\square K_2\) with \(n\ge4\) and the 2023 interval convention, not all rectangular rook graphs, complete multipartite graphs, other Roman-type functions, or the later exact-sum perfect Roman \(\{3\}\) convention. The special case \(n=4\) has only one nonempty weight gap, while the stated three disjoint bands require \(n\ge5\). Publication-priority completeness and independent mathematical audit are not claimed.

## References
1. G. Hao, P. Jalilolghadr, D. A. Mojdeh, “Perfect double Italian domination of a graph,” *AKCE International Journal of Graphs and Combinatorics* 20(3) (2023), 247–257, DOI: 10.1080/09728600.2023.2218457, first published online 2023-06-21. Open article PDF: https://www.tandfonline.com/doi/pdf/10.1080/09728600.2023.2218457.
2. “Roman \(\{3\}\)-domination of complete prisms” (2026), published research record: https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-roman-3-domination-of-complete-prisms--879e297963d2/RESULT.md.
3. “Perfect double Italian domination of square rook graphs” (2026), published research record: https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-perfect-double-italian-domination-of-square-rook-graphs--4f59f40e97e0/RESULT.md.
4. A. Almulhim, “Perfect Roman \(\{3\}\)-Domination in Graphs: Complexity and Bound of Perfect Roman \(\{3\}\)-Domination Number of Trees,” *Journal of Mathematics* (2024), article 1900923, DOI: 10.1155/jom/1900923, published online 2024-12-24.
