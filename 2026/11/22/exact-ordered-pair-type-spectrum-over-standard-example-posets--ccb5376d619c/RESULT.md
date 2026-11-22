# Exact ordered-pair type spectrum over standard-example posets

## Finding
For every integer \(n\ge2\), let \(S_n\) be the standard-example partial order with individually named minima \(a_1,\ldots,a_n\) and maxima \(b_1,\ldots,b_n\), where \(a_i<b_j\) if and only if \(i\ne j\). Embed this induced finite parameter order into the countable universal homogeneous partial order. Count complete types of **ordered distinct** pairs \((x,y)\) outside the parameter set, with every parameter individually fixed.

Write \(C_n\) for the number with \(x<y\), \(I_n\) for the number with \(x\parallel y\), and \(T_n=2C_n+I_n\) for all ordered injective pair types. Put \(R_n=2^n+n-1\). Then the following all-size formulas hold:

\[
\boxed{\begin{aligned}
C_n={}&3\cdot6^n+4n3^{n-1}+(n-2)2^n+2n+R_n^2,\\
I_n={}&9^n+4(5^n-3^n+2n3^{n-1})+2R_n^2+2n,\\
T_n={}&2C_n+I_n.
\end{aligned}}
\]

Consequently, under the uniform distribution on these **logical pair types**, comparability has the sharp asymptotic
\[
\boxed{\frac{2C_n}{T_n}\sim 6\left(\frac23\right)^n\qquad(n\to\infty).}
\]
The three orientations are counted separately, so the probability of \(x<y\) is half the displayed fraction. The result contrasts with the complete height-two parameter order, where the corresponding balanced-base comparability fraction has exponential base \(9/16\) and leading factor \(2\), as established in the cited comparison. These are counts of types, not probabilities over sampled points of the countable structure.

## Assumptions and scope
The language contains a strict partial order. The ambient structure is the Fraïssé limit of finite partial orders. Its finite-extension property realizes every finite labelled partial-order diagram consistent with the named base, and ultrahomogeneity identifies every such diagram with exactly one complete tuple type. The tuple entries are different from one another and from the named parameters. Algebraic types, parameter permutations, and coordinate identifications are excluded.

For one new point \(z\), write \(L_z=\{p:p<z\}\), \(U_z=\{p:z<p\}\). The admissible pairs are precisely those with \(L_z\) a downset, \(U_z\) an upset, and \(l<u\) for each \(l\in L_z,u\in U_z\). This standard ideal/filter characterization is prior background, not part of the novelty claim.

## Proof
**1. Complete classification of one-point patterns.** Each admissible \((L,U)\) on \(S_n\) belongs to exactly one of three disjoint families:

* **Core \(K\):** \(L\subseteq\{a_i\}\), \(U\subseteq\{b_i\}\), with no index occurring in both \(L\) and \(U\). At each index the possibilities are neither, lower, or upper. Hence \(|K|=3^n\).
* **Lower-heavy \(D\):** \(U=\varnothing\) and either \(L=\{a_i:1\le i\le n\}\cup S\) for a nonempty \(S\subseteq\{b_i\}\), or \(L=(\{a_i\}\setminus\{a_j\})\cup\{b_j\}\) for a unique \(j\). Thus \(|D|=(2^n-1)+n=R_n\).
* **Upper-heavy \(E\):** the order-dual of \(D\), with \(L=\varnothing\) and \(|E|=R_n\).

Indeed, if a downset contains two distinct upper-level elements, it contains all lower-level elements; if it contains only \(b_j\) on the upper level, it contains all lower elements except possibly \(a_j\). A downset containing any maximal point cannot coexist with a nonempty upper set on a strict cross-comparable one-point pattern; the dual holds for an upset containing a minimum. If no such point occurs, the core description and its three independent choices per index are forced. Consequently the known one-point type total is \(3^n+2R_n\).

**2. Compatibility for increasing pairs.** For admissible one-point patterns, adjoining \(x<y\) gives a partial order precisely when \(L_x\subseteq L_y\) and \(U_y\subseteq U_x\). Necessity is transitivity; sufficiency follows by checking the only new two-step paths involving the tuple points. The possible family combinations and their counts are

| Family of \(x\) and \(y\) | Count |
|---|---:|
| \(K,K\) | \(6^n\) |
| \(K,D\) and \(E,K\), each | \(6^n-3^n+2n3^{n-1}\) |
| \(D,D\) and \(E,E\), each | \(3^n-2^n+n2^{n-1}+n\) |
| \(E,D\) | \(R_n^2\) |

All other combinations are impossible. The \(K,K\) count has six allowed ordered local pairs per index. In \(K,D\), the ordinary \(D\) supports contribute \((2^n-1)3^n\), and the \(n\) exceptional supports contribute \(2n3^{n-1}\). For \(D,D\), nonempty included pairs of upper subsets contribute \(3^n-2^n\), exceptional-to-ordinary inclusions contribute \(n2^{n-1}\), and each exception includes itself, contributing \(n\). Finally every \(E\) pattern precedes every \(D\) pattern by inclusion of their empty lower and upper sets. Summing the six displayed family contributions and simplifying establishes the formula for \(C_n\). Reversing the coordinates shows there are equally many types with \(y<x\).

