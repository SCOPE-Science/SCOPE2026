# Minimal generators of the identity-preserving endomorphism monoid of a full transformation monoid

## Finding
For each integer \(n\ge5\), let \(\mathcal T_n\) be the monoid of all maps from an \(n\)-element set to itself and let \(\mathcal U_n=\operatorname{End}_{\mathrm{Mon}}(\mathcal T_n)\) be its monoid of composition-preserving **and identity-preserving** endomorphisms. Write \(p(n)\) for the number of partitions of \(n\), and put
\[
C(z)=\prod_{j\ge1}(1-z^j)^{-\lceil j/2\rceil},\qquad c_n=[z^n]C(z).
\]
Then the exact minimum size of a generating set of \(\mathcal U_n\) is
\[
\boxed{\operatorname{rank}(\mathcal U_n)=3+c_n-p(n)+\lfloor n/2\rfloor.}
\]
This is the usual semigroup generating rank (products of positive length); the displayed generating sets contain the identity as a product of group generators, so the answer also holds under the convention allowing an empty product. The values for \(n=5,6,7,8,9,10,11,12\) are \(10,16,25,41,67,109,175,280\), respectively.

The proof also classifies the necessary singular generators: there are \(c_n-p(n)\) distinct conjugacy types with a nonidentity involution parameter, and exactly \(\lfloor n/2\rfloor+1\) additional essential conjugacy types of retraction parameters.

## Assumptions and scope
All mappings are total mappings on the finite set \(\{1,\ldots,n\}\); the integer \(n\) is at least five. A monoid endomorphism fixes the identity transformation, whereas a semigroup endomorphism need not. The composition convention below is right action: \((\alpha\beta)(s)=\beta(\alpha(s))\). Automorphisms of \(\mathcal T_n\) are \(\psi_g(s)=g^{-1}sg\), with \(g\in S_n\). The classical Schein–Teclezghi classification, recalled in Gould–Grau–Johnson, is used as an established theorem and **is not** asserted as a new result.

For \(n\ge5\), every other monoid endomorphism is uniquely \(\phi_{t,e}\), where \(t\in S_n\) is an involution, \(e\in\mathcal T_n\) is an idempotent, and \(te=et=e\). Its values on \(\mathcal T_n\) are \(\mathrm{id}\) on even permutations, \(t\) on odd permutations, and \(e\) on nonpermutations. The requirement \(\phi_{t,e}(\mathrm{id})=\mathrm{id}\) in the general semigroup-endomorphism classification is precisely \(t^2=\mathrm{id}\). The one constant-identity endomorphism is \(c=\phi_{\mathrm{id},\mathrm{id}}\).

## Proof
**1. Conjugacy-orbit types.** From \(e^2=e\), the image \(R\) of \(e\) is fixed pointwise by \(e\). From \(et=te=e\), every member of \(R\) is fixed by \(t\) and each transposition of \(t\) has its two points in the same fiber of \(e\). Thus, for each root \(r\in R\), its fiber comprises \(r\), \(a_r\ge0\) additional fixed points of \(t\), and \(b_r\ge0\) transposition pairs of \(t\). Conversely, every such partition into rooted fibers constructs one permissible pair. Simultaneous conjugation by \(S_n\) discards all labels, leaving an unordered multiset of ordered pairs \((a_r,b_r)\), each of size \(1+a_r+2b_r\). There are exactly \(\lceil j/2\rceil\) such types of size \(j\). Hence the number of singular conjugacy orbits is \(c_n\), and the multivariate refinement is
\[
\prod_{a,b\ge0}(1-u z^{1+a+2b}v^b)^{-1}.
\]
For \(t=\mathrm{id}\), every \(b_r=0\); the orbits are then exactly the partitions of \(n\), numbering \(p(n)\). Consequently, precisely \(c_n-p(n)\) singular conjugacy orbits have \(t\ne\mathrm{id}\).

**2. Multiplication and indispensable nontrivial involutions.** Products of automorphisms follow the group law; an automorphism to the left of a singular endomorphism leaves the latter unchanged, while an automorphism to its right conjugates both \(t\) and \(e\). For singular endomorphisms \(\phi_{t,e}\), \(\phi_{u,f}\), if the left one is not \(c\), direct evaluation on even permutations, odd permutations, and nonpermutations gives
\[
\phi_{t,e}\phi_{u,f}=
\begin{cases}
\phi_{u,f},&t\text{ odd},\\
\phi_{\mathrm{id},f},&t\text{ even}.
\end{cases}
\]
The exceptional constant-identity map is a left zero: \(c\phi_{u,f}=c\). Therefore any product with a nontrivial involution parameter has the conjugacy type of the rightmost singular factor carrying that nontrivial parameter, up to subsequent unit conjugation. Every generating set must accordingly contain at least one representative from each of the \(c_n-p(n)\) such orbits.

