# Sharp quantifier-free one-types of finite dimension-two posets

## Finding

Let \(\mathcal D_2\) be the class of finite partially ordered sets of Dushnik–Miller order dimension at most two. In the pure strict-order language \(\{<\}\), for a finite marked set \(U\subseteq P\), define a **quantifier-free one-type over \(U\)** to be the complete pattern of all formulas \(x<u\), \(x=u\), \(u<x\), and their negations, for \(u\in U\). Let \(\tau(P,U)\) be the number of such patterns realized by elements of \(P\).

For each integer \(m\ge0\), the sharp extremal profile is
\[
\max_{P\in\mathcal D_2,\,U\subseteq P,\,|U|=m}\tau(P,U)=(m+1)^2.
\]
If the realizations are restricted to \(x\notin U\), the maximum is instead \(m^2+m+1\). The maximum is attained with \(U\) an antichain. A model attaining all \((m+1)^2\) patterns can be chosen to contain exactly \((m+1)^2\) vertices, and no smaller model can attain that many patterns.

## Assumptions and scope

Order dimension at most two means that there exist two linear orders whose intersection is the poset; a linear order itself may be realized by taking the same order twice. The parameters are \(m\) distinct individually named elements. Types are realized quantifier-free types in the one-symbol **pure poset reduct**, not complete first-order types and not types in the richer language naming the two linear orders. An incomparable relation is simply the conjunction \(\neg(x<u)\land\neg(u<x)\land x\ne u\). The empty marked set is allowed and has exactly one realized type whenever \(P\) is nonempty.

## Proof

**Two-order grid encoding.** Fix a finite poset \(P\) of dimension at most two and a two-linear-order realizer. Number the elements of \(U\) from \(1\) through \(m\) in the first linear order. Write \(p_i\) for the position of the \(i\)-th parameter in the second order; \(p=(p_1,\ldots,p_m)\) is a permutation of \(1,\ldots,m\). Every point \(x\notin U\) has a unique insertion cut \((r,s)\in\{0,\ldots,m\}^2\): there are \(r\) parameters preceding \(x\) in the first order and \(s\) in the second. Its strict predecessors and strict successors in the marked set are exactly
\[
 L_{r,s}=\{i:i\le r,\ p_i\le s\},\qquad
 G_{r,s}=\{i:i>r,\ p_i>s\}.
\]
Since \(U\) is fixed and each parameter is named, the pair \((L_{r,s},G_{r,s})\) determines the full quantifier-free one-type of \(x\). The naive number of cut pairs is \((m+1)^2\).

**Unavoidable collisions.** For each \(i\in\{1,\ldots,m\}\), consider the two distinct cut pairs
\[
 a_i=(i-1,p_i),\qquad b_i=(i,p_i-1).
\]
They have exactly the same predecessor and successor sets. Indeed, parameter \(i\) is incomparable to the new point at both cuts. For an earlier parameter \(j<i\), membership in \(L\) tests \(p_j\le p_i\) at the first cut and \(p_j\le p_i-1\) at the second; these are equivalent because \(p_j\ne p_i\). For a later parameter \(j>i\), membership in \(G\) tests \(p_j>p_i\) at the first cut and \(p_j>p_i-1\) at the second; again they are equivalent. No other membership can occur.

Draw an undirected graph on the \((m+1)^2\) grid cuts, placing an edge between \(a_i\) and \(b_i\) for each \(i\). This graph is a forest with exactly \(m\) edges: its \(i\)-th edge is the only edge crossing the boundary from first-cut coordinate \(r<i\) to \(r\ge i\); a cycle would have to cross the boundary at least twice. As the endpoints of each edge have equal types, each connected component yields at most one type. A forest of \((m+1)^2\) vertices and \(m\) edges has \((m+1)^2-m=m^2+m+1\) components. Thus at most \(m^2+m+1\) distinct nonparameter types occur. Exactly \(m\) additional, pairwise distinct equality types can occur at the marked vertices themselves. Hence \(\tau(P,U)\le(m+1)^2\).

**Sharp antichain witness.** Let the marked elements be \(u_i=(i,m+1-i)\), for \(1\le i\le m\), in the product of two dense linearly ordered coordinate sets. Define strict order by \(v<w\) exactly when both coordinates of \(v\) are less than those of \(w\); this is the intersection of the two coordinate orders. The marked set is an antichain and has second-order ranking \(p_i=m+1-i\).

