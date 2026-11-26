# The minimal composition repair has a \(\Pi^0_2\)-complete two-point spectrum
## Finding

Fix an acceptable Kleene numbering
\[
(\varphi_e)_{e\in\omega}
\]
of the unary partial recursive functions and a standard primitive-recursive computation predicate
\[
T_1(e,n,s).
\]

Uniformly in \(e\), define the recursively enumerable extension of Peano arithmetic
\[
T_e
=
\mathrm{PA}
+
\{\exists s\,T_1(\bar e,\bar n,s):n\in\omega\}.
\]

Let \(\approx_e\) denote pointwise provable equality of unary program indices over \(T_e\), and let \(\sim_e\) be the least congruence for program composition that contains \(\approx_e\). Then
\[
e\in\mathrm{TOT}
\quad\Longleftrightarrow\quad
\sim_e=\{(a,b):\varphi_a=\varphi_b\},
\]
where
\[
\mathrm{TOT}=\{e:\varphi_e\text{ is total}\},
\]
whereas
\[
e\notin\mathrm{TOT}
\quad\Longleftrightarrow\quad
\sim_e=\omega\times\omega.
\]

Thus this computable family has an exact two-point repair spectrum. The repaired quotient is either the full monoid of unary partial recursive functions or the one-element monoid, and deciding which endpoint occurs is arithmetically sharp:
\[
\{e:\sim_e\text{ is extensional equality}\}
\]
is \(\Pi^0_2\)-complete, while
\[
\{e:\sim_e=\omega\times\omega\}
\]
is \(\Sigma^0_2\)-complete.

## Assumptions and scope

The numbering and computation predicate are chosen in the standard acceptable sense. The bars in
\[
\bar e,\bar n
\]
denote the corresponding numerals of arithmetic.

For a theory \(T\supseteq\mathrm{PA}\), pointwise provable equality identifies two program indices when \(T\) proves their Kleene equality separately at every standard input. The proof may depend on the input. The relation \(\sim_T\) is the least equivalence relation containing that pointwise relation and preserved by program-index composition in both coordinates.

No consistency assumption is imposed on \(T_e\). This matters: when \(\varphi_e\) is not total, \(T_e\) contains a false halting assertion, but Lengyel's generated-congruence theorem applies to arbitrary extensions of \(\mathrm{PA}\), including inconsistent ones.

Completeness is many-one completeness in the ordinary arithmetical hierarchy.

## Proof

For each \(e,n\), let
\[
H_{e,n}:=\exists s\,T_1(\bar e,\bar n,s).
\]
This is a \(\Sigma^0_1\) sentence saying that program \(e\) halts on input \(n\). The map
\[
(e,n)\longmapsto H_{e,n}
\]
is effective, so
\[
T_e=\mathrm{PA}+\{H_{e,n}:n\in\omega\}
\]
is recursively enumerable uniformly in \(e\).

Suppose first that
\[
e\in\mathrm{TOT}.
\]
Then every sentence \(H_{e,n}\) is true in the standard natural numbers. The axioms of \(\mathrm{PA}\) are also true there, so every axiom of \(T_e\) is true. By soundness of first-order deduction, every theorem of \(T_e\) is true. In particular, \(T_e\) is \(\Sigma^0_1\)-sound.

Lengyel's generated-congruence theorem therefore gives
\[
\sim_e
=
\{(a,b):\varphi_a=\varphi_b\}.
\]
The quotient is consequently the monoid of unary partial recursive functions under composition.

Conversely, suppose
\[
e\notin\mathrm{TOT}.
\]
Choose \(n\) such that \(\varphi_e(n)\) is undefined. Then \(H_{e,n}\) is a false \(\Sigma^0_1\) sentence, but it is an axiom of \(T_e\). Hence \(T_e\) is not \(\Sigma^0_1\)-sound. Lengyel's theorem now gives
\[
\sim_e=\omega\times\omega,
\]
so the quotient has one element.

This proves both equivalences.

