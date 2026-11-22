# Corank-two Motzkin multiplication: seven exact rank–path–loop strata

## Finding
For every integer \(n\ge 3\), let \(\mathcal M_n\) be the Motzkin diagram monoid on two rows of \(n\) vertices, and let \(\mathcal D_{n-2}\) be its complete set of diagrams with exactly \(n-2\) propagating strings. When two diagrams \(\alpha,\beta\in\mathcal D_{n-2}\) are stacked to multiply, let \(R(\alpha,\beta)=\operatorname{rank}(\alpha\beta)\), let \(P(\alpha,\beta)\) be the number of floating path components in their middle row (including isolated middle vertices), and let \(L(\alpha,\beta)\) be the number of floating loop components.

Put \(W_n=(n-1)(n+2)/2\). There are exactly \(W_n^2\) diagrams in \(\mathcal D_{n-2}\). The complete joint counting polynomial
\[
F_n(u,v,w)=\sum_{\alpha,\beta\in\mathcal D_{n-2}}u^{R(\alpha,\beta)}v^{P(\alpha,\beta)}w^{L(\alpha,\beta)}
\]
is exactly
\[
\boxed{F_n(u,v,w)=W_n^2\left[\frac{n(n+3)(n-2)(n-3)}4u^{n-4}+(n-1)(n-2)(nv+4)u^{n-3}+\left(\binom n2v^2+2(n-1)v+(n-1)w+2(n-2)\right)u^{n-2}\right].}
\]
When \(n=3\), the first term, whose coefficient is zero, is **omitted**; no negative power is intended. All other coefficients are nonnegative integers. For \(n\ge4\) the polynomial has precisely seven nonzero monomials; for \(n=3\), it has six.

In particular, if \(\alpha,\beta\) are independent and uniform on \(\mathcal D_{n-2}\), the probability of forming a floating loop is exactly
\[
\Pr[L=1]=\frac{n-1}{W_n^2}=\frac4{(n-1)(n+2)^2}.
\]
The two inner hooks can share exactly one vertex and *rescue* a propagating connection: these ordered inner decorations contribute exactly \(2(n-2)\) to the rank-\(n-2\), no-floating-component class, despite having distinct omitted-vertex pairs. This accounts for the term \(2(n-2)u^{n-2}\) in the inner polynomial.

## Assumptions and scope
A Motzkin diagram is a planar partial matching on a top row and a bottom row of \(n\) linearly ordered vertices. Every connected block has one or two vertices, and edges do not cross. A transversal edge joining top to bottom is a *propagating string*. Multiplication stacks the first diagram above the second, identifies their shared row, removes middle-only components, and retains all boundary connections. The graph *before* removal determines \(P\) and \(L\); an isolated middle vertex counts as a path of length zero, never as a loop. No ground field, probability limit, idempotency, or weighting assumptions are required for the counting identity. The two variables \(v,w\) distinguish respectively floating paths and floating loops even though the untwisted monoid product deletes both.

## Proof
**One-sided parametrization.** In a rank-\(n-2\) diagram exactly two vertices of each boundary row are not incident to propagating strings. Choose their two-element set \(A\). They are either two singletons (possible for every \(A\)) or form a nonpropagating hook (possible precisely when the two elements of \(A\) are adjacent). All \(n-2\) remaining top vertices join the \(n-2\) remaining bottom vertices in increasing order: this is forced by planarity. Hence the one-sided decorations have number
\[
W_n=\binom n2+(n-1)=\frac{(n-1)(n+2)}2.
\]
The top and bottom one-sided decorations are independent, so the rank class has \(W_n^2\) elements. For a product \(\alpha\beta\), the *outer* top decoration of \(\alpha\) and bottom decoration of \(\beta\) vary freely and do not affect the three measured statistics; each choice of two *inner* decorations therefore has exactly \(W_n^2\) ordered lifts \((\alpha,\beta)\).

**Inner sets are disjoint.** Let \(A\) be the omitted bottom vertices of \(\alpha\), and \(B\) the omitted top vertices of \(\beta\). If \(A\cap B=\varnothing\), all four omitted middle vertices are distinct. Each of the \(n-4\) other middle vertices joins a surviving propagating string, while each omitted vertex has a connection to a boundary in at most one direction. There are no floating components, and \(R=n-4\). The contributions from no hooks, exactly one hook, and two disjoint hooks are respectively
\[
\binom n2\binom{n-2}2,\qquad 2(n-1)\binom{n-2}2,\qquad (n-2)(n-3).
\]
Their sum is \(n(n+3)(n-2)(n-3)/4\). The final expression vanishes when \(n=3\), as it must.

