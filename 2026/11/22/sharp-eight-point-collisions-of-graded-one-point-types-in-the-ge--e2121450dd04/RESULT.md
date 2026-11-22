# Sharp eight-point collisions of graded one-point types in the generic poset

## Finding
Let \(\mathbb D\) be the countable homogeneous universal strict partial order and \(P\subseteq\mathbb D\) an induced finite poset whose elements are fixed individually as named parameters. For a complete nonalgebraic one-type \(p(x)\) over \(P\), let \(L_p=\{a\in P:a<x\in p\}\) and \(U_p=\{a\in P:x<a\in p\}\), and define its **graded one-point type fingerprint**
\[
\Phi_P(u,v)=\sum_{p\text{ nonalgebraic}}u^{|L_p|}v^{|U_p|}.
\]

**Sharp finite classification.** Among nonisomorphic posets of every fixed order \(n\le7\), the polynomial \(\Phi_P\) is injective on isomorphism classes. At \(n=8\), among precisely \(16{,}999\) unlabelled posets there are \(16{,}964\) different polynomials and **exactly \(31\) non-singleton fibres**, comprising \(28\) two-member, \(2\) three-member and \(1\) four-member fibres. The accompanying `census.json` records each entire collision fibre by its polynomial coefficients and the strict predecessor sets of its members; `verify_census.py` is a complete independent finite enumeration recipe. No conclusion about the fibres at higher orders is asserted.

An explicit pair of nonisomorphic colliding eight-point strict posets has strict-predecessor bitmask tuples
\[
A=(0,0,0,0,1,2,13,19),\qquad B=(0,0,0,0,1,2,7,25).
\]
In either tuple, the entry indexed by \(j\in\{0,\ldots,7\}\) records the bitmask of those \(i\) with \(i<j\). Both give \(\Phi(1,1)=120\) and the same full polynomial
\[
\begin{aligned}
\Phi(u,v)={}&1+3v+6v^2+9v^3+10v^4+10v^5+8v^6+4v^7+v^8\\
&+u(4+6v+3v^2+v^3)+u^2(8+5v)+u^3(10+2v)\\
&+10u^4+9u^5+6u^6+3u^7+u^8.
\end{aligned}
\]
This collision is **distinct** from the two published eight-point pairs of posets indistinguishable by two-variable counting logic: the two published pairs have different total nonalgebraic one-type counts, namely \(115\) versus \(109\) and \(100\) versus \(96\), respectively.

## Assumptions and scope
A finite poset means a finite set equipped with an irreflexive transitive relation \(<\). All finite posets occur as induced finite parameter structures inside \(\mathbb D\). Types counted here are complete first-order one-types realized by new elements distinct from all parameters. Parameters are fixed pointwise, so symmetries of the finite base are **not** used to identify types. The polynomial keeps the two cardinalities of named predecessors and successors, but not the actual named subsets. The classification ranges over all unlabelled finite strict posets of sizes one through eight. Posets of equal order are compared; the polynomial of a finite base has total degree equal to its cardinality because the empty upper/lower cases include the full ideal and filter.

## Proof
**Type representation.** Every nonalgebraic type is uniquely determined by a pair \((L,U)\) where \(L\) is an order ideal, \(U\) an order filter, and every element of \(L\) is below every element of \(U\). Necessity follows from transitivity of the extension. Conversely, adjoin a new vertex having precisely the prescribed predecessor and successor sets; ideal/filter closure and the cross-condition guarantee a valid induced extension. The Fraïssé extension property realizes it, and ultrahomogeneity identifies precisely equal patterns as equal complete types. In particular, a type can be counted by enumerating all ideal/filter pairs and checking the cross-condition. The representation is an established lemma in the prior literature, not claimed as a new theorem.

**Exhaustive representation of finite posets.** Every nonempty finite poset has a maximal point \(z\). Removing \(z\) leaves a smaller poset \(Q\), and the strict predecessors of \(z\) form an ideal of \(Q\). Thus every isomorphism type at order \(n\) arises when, for each isomorphism type at order \(n-1\), we append a maximal vertex above every order ideal. The verifier starts with the empty poset, performs exactly that recursion, and checks duplicates by an exhaustive backtracking isomorphism test. A necessary vertex invariant is the pair of numbers of strict predecessors and successors; within matching invariant classes, the backtracker searches all bijections while checking both directions of every comparison against previously mapped vertices. Therefore two generated relations are identified if and only if they are isomorphic. This is an exhaustive finite proof method, not sampling or a hash collision assertion.

