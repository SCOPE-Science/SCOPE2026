# Rigid coloured actions of finite Dedekind groups as full-shift substructures

## Finding

Let \(G\) be a **finite Dedekind group**: every subgroup of \(G\) is normal. In particular, every finite abelian group is permitted, as are nonabelian Dedekind groups. Let \(q\ge1\) be an integer. A coloured \(G\)-set is a finite left \(G\)-set \(X\) equipped with one of \(q\) named, mutually exclusive colours at every point; individual colour classes may be empty. An automorphism is a colour-preserving \(G\)-equivariant bijection, with the elements of \(G\) individually named and not allowed to be permuted.

Let \(\mathcal W=[q]^G\) be the set of all \(q\)-colour words on \(G\), acted upon by right shifts \((a\cdot w)(g)=w(ga)\), and colour each word by its value \(w(e)\) at the group identity. For any coloured \(G\)-set define its **orbit-profile map**
\[
\Phi_X(x)(g)=\kappa(gx),\qquad x\in X,\ g\in G.
\]

**Canonical rigidity theorem.** A finite coloured \(G\)-set is rigid (has only the identity automorphism) **if and only if** \(\Phi_X\) is injective. Every rigid isomorphism type is therefore represented by a **unique** \(G\)-invariant subset of \(\mathcal W\), with the inherited action and evaluation colouring; conversely every invariant subset is rigid.

Write \(r_{G,q}(n)\) for the number of rigid isomorphism classes of size \(n\), with the empty structure included at \(n=0\). Then the exact polynomial is
\[
\boxed{R_{G,q}(z)=\sum_{n\ge0}r_{G,q}(n)z^n
=\prod_{\mathcal O\in\mathcal W/G}(1+z^{|\mathcal O|}).}
\]
There is exactly one maximum-size rigid type and its order is
\[
\boxed{\max\{|X|:\operatorname{Aut}_G(X,\kappa)=1\}=q^{|G|}.}
\]
No larger rigid model exists. The coefficients are palindromic, and the number of labelled rigid models on a prescribed \(n\)-element set is \(n!r_{G,q}(n)\).

There is also a formula in terms of the **subgroup-lattice Möbius function** \(\mu\). For \(H\le G\), put
\[
M_H(q)=\sum_{K\ge H}\mu(H,K)q^{[G:K]}.
\]
Then \(M_H(q)\) counts the words with right-shift stabilizer exactly \(H\), is divisible by \([G:H]\), and
\[
\boxed{R_{G,q}(z)=\prod_{H\le G}
 (1+z^{[G:H]})^{M_H(q)/[G:H]}.}
\]
This gives all rigid-size strata and all isomorphism counts, not just the extremal order.

For example, with two colours and groups of order four,
\[
R_{C_4,2}(z)=(1+z)^2(1+z^2)(1+z^4)^3,
\]
while
\[
R_{C_2\times C_2,2}(z)=(1+z)^2(1+z^2)^3(1+z^4)^2.
\]
Both have maximum order sixteen, but the respective numbers of two-point rigid types are **two** and **four**. More generally, if \(t_2(G)\) is the number of index-two subgroups, then
\[
r_{G,q}(2)=(1+t_2(G))\binom q2.
\]
For a cyclic group of prime order \(p\), the complete rigid-size spectrum is the support of
\[
(1+z)^q(1+z^p)^{(q^p-q)/p},
\]
so missing intermediate sizes can occur: for \(q=2,p=5\), no rigid model has three or four vertices although models attain the maximum thirty-two.

The normal-subgroup hypothesis cannot simply be omitted. With one colour, the nonabelian group \(S_3\) has a rigid four-point set: its natural three-point action together with one fixed point. But its one-colour full shift has only one point.

## Assumptions and scope

All actions are finite, total and not necessarily faithful; the acting group \(G\) is fixed and finite, with every subgroup normal. The language can equivalently use a named unary permutation for each group element, constrained by the group multiplication equations, plus \(q\) exclusive exhaustive unary colour predicates. Isomorphisms commute with all named group actions. The empty coloured set is only needed for the constant term of the counting polynomial; the maximum theorem applies equally if empty objects are excluded. The full shift has \(q^{|G|}\) elements. Its action by right shifts is a left action, since \(a\cdot(b\cdot w)=(ab)\cdot w\).

A group element \(h\) is a right period of \(w\) when \(w(gh)=w(g)\) for all \(g\in G\). The right periods form the stabilizer subgroup of \(w\) under the displayed action. \(\mu(H,K)\) is defined by \(\mu(H,H)=1\) and \(\sum_{H\le L\le K}\mu(H,L)=0\) for \(H<K\). All exponent expressions are nonnegative integers, proved by their orbit interpretation. "Rigid" means a trivial **full structure automorphism group**, not an absence of nonidentity elements of the acting group fixing individual points.