It remains to identify the exact complexity of the two parameter sets. Membership in \(\mathrm{TOT}\) has the normal form
\[
e\in\mathrm{TOT}
\quad\Longleftrightarrow\quad
(\forall n)(\exists s)\,T_1(e,n,s),
\]
so \(\mathrm{TOT}\) is \(\Pi^0_2\). For hardness, if
\[
P=\{k:(\forall n)(\exists s)\,R(k,n,s)\}
\]
is any \(\Pi^0_2\) set with computable \(R\), uniformly construct a program \(p_k\) which, on input \(n\), searches for an \(s\) satisfying \(R(k,n,s)\) and halts when one is found. Then
\[
k\in P
\quad\Longleftrightarrow\quad
p_k\in\mathrm{TOT}.
\]
Thus \(\mathrm{TOT}\) is \(\Pi^0_2\)-complete. Its complement is therefore \(\Sigma^0_2\)-complete. Combining this with the two displayed equivalences gives the claimed exact complexity of the repair endpoints.

## Verification

The recent source was checked in full text. Its Theorem 4 defines the least composition congruence containing pointwise provable equality and proves the dichotomy
\[
\sim_T=
\begin{cases}
\text{extensional equality},&T\text{ is }\Sigma^0_1\text{-sound},\\
\omega\times\omega,&\text{otherwise}.
\end{cases}
\]
It further identifies the corresponding quotients as the monoid of unary partial recursive functions and the one-element monoid.

The same source fixes an acceptable Kleene numbering and a standard arithmetization of computation, so the halting sentences used above are in precisely the framework required by Theorem 4.

The reduction itself was checked directly. The family \(T_e\) is uniformly recursively enumerable; totality of \(\varphi_e\) makes every added halting axiom true, while one divergent input inserts a false \(\Sigma^0_1\) axiom. The standard search-program reduction proves \(\Pi^0_2\)-hardness without an oracle or finite experiment.

No computation log or enumeration is used as a substitute for the infinite proof.

## Relationship to prior work

Lengyel determines the generated congruence for an arbitrary extension \(T\supseteq\mathrm{PA}\) by the semantic boundary of \(\Sigma^0_1\)-soundness. The paper does not study the parameter-set complexity of that boundary: full-text searches for “undecidable,” “TOT,” and “index set” return no occurrence, and no arithmetical-completeness result for the generated repair is stated.

Earlier work on computable quotient presentations concerns which quotient structures admit computable presentations. Work on arithmetical classification of provably recursive functions establishes related \(\Pi^0_2\)-complete index phenomena, but for a different object. The present construction instead turns the new generated-congruence dichotomy into a uniform family whose quotient jumps exactly between two algebraic endpoints according to a \(\Pi^0_2\)-complete parameter set.

A separate structural consequence of the same recent source is that the original pointwise-provability quotient carries a natural one-sided action. That structure does not classify the least generated congruence or the complexity of choosing between its two endpoints.

## Limitations

The result concerns unary program composition and the least composition congruence generated by pointwise provable equality. It does not claim a corresponding completeness classification for all objects and morphism sorts of the proposed syntactic categories.

The family \(T_e\) is deliberately designed to encode totality through its added halting axioms. No claim is made that every natural enumeration of recursively enumerable extensions of \(\mathrm{PA}\) has exactly the same index-set presentation, although the reduction shows that the repair decision problem already has full \(\Pi^0_2\) difficulty on this simple uniform subfamily.

The two-point conclusion concerns the generated repair, not the unrepaired pointwise relation itself.

## References

[1] Florian Lengyel, “Pointwise provable equality and the failure of composition,” arXiv:2609.25556v2, first posted 22 September 2026.

[2] S. C. Kleene, *Introduction to Metamathematics*, North-Holland, 1952.

[3] H. Rogers, Jr., *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.

[4] M. T. Godziszewski and J. D. Hamkins, “Computable quotient presentations of models of arithmetic and set theory,” RIMS Kôkyûroku 2050 (2017), 9–23.
