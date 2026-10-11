# Fox–Milnor parity law for multiple-tangle extended symmetric unions
## Finding
Let \(K=K(\hat K;T_1,\ldots,T_n)\) be a multiple-tangle extended symmetric union in the sense of Kitano--Nakae, and define
\[
P_T(t)=\prod_{i=1}^{n}\Delta_{N(T_i)}(t).
\]
Then
\[
\Delta_K(t)\doteq f(t)f(t^{-1})
\]
for some \(f\in\mathbb Z[t,t^{-1}]\) if and only if
\[
P_T(t)\doteq g(t)g(t^{-1})
\]
for some \(g\in\mathbb Z[t,t^{-1}]\). Here \(\doteq\) denotes equality up to a Laurent unit \(\pm t^k\).

Equivalently, factor all numerator-knot Alexander polynomials in \(\mathbb Z[t,t^{-1}]\). Every irreducible factor that is associate to its reciprocal must occur with even total multiplicity across
\[
\Delta_{N(T_1)}(t),\ldots,\Delta_{N(T_n)}(t).
\]
The non-self-reciprocal factors occur in reciprocal pairs with equal multiplicities automatically.

Consequently, if \(K\) is topologically slice, the displayed parity condition on the tangle numerators is necessary. The partial knot \(\hat K\) makes no difference to this classical Alexander-polynomial slice obstruction.

A repeated-tangle specialization gives a sharp parity law. If all \(T_i=T\) and \(\Delta_{N(T)}\) is not a Fox--Milnor norm, then the constructed Alexander polynomial fails the Fox--Milnor condition exactly when \(n\) is odd. For even \(n\), it always passes the Fox--Milnor condition, regardless of the partial knot.

Kitano--Nakae exhibit an admissible tangle with \(N(T)=5_2\) and
\[
\Delta_{5_2}(t)=2t^2-3t+2.
\]
This polynomial is irreducible over \(\mathbb Z\) and self-reciprocal. Therefore any such construction using an odd number of copies of this tangle is not topologically slice, whereas the even-copy constructions pass the classical Fox--Milnor test.

## Assumptions and scope
The Alexander polynomial is considered up to multiplication by \(\pm t^k\). A Laurent polynomial is called a Fox--Milnor norm when it is associate to \(f(t)f(t^{-1})\) for an integral Laurent polynomial \(f\).

The input construction is exactly the multiple-tangle extended symmetric union of Kitano--Nakae. Their Theorem 1.1 gives
\[
\Delta_K(t)=\Delta_{N(T_1)}(t)\cdots\Delta_{N(T_n)}(t)\bigl(\Delta_{\hat K}(t)\bigr)^2
\]
under their normalization.

The sliceness conclusion uses only the classical necessary Fox--Milnor condition: a topologically slice knot has Alexander polynomial of Fox--Milnor norm form. Passing that condition is not sufficient for sliceness.

## Proof
Put \(R=\mathbb Z[t,t^{-1}]\), a unique-factorization domain, and let \(r^*(t)=r(t^{-1})\). The involution \(*\) permutes irreducible factors up to associates.

Consider one irreducible orbit. If \(r\) and \(r^*\) are nonassociate, then a norm \(ff^*\) contains \(r\) and \(r^*\) with the same exponent. If \(r\) is associate to \(r^*\), then its exponent in \(ff^*\) is even. Conversely, these orbit conditions allow one to choose one factor from each non-self-reciprocal pair and half the exponent from each self-reciprocal orbit, producing an \(f\) with the required norm. Thus these conditions characterize Fox--Milnor norms in \(R\), up to units.

Every knot Alexander polynomial is reciprocal. Hence for the product \(P_T\), the exponents on every non-self-reciprocal pair are already equal. Its norm status is therefore controlled exactly by the parities of its self-reciprocal irreducible exponents.

Kitano--Nakae give
\[
\Delta_K=P_T\bigl(\Delta_{\hat K}\bigr)^2.
\]
Because \(\Delta_{\hat K}\) is reciprocal, its square adds an even exponent to every self-reciprocal orbit and equal even increments to both members of every non-self-reciprocal orbit. The orbit conditions for \(\Delta_K\) are therefore identical to those for \(P_T\). This proves the equivalence and the independence from the partial knot.

