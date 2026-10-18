# Interpreting \(\omega\) forces finite-parameter algebraicity in minimal structures
## Finding

Let \(M\) be an infinite minimal first-order structure. Suppose that, for some finite integer \(d\ge 1\), \(M\) interprets the linear order \((\omega,<)\) in \(M^d\), with parameters allowed. Then there is a finite parameter set \(A\subseteq M\) such that
\[
M\subseteq \operatorname{acl}(A).
\]
Equivalently, every element of the home sort belongs to a finite set definable over one fixed finite parameter set.

Consequently, if \(M\) has locally finite algebraic closure on the home sort,
\[
\operatorname{acl}(A)\cap M\text{ is finite for every finite }A\subseteq M,
\]
then \(M\) cannot interpret \((\omega,<)\) in any finite dimension.

## Assumptions and scope

A structure is minimal when every definable subset of its home sort, with parameters allowed, is finite or cofinite. An interpretation of \((\omega,<)\) in dimension \(d\) is a definable quotient of a definable subset of \(M^d\) carrying a definable order isomorphic to \((\omega,<)\).

Jagiella's Proposition 5.2 applies to arbitrary structures and shows that an interpretation of an infinite linear order in finite dimension can be reduced to dimension \(1\); when the original order is \((\omega,<)\), the dimension-one order may also be chosen to have order type \(\omega\). Thus the only additional hypothesis used here is minimality, which controls the sizes of the quotient fibers.

The algebraic closure \(\operatorname{acl}(A)\) is taken in an elementary extension; the displayed inclusion concerns the original home sort \(M\).

## Proof

Apply Proposition 5.2 to the given interpretation. There is a dimension-one interpretation of \((\omega,<)\). Choose a finite tuple of parameters \(A\) over which its defining formulas are written. We may describe the interpretation by an \(A\)-definable equivalence relation \(E\) on \(M\) and an \(A\)-definable strict relation \(R\) such that the induced quotient order
\[
(M/E,R/E)
\]
is isomorphic to \((\omega,<)\).

For each \(n<\omega\), let \(L_n\) be the inverse image in \(M\) of the \(n\)-th point of the quotient. These levels are uniformly recoverable one at a time from \(E\) and \(R\): \(L_0\) is the set of elements whose quotient class has no strict predecessor, and, once \(L_n\) is defined, \(L_{n+1}\) is the class immediately succeeding \(L_n\). Hence every fixed \(L_n\) is \(A\)-definable.

Each \(L_n\) is finite. Indeed, the levels are pairwise disjoint and nonempty. If some \(L_n\) were infinite, minimality would make it cofinite. Its finite complement could then contain only finitely many nonempty disjoint levels, contradicting the existence of \(L_m\) for every \(m<\omega\).

Therefore each element \(a\in L_n\) lies in the finite \(A\)-definable set \(L_n\), so
\[
a\in\operatorname{acl}(A).
\]
Since the levels partition \(M\), this proves
\[
M\subseteq\operatorname{acl}(A).
\]

If algebraic closure is locally finite on the home sort, then \(\operatorname{acl}(A)\cap M\) is finite for every finite \(A\). The inclusion just proved would force the infinite set \(M\) to be finite, a contradiction. Thus no such interpretation of \((\omega,<)\) exists in any finite dimension.

## Verification

The proof was reconstructed from the definitions and from the dimension-reduction statement in the primary source. Proposition 5.2 was checked in the full text: it reduces any finite-dimensional interpretation of an infinite linear order to dimension \(1\), and explicitly preserves order type \(\omega\). The source also records for dimension-one \(\omega\)-interpretations in minimal structures that the levels are the incomparability classes and are finite.

The remaining argument is elementary. For each fixed natural number \(n\), the \(n\)-th quotient point is first-order definable in \((\omega,<)\), so its pullback is \(A\)-definable. Minimality forces all these pairwise disjoint levels to be finite, and membership in a finite \(A\)-definable set is exactly the required algebraicity statement.

No computation, enumeration, compactness approximation, or external certificate is used.

## Relationship to prior work

Jagiella proves the finite-dimensional-to-one-dimensional reduction and develops the canonical dimension-one order for minimal ordered structures. The paper explicitly notes that the levels of a dimension-one \(\omega\)-interpretation are finite, but it does not state the resulting common finite-parameter algebraicity of the entire home sort or the locally-finite-algebraic-closure obstruction.

Earlier work of Krupiński, Tanović, and Wagner studies almost linear minimal structures and includes algebraic-closure calculations for particular examples. The checked material does not give the general implication from an arbitrary finite-dimensional \(\omega\)-interpretation to one finite parameter set algebraizing the whole home sort.

The point of the result is that interpretation of \(\omega\) imposes a global algebraic constraint, not merely an order-theoretic one. It supplies a direct obstruction criterion for minimal structures whose finite algebraic closures are known to stay finite.

## Limitations

The theorem is a necessary condition, not a converse: having \(M\subseteq\operatorname{acl}(A)\) for some finite \(A\) does not by itself produce an interpretation of \((\omega,<)\).

The conclusion is stated for the home sort. It does not assert that every imaginary or every element of an ambient monster model is algebraic over \(A\).

The argument uses the rigidity of the specific quotient order \((\omega,<)\), whose individual positions are definable. It does not, without further analysis, give the same conclusion for an arbitrary infinite interpreted linear order.

## References

[1] Grzegorz Jagiella, “On canonicity of almost linear minimal orders,” arXiv:2609.36313v2, first posted 28 September 2026. See Definition 1.1, Definition 2.9, Proposition 5.2, and Theorem 5.4.

[2] Krzysztof Krupiński, Predrag Tanović, and Frank O. Wagner, “Around Podewski’s conjecture,” *Fundamenta Mathematicae* 222 (2013), 175–193; arXiv:1201.5709.