**3. Indispensable identity-involution types.** A singular \(\phi_{\mathrm{id},e}\) can be obtained by collapsing a nontrivial involution from a preceding singular factor precisely when there exists a nonidentity involution \(t\) with \(te=et=e\). Such an involution exists if and only if some fiber of \(e\) has at least three elements: interchange any two nonroot members of that fiber. The converse holds because \(t\) must fix every root and permute the nonroot members within their respective fibers. Thus the essential \(t=\mathrm{id}\) types are exactly the retractions whose fibers all have size one or two. Their conjugacy types correspond to partitions into ones and twos, numbering \(\lfloor n/2\rfloor+1\). The multiplication rule shows that these orbits cannot be created from different singular orbits; each requires its own generator.

**4. Sharp construction.** Choose two automorphisms generating \(S_n\), one representative of every \(t\ne\mathrm{id}\) singular orbit, and one representative of each essential \(t=\mathrm{id}\) orbit. These elements generate all conjugates of the chosen singular representatives. For every other retraction \(e\), the preceding fiber criterion provides \(t\ne\mathrm{id}\) with \(te=et=e\); its singular orbit is among the chosen generators. Because \(n\ge5\), there is an even nonidentity involution consisting of two transpositions and at least one fixed point; a permissible singular map with this parameter is also among the generated orbits. Multiplication of that even-type map on the left of \(\phi_{t,e}\) produces \(\phi_{\mathrm{id},e}\). This generates every remaining singular endomorphism. The group of units requires at least two generators, because \(S_n\) is noncyclic, and two suffice. Adding the indispensable singular orbits yields the displayed sharp rank formula.

## Verification
The files `orbit_census.py`, `generator_closure.py`, and `direct_composition.py` are self-contained together and use only the Python standard library. Run them from the same directory in that order. The first directly enumerates the involutions and all compatible idempotents on up to six labeled points, obtains their complete conjugacy-orbit profiles, and compares each cell with both the weighted-multiset series and the independently derived labeled count
\[
\frac{n!}{2^s s!(n-2s)!}\binom{n-2s}{r}r^{n-s-r},
\]
where \(r\) is the number of roots and \(s\) the number of transpositions. The second constructs an explicit generating family, closes it under the multiplication rule, and obtains **all** \(511\) identity-preserving endomorphisms on five points from ten generators, and all \(3427\) on six points from sixteen generators. The third compares the abstract multiplication with genuine composition as maps on transformations, including the exceptional left zero and both involution parities; it passes direct checks on the five-point case. The series coefficients are also calculated exactly through \(n=12\). These finite checks are corroboration of, not replacements for, the proof valid for every \(n\ge5\).

## Relationship to prior work
Schein and Teclezghi (1998) describe **all semigroup endomorphisms** and enumerate labeled endomorphisms. Gould, Grau, and Johnson (arXiv 2023, §4) analyze the endomorphism monoid of all such semigroup maps and give a minimal-generator reduction. Their §8 explicitly distinguishes the identity-preserving endomorphism monoid and proposes studying it; it does not compute the present rank. A subsequent published enumeration of the full semigroup-endomorphism monoid gives a plane-partition formula for its minimal generator rank. Its ambient monoid includes nonidentity-preserving maps and its essential orbit analysis is different, so the rank of the identity-preserving submonoid is not obtained by replacing an argument in that full-monoid rank value. The weighted-partition orbit census and fiber-size-two essentiality criterion here supply that missing comparison. The classical orbit classification and integer-partition identities are credited; no novelty for those foundations is claimed.

## Limitations
The theorem is asserted only for \(n\ge5\); the degree-four exceptional semigroup-endomorphism family requires separate treatment. The quantity calculated is minimum generating-set size, not the number of minimal generating sets and not the cardinality of the endomorphism monoid. The weighted product is an exact coefficient formula rather than an elementary closed form or an asymptotic. The novelty comparison supports the specific identity-preserving rank theorem relative to the inspected literature and published records, not an exhaustive proof of publication priority; equivalent unindexed results remain possible.

## References
1. V. Gould, A. Grau, M. Johnson, *The structure of \(\operatorname{End}(\mathcal T_n)\)*, arXiv:2307.11596, first publicly posted 2023-07-21; especially §§2, 4 and 8. https://arxiv.org/abs/2307.11596
2. B. M. Schein, B. Teclezghi, *Endomorphisms of finite full transformation semigroups*, Proceedings of the American Mathematical Society 126 (1998), 2579–2587. https://doi.org/10.1090/S0002-9939-98-04764-9
3. *Plane partitions and exact generator ranks for endomorphism monoids of full transformation semigroups*, published 2026-10-25, `RESULT.md`, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-plane-partitions-and-exact-generator-ranks-for-endomorphism-mono--05f93685b217