**Inner sets meet at one vertex.** If \(|A\cap B|=1\) and neither side is a hook, the common omitted vertex is an isolated floating path, giving \((R,P,L)=(n-3,1,0)\). Such ordered pairs number \(n(n-1)(n-2)\). If exactly one inner side is a hook, it absorbs the common vertex into a path attached to a surviving boundary at its other end. There is no floating component, and \((R,P,L)=(n-3,0,0)\); the number of decorations is \(4(n-1)(n-2)\). If both sides are hooks, they must be adjacent edges of the path on \([n]\) sharing their central vertex. They form one alternating connection from a surviving upper boundary to a surviving lower boundary, restoring one propagating string. Thus \((R,P,L)=(n-2,0,0)\); there are \(2(n-2)\) ordered adjacent-edge pairs.

**Inner sets coincide.** When \(A=B\), the two omitted middle vertices are either both isolated (no hooks), form one floating path (exactly one hook), or form one floating loop of length two (two hooks). The respective \((R,P,L)\) are \((n-2,2,0)\), \((n-2,1,0)\), \((n-2,0,1)\), with counts \(\binom n2\), \(2(n-1)\), and \(n-1\).

Every ordered pair of inner two-sets belongs to one and only one of these three intersection cases. Their seven disjoint subclasses exhaust all two-factor products. Multiplication by the free outer factor \(W_n^2\) gives the displayed polynomial. Finally, setting \(u=v=w=1\) gives \(F_n(1,1,1)=W_n^4=|\mathcal D_{n-2}|^2\), confirming the total count. A loop occurs only when both inner decorations are the same adjacent hook, so its probability is \((n-1)/W_n^2\).

## Verification
The accompanying `motzkin_product_checker.py` independently constructs each entire rank-\(n-2\) class as explicit planar matchings, glues every ordered pair as a three-row graph, computes connected components, and counts the three invariants. The captured output, `checker_output.txt`, agrees with every predicted coefficient for \(n=3,4,5,6\): respectively 625, 6,561, 38,416, and 160,000 products. The script uses only Python's standard library, and can be run with `python motzkin_product_checker.py`. This finite exhaustive test is a consistency check; the proof above establishes the formula for all integers \(n\ge3\).

## Relationship to prior work
Dolinka, East, and Gray (2015, arXiv:1512.02279), particularly Proposition 2.8 and Sections 5.2–5.3, supply the rank-class parametrization and the two distinct middle-component weights in the twisted Motzkin algebra. Their results count individual diagram classes and define weighted diagram multiplication; they do not state this joint two-factor rank–path–loop polynomial. Benkart and Halverson (2011, arXiv:1106.5277) develop Motzkin diagrams, weighted multiplication, and cell modules; their representation-theoretic formulas do not provide these seven aggregate multiplication coefficients. Hatch, Ly, and Posner (2013, arXiv:1301.4518) give a presentation and normal forms, not a joint two-factor census. The published planar-idempotent enumeration (arXiv:1507.04838) concerns idempotent diagrams rather than unrestricted ordered rank-class products. A separate Brauer-monoid product-rank result does not subsume these planar Motzkin counts: its factors have no singleton middle paths, and its hook configurations and rank transitions differ. The new assertion here is specifically the closed seven-stratum *aggregate convolution*, not the known definitions, the one-sided counts, or the diagram multiplication rule.

## Limitations
The formula applies only to products of two factors in the rank-\(n-2\) class. It does not determine each prescribed output-diagram fiber, products at other ranks, or the entire Motzkin algebra's structure constants. The distinction between floating paths and loops depends on retaining middle-component data before the untwisted product erases it. The originality assessment was limited to accessible literature and indexed mathematical records; equivalent unindexed or differently formulated prior results remain possible. Numerical checks for \(n\le6\) do not replace the general proof, and there has been no external mathematical audit.

## References
1. I. Dolinka, J. East, R. D. Gray, *Motzkin monoids and partial Brauer monoids*, first posted 2015-12-07, arXiv:1512.02279, https://arxiv.org/abs/1512.02279. Primary MSC: 20M20. Proposition 2.8; Sections 5.2–5.3.
2. G. Benkart, T. Halverson, *Motzkin Algebras*, first posted 2011-06-26, arXiv:1106.5277, https://arxiv.org/abs/1106.5277. Sections 2 and 4.
3. K. Hatch, M. Ly, E. Posner, *Presentation of the Motzkin Monoid*, first posted 2013-01-18, arXiv:1301.4518, https://arxiv.org/abs/1301.4518.
4. I. Dolinka and collaborators, *Enumeration of idempotents in planar diagram monoids*, arXiv:1507.04838, https://arxiv.org/abs/1507.04838.
