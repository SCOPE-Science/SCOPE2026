# Sharp two-distance composition law for exchangeable uniform couplings

## Finding

Let \(0<d\le 1/2\), and consider every exchangeable pair \((U,V)\) with both marginals uniform on \([0,1]\) and with \(\Pr(|U-V|\in\{d,2d\})=1\). The attainable set of long-displacement probabilities
\[
 p_2=\Pr(|U-V|=2d)
\]
is the *entire closed interval* \([L(d),H(d)]\) specified below. Define
\[
 q=\lfloor1/d\rfloor,\qquad r=1-qd\in[0,d).
\]
The sharp lower endpoint is
\[
 L(d)=\begin{cases}r,&q\text{ even},\\d-r,&q\text{ odd},\end{cases}
\]
and the sharp upper endpoint has a distinct four-residue dependence:
\[
 H(d)=\begin{cases}
 1-2r,&q\equiv0\pmod4,\\
 1-2(d-r),&q\equiv3\pmod4,\\
 1-2d,&q\equiv1,2\pmod4.
 \end{cases}
\]
Both endpoints are attained by explicitly given symmetric, singular copulas. Every intermediate value is attained by mixing the endpoint copulas.

There is also a sharp determinism obstruction: such a coupling can be represented as \((U,T(U))\) with \(T\) a measure-preserving measurable involution *if and only if* \(d=1/(2j)\) for an integer \(j\ge1\). For other values of \(d\), the construction of an exchangeable coupling supported on the two distances necessarily uses a non-Dirac conditional kernel. If imperfect support is allowed, the largest proportion of the pairs in the two-distance set achieved by a measure-preserving involution is \(1-L(d)\). This deterministic envelope agrees with the known single-distance envelope; the new classification is the attainable **long-displacement proportion under exact two-distance support**.

## Assumptions and scope

Exchangeability means \((U,V)\overset{d}= (V,U)\), without any density assumption. A copula is identified with its measure on \([0,1]^2\). The support constraint is exact, up to a probability-zero exception. The main classification is only for \(0<d\le1/2\); for \(d>1/2\) no coupling can obey the two-distance support constraint almost surely, since both possible distances exceed the available distance for some marginal values. The word "involution" means \(T(T(u))=u\) for Lebesgue-almost every \(u\), and \(T\) preserves Lebesgue measure.

## Proof

**1. Reduction to a pair of finite path-square problems.** Let \(t\) be the residue of a point in \([0,1]\) modulo \(d\), chosen in \([0,d)\). Outside a null set, each residue fiber is
\[
 \{t,t+d,\ldots,t+(n(t)-1)d\},\qquad
 n(t)=\begin{cases}q+1,&0<t<r,\\q,&r<t<d.\end{cases}
\]
Lebesgue measure disintegrates as \(\int_0^d\sum_{j=0}^{n(t)-1}\delta_{t+jd}\,dt\). Since either permitted jump changes position by \(d\) or \(2d\), the two coordinates have the same residue. Equal uniform marginals and exchangeability therefore give, for almost every residue, a symmetric nonnegative \(n(t)\)-by-\(n(t)\) matrix \(A(t)\) with unit row sums, zero diagonal, and entries allowed only when the index difference is \(1\) or \(2\). Write \(w_{ij}=A_{ij}=A_{ji}\) on these unordered edges. Then
\[
 \sum_{j:\,|i-j|\in\{1,2\}}w_{ij}=1,\qquad
 p_2=\int_0^d 2\sum_{i<j:\,j-i=2}w_{ij}(t)\,dt.
\]
The unit row sums follow from the normalized counting measure on each fiber, not from assuming absolute continuity of the copula.

**2. Finite sharp lower bound.** For an integer \(n\ge2\), let \(P_2\) be twice the sum of the weights on edges of length two in the graph on \(\{0,\ldots,n-1\}\). If \(n\) is odd, the numbers of even- and odd-indexed vertices differ by one. Length-one edges contribute equally to the two parity degree sums, while length-two edges each contribute an absolute difference at most twice their weight. Thus \(P_2\ge1\). If \(n\) is even, nonnegativity gives \(P_2\ge0\). Both bounds are attained: pair adjacent vertices with weight one if \(n\) is even, and if \(n\) is odd first put weight \(1/2\) on each edge of the triangle with vertices \(0,1,2\), then pair the remaining adjacent vertices. Hence
\[
 m_n:=\min P_2=\begin{cases}0,&n\text{ even},\\1,&n\text{ odd}.\end{cases}
\]

**3. Finite sharp upper bound.** Since each row sums to one, \(P_1+P_2=n\), where \(P_1\) is twice the total weight on edges of length one. When \(n\equiv0\pmod4\), the upper bound \(P_2\le n\) is achieved by pairing the vertices in each consecutive four-block using only the edges \((0,2)\) and \((1,3)\), translated to that block. For the other three residue classes, consider vertex counts by index modulo four. When \(n\equiv1,2\pmod4\), class zero contains one more vertex than class two; when \(n\equiv3\pmod4\), class one contains one more vertex than class three. Length-two edges join opposite classes in the relevant pair, contributing zero to the difference of their degree sums. The remaining length-one edges have total weight at least one, since a single such edge contributes absolute difference at most its weight. Thus \(P_1\ge2\) and \(P_2\le n-2\).

