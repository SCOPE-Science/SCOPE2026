# Exact ternary free-algebra census across a seven-element power-semiring variety interval

## Finding

Let \(S=\{a,b,c\}\) be the three-element semigroup with \(xy=f(x)\), where \(f(a)=a\), \(f(b)=b\), and \(f(c)=a\). In the constant-free signature \((+,\cdot)\) of additively idempotent semirings, let \(A=\mathrm V(\mathcal P^+(S))\), \(U=\mathrm V(\mathcal P(S))\). The six subvarieties \(U_\alpha,U_\beta,U_\eta,U_\delta,U_\gamma,A\) between these endpoints are defined by the respective additional absorption identities in Wang–Wang–Yin (2026, §4). For \(F_W(r)\), the free \(r\)-generated algebra in \(W\), the full rank-three order census is

\[
\begin{array}{c|rrrrrrr}
W&U&U_\alpha&U_\beta&U_\eta&U_\delta&U_\gamma&A\\\hline
|F_W(3)|&1727&1065&583&511&239&188&63.
\end{array}
\]

All seven orders are different, so three is the smallest free generator rank at which cardinality distinguishes all seven varieties. At rank one all seven orders are three; at rank two the orders are \(35,35,35,24,24,24,15\) in the same order. This is an exact result for the seven fixed varieties, not a statement about arbitrary semiring varieties.

## Assumptions and scope

The addition is associative, commutative and idempotent; multiplication is associative and distributes over addition. No nullary symbols are included. The power semirings are respectively over nonempty and all subsets of \(S\), with union and setwise multiplication. The seven-element nondegenerate variety interval and its covering order are those of Wang–Wang–Yin, arXiv:2611.11082. Its intermediate absorption rules are

\[
\begin{aligned}
\alpha:&\ xy\le x+y^2+xz, &\beta:&\ xy\le y^2+xz,\\
\eta:&\ x^2\le x+xy, &\delta:&\ xy\le y+xz+yz,\\
\gamma:&\ xy\le y+xz, &\sigma:&\ x^2\le xy,
\end{aligned}
\]

where \(u\le v\) abbreviates \(u+v=v\), and \(U_\sigma=A\). Only the cardinalities at exactly three free generators are asserted as the new census.

## Proof

**Finite completeness reduction.** By the normal-form identities of the upper endpoint \(U\) (Wang–Wang–Yin, Proposition 3.2), every product word on three variables is equivalent to either a single letter \(x_h\), or a long word \(w_{h,C}\) determined by its initial variable \(h\) and its nonempty content \(C\ni h\). There are exactly three singleton terms and \(3\cdot 2^2=12\) long-word types. Additive idempotence therefore ensures every element of each free algebra is represented by a nonempty subset of these fifteen types. Thus enumerating all \(2^{15}-1=32767\) subsets is mathematically exhaustive; their number is merely an upper bound prior to quotienting by identities.

**Absorption construction.** For each representative polynomial \(p\), record the three singleton-absorption bits and the twelve long-word-absorption bits. For each of the seven varieties, Theorem 4.2 and Lemma 3.1 of the cited paper give the exact predicate for each bit in terms of the first-letter set, long-word first-letter set, and the support-subset predicates \(H,N,T,J\). Two polynomials represent the same free-algebra element if and only if all fifteen bits agree: one direction is invariance of provable absorptions; the other follows by absorbing every summand of either polynomial into the other, because every word has one of the fifteen normal forms. Enumerating all nonempty subsets of the fifteen terms and taking the number of distinct signatures gives, in interval order, \(1727,1065,583,511,239,188,63\). The reproducible implementation is `checks/absorption_census.py`.

**Independent finite-generator construction.** Write \(N=\{o,d\}\) for the two-element null semigroup and \(L=\{p,q\}\) for the two-element left-zero semigroup. Put \(D=\mathrm V(\mathbf 2)\), the distributive-lattice variety. The same paper, Proposition 8.1, supplies

\[
\begin{aligned}
U_\gamma&=A\vee D, & U_\beta&=A\vee\mathrm V(\mathcal P(N)),\\
U_\eta&=A\vee\mathrm V(\mathcal P(L)), &
U_\alpha&=A\vee\mathrm V(\mathcal P(N))\vee\mathrm V(\mathcal P(L)),\\
U_\delta&=U_\beta\cap U_\eta.
\end{aligned}
\]

For any of the first four joins, equality in the variety is exactly simultaneous equality under all evaluations in the specified finite generators. Every representative word is evaluated at every assignment of three variables to elements of the relevant power semirings (orders \(8,7,4,4,2\) for \(\mathcal P(S),\mathcal P^+(S),\mathcal P(N),\mathcal P(L),\mathbf2\)). For \(U_\delta\), the defining equational congruence is the join of the congruences for \(U_\beta\) and \(U_\eta\); the equivalence classes are precisely connected components under the union of these two equivalence relations. This gives the same seven counts, using finite-algebra evaluation rather than the individual absorption predicates. An independently implemented checker appears at `checks/direct_census.py`.

Both checkers also recover the published rank-one and rank-two cardinalities \(3\) and \(35/24/15\); their agreement on rank three is a reproducibility cross-check. The proofs of completeness of the reduction and the finite generator descriptions are invoked from the cited paper rather than reproved here.

## Verification

Run `python3 checks/absorption_census.py` and `python3 checks/direct_census.py` from the directory containing the embedded files. Each enumerates all nonempty term-subsets on three variables and prints `VERIFY_OK`, and each asserts the seven-element rank-three table. The direct checker independently runs all substitutions into the five small finite algebras and computes the join congruence for \(U_\delta\). The separate derivations use distinct representations; no stochastic sampling is involved. Computation is exhaustive only at the stated generator rank, not an infinite-rank proof.

## Relationship to prior work

Wang, Wang and Yin (2026) establish the seven-element interval, its complete absorption criteria and finite generators, and the complete two-generated free algebra sizes. Their Proposition 6.3 gives \(|F_U(3)|=1727\) and \(|F_A(3)|=63\), and Corollary 6.4 gives the upper bound \(1727\) on all seven rank-three orders. The five exact intermediate rank-three orders above are a derived, explicit census filling the first generator rank that separates the seven interval elements. This finding does **not** claim the variety classification, identities, join descriptions, two-generator counts, or endpoint rank-three counts as new. It is an enumerative refinement based on those structural theorems.

## Limitations

The five intermediate numbers depend on the cited paper's exact normal-form and finite-generator results. This work does not establish formulas at arbitrary higher rank or a new equational classification. The original paper's general criteria enable the present finite computation, so priority should be interpreted narrowly as the explicit rank-three census rather than the underlying computability. No independent mathematical validation has been performed, and historical equivalents not located in the searched record remain possible.

## References

1. A. Wang, L. Wang and Q. Yin, *A seven-element interval of power-semiring varieties*, arXiv:2611.11082, first posted 2026-11-08, https://arxiv.org/abs/2611.11082 (especially §§3–4, 6, 8).
2. J. M. Howie, *Fundamentals of Semigroup Theory*, Clarendon Press, 1995 (background on semigroups; not relied upon for the census).
