# Modus-ponens preconditionals on the eight-element Boolean algebra: an exact census

## Finding
Let \(X=\{1,2,3\}\) and \(B=\mathcal P(X)\), ordered by inclusion. Exactly \(19{,}127\) binary operations \(\to:B\times B\to B\) satisfy the five preconditional axioms (P1)--(P5) and the additional modus-ponens inequality. Under the natural relabelling action of \(S_3\) on the atoms, these operations form exactly \(3{,}369\) isomorphism classes. The fixed-operation counts for the identity, each transposition, and each three-cycle are respectively \(19{,}127\), \(341\), and \(32\).

More generally, for every finite set \(X\), these operations are in bijection with families of monotone functions \(\sigma_A:\mathcal P(A)\to\mathcal P(X\setminus A)\), one per subset \(A\subseteq X\), obeying one explicit compatibility law (below). This yields a finite parametrization beyond the three-atom case.

## Assumptions and scope
A preconditional on a bounded lattice is a binary operation \(\to\) satisfying, for every \(a,b,c\):

\[
\begin{aligned}
\mathrm{(P1)}&\quad 1\to a\leq a,\\
\mathrm{(P2)}&\quad a\wedge b\leq a\to b,\\
\mathrm{(P3)}&\quad a\to b\leq a\to(a\wedge b),\\
\mathrm{(P4)}&\quad a\to(b\wedge c)\leq a\to b,\\
\mathrm{(P5)}&\quad a\to((a\wedge b)\to c)\leq(a\wedge b)\to c.
\end{aligned}
\]

The extra assumption is modus ponens \(\mathrm{(MP)}:\ a\wedge(a\to b)\leq b\). These are inequalities between subsets when the lattice is \(\mathcal P(X)\); no weak-monotonicity, conditional identity, or extra negation laws are imposed. All operations and isomorphism classes are on the *entire labelled Boolean algebra*, not just on its atoms.

## Proof
**1. Normal form.** Fix any finite \(X\). By (P2) and (MP),
\[ A\cap(A\to B)=A\cap B. \]
By (P3), \(A\to B\subseteq A\to(A\cap B)\), while (P4), with its antecedent fixed, implies the reverse inclusion. Thus \(A\to B\) depends only on \(T=A\cap B\), and its trace inside \(A\) is exactly \(T\). Consequently there is a uniquely determined map \(\sigma_A:\mathcal P(A)\to\mathcal P(X\setminus A)\) with
\[
 A\to B=(A\cap B)\cup\sigma_A(A\cap B).
\]
(P4) is equivalent to monotonicity of each \(\sigma_A\), since its input sets are nested subsets of \(A\). Conversely, this normal form with monotone \(\sigma_A\) satisfies (P1)--(P4) and (MP). Indeed \(X\to B=B\), and intersection with \(A\) gives exactly \(A\cap B\).

**2. Compatibility law.** Substitute this normal form into (P5), put \(D=A\cap B\subseteq A\), and \(T=D\cap C\subseteq D\). Then
\[
D\to C=T\cup\sigma_D(T),
\quad
A\cap(D\to C)=T\cup(A\cap\sigma_D(T)).
\]
The portion of \(A\to(D\to C)\) inside \(A\) already lies in \(D\to C\). Therefore (P5) holds **if and only if**, for every \(D\subseteq A\subseteq X\) and \(T\subseteq D\),
\[
\boxed{\quad
\sigma_A\!\left(T\cup(A\cap\sigma_D(T))\right)
\subseteq \sigma_D(T)\setminus A.
\quad}
\tag{*}
\]
This equivalence includes empty and full subsets, so it is a complete classification for arbitrary finite \(X\), rather than a necessary condition alone.

