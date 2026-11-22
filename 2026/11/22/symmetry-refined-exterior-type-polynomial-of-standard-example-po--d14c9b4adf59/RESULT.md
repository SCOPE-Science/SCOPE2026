# Symmetry-refined exterior-type polynomial of standard-example posets

## Finding
For every integer \(n\ge2\), consider the **standard-example poset** \(S_n\) consisting of minima \(a_1,\ldots,a_n\) and maxima \(b_1,\ldots,b_n\), ordered by \(a_i<b_j\) exactly when \(i\ne j\). Write \(\mathbb P\) for the countable generic homogeneous poset, and identify a fixed induced finite copy of \(S_n\) within \(\mathbb P\). For each complete nonalgebraic one-point type \(p\) over the individually named copy, define \(L_p=\{s\in S_n:s<x\text{ in }p\}\) and \(U_p=\{s\in S_n:x<s\text{ in }p\}\). Then its bivariate type-size polynomial is
\[
\boxed{T_n(x,y)=\sum_p x^{|L_p|}y^{|U_p|}=(1+x+y)^n+x^n(1+x)^n+y^n(1+y)^n+(n-1)(x^n+y^n).}
\]
The full poset automorphism group is the simultaneous index-permutation group \(\operatorname{Aut}(S_n)\cong\mathfrak S_n\). Let
\[
J_n(z)=\sum_{k=0}^{n}z^k+z^n+\sum_{k=1}^{n}z^{n+k}.
\]
Each orbit \([p]\) under this group has well-defined cardinalities \((|L_p|,|U_p|)\). Its complete orbit-size polynomial is
\[
\boxed{O_n(x,y)=\sum_{[p]} x^{|L_p|}y^{|U_p|}=J_n(x)+J_n(y)-1+\sum_{\substack{a,b\ge1\\a+b\le n}}x^a y^b.}
\]
Consequently, exactly \(3^n+2^{n+1}+2n-2\) one-point types exist over the individually named parameters, versus exactly \((n+1)(n+6)/2\) types up to automorphisms of the base. Under ultrahomogeneity, the latter are precisely the orbits of the setwise stabilizer of the base in \(\operatorname{Aut}(\mathbb P)\) on exterior points. This is an exponential-versus-quadratic symmetry compression for the canonical dimension-unbounded family of standard-example posets. The **scalar named-type formula alone is a specialization of a previously published general height-two identity** and is not independently claimed as new.

## Assumptions and scope
The signature is the strict binary partial order, with no unary colours and no added constants apart from the \(2n\) individually named parameters when defining \(p\). The order is irreflexive and transitive. The index range is \(n\ge2\); at \(n=2\), the poset is two disjoint two-point chains and its automorphism group is still the simultaneous two-index permutation group. The variables \(x,y,z\) are formal commuting indeterminates. A nonalgebraic type requires its new vertex to differ from every parameter; algebraic equality types are excluded throughout. An orbit type here means a one-point extension up to an automorphism of the **unlabelled base**, not up to arbitrary isomorphism of the enlarged structure with the base forgotten. Every finite one-point extension is realized in \(\mathbb P\) by its Fraïssé extension property.

## Proof
**1. Extension profiles.** For any finite poset \(P\), a relation profile of a new vertex is determined by \((L,U)\), where \(L\) is a downset, \(U\) an upset, and every element of \(L\) lies strictly below every element of \(U\). These conditions are necessary for transitivity. They are sufficient: add a fresh vertex above all of \(L\), below all of \(U\), and incomparable with the remaining elements; the three conditions make the enlarged strict relation transitive. Every resulting profile is a complete nonalgebraic type in \(\mathbb P\), because finite poset extensions are realized and the generic poset is ultrahomogeneous. We use this established profile description, not claim it as new.

**2. Two-sided profiles.** Suppose \(L\ne\varnothing\) and \(U\ne\varnothing\). Since every lower-upper pair must be strictly comparable, every member of \(L\) lies among the minima \(a_i\), and every member of \(U\) among the maxima \(b_i\). Their index sets must be disjoint: \(a_i\) and \(b_i\) are incomparable. Conversely, every pair of nonempty disjoint index sets is valid, and all other parameters are incomparable with the new vertex. Each index has three states (below, above, neither). After excluding configurations missing one or the other nonempty state, the two-sided contribution equals
\[
C_n(x,y)=(1+x+y)^n-(1+x)^n-(1+y)^n+1.
\]

