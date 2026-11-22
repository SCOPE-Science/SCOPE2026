# Finite bounded-fiber unary algebras: sharp colour obstruction to amalgamation and explicit homogeneous limits

## Finding

For integers \(q,k\geq 1\), let \(\mathcal K_{q,k}\) consist of all finite structures with a total unary function \(f\), an exhaustive partition into \(q\) named unary colour predicates, and \(|f^{-1}(v)|\leq k\) for every element \(v\). Embeddings preserve the function and named colours. Then:

\[
\boxed{\mathcal K_{q,k}\text{ has AP }\Longleftrightarrow(q=1\text{ or }k=1),\qquad
\mathcal K_{q,k}\text{ has SAP }\Longleftrightarrow k=1.}
\]

Here AP is ordinary amalgamation, allowing identification of new elements from opposite extensions; SAP is strong amalgamation, disallowing such identifications. The class has the hereditary property and joint embedding for all \(q,k\). If the finite fiber cap is removed, both AP and SAP hold for any finite \(q\).

For the AP-positive cases, the associated countable homogeneous limit is explicit. At \(k=1\), for any \(q\), it consists of countably infinitely many copies of every finite *coloured directed cycle* (cyclic colour words considered up to rotation). At \(q=1\), \(k\geq2\), it consists of countably infinitely many components for each possible directed cycle length; at each cycle vertex there are exactly \(k-1\) infinite incoming rooted \(k\)-ary branches, and every noncycle vertex has exactly \(k\) immediate predecessors. Every vertex has a finite forward orbit.

## Assumptions and scope

All structures are finite unless the homogeneous limit is explicitly discussed. Every element has exactly one of the \(q\) colours, with no compatibility condition between its colour and that of its image under \(f\). The fiber bound counts **all** preimages, including a possible cycle predecessor or fixed-point self-preimage. The language contains a total unary operation, so a substructure must be closed under \(f\). Amalgamation means amalgamation of injective colour-preserving function homomorphisms. Empty domains may be included without changing the results, since disjoint union proves joint embedding.

## Proof

**(1) Heredity and joint embedding.** An \(f\)-closed substructure has no larger fiber than its parent and inherits the colour partition. A disjoint union of two finite models preserves each fiber size and gives a common extension.

**(2) Ordinary amalgamation with one colour.** Replace an arbitrary span of embeddings by inclusions \(A\subseteq B,C\), with the two copies otherwise disjoint. The complement of \(A\) in either functional digraph has two kinds of components: rooted in-trees whose forward paths first enter \(A\), and complete cycle-with-in-trees components disjoint from \(A\). Keep the latter components disjoint. For each \(a\in A\), consider new immediate predecessors in \(B\) and \(C\). Pair arbitrarily as many as possible and identify each paired pair. For every paired pair, recursively do the same to their new immediate predecessors. Retain unmatched subtrees disjointly.

This recursion terminates because the two original structures are finite and each new vertex outside \(A\) has strictly shorter remaining distance to its chosen root upon moving forward. Pairings identify only one vertex of \(B\setminus A\) with one vertex of \(C\setminus A\), never two vertices from the same side. Function targets coincide after identification, so the quotient carries a well-defined total function and both original embeddings remain injective. For \(a\in A\), the number of preimages in the quotient is

\[
|f_A^{-1}(a)|+\max\{|f_B^{-1}(a)\setminus A|,\ |f_C^{-1}(a)\setminus A|\}\leq k.
\]

At each paired new vertex, the quotient has the maximum of the two original incoming-fiber sizes, at most \(k\). All unmatched vertices retain their original fibers. Thus the quotient is a finite amalgam satisfying the same bound. With only one colour, there is no colour incompatibility. This proves AP for every finite \(k\) when \(q=1\).

**(3) Strong amalgamation and the cap-one boundary.** If \(k=1\), a finite total function of fiber size at most one is bijective. Every \(f\)-closed substructure is therefore a disjoint union of complete directed cycles. Any span can be strongly amalgamated by taking the disjoint union outside its common cycles, preserving arbitrary named colours.

For \(k\geq2\), let \(A\) consist of a single fixed point \(a\). Each of \(B\) and \(C\) extends it by \(k-1\) fresh predecessors of \(a\). Every side obeys the cap, but in a strong amalgam the two sets of new points must remain disjoint. The image of \(a\) would then have \(1+2(k-1)>k\) distinct preimages. Consequently SAP fails for every \(k\geq2\), regardless of colours.

