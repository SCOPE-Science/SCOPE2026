# Exact term operations and the sharp atom threshold for finite Boolean algebras with a consistency operator

## Finding

For integers \(k,m\geq1\), let \(B_k=\mathcal P([k])\) and expand its usual Boolean operations by the **endpoint test**
\[
\circ X=\begin{cases}[k],&X=\varnothing\text{ or }X=[k],\\\varnothing,&\text{otherwise}.\end{cases}
\]
This is the consistency operation considered by Freire and Martins. Write \(T_{k,m}\) for the number of distinct \(m\)-ary **term operations** in the signature \(\{\neg,\wedge,\vee,\circ\}\); terms use \(m\) variables and no additional named elements.

**Normal form and exact count.** Put \(H=\{0,1\}^m\). For an input tuple \(\mathbf X=(X_1,\ldots,X_m)\), partition \([k]\) into the \(2^m\) Boolean cells
\[
E_s(\mathbf X)=\bigcap_{i:s_i=1}X_i\ \cap\ \bigcap_{i:s_i=0}([k]\setminus X_i),\qquad s\in H.
\]
Let \(P(\mathbf X)=\{s:E_s(\mathbf X)\ne\varnothing\}\). The term operations are **exactly** the maps of the form
\[
 f(\mathbf X)=\bigcup_{s\in F(P(\mathbf X))}E_s(\mathbf X),
\]
where \(F\) is any assignment \(P\mapsto F(P)\subseteq P\) on the nonempty subsets \(P\subseteq H\) of cardinality at most \(k\). Distinct assignments give distinct operations. Consequently,
\[
\boxed{T_{k,m}=2^{\sum_{r=1}^{\min(k,2^m)}r\binom{2^m}{r}}
=2^{2^m\sum_{j=0}^{\min(k,2^m)-1}\binom{2^m-1}{j}}.}
\]

**Sharp equational threshold.** The identities in at most \(m\) variables true in \(B_k\) with \(\circ\) are strictly decreasing as \(k\) increases from \(1\) to \(2^m\), and stabilize exactly at \(k=2^m\). Thus two expanded algebras \(B_k\), \(B_\ell\) have the same \(m\)-variable identities if and only if \(\min(k,2^m)=\min(\ell,2^m)\).

Examples: \(T_{1,1}=4\), \(T_{k,1}=16\) for \(k\ge2\); \(T_{1,2}=16\), \(T_{2,2}=65{,}536\), \(T_{3,2}=2^{28}\), and \(T_{k,2}=2^{32}\) for \(k\ge4\). These are counts of extensional operations, not of formulas.

## Assumptions and scope

The Boolean algebra is finite, nontrivial, with exactly \(k\) atoms. The operation \(\circ\) returns the top element precisely at the bottom and top inputs; it returns bottom elsewhere. The language is purely **propositional/algebraic**: it does not include modal operators, quantifiers, named nontrivial constants, or arbitrary parameters. Equivalence is equality of the \(B_k\)-valued functions on every input tuple, not mere agreement in a chosen ultrafilter. Both \(k\) and \(m\) range over all positive integers. All inputs and outputs are subsets of \([k]\).

## Proof

1. **Invariants.** The cells \(E_s(\mathbf X)\), for \(s\in H\), are pairwise disjoint and partition the carrier. Exactly \(|P(\mathbf X)|\) cells are nonempty, hence \(1\le |P(\mathbf X)|\le\min(k,2^m)\). Every such nonempty support pattern occurs: partition the \(k\) atoms into \(|P|\) nonempty groups and define each \(X_i\) as the union of groups whose type has \(s_i=1\). By structural induction, every term value is a union of cells selected solely by the support pattern. Variables select a fixed collection of types; Boolean negation, meet and join complement, intersect and unite the selected types relative to \(P\). If the selected set is \(Q\subseteq P\), then \(\circ\) yields the whole carrier exactly when \(Q=\varnothing\) or \(Q=P\), and the empty set otherwise. Thus no step can see the positive cardinality of an occupied cell.

2. **Every assignment is realized.** Form the abbreviation \(\delta_0(Y)=\neg Y\wedge\circ Y\). Direct evaluation shows that \(\delta_0(Y)=[k]\) exactly when \(Y=\varnothing\), and otherwise \(\delta_0(Y)=\varnothing\). Let \(e_s\) be the Boolean term defining \(E_s\), put \(z_s=\delta_0(e_s)\), and \(n_s=\neg z_s\). For a nonempty feasible pattern \(P\), define the Boolean selector
\[
q_P=\bigwedge_{s\in P}n_s\ \wedge\ \bigwedge_{s\notin P}z_s.
\]
This term evaluates to \([k]\) exactly at inputs with support \(P\), and to \(\varnothing\) otherwise. For any assignment \(F(P)\subseteq P\), the term
\[
\bigvee_{P\text{ feasible}}\left(q_P\wedge\bigvee_{s\in F(P)}e_s\right)
\]
realizes precisely the claimed operation. Empty Boolean meets/joins are interpreted as the definable constants \(\top=x_1\vee\neg x_1\) and \(\bot=x_1\wedge\neg x_1\). The sum is finite, with no bound on term length assumed.