**3. One-sided profiles.** With \(U=\varnothing\), the lower set \(L\) may be any downset of \(S_n\). If \(L\) contains no maxima, any subset of minima is permitted, giving \((1+x)^n\). If \(L\) contains at least one maximum \(b_j\), it must contain all minima except possibly \(a_j\). With exactly \(n-1\) minima, there is just one eligible maximum and exactly \(n\) such downsets, giving \(n x^n\). With all \(n\) minima present, choose any nonempty subset of maxima, giving \(x^n((1+x)^n-1)\). Thus the one-sided profile is
\[
I_n(x)=(1+x^n)(1+x)^n+(n-1)x^n.
\]
Order duality yields \(I_n(y)\) when \(L=\varnothing\). The all-incomparable type was counted twice, so the full polynomial is \(I_n(x)+I_n(y)-1+C_n(x,y)\); simplifying gives the displayed \(T_n\). Substituting \(x=y=1\) gives the scalar count.

**4. Automorphisms and orbit classification.** The minimal and maximal layers of \(S_n\) are definable from its order. Each minimum has a unique incomparable maximal vertex, namely its paired index. Therefore every automorphism permutes the index pairs simultaneously, and every such permutation is allowed, proving \(\operatorname{Aut}(S_n)\cong\mathfrak S_n\). For a one-sided downset, the base action has one orbit for each subset size \(0,\ldots,n\) with no selected maximum; one further orbit consisting of all \(n\) downsets with exactly \(n-1\) minima and their one eligible maximum; and one orbit for each of the \(n\) nonempty numbers of selected maxima when all minima are present. They have weights \(z^k,z^n,z^{n+k}\), respectively. This is exactly \(J_n(z)\). The upper-only profiles yield \(J_n(y)\). For two-sided profiles, permutations are transitive on ordered pairs of disjoint index subsets with prescribed sizes \(a,b\ge1\), \(a+b\le n\); this gives precisely one orbit in each such bidegree. Subtract the double-counted empty type to obtain \(O_n\). Finally \(J_n(1)=2n+2\), while there are \(n(n-1)/2\) admissible positive ordered size pairs. The orbit count is \(2(2n+2)-1+n(n-1)/2=(n+1)(n+6)/2\). No other profiles are possible, proving completeness.

## Verification
The bundled standalone standard-library Python checker `verify.py` independently enumerates every ternary relation of the fresh vertex to all \(2n\) old vertices and rejects any violation of transitivity in the full enlarged structure. It compares the coefficient-by-coefficient lower/upper type-size counts with the theorem for every \(2\le n\le6\): \(597861\) tested ternary assignments and \(1367\) valid extension profiles in total. For \(2\le n\le5\), it also computes genuine orbits under all simultaneous permutations, comparing every coefficient of the orbit polynomial and all \(88\) orbit classes. The recorded output is in `verification_output.txt`. The all-size proof, not finite enumeration, establishes the theorem for unbounded \(n\).

## Relationship to prior work
Kwiatkowska, Sullivan and Winkel, first public February 23, 2025, study external one-point types in the generic poset. Their Definition 2.2 and Lemma 2.4 give the general valid-triple framework used here; their main result concerns unique extensions of embeddings and does not enumerate the full bivariate or symmetry-refined spectra over standard-example bases. The previously published general height-two type-count identity in *Sharp one-comparability sensitivity and local counting hardness for random-poset one-types* does imply the **univariate total** here by substituting the graph \(K_{n,n}\) with the perfect matching removed; consequently the total is presented only as a derived corollary, not a standalone novelty assertion. That work gives neither the bivariate distribution of lower/upper positions nor the orbit polynomial under paired-index permutations. The published *Five-statistic convex-set polynomial and defect localization for standard-example posets* concerns the same parameter posets but counts vertex-subset convexity statistics, not extensions or their automorphism orbits. Searches of equivalent exterior-type, generic-poset one-type, standard-example, matching-deleted height-two-poset and symmetry-orbit descriptions located no covering published formula. Noncoverage is best-knowledge, not proof of absolute historical priority.

## Limitations
This is a complete classification for standard-example bases, not for arbitrary height-two posets, or multi-point extensions. The scalar named-type formula is already implied by earlier general literature; the substantive contribution is the two-variable distribution and the automorphism-orbit classification. There is no claim of new general poset-type machinery or of historical uniqueness. Sources indexed incompletely or older unpublished formulas might contain an equivalent specialization. The independent scientific audit has not been performed.

## References
1. A. Kwiatkowska, R. Sullivan, and J. Winkel, *Embeddings into the random poset*, arXiv:2502.16695v1, first public 2025-02-23, https://arxiv.org/html/2502.16695v1, especially Definition 2.2 and Lemma 2.4.
2. *Finite-parameter 1-type counting in the random poset is #P-complete*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1, for the general ideal/filter profile and counting problem.
3. *Sharp one-comparability sensitivity and local counting hardness for random-poset one-types*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-one-comparability-sensitivity-and-local-counting-hardness--9c2af418ff79, for the general height-two scalar identity.
4. *Five-statistic convex-set polynomial and defect localization for standard-example posets*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-five-statistic-convex-set-polynomial-and-defect-localization-for--84ba1197a0d2, for a distinct enumeration on the same posets.