If all \(T_i=T\), write \(Q=\Delta_{N(T)}\). Then \(P_T=Q^n\). If \(Q\) is not a norm, at least one self-reciprocal irreducible factor of \(Q\) has odd exponent. In \(Q^n\), every such odd exponent remains odd exactly when \(n\) is odd. When \(n\) is even, every self-reciprocal exponent is even, so \(Q^n\) is a norm. This proves the parity law.

Finally,
\[
2t^2-3t+2
\]
has discriminant \(-7\), so it is irreducible over \(\mathbb Q\), hence over \(\mathbb Z\) by Gauss's lemma. Its coefficients are palindromic, so it is self-reciprocal up to a Laurent unit. It therefore occurs to odd multiplicity in an odd-repeat product and violates the Fox--Milnor condition.

## Verification
The current multiple-tangle source was inspected at its construction and Theorem 1.1, including the exact Alexander-polynomial product formula. Its introduction was also checked for downstream applications: it records a nonfiberedness consequence from nonmonic numerator factors, but no sliceness or Fox--Milnor application is stated there.

The earlier single-tangle source was inspected at the explicit \(10_{65}\) example. It identifies an admissible tangle with numerator \(5_2\) and records
\[
\Delta_{5_2}(t)=2t^2-3t+2.
\]
The classical Fox--Milnor necessary condition for slice knots was checked against standard references to the 1966 Fox--Milnor theorem.

The bundled verifier stress-tests the irreducible-orbit parity bookkeeping under multiplication by arbitrary reciprocal squares in a finite exponent box, checks the \(5_2\) discriminant and reciprocity, and checks the first twelve repetition parities. It prints:

`VERIFY_OK orbit_parity_invariant=true delta_5_2_disc=-7 repeated_n_1_12=FPFPFPFPFPFP odd_fail_even_pass=true`

The finite program is not the proof of the general theorem. The infinite statement is proved by unique factorization and reciprocal-factor orbits as above.

## Relationship to prior work
Kitano--Nakae prove the product formula for the Alexander polynomial of a multiple-tangle extended symmetric union and use it to construct nonfibered examples when a numerator polynomial is nonmonic. Their paper does not state a Fox--Milnor criterion, a sliceness obstruction, partial-knot independence for that obstruction, or a repetition-parity law.

Their earlier single-tangle paper gives the explicit \(5_2\)-numerator tangle used here, again in a nonfiberedness discussion. The classical Fox--Milnor theorem supplies the independent sliceness obstruction but contains no information about this 2026 construction.

Targeted literature searches using the construction name, Fox--Milnor terminology, sliceness, numerator tangles, repeated regions, and partial-knot dependence did not locate an equivalent criterion or parity statement.

## Limitations
This is a complete classification only of the classical Fox--Milnor Alexander-polynomial obstruction within the construction. A knot whose polynomial passes the condition need not be algebraically slice, topologically slice, smoothly slice, or ribbon.

The result does not analyze signatures, Casson--Gordon invariants, Floer-theoretic concordance invariants, or twisted Alexander polynomials. Such invariants can still depend on the partial knot or on finer tangle data even when the classical Fox--Milnor test does not.

The odd-repeat conclusion for the \(5_2\) tangle is an obstruction to sliceness; the even-repeat conclusion says only that this one obstruction vanishes.

## References
1. T. Kitano and Y. Nakae, *An extended symmetric union with multiple tangle regions and its Alexander polynomial*, arXiv:2601.02800v1, first posted 2026-01-06.
2. T. Kitano and Y. Nakae, *An extended symmetric union and its Alexander polynomial*, arXiv:2502.08229v1, first posted 2025-02-12.
3. R. H. Fox and J. W. Milnor, *Singularities of 2-spheres in 4-space and cobordism of knots*, Osaka Journal of Mathematics 3 (1966), 257--267, DOI `10.18910/7307`.