**Full fingerprint census.** For each generated representative, enumerate all subsets \(L\) closed downwards and all subsets \(U\) closed upwards, reject intersections and any pair without all required strict cross-relations, and increment the coefficient of \(u^{|L|}v^{|U|}\). This is exhaustive since the type representation is bijective. Group the exact coefficient arrays, without numerical rounding. The computation gives the successive class totals
\[
1,2,5,16,63,318,2045,16999
\]
for orders one through eight, agreeing with the independent classical unlabelled-poset census. It produces zero non-singleton fibres at orders one through seven and precisely \(28,2,1\) fibres of sizes \(2,3,4\), respectively, at order eight. The complete coefficient and relation data for all fibres are serialized in `census.json`; thus each claim is reduced to executable, finite exhaustive steps using exact integers.

**Explicit witness.** For the two given relations, every initial predecessor mask contains all predecessors of its elements, proving transitivity. Each has four minimal vertices. Among these there is a unique vertex with exactly two strict successors, namely vertex \(1\). Also there is a unique maximal vertex with three minimal predecessors, namely vertex \(6\). In \(A\) vertex \(1\) does not lie below vertex \(6\), whereas in \(B\) it does. These first-order invariant descriptions rule out an isomorphism. Direct enumeration of all ternary predecessor/incomparable/successor labels independently returns the displayed identical polynomial. The claimed collision and completeness follow together from the witness and census.

**Comparison to counting logic.** The two published \(\mathrm C^2\)-equivalent eight-vertex pairs are given by strict successor row codes \((48,48,192,192,0,0,0,0)\) versus \((48,80,160,192,0,0,0,0)\), and \((204,240,64,64,128,128,0,0)\) versus \((204,240,64,128,64,128,0,0)\). Convert each row code to predecessor masks and apply the exact type-pair enumeration above to obtain the four totals \(115,109,100,96\). Thus neither published \(\mathrm C^2\) collision implies one of the newly classified fingerprint collisions.

## Verification
Run `python3 verify_census.py` in the same directory as `census.json` using Python 3 with only its standard library. The program reconstructs the entire census and rewrites `census.json` deterministically. It checks all unlabelled-poset totals against the independent classical sequence, performs exact isomorphism deduplication, and compares the pair-of-ideals enumeration to an independently programmed direct three-state extension test for **every** poset through five points, 25 deterministic representatives at each of orders six through eight, and both explicit witness posets. It checks all claimed collision fibre sizes and the explicit nonisomorphism. The successful run output is `verification_output.txt`.

The finite exhaustive census is the proof of the sharp finite threshold. The checks at larger sample orders validate the two different implementations, and no extrapolation to arbitrary orders is used. Exact program replay supplies an inspectable computation, not independent external certification.

## Relationship to prior work
Dolinka and Mašulović's 2010 preprint (published 2012) supplies the one-point ideal/filter extension criterion, which is credited. Brinkmann and McKay (2002) enumerate posets and provide an independent check on the exact number of unlabelled structures; their enumeration alone does not determine bivariate type-polynomial fibres. A previously archived exact one-type counting result develops the general type/ideal correspondence and #P-completeness but does not establish this small-order graded collision census. A separately archived theorem finds exactly two \(\mathrm C^2\)-equivalent pairs at eight vertices; that stronger logical equivalence is mathematically distinct, and both pairs have different values of \(\Phi_P(1,1)\). Previously published special-family graded-type formulas and degree-profile collision classifications address different invariants or smaller classes. Searches for equivalent first-collision thresholds, graded one-point type polynomials, and poset fingerprint fibres found no direct covering statement; mathematical priority beyond the inspected literature cannot be certified.

## Limitations
The complete classification ends at eight vertices. No asymptotic collision-frequency law or reconstruction theorem beyond that bound is claimed. The automorphism quotient is not taken in the type polynomial. The finite computer census is an exhaustive mathematical proof conditional on the transparent source code and its correct execution; independent implementation or expert review remains outstanding. An unindexed equivalent computation could predate this result.

## References
1. I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, first public preprint 2010-09-15, arXiv:1009.2892, especially Lemma 4.3; *Proceedings of the Edinburgh Mathematical Society* 55 (2012), 635–656. https://arxiv.org/abs/1009.2892
2. G. Brinkmann and B. D. McKay, *Posets on up to 16 points*, *Order* 19 (2002), 147–179. https://users.cecs.anu.edu.au/~bdm/papers/posets.pdf
3. *Finite-parameter 1-type counting in the random poset is #P-complete*, mathematical finding, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1/RESULT.md
4. *The eight-element threshold for two-variable counting equivalence of finite posets*, mathematical finding, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-eight-element-threshold-for-two-variable-counting-equivalenc--fe3ab073af88/RESULT.md
5. *Linear-arithmetic exact one-type counting on oriented tree-cover posets*, mathematical finding, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-linear-arithmetic-exact-one-type-counting-on-oriented-tree-cover--23742e530543/RESULT.md
