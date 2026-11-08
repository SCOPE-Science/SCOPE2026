# Exceptional co-singleton symmetries of finite-group power semigroups

## Finding
Let \(G\) be any finite group and let \(\mathcal P^*(G)\) be the semigroup of its nonempty subsets with setwise multiplication. Put \(C_g=G\setminus\{g\}\), and let \(\mathscr T(G)\) be the subgroup of \(\operatorname{Aut}(\mathcal P^*(G))\) consisting of automorphisms fixing every subset except possibly the co-singletons \(C_g\) (when nonempty). Then
\[
\mathscr T(G)\cong
\begin{cases}
 C_3,&G\cong C_3,\\
 C_2\times C_2,&G\cong C_2\times C_2,\\
 \{1\},&\text{otherwise}.
\end{cases}
\]
Furthermore, the full automorphism groups in the two exceptional cases are
\[
\operatorname{Aut}(\mathcal P^*(C_3))\cong C_3\rtimes C_2\cong S_3,
\qquad
\operatorname{Aut}(\mathcal P^*(C_2\times C_2))
\cong (C_2\times C_2)\rtimes\operatorname{GL}_2(\mathbb F_2)
\cong S_4.
\]
The action of each kernel factor on co-singletons is a regular translation action on the missing element, fixing all singletons and all other subsets. In particular, the natural augmentation \(\operatorname{Aut}(G)\hookrightarrow\operatorname{Aut}(\mathcal P^*(G))\) is not surjective for either exceptional group. No claim is made that all nonaugmented automorphisms of larger power semigroups have co-singleton support.

## Assumptions and scope
Throughout, \(G\) is a finite group, with identity \(1\). Multiplication on \(\mathcal P^*(G)\) is \(XY=\{xy:x\in X,y\in Y\}\). A co-singleton is the complement of one group element; for the trivial group it is empty and is not in \(\mathcal P^*(G)\). The group \(\mathscr T(G)\) is defined by pointwise fixation of every nonempty subset not of size \(|G|-1\). The automorphism groups in the last display concern *all* semigroup automorphisms, without any assumption that they preserve subset cardinalities.

## Proof
**1. A product-filling observation.** If \(A,B\subseteq G\) are nonempty and \(|A|+|B|>|G|\), then \(AB=G\): for any \(g\in G\), the sets \(A\) and \(gB^{-1}\) intersect, so \(g=ab\) for some \(a\in A,b\in B\). In particular, for \(|G|\ge3\), multiplying a co-singleton on either side by a subset of size at least two gives all of \(G\). For singleton multiplication,
\[
\{a\}C_g=C_{ag},\qquad C_g\{a\}=C_{ga}.
\]

**2. Co-singleton factorization dichotomy.** Call a factorization \(C_g=AB\) *interior* when neither \(A\) nor \(B\) is a singleton or a co-singleton. For every finite \(G\) of order at least four other than \(C_2\times C_2\), every co-singleton has an interior factorization.

Indeed, if \(G\) contains an element \(a\) of order at least three, fix \(g\in G\) and put
\[
 A=\{1,a\},\qquad B=G\setminus\{g,a^{-1}g\}.
\]
As \(a^{-1}g\ne ag\),
\[
 AB=\bigl(G\setminus\{g,a^{-1}g\}\bigr)
 \cup\bigl(G\setminus\{ag,g\}\bigr)=G\setminus\{g\}=C_g.
\]
Both factors have size at least two and strictly less than \(|G|-1\) when \(|G|\ge4\).

Otherwise every element has order dividing two, so \(G\) is an elementary abelian two-group. If \(|G|\ge8\), choose distinct nonidentity \(u,v\), put \(A=\{1,u,v\}\), and \(B=G\setminus A\). In additive notation,
\[
 A\cap(u+A)\cap(v+A)=\{0\},
\]
so \(AB=G\setminus\{1\}\). Translating \(A\) on the left by \(g\) gives a factorization of \(C_g\) for every \(g\); the factors have sizes three and \(|G|-3\), which are interior when \(|G|\ge8\). This exhausts groups of order at least four except \(C_2\times C_2\).

For \(C_3\), the product of two subsets each of cardinality at least two is all of \(G\) by the first observation, so no co-singleton has such a factorization. For \(C_2\times C_2\), products involving subsets of respective sizes at least three and two are all of \(G\). A product of two two-element sets has size two or four: write them as translates of \(\{1,u\}\) and \(\{1,v\}\), with \(u,v\ne1\); their product is a translate of \(\{1,u,v,uv\}\). Thus no product of two nonsingletons is a co-singleton in either exceptional group.

**3. Determine the top-layer symmetry group.** For \(|G|\ge4\) outside the Klein group, every \(C_g\) is a product of two sets fixed by a member \(\Phi\in\mathscr T(G)\), hence is itself fixed; thus \(\mathscr T(G)\) is trivial. The trivial group gives a one-element power semigroup. For \(C_2\), the two co-singletons are the singleton units, the remaining set \(G\) is the unique absorbing element, and \(\operatorname{Aut}(C_2)\) is trivial, so \(\mathscr T(C_2)\) is trivial too.

Now let \(|G|\ge3\), and let \(\Phi\in\mathscr T(G)\). Singletons are fixed, and bijectivity forces \(\Phi(C_g)=C_{f(g)}\) for a bijection \(f:G\to G\). The singleton identities in Step 1 give
\[
 f(ag)=af(g),\qquad f(ga)=f(g)a
\]
for all \(a,g\in G\). Hence \(f(g)=gz=zg\) for some \(z=f(1)\in Z(G)\). The map is therefore determined by its central shift parameter.