3. **Counting and uniqueness.** For each feasible \(P\) with \(|P|=r\), the set \(F(P)\) has \(2^r\) choices. Choices for distinct patterns are independent because each pattern is realized; if two choices differ at type \(s\), every atom in its nonempty cell witnesses distinct output. Multiplication over the \(\binom{2^m}{r}\) patterns gives the formula. The alternative exponent follows from \(r\binom{N}{r}=N\binom{N-1}{r-1}\).

4. **Identity threshold.** The normal form identifies term-equivalence classes with the functions \(F\) on feasible patterns. Once \(k\ge2^m\), the domain of such patterns is unchanged, hence exactly the same pairs of terms are equivalent for every larger \(k\). For \(k<2^m\), choose \(P\subseteq H\) with \(|P|=k+1\). The term \(q_P\) above is identically bottom in \(B_k\), yet takes the top value in \(B_{k+1}\) on an input realizing \(P\). Hence \(q_P\approx\bot\) separates the identities at consecutive levels. Since an identity with fewer variables is also one with at most \(m\) variables, the statement covers all at-most-\(m\)-variable equations.

## Verification

A standalone, standard-library-only executable \(`verify.py`\) checks the formula and two independent finite-algebra constructions. First, it exhaustively closes unary term tables under complement, meet, join and the actual endpoint-test operator for \(k=1,2,3\) (obtaining \(4,16,16\) operations). Second, for \((k,m)=(1,1),(1,2),(2,1),(2,2),(3,1)\), it computes the generated Boolean algebra of all atomic term-table coordinates and refines it under the endpoint test until closed; its dimensions match the formula (in particular, \(16\) independent coordinates and thus \(65{,}536\) operations for \(k=m=2\)). The checker also evaluates selected numerical cases. Execute \(`python3 verify.py`\); the success marker is \(`ENDPOINT_TEST_TERM_CLONE_VERIFY_OK`\). The infinite families are proved by the preceding induction and constructions, not by extrapolation from the checks.

## Relationship to prior work

Freire and Martins, *Regular non-normal modal classicalities* (arXiv:2602.20287, first submitted February 23, 2026), define the endpoint-testing consistency operator on finite Boolean algebras and study axiomatization over four values and a mixed eight-valued modal semantics. Their available full text, especially Sections 2–5, does not state an all-arity term clone normal form, the exact count, or an identity-stabilization threshold.

The general quasi-primal/discriminator theory of Pixley and of Davey, Schumann and Werner supplies an important broader interpolation mechanism. Indeed this algebra admits equality testing by \(\delta_0\) applied to Boolean symmetric difference, hence admits a discriminator term. The present result explicitly works out the resulting term operations for the particular consistency expansion, their unique nonempty-cell support normal forms, and an exact arity/carrier formula and sharp threshold; it does not claim invention of discriminator theory. Known quantifier-rank atom-visibility results for *plain* finite Boolean algebras concern a different language and a different complexity parameter.

## Limitations

The result concerns exact algebra-valued term operations, not theoremhood, modal validity, or the ultra-filter designated-value consequence relation. It does not classify expansions by other consistency operators, nor infinite Boolean algebras. The source paper provides the original operation, while the algebraic interpolation framework substantially predates it; a previously unlocated explicit instance of the same finite clone census remains a historical-priority risk.

## References

1. A. R. Freire and M. A. Martins, *Regular non-normal modal classicalities*, arXiv:2602.20287 (2026), https://arxiv.org/abs/2602.20287 ; openly available author full text at https://www.researchgate.net/publication/401178699_Regular_non-normal_modal_classicalities .
2. B. A. Davey, V. J. Schumann, H. Werner, *From the subalgebras of the square to the discriminator*, Algebra Universalis **28** (1991), 500–519, doi:10.1007/BF01195860 .
3. A. F. Pixley, *The ternary discriminator function in universal algebra*, Math. Ann. **191** (1971), 167–180, doi:10.1007/BF01578706 .
4. S. Burris and H. P. Sankappanavar, *A Course in Universal Algebra*, Springer (1981), general reference for term functions and finite universal algebras.