**3. Compatibility for incomparable pairs.** Adjoining \(x\parallel y\) is valid precisely when
\[
U_x\cap L_y=\varnothing\quad\text{and}\quad U_y\cap L_x=\varnothing.
\]
Otherwise one of the tuple points is forced below the other through a named intermediary. The intersections being empty, there are no other new transitivity constraints. The disjoint family contributions are

| Family combination | Count |
|---|---:|
| \(K,K\) | \(9^n\) |
| \(K,D\), \(D,K\), \(K,E\), \(E,K\), each | \(5^n-3^n+2n3^{n-1}\) |
| \(D,D\), \(E,E\), each | \(R_n^2\) |
| \(D,E\), \(E,D\), each | \(n\) |

For example, when the nonempty upper subset \(S\) of an ordinary \(D\) pattern is selected, a core pattern cannot put its upper status on any index in \(S\), giving \(2^{|S|}3^{n-|S|}\) choices. Summation over nonempty \(S\) yields \(5^n-3^n\); the \(n\) exceptional \(D\) patterns each allow \(2\cdot3^{n-1}\). The remaining mixed counts follow by order duality and coordinate exchange. In the cross-family \(D,E\) case, the only compatible pairs are the two exceptional patterns carrying the same missing-comparability index, giving exactly \(n\). Summing proves the formula for \(I_n\).

**4. Sharp large-base probability.** Since \(R_n=O(2^n+n)\), the formulas give \(C_n=3\cdot6^n+O(4^n+n3^n)\) and \(I_n=9^n+O(5^n+n3^n+4^n)\). Therefore \(T_n\sim9^n\), and dividing \(2C_n\) by \(T_n\) proves the stated \(6(2/3)^n\) asymptotic. The error estimates apply to integer \(n\to\infty\); no uniformity in changing parameter families is claimed.

## Verification
The standalone standard-library program `check.py` independently enumerates all ternary one-point relation words on the named base and tests downset, upset and strict cross-comparability conditions, then counts allowed pairs using the separate increasing/incomparable compatibility predicates. It confirms both complete formulas for \(n=2,3,4,5\). For \(n=2,3\), it also independently constructs every augmented finite order diagram for each pair pattern and relation, computes transitive closure, and checks that the original relation profile is unchanged. Its recorded output is in `verification_output.txt`. These finite checks corroborate the above general combinatorial proof; they are not its substitute. Reproduce with `python3 check.py` without dependencies.

## Relationship to prior work
The generic homogeneous-poset finite-extension principle and its standard one-point ideal/filter encoding are established background, as in Hubička's 2010 treatment and Dolinka–Mašulović's one-point-extension framework. Exact one-point enumeration for matching-deletion height-two bases, including \(3^n+2^{n+1}+2n-2\), has already been obtained and is not a claimed contribution here. At \(n=2\), the standard example is the disjoint union of two two-element chains, also a covered special case of earlier disjoint-chain ordered-pair enumeration; the novelty claim concerns the uniform all-size standard-example formulas and the unbounded-\(n\) rare-event asymptotic.

The closest published ordered-pair spectrum is the complete height-two calculation for two fully comparable antichain levels. Its theorem explicitly assumes **every** cross-level comparability; the present standard-example base deletes one diagonal matching of comparabilities and has a different exact count and comparability decay base. Published antichain-parameter pair counts concern a base with **no** cross-level comparabilities. The five-statistic convex-set polynomial of the standard-example poset studies subsets of the base, not one- or two-point extension diagrams. Neither of those statements implies the displayed formulas. Full available text of the relevant mathematical statements was inspected; no equivalent published formula was identified in the sources checked. An inaccessible or unindexed independent derivation remains possible.

## Limitations
The result is restricted to the standard-example parameter family and injective, individually named ordered pair types. It does not count pairs with repetitions, or provide analogous formulas for every bipartite parameter poset. Uniformity refers to the finite set of logical types, not to points chosen randomly in the countably infinite structure. The independent audit of the theorem and its historical priority have not been performed.

## References
1. J. Hubička, *Combinatorial Properties of Finite Models*, arXiv:1009.0566v1, first publicly posted September 3, 2010, especially Section 3.1 on the generic partial order. https://arxiv.org/abs/1009.0566
2. I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892 (2010), on ideal/filter one-point extension data. https://arxiv.org/abs/1009.2892
3. *Exact ordered-pair type spectrum over complete height-two parameter posets*, published mathematical record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-exact-ordered-pair-type-spectrum-over-complete-height-two-parame--8b01eae861b0/RESULT.md
4. *Exact two-point and fixed-arity type spectra over antichains in the random poset*, published mathematical record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-exact-two-point-and-fixed-arity-type-spectra-over-antichains-in--3d742ffe8f7d/RESULT.md
5. *Five-statistic convex-set polynomial and defect localization for standard-example posets*, published mathematical record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-five-statistic-convex-set-polynomial-and-defect-localization-for--84ba1197a0d2/RESULT.md