**(4) Named colours obstruct ordinary amalgamation.** Let \(q\geq2\) and \(k\geq2\). Construct \(A\) with a fixed point \(a\) and \(k-2\) distinct extra predecessors of \(a\); then \(|f_A^{-1}(a)|=k-1\). Form \(B\) by adding one new predecessor \(b\) of \(a\) of colour 1, and \(C\) by adding one new predecessor \(c\) of \(a\) of colour 2. Both extensions respect the cap. In any amalgam, the images of \(b\) and \(c\) cannot agree because named colours differ, while all \(k-1\) preimages from \(A\) remain distinct. The image of \(a\) would have at least \(k+1\) preimages, contradiction. Hence AP fails. Together with (2) and (3), this proves both exact thresholds.

**(5) The homogeneous limits.** Every finite member is a union of directed cycles with finite rooted in-trees attached. The classes with AP also have heredity, joint embedding, countably many isomorphism types and finite generation (the forward orbit of any finite set is finite). Fraïssé's back-and-forth construction therefore applies. One can directly identify its limit: the extension property forces infinitely many components of each permitted cycle type, and forces every point to realize its entire \(k\)-element preimage capacity in the uncoloured case. Those conditions uniquely yield the structures described in the Finding section. Their universality for finite members follows by embedding finite in-trees into the available infinite regular incoming trees. Their ultrahomogeneity follows by extending an isomorphism between finite forward-closed substructures to permutations of matching cycle components and recursively to isomorphisms of regular rooted incoming trees. At \(k=1\), all substructures are unions of finite coloured cycles; the countably infinite copies of every cyclic colour type give the same extension property.

If no fiber bound is imposed, the disjoint-overlap union itself is a strong amalgam, since a function defined identically on the common substructure is well defined on that union.

## Verification

The accompanying standalone finite checker `verify.py` enumerates 13,169 uncoloured amalgamation diagrams: common structures of orders one to three, extensions of orders at most four, and caps \(k\in\{1,2,3\}\). It constructs the described quotient, then checks functional consistency, preservation and injectivity of both embeddings, agreement on the common part, and all fiber caps. It separately checks the saturation arithmetic in the colour-based AP and SAP obstruction constructions for each \(k=2,\dots,8\). It reports `AMALGAM_VERIFIED 13169 uncoloured test diagrams; color and strong obstructions k=2..8`. The infinite and all-parameter statements follow from the displayed proofs, not from those finite tests.

## Relationship to prior work

The motivating 2026 paper by Rydval studies complexity of amalgamation for universal Horn theories over relational languages. Its August 12 first version was later substantially revised; the November 9 version is *Exponential Lower Bounds for Horn Amalgamation*, and its introduction, definition of AP/SAP, reduction theorems, and conclusion concern computational hardness rather than this family of coloured total unary functions. Previously claimed general upper bounds were withdrawn in the new version; none is used here. Evans, Hubička and Nešetřil (2017) study free amalgamation and extension of partial automorphisms for relational and partial-function structures; our bounded incoming-fiber restriction specifically prevents free or strong amalgamation in nontrivial cases. Mašulović (2021/2024) studies Ramsey degrees in classes of unary algebras, not this coloured bounded-fiber AP phase transition. The general Fraïssé theorem is used only as standard background; the threshold and concrete limits are proved here.

## Limitations

Only a **single total unary function**, independent named colours, and a uniform finite incoming-fiber cap are covered. Colour/function compatibility axioms, multiple unary functions, nonuniform vertex-dependent capacities and infinite-dimensional cardinality restrictions are not classified. The historical novelty comparison cannot establish absolute priority: an equivalent specialization could exist in older universal-algebra treatments not indexed by the inspected searches. The current 2026 source was examined in text form but the older Ramsey-degrees source was available at abstract level only. No external independent proof audit has been performed.

## References

- Jakub Rydval, *Exponential Lower Bounds for Horn Amalgamation*, arXiv:2608.12206, first version submitted 2026-08-12; revised 2026-11-09. https://arxiv.org/abs/2608.12206
- David M. Evans, Jan Hubička, Jaroslav Nešetřil, *Ramsey properties and extending partial automorphisms for classes of finite structures*, arXiv:1705.02379 (2017). https://arxiv.org/abs/1705.02379
- Dragan Mašulović, *Coalgebraic methods for Ramsey degrees of unary algebras*, arXiv:2111.05099 (2021; revision 2024). https://arxiv.org/abs/2111.05099
- R. Fraïssé, classical amalgamation/ultrahomogeneity theorem (standard background).