**3. Exact finite enumeration.** Take \(|X|=3\), encode subsets by masks \(0,\ldots,7\), and enumerate the monotone maps \(\sigma_A\) by their full truth tables on \(\mathcal P(A)\). A coordinate of \(\sigma_A\) is a monotone Boolean function of \(|A|\) Boolean inputs. The resulting number of row choices at cardinalities \(0,1,2,3\) is \(8,9,6,1\), respectively (using the first four Dedekind numbers \(2,3,6,20\), with zero complement coordinates for \(|A|=3\)). The raw candidate space thus has size
\[
 8\cdot 9^3\cdot 6^3=1{,}259{,}712.
\]
The standalone exhaustive checker `checker_normal_form.cpp` enumerates precisely this space and rejects a row as soon as (*) fails for one \(D\subseteq A\) and \(T\subseteq D\). Its accepted counts, stratified by the mask \(\sigma_\varnothing(\varnothing)\) in order \(0,1,\ldots,7\), are
\[
 864,\ 509,\ 509,\ 843,\ 509,\ 843,\ 843,\ 14{,}207.
\]
Their sum is \(19{,}127\). This enumeration is exhaustive because each \(\sigma_A\) is selected from *all* monotone maps on its exact domain and all compatibility triples are checked. Independently, `checker_direct_axioms.cpp` loops over the same unfiltered candidate products and tests the six original inequalities directly on every corresponding operation table, obtaining the same accepted total and stratification without using (*) as its acceptance test.

**4. Isomorphisms.** Each automorphism of the eight-element Boolean algebra is a permutation of its three atoms. The normal-form checker tests directly, on all \(64\) ordered input pairs, whether the operation commutes with each of the six permutations. The fixed counts are \(19{,}127\) for the identity, \(341\) for each transposition, and \(32\) for each three-cycle. By Burnside's lemma, the orbit count is exactly
\[
 \frac{19{,}127+3(341)+2(32)}6=3{,}369.
\]

## Verification
Both C++17 sources are standalone and depend only on the standard library. Compile with `g++ -O2 -std=c++17 checker_normal_form.cpp -o norm` and `g++ -O2 -std=c++17 checker_direct_axioms.cpp -o direct`; run `./norm` and `./direct`. The first prints the row-choice sizes, totals, fixed-point counts, and orbit count. The second checks all six defining inequalities on all relevant triples for each of the \(1{,}259{,}712\) candidate families. The proof of the universal normal form and the finite-exhaustiveness argument do not depend on trusting a numerical log.

## Relationship to prior work
Holliday's *Preconditionals* introduces axioms (P1)--(P5) and discusses the further modus-ponens condition, including its interaction with Heyting implication. Chen's 2026 work develops general completeness, finite-model, and translation theorems for preconditionals, but no matching three-atom modus-ponens census was identified in the accessible full-text material. The previously established finite-chain preconditional classification concerns a different lattice geometry. A related finite eight-element enumeration under **additional \(\mathsf F\)-type laws** counts a distinct class; those extra laws are not assumed here, and this classification is neither its restatement nor an implication of its reported count. An unindexed or differently formulated enumeration remains possible.

## Limitations
The exact numeric counts are proved for a three-atom Boolean algebra. Equation (*) applies to arbitrary finite Boolean algebras, but no closed-form count for arbitrary atom number is claimed. The finite checking programs confirm a mathematically exhaustive reduction; they do not establish independent peer review or comprehensive historical priority. The present operation class does **not** impose weak monotonicity, which together with modus ponens characterizes Heyting implications among preconditionals.

## References
1. W. H. Holliday, *Preconditionals*, first public arXiv version 2024-02-03, arXiv:2402.02296, https://arxiv.org/abs/2402.02296 .
2. Z. Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, first public arXiv version 2026-07-22, arXiv:2607.20221, https://arxiv.org/abs/2607.20221 .
3. *Fixed-point normal form for finite-chain preconditionals*, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-fixed-point-normal-form-for-finite-chain-preconditionals--3d55c0067825 (related finite-chain comparison).
