# Logical width of balanced complete multipartite graphs

## Finding
For positive integers \(r,s\), let \(T_{r,s}\) be the complete \(r\)-partite graph with every part of size \(s\). In ordinary first-order graph logic with adjacency and equality, its logical width is
\[
W(T_{r,s})=\max\{r,s\}+1.
\]
Equivalently, the balanced Turán graph on \(rs\) vertices with \(r\) parts needs exactly one more variable than the larger of its number of parts and its part size.

## Assumptions and scope
Graphs are finite, nonempty, simple, and undirected. Logical width means the minimum number of distinct variable symbols in a first-order sentence that defines the graph up to isomorphism among finite graphs. No counting quantifiers are allowed. The parameters \(r\) and \(s\) are positive integers.

## Proof
Put \(m=\max\{r,s\}\).

For the upper bound, first suppose \((r,s)\ne(1,1)\), so \(m+1\ge3\). Write
\[
x\equiv y \quad\text{for}\quad (x=y)\lor\neg E(x,y).
\]
In a simple graph, a three-variable sentence can require \(\equiv\) to be transitive. Since reflexivity and symmetry are automatic, this makes \(\equiv\) an equivalence relation; equivalently, the graph is complete multipartite, with the equivalence classes as its parts.

Using a single common pool of \(m+1\) variable symbols, we can then conjoin the following requirements. There are at least \(r\) equivalence classes, witnessed by \(r\) pairwise inequivalent vertices; there are at most \(r\) classes, by forbidding \(r+1\) pairwise inequivalent vertices. Every class has at least \(s\) elements, witnessed for an arbitrary vertex \(x\) by \(s-1\) further distinct vertices equivalent to \(x\); and every class has at most \(s\) elements, by forbidding \(x\) together with \(s\) further distinct vertices all equivalent to \(x\). These conjuncts use at most \(r+1\), \(s+1\), and three variables, respectively, and bound variables can be recycled between conjuncts. Hence they define exactly \(T_{r,s}\) with \(m+1\) variables. If \(r=s=1\), the one-vertex graph is defined with two variables by \(\forall x\forall y\,(x=y)\). Thus
\[
W(T_{r,s})\le m+1.
\]

For the lower bound, use the standard \(k\)-pebble characterization of \(k\)-variable first-order equivalence, with \(k=m\).

If \(s\ge r\), compare \(T_{r,s}\) with \(T_{r,s+1}\). Duplicator maintains a partial isomorphism by matching every part currently touched by pebbles with a part on the other side, and within each matched pair of parts matching pebbled vertices injectively. When a pebble is moved, at most \(s-1\) other pebbles remain. Therefore an already matched part of the smaller graph always has an unused vertex whenever a fresh response is required. If Spoiler enters a previously untouched part, then at most \(s-1\) parts are occupied; because \(r\le s\), after the moved pebble has been lifted there is an unmatched part available on both sides. The invariant can therefore be maintained forever.

If \(r\ge s\), compare \(T_{r,s}\) with \(T_{r+1,s}\). Again Duplicator matches occupied parts and pebbled vertices within them. After a pebble is lifted, at most \(r-1\) parts remain occupied, so even the graph with only \(r\) parts has an unmatched part whenever Spoiler enters a fresh one. Inside a matched part the two sides both have exactly \(s\) vertices, so equality and nonadjacency patterns can always be matched. Thus Duplicator also wins the \(r\)-pebble game in this case.

The comparison graph is nonisomorphic to \(T_{r,s}\) in either case. Consequently no sentence using only \(m\) variables defines \(T_{r,s}\), and
\[
W(T_{r,s})\ge m+1.
\]
Together with the upper bound this proves the formula.

## Verification
A supplementary finite checker constructs the atomic partial-tuple types for the lower-bound comparison graphs and verifies the back-and-forth move condition for every \(1\le r,s\le4\). It returns

`VERIFY_OK cases=16 r_s_range=1..4 lower_witness_pebble_bisimulation`

The computation is only a sanity check. The theorem for arbitrary \(r,s\) follows from the symbolic Duplicator strategies above.

## Relationship to prior work
Finite-variable first-order logics are a standard part of finite model theory: Grohe's survey denotes by \(L^k\) the fragment using at most \(k\) variables. Pikhurko and Verbitsky define the logical width \(W(G)\) of a finite graph as the minimum number of variables in a defining sentence and note the general complement invariance \(W(G)=W(\overline G)\). Their survey contains no occurrence of “multipartite” or “Turán,” and targeted searches for complete multipartite graphs, balanced Turán graphs, and exact finite-variable width did not locate this formula.

The result supplies an exact two-parameter calibration family: it gives \(W(K_n)=n+1\) at \((r,s)=(n,1)\), the same value for the edgeless \(n\)-vertex graph at \((1,n)\), and \(W(K_{s,s})=s+1\) for balanced complete bipartite graphs.

## Limitations
The theorem concerns balanced complete multipartite graphs only. It does not give the logical width of an arbitrary complete multipartite graph with unequal part sizes, does not use counting quantifiers, and does not address minimum formula length or quantifier depth. The finite checker covers only small parameter values and is not a substitute for the general proof.

## References
1. Martin Grohe, “Finite Variable Logics in Descriptive Complexity Theory,” *Bulletin of Symbolic Logic* 4(4) (1998), 345–398. DOI: 10.2307/420954.
2. Oleg Pikhurko and Oleg Verbitsky, “Logical complexity of graphs: a survey,” *Contemporary Mathematics* 558 (2011), 129–180; arXiv:1003.4865, first posted 25 March 2010.