All distinct nonparameter types of this antichain are obtained by one all-incomparable pattern and, for every nonempty consecutive interval \([a,b]\subseteq\{1,\ldots,m\}\), the two patterns:
\[
 L=\{a,\ldots,b\},\ G=\varnothing,
 \qquad\text{and}\qquad
 L=\varnothing,\ G=\{a,\ldots,b\}.
\]
For the former choose cut \((r,s)=(b,m+1-a)\). For the latter choose \((r,s)=(a-1,m-b)\). The all-incomparable pattern is realized at cut \((0,m)\). Distinct intervals and orientations yield distinct types, for a total of \(1+2\binom{m+1}{2}=m^2+m+1\) nonparameter types. Choose one point in each required open cut rectangle with coordinates avoiding the coordinates of all existing points and one another; this is possible over the rationals by arbitrarily small distinct perturbations. Append the \(m\) marked points. This defines a finite dimension-at-most-two poset having exactly \((m+1)^2\) points and pairwise different quantifier-free types. Since every realized type needs at least one realizing vertex, that number of points is also the least possible for any maximizer.

The \(m=0\) case consists of a single point. This proves all claims.

## Verification

The standalone `verify.py` enumerates every permutation of \(m\) parameter ranks for all \(0\le m\le8\), computes each distinct pair \((L_{r,s},G_{r,s})\), and checks the universal upper bound. It independently generates all reverse-permutation witness signatures and verifies equality with the interval-pattern family for each such \(m\). The resulting maximum nonparameter counts are \(1,3,7,13,21,31,43,57,73\); adding equality types gives \(1,4,9,16,25,36,49,64,81\). The script prints `VERIFY_OK`. This finite check supports, but is not a substitute for, the all-parameter collision-forest proof.

## Relationship to prior work

Bednarczyk, Kojelis and Szymański (2026), *Two Variables and Two-Dimensional Structures*, analyze two named linear orders, successors and finite satisfiability in two-variable logic. Their order-coordinate representation provides closely related motivation, but they do not state the maximum number of **pure-order-reduct** quantifier-free one-types over arbitrary named parameters. Dreier, Mählmann and Toruńczyk (2026), *First-Order Model Checking on Monadically Dependent Graph Classes*, discuss general finite-rank type bounds, not this exact sharp profile.

A particularly relevant comparison is *Exact quadratic \(1\)-type profile of Simon’s monotone two-order Fraïssé limit* (public finding, October 2026), which counts \(2(m+1)^2-1\) **complete first-order** types in a Fraïssé limit with **two named orders and an additional monotone binary relation**. Neither its object nor its notion of type is the present pure finite-poset-reduct atomic type count; the corresponding results do not imply one another directly. Other nearby finite-parameter type spectra refer to the countable homogeneous random poset, whose unrestricted one-point extension patterns do not obey the two-realizer grid collisions. A previous neighborhood result for undirected permutation graphs treats binary adjacency traces rather than directed strict-order comparisons. Searches for equivalent expressions, two-dimensional one-point poset extensions and parameter type spectra did not identify a covering result. This is evidence of a gap, not proof of historical novelty.

## Limitations

The theorem concerns **quantifier-free, one-variable** types only; it makes no assertion about complete first-order types, multiple new variables, or posets of dimension three or higher. Its extremal witness does not assert uniqueness of the maximizing parameter permutation or of the realizing model. Earlier geometric or model-theoretic folklore could contain an equivalent result. The verification checks parameter sizes at most eight; the proof is symbolic for all finite sizes. Independent mathematical or historical-priority review has not been performed.

## References

1. Bartosz Jan Bednarczyk, Daumantas Kojelis and Krzysztof Szymański, “Two Variables and Two-Dimensional Structures,” arXiv:2610.20937, first public version 2026-10-14. https://arxiv.org/abs/2610.20937
2. Jan Dreier, Niklas Mählmann and Szymon Toruńczyk, “First-Order Model Checking on Monadically Dependent Graph Classes,” arXiv:2611.08143, first public version 2026-11-05. https://arxiv.org/html/2611.08143v1
3. “Exact quadratic \(1\)-type profile of Simon’s monotone two-order Fraïssé limit,” publicly available mathematical finding (2026-10-04). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-quadratic-1-type-profile-of-simon-s-monotone-two-order-fra--ee696f008d98