This upper bound is attained in all three cases. For \(n\equiv2\pmod4\), pair the initial two vertices at distance one; for \(n\equiv3\pmod4\), put weight \(1/2\) on each of the initial triangle's edges; for \(n\equiv1\pmod4\), where necessarily \(n\ge5\), put weight \(1/2\) on the five-cycle with consecutive edges \((0,1),(1,3),(3,4),(4,2),(2,0)\). In each case pair the remaining vertices in consecutive four-blocks using length-two edges. In all cases the total weight of the length-one edges is exactly one. Consequently
\[
 M_n:=\max P_2=\begin{cases}n,&n\equiv0\pmod4,\\n-2,&n\not\equiv0\pmod4.\end{cases}
\]
These explicit witnesses establish nonemptiness of the finite feasible polytopes at every order at least two.

**4. Integration and full attainability.** Apply the finite bounds fiberwise and use the lengths of the two residue regions:
\[
 (d-r)m_q+rm_{q+1}\le p_2\le(d-r)M_q+rM_{q+1}.
\]
The first expression simplifies to \(L(d)\); the second simplifies to \(H(d)\), using \(qd+r=1\). Choose the indicated finite witnesses on each of the two residue regions and push them forward by \((t,i,j)\mapsto(t+id,t+jd)\). This constructs symmetric copula measures attaining both endpoints with exactly uniform marginals. Convex mixing yields all intermediate values.

**5. Deterministic exchangeable obstruction.** If \(V=T(U)\) almost surely and the coupling is exchangeable with uniform marginals, symmetry of its graph-supported law forces \(T\circ T=\mathrm{id}\) almost everywhere. Thus the successful transitions on a residue fiber form disjoint transpositions; an odd fiber has at least one unmatched vertex. The mass of odd fibers is \((d-r)\mathbf1_{q\text{ odd}}+r\mathbf1_{q+1\text{ odd}}=L(d)\). If the support constraint is required almost surely, this quantity must vanish. The equality \(L(d)=0\) in the stated domain occurs exactly when \(r=0\) and \(q\) is even, that is, \(d=1/(2j)\). Pairing consecutive vertices then provides an involution satisfying the constraint. Without the support requirement, the same fiberwise unmatched-vertex argument bounds successful mass by \(1-L(d)\), achieved by adjacent transpositions while fixing any leftover vertex. This proves the final assertions.

## Verification

The standalone Python 3 standard-library script `verify.py` constructs exact-rational symmetric edge weights in the finite graphs, checks every row sum and both asserted extremal objective values for graph orders \(2\) through \(160\), and checks the integrated formulas for reduced rational distances with denominator at most \(120\). It also checks five explicit benchmark cases. Its output is `PASS: 2516 exact rational witness/range tests`. These checks illustrate and test finite constructions; the argument in the preceding section, not the computation, proves every real parameter value and every graph order.

## Relationship to prior work

Trutschnig and Úbeda-Flores (2026, arXiv:2610.33646v1, first publicly available 2026-10-24) study geometric support and mass restrictions for special copula classes, including exchangeable completely dependent copulas generated by measure-preserving involutions, and investigate off-diagonal chains. Their results do not evaluate the attainable mass of one jump length when only two specific displacement lengths are permitted. General fractional-perfect-matching and half-integrality results (e.g., Scheinerman and Ullman) provide the finite framework and the triangle/five-cycle mechanisms, but do not state the integrated length-dependent \(\pmod4\) interval. Côté and Wang (arXiv:2611.25237v1, first publicly available 2026-11-18) study upper copula capacities and connections with multipartite fractional matching; their inspected text does not state these particular symmetric two-distance composition extrema. Their framework is independent of the exact two-distance probability interval. The previously published exact-one-distance capacity formula already yields the deterministic envelope \(1-L(d)\); that consequence is acknowledged as covered, not offered as the new contribution.

## Limitations

The result covers equal uniform marginals, exchangeable bivariate laws and precisely the two commensurate allowed distances \(d\) and \(2d\). It does not classify optimizers uniquely, unequal marginals, arbitrary pairs of distances, or absolutely continuous copulas (the latter cannot charge the finite union of lines). The exact infinite-parametric theorem has an analytical proof but no independent external validation. A broader unlocated weighted-fractional-matching specialization remains a residual priority risk; no claim of historical uniqueness is made.

## References

1. W. Trutschnig and M. Úbeda-Flores, *The closed convex hull of all associative copulas is a Z-set in the family of all bivariate Schur concave copulas, and related results*, arXiv:2610.33646v1 (2026-10-24), https://arxiv.org/abs/2610.33646 .
2. E. R. Scheinerman and D. H. Ullman, *Fractional Graph Theory*, Dover reprint (2011), Chapter 2.
3. B. Côté and R. Wang, *The upper copula capacity*, arXiv:2611.25237v1 (2026-11-18), https://arxiv.org/abs/2611.25237 . Later supporting framework only.
4. M. Longla, *Continuous Exchangeable Markov Chains, Idempotent and 1-Dependent Copulas*, Mathematics 13(12), 2034 (2025), https://doi.org/10.3390/math13122034 .