Conversely, when \(G=C_3\) or \(G=C_2\times C_2\), define for each \(z\in G\)
\[
 \Phi_z(C_g)=C_{gz},\qquad
 \Phi_z(X)=X\quad\text{for every other nonempty }X\subseteq G.
\]
Products involving a singleton respect this map by the translation identities. Products of two nonsingletons are never co-singletons by Step 2; if one factor is a co-singleton, both its original and shifted products are \(G\), and otherwise both factors and their product are fixed. Hence \(\Phi_z\) is a multiplicative bijection. The maps \(z\mapsto\Phi_z\) form a faithful copy of \(G\). This proves the classification of \(\mathscr T(G)\).

**4. Determine the full small automorphism groups.** In \(\mathcal P^*(G)\), the units are precisely the singleton sets, since any product equal to \(\{1\}\) has singleton factors. Hence every power-semigroup automorphism restricts to an automorphism of \(G\); this restriction is surjective because every automorphism of \(G\) augments to one of its power semigroup. Also \(G\) is the unique absorbing element of \(\mathcal P^*(G)\), since the only nonempty set fixed by multiplication by every singleton is \(G\).

For \(G=C_3\), the seven nonempty subsets consist exactly of three singleton units, three co-singletons, and \(G\). Consequently every power-semigroup automorphism acting identically on the singleton units belongs to \(\mathscr T(C_3)\). The restriction kernel is \(C_3\); the natural split extension by \(\operatorname{Aut}(C_3)\cong C_2\) acts on this kernel by inversion. Thus the full group is \(S_3\).

For \(G=C_2\times C_2\), let \(\Phi\) act identically on singleton units. The nonempty idempotent subsets of a finite group are exactly its subgroups: an idempotent subset is closed under multiplication, and a nonempty finite subsemigroup of a group is a subgroup. Let \(H_u=\{1,u\}\) be one of the three order-two subgroups. Because \(\Phi\) commutes with all left singleton translations, it preserves the left-translation stabilizer of every subset. For a subgroup \(H\), that stabilizer is exactly \(H\). Since \(\Phi(H_u)\) is a subgroup with the same stabilizer, \(\Phi(H_u)=H_u\). Every two-element subset is a coset \(gH_u\), so all six two-element subsets are fixed. The singleton units and \(G\) are fixed too; the only remaining subsets are the four co-singletons. Therefore the restriction kernel is exactly \(\mathscr T(C_2\times C_2)\cong C_2\times C_2\).

The restriction extensions split by augmentation in both cases, and conjugation by an augmented \(\alpha\in\operatorname{Aut}(G)\) sends \(\Phi_z\) to \(\Phi_{\alpha(z)}\). Since \(\operatorname{Aut}(C_2\times C_2)\cong\operatorname{GL}_2(\mathbb F_2)\cong S_3\), its semidirect product with the Klein translation group is \(\operatorname{AGL}_2(\mathbb F_2)\), which acts faithfully on four points and has order \(4\cdot6=24\), hence is \(S_4\). This proves all claims.

## Verification
Execute `python3 CHECK.py` using only the Python standard library. Its recorded stdout is `CHECK_OUTPUT.txt`; the run ends in `VERIFY_OK`. The program constructs complete multiplication tables for \(C_2,C_3,C_4,C_5,C_6,C_7,C_8,C_2^2,C_2^3,S_3\), exhaustively checks which co-singletons are products of two nonsingletons, and checks every ordered pair of nonempty subsets against all six proposed automorphisms for \(C_3\) and all twenty-four for \(C_2^2\). These finite experiments are consistency tests, not the proof for arbitrary finite groups.

## Relationship to prior work
Liu and Tringali's 2026 work on Kobayashi's problem proves singleton preservation under isomorphisms of inverse-semigroup power semigroups, and their earlier group rigidity theorem shows that the underlying group is recovered from its nonempty-subset power semigroup. Neither statement asserts that every power-semigroup automorphism is the augmentation of a group automorphism. The explicit nonaugmented small-group automorphisms here show why the distinction matters.

Rago's classification concerns the **reduced** power monoid of subsets containing the identity, and in particular gives an exceptional larger group for the reduced Klein-four case. That is a different domain from the full set of *all nonempty* subsets: the present co-singleton translations need not preserve the reduced submonoid, and Rago's result does not supply the two full-power automorphism groups here. Tringali and Wen study power semigroups of numerical semigroups rather than finite groups. Their results and methods provide context, not coverage of the present precise claims.

## Limitations
The support-classification statement says only which automorphisms can move **exclusively** co-singletons. It does not classify the entire automorphism groups for finite groups other than \(C_3\) and \(C_2\times C_2\), and it does not show that larger groups have no nonaugmented automorphisms with broader support. The small-group group orders are proved directly. The novelty comparison covers accessible sources but is not an independent priority certification; literature on full rather than reduced power-semigroup automorphisms could contain related observations.

## References
1. S. Liu and S. Tringali, *Kobayashi's problem for power semigroups of inverse semigroups*, arXiv:2610.29525v1, first submitted 21 October 2026. https://arxiv.org/abs/2610.29525
2. S. Liu and S. Tringali, *Power Semigroups and Two Rigidity Theorems for Groups*, arXiv:2606.01917v1, 1 June 2026. https://arxiv.org/abs/2606.01917
3. B. Rago, *The automorphism group of reduced power monoids of finite abelian groups*, arXiv:2510.17533v1, 20 October 2025. https://arxiv.org/abs/2510.17533
4. S. Tringali and K. Wen, *On the automorphisms of the power semigroups of a numerical semigroup*, Transactions of the London Mathematical Society 13 (2026), e70030; open access. https://doi.org/10.1112/tlm3.70030