## Proof

**1. The profile is equivariant, and injectivity suffices for rigidity.** For every \(a,g\in G\),
\[
\Phi_X(ax)(g)=\kappa(gax)=(a\cdot\Phi_X(x))(g).
\]
Any automorphism \(u\) commuting with the \(G\)-action and preserving colours satisfies \(\Phi_X(u(x))=\Phi_X(x)\). Thus an injective profile forces \(u(x)=x\) for every \(x\). This implication does not need the Dedekind condition.

**2. Rigidity forces every orbit to have maximal colour information.** Let \(x\in X\). Its point stabilizer \(H_x\) is normal by hypothesis. The profile \(w=\Phi_X(x)\) has a right-period subgroup \(K_w\) containing \(H_x\), because \(h x=x\) implies \(w(gh)=w(g)\). Suppose \(b\in K_w\setminus H_x\). On the orbit \(Gx\), define
\[
u_b(gx)=gbx.
\]
The map is well defined: if \(gx=g'hx\) for some \(h\in H_x\), normality of \(H_x\) gives \(h b x=b x\). It is a bijective \(G\)-map, and it is colour-preserving because \(w(gb)=w(g)\). It moves \(x\) to \(bx\ne x\). Extending it by the identity on all other orbits gives a nontrivial full automorphism. Consequently a rigid coloured \(G\)-set must satisfy
\[
H_x=K_{\Phi_X(x)}\qquad\text{for every }x\in X.
\]

**3. Profiles cannot coincide in a rigid structure.** Suppose \(\Phi_X(x)=\Phi_X(y)\). The last equality yields \(H_x=H_y\). If \(x,y\) belong to the same orbit, write \(y=bx\); then \(b\) fixes the common profile. Hence \(b\in K_{\Phi_X(x)}=H_x\) and \(y=x\). If they belong to different orbits, the map \(gx\mapsto gy\) is a well-defined equivariant, colour-preserving bijection of the two orbits: well-definedness follows from \(H_x=H_y\), and colour preservation from equality of profiles. Swapping these two orbits, while fixing every other orbit, is a nontrivial full automorphism. This contradicts rigidity. The profile is injective.

**4. Every invariant subset of the shift is canonically rigid.** Let \(S\subseteq\mathcal W\) be invariant and colour it by evaluation at \(e\). Its own profile map is the identity:
\[
\Phi_S(w)(g)=\operatorname{ev}_e(g\cdot w)=(g\cdot w)(e)=w(g).
\]
Step 1 makes \(S\) rigid. Conversely Steps 1–3 identify any rigid \(X\) canonically with the invariant subset \(\Phi_X(X)\). If two rigid structures are isomorphic, their image subsets coincide because the profile is preserved by every coloured equivariant isomorphism. This proves both existence and uniqueness of the subset representative.

**5. Enumerate invariant subsets and prove the capacity.** Any invariant subset of the full shift is uniquely the union of a selected subcollection of its \(G\)-orbits. Every orbit \(\mathcal O\) can be selected once or not at all and contributes \(|\mathcal O|\) points, yielding the first product. Selecting **all** the shift orbits produces the unique top-degree type, of total cardinality \(|\mathcal W|=q^{|G|}\); no larger invariant subset exists. Complementing the selected orbit subcollection reverses degree about the total size, proving palindromicity. Since rigid objects have exactly \(n!\) labelled presentations on \([n]\), their labelled count is as stated.

**6. Subgroup Möbius inversion.** For every \(H\le G\), the number of words fixed by all right shifts in \(H\) is \(q^{[G:H]}\), one independent colour choice per right coset. If \(M_K(q)\) counts words with exact stabilizer \(K\), then
\[
q^{[G:H]}=\sum_{K\ge H}M_K(q).
\]
Möbius inversion gives the displayed formula for \(M_H(q)\). The group is Dedekind, so an orbit with stabilizer \(H\) has \([G:H]\) words and every point on that orbit has stabilizer \(H\). Therefore \(M_H(q)/[G:H]\) is precisely the number of orbits of that stabilizer type, proving the second product.

**7. Sharp distinctions and limits of generalization.** The only one-point shift orbits are the \(q\) constant words. A two-point shift orbit has an index-two stabilizer. For each such subgroup, there are \(q^2-q\) words with exact stabilizer, yielding \(\binom q2\) orbits. To make a two-point invariant subset, select either two distinct one-point orbits or one two-point orbit; thus the displayed index-two formula. The group-specific products follow by counting period-one, period-two and period-four words, or directly from subgroup inversion. For \(G=C_p\), nonconstant words form orbits of size \(p\), yielding the prime cyclic specialization.

Finally, in the action of \(S_3\) on three points, the equivariant automorphism group is the centralizer of the full symmetric permutation group on three points, hence trivial. The disjoint additional fixed point cannot be exchanged with any point in the three-orbit. This gives the promised non-Dedekind counterexample for a one-colour shift of size one.

## Verification

Run `python3 checker.py` using the Python 3 standard library. Three separate enumerations compare orbit-count multiplicities: direct translation orbits of all words; subgroup-lattice Möbius inversion; and independent enumeration of primitive colour patterns on the transitive quotients. They agree for \(C_2,C_3,C_4,C_6,C_2\times C_2,C_2\times C_3\), with two or three colours, and for the nonabelian Dedekind group \(Q_8\) with two colours. The code also independently constructs all finite actions on at most four points for five chosen generator/colour cases, applies every possible relabelling, tests actual automorphisms and compares the resulting rigid isomorphism counts to the polynomial. Both four-point order-four group examples and the \(S_3\) non-Dedekind counterexample are tested. The run ends with `ALL_CHECKS_OK`.

These finite checks are corroborative. The equivalence, Möbius formula, exact capacity and all-parameter claims follow from Steps 1–7, not from the enumerated group sizes.

## Relationship to prior work

The full shift and the canonical equivariant profile map are instances of the classical **cofree \(G\)-set** construction, examined explicitly by Murphy-Hernandez [2]. That prior paper proves the cofree adjunction, fixed-word characterizations and Burnside orbit counts; neither the existence of the cofree functor nor its uncoloured orbit counts is asserted here as novel. Kuželka [1] motivates exact labelled/unlabelled model counting with genuine unary operations and automorphism marking. A published result [3] classifies automorphism groups of coloured *single permutations* through primitive necklaces and gives their random limit law; its cited 2016 Lyndon work [4] already supplies a related cyclic-word enumeration, and the classical cyclic case is not claimed independent of this literature. The current result differs in its universal full-shift characterization for **every finite Dedekind action**, the structure-independent sharp bound \(q^{|G|}\), and the subgroup-sensitive rigid polynomial, which distinguishes \(C_4\) from \(C_2\times C_2\) even though their orders agree.

The published commuting-involution classification [5] gives the uncoloured subgroup normal form and two-variable counting theory, not the stated coloured rigidity characterization and sharp full-shift census. The coloured idempotent-unary rigidity theorem [6] is a distinct rooted-star class with another capacity. The general colour-asymmetry literature [7] investigates stabilizers of a fixed group action under colouring; here the **entire coloured action** can vary and its full automorphism group, including orbit exchanges, must be trivial. These comparisons do not establish universal historical novelty; the subgroup-lattice and full-shift ingredients are classical tools.

## Limitations

The cofree-group-action construction and elementary subgroup counting are prior mathematical inputs, not new stand-alone claims. The exact equivalence relies on all point stabilizers being normal, ensured by the Dedekind hypothesis. It is false for arbitrary nonabelian groups, as the \(S_3\) example shows; no classification for all groups is claimed. Colours are named and mutually exclusive, group elements are named, and the action is finite. The generating polynomials count isomorphism classes, not arbitrary labelled homomorphisms without accounting for symmetries. The available primary source material and database comparisons do not establish universal priority; generalized necklace identities or cofree-action literature could contain equivalent formulations. No independent mathematical validation has been conducted.

## References

[1] O. Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580, first submitted 2026-08-31. https://arxiv.org/abs/2608.30580

[2] F. Murphy-Hernandez, *The Cofree Functor on G-Sets and Its Approximations*, arXiv:2608.23866v1, first submitted 2026-08-24. https://arxiv.org/abs/2608.23866

[3] *A finite-group limit law for coloured unary permutations*, published mathematical note, 2026-11-02. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-finite-group-limit-law-for-coloured-unary-permutations--a14c729a8c1b/RESULT.md

[4] R. Band, J. M. Harrison and M. Sepanski, *Lyndon word decompositions and pseudo orbits on q-nary graphs*, arXiv:1610.03808, first submitted 2016-10-12. https://arxiv.org/abs/1610.03808

[5] *Stirling–Gaussian enumeration of counting types for commuting involutions*, published mathematical note, 2026-10-18. https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-stirling-gaussian-enumeration-of-counting-types-for-commuting-in--83c7d95173f7/RESULT.md

[6] *Sharp rigidity capacity and exact census of coloured idempotent unary models*, published mathematical note, 2026-11-02. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-sharp-rigidity-capacity-and-exact-census-of-coloured-idempotent--4d19fd7927e8/RESULT.md

[7] *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society, https://doi.org/10.1112/blms.70201
