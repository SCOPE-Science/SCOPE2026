# Sharp \(n+2\)-variable saturation and its first failure for Latin hypercubes

## Finding

For every integer \(n\ge 2\), let \(\mathcal L(Q)\) denote the \((n+1)\)-sorted relational structure of a finite \(n\)-ary quasigroup \(Q\) of order \(q\ge1\). Its sorts \(S_0,\ldots,S_n\) have \(q\) elements each. The sole non-unary relation \(R\) has arity \(n+1\) and records \(R(y,x_1,\ldots,x_n)\) precisely when \(y=Q(x_1,\ldots,x_n)\). The sorts are named, equality is available, and no coordinate identifications, operation symbols, constants, or counting quantifiers are present.

**Theorem (saturation, exact classification, and sharpness).** For every \(1\le k\le n+2\), and every pair \(Q,Q'\) of finite \(n\)-ary quasigroups of orders \(q,r\ge1\), respectively,

\[
\mathcal L(Q)\equiv_{\mathrm{FO}^k}\mathcal L(Q')
\quad\Longleftrightarrow\quad
\begin{cases}
\text{always},&k=1,\\
\min(q,k)=\min(r,k),&2\le k\le n+2.
\end{cases}
\]

Equivalence refers to all first-order sentences with at most \(k\) reusable variable names, at *unrestricted* quantifier depth. Hence there are exactly \(k\) different theories in this family for each \(2\le k\le n+2\), represented by orders \(1,\ldots,k-1\) and by the common class of all orders at least \(k\). The threshold \(n+2\) is the highest variable width for which such a universal order-truncation classification holds for all \(n\)-ary quasigroups: for every \(n\ge2\), some two additive \(n\)-ary quasigroups of orders both at least \(n+3\) are distinguishable in \(\mathrm{FO}^{n+3}\).

For binary quasigroups (Latin squares), this means that all squares of orders at least four, including non-isotopic squares of equal order, share exactly the same four-variable theory. For example, the order-four addition tables of the cyclic group and the Klein four-group are equivalent in this sorted four-variable relational language, although they have respectively four and twelve \(2\times2\) intercalates.

## Assumptions and scope

A finite \(n\)-ary quasigroup is a nonempty finite array \(Q:A_1\times\cdots\times A_n\to A_0\), with all coordinate sets of the same cardinality, whose defining equation is uniquely solvable in *each* coordinate when the other \(n\) coordinates are fixed. We use **disjoint copies** of the \(n+1\) sets as sorts, even if the underlying operation was given on one common set. The \(n+1\) sort predicates are part of the signature. The theorem concerns finite models of this precise signature; changing to a single-sorted operation language permits nested terms and changes logical width. An \(n\)-ary quasigroup exists at every positive order, for instance addition modulo that order.

## Proof

**1. Finite-variable back-and-forth.** Fix \(k\le n+2\). In the ordinary \(k\)-pebble game, maintain the invariant that the positions of all occupied pebbles have the same atomic diagram: the same equality partition, the same named sorts, and the same truth values of all \(R\)-atoms. At a move, at most \(k-1\le n+1\) pebbles stay fixed. Suppose a new element is chosen in sort \(S_i\).

The prescribed \(R\)-facts involving this new element are determined by completion requests: one selected fixed element from each of the other \(n\) sorts specifies **exactly one** element of sort \(S_i\). There are at most two such requests. Indeed, with at most \(n+1\) fixed elements, either not all other sorts occur; all occur exactly once; or one other sort occurs twice and every remaining other sort once. In the last case the two forced completions are *distinct*, since otherwise two tuples agreeing in all but the duplicated coordinate would contradict the quasigroup property.

There are three mutually exclusive possibilities for the chosen new element: (a) it coincides with a fixed element of its sort; (b) it equals one of the at most two forced completions not already fixed; or (c) it is distinct from all fixed elements of its sort and from all forced completions. In case (a), the required relations are determined by the fixed atomic diagram. In case (b), if a forced completion also coincides with a fixed element, this is likewise exactly an already recorded \(R\)-atom. When two completions occur, **no** fixed element of the candidate sort can occur, because the full \(n+1\)-element stationary allowance has already been used in the other sorts. Therefore all equality and completion categories, with their necessary distinctness, match between structures whose fixed diagrams match. In case (c), a generic element exists in both structures whenever their orders are equal; and it also exists in both whenever both orders are at least \(k\), since at most \(k-1\) elements of the candidate sort can be excluded. The latter bound is immediate if no completion is required, and is at most two if completions are required (a completion and possibly one fixed candidate, or two completions and no fixed candidate).

Thus all atomic extension types are identical across equal orders, or across orders both at least \(k\). Duplicator chooses a corresponding category, preserving the atomic invariant indefinitely. The same argument works if some of the stationary pebbles are unoccupied, and works in either direction. The permanent \(k\)-pebble strategy proves the claimed \(\mathrm{FO}^k\) equivalences for \(2\le k\le n+2\). With one variable, the higher-arity relation has no true atom because the sorts are disjoint, and every sort is nonempty, so all structures agree in \(\mathrm{FO}^1\).

**2. Distinguishing different truncated orders.** For every \(2\le t\le k\), a sentence with \(t\) reusable variables asserts that sort \(S_0\) contains at least \(t\) pairwise distinct elements. If \(\min(q,k)\ne\min(r,k)\), one such sentence separates the structures. Together with step 1 this gives the exact classification and the \(k\) classes.

**3. Optimality of the cutoff.** Let \(Q_s(x_1,\ldots,x_n)=x_1+\cdots+x_n\pmod s\) on the cyclic group of order \(s\). Consider the following *intercalate* sentence, with the quantifiers on the displayed elements restricted to their designated sorts. Choose distinct \(a,a'\in S_1\) and distinct \(b,b'\in S_2\), and choose \(t_j\in S_j\) for \(3\le j\le n\). Require both

\[
\exists z\in S_0\ [R(z,a,b,t_3,\ldots,t_n)\land R(z,a',b',t_3,\ldots,t_n)]
\]

and

\[
\exists z\in S_0\ [R(z,a,b',t_3,\ldots,t_n)\land R(z,a',b,t_3,\ldots,t_n)].
\]

The two occurrences of \(z\) use the *same* variable name in separately scoped existential quantifiers. Thus exactly \(4+(n-2)+1=n+3\) variable names are needed; this is one ordinary first-order sentence. For cyclic addition, its two equalities imply \(a-a'=b'-b=b-b'\), hence \(2(a-a')=0\). Conversely a nonzero involution supplies a solution by choosing the two differences equal to it. The sentence therefore holds in \(\mathcal L(Q_s)\) exactly when \(s\) is even. Choosing any odd \(s\ge n+3\) and any even \(s'\ge n+3\) gives two structures in the same purported saturated order regime that the \((n+3)\)-variable sentence separates. This proves sharpness for **every** arity \(n\ge2\).

## Verification

The included standalone program `hypercube_check.py` enumerates **all** atomic extension catalogues from every ordered stationary tuple of length \(n+1\), in the named-sort union, for binary quasigroups of orders \(2,3,4,5,6\), comparing the cyclic and Klein structures at order four. It separately enumerates all stationary four-tuples for ternary quasigroups of order four, comparing cyclic addition and coordinatewise addition over the Klein group. Its direct results are 63 stationary triple types and 417 distinct extensions for each of the tested binary orders at least four, and 780 stationary quadruple types and 6144 extensions for each of the two ternary examples. All compared catalogues agree exactly. The checker also enumerates intercalates: four for cyclic order four, twelve for Klein order four, none for cyclic order five, and nine for cyclic order six. `hypercube_check_output.txt` records the reproducible output.

This computation is a finite cross-check of the local-case proof, **not** an exhaustive verification over all finite quasigroups, and it does not independently establish the unrestricted theorem.

## Relationship to prior work

The defining uniqueness of \(n\)-ary quasigroups, their relational predicate form, and isotopy are developed in Krotov and Potapov, *n-Ary quasigroups of order 4* (first posted 18 January 2007, arXiv:math/0701519), especially Definitions 2.1–2.3 and Theorem 3.1. Their theorem classifies reducibility or semilinearity at order four, not equivalence under bounded-variable logic. Grohe and Otto, *Pebble Games and Linear Equations* (2012), Sections 1–2 and 5, develop the finite-variable pebble-game framework and its general logical interpretation; they do not compute Latin-hypercube equivalence classes. Vagnozzi, *Variations on the theme of higher dimensional Weisfeiler–Leman algorithms* (2021 thesis), Section 4.5, interprets finite groups and their Latin-square **graphs** in first-order logic; the objects and conclusion there differ from the present named-coordinate-sort quasigroup structures and sharp variable-width bound. A related published mathematical research record on Latin-array inflations establishes a homotopy invariant, rather than the logical classification here.

A broader, currently unidentified theorem concerning finite partial Latin hypercubes, quasigroup isotopy, or pebble games might imply the result. The stated novelty is therefore a qualified claim about the explicit sharp classification, not a proof of absolute historical priority.

## Limitations

The order-truncation theorem is restricted to \(k\le n+2\), and the intercalate example only shows that uniform order-truncation fails at \(n+3\); it does **not** classify all \((n+3)\)-variable theories. No claim is made for counting quantifiers, an unsorted quasigroup multiplication relation on a single carrier, operation symbols, arbitrary partial quasigroups, or coordinate sorts without labels. The verification program covers finitely many examples only.

## References

1. D. S. Krotov and V. N. Potapov, *n-Ary quasigroups of order 4*, arXiv:math/0701519, first submitted 2007-01-18; *SIAM Journal on Discrete Mathematics* 23 (2009), 561–570. https://arxiv.org/abs/math/0701519
2. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, *Computer Science Logic* (2012), 289–304. DOI:10.4230/LIPIcs.CSL.2012.289. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2012.289
3. D. Vagnozzi, *Variations on the theme of higher dimensional Weisfeiler–Leman algorithms*, PhD thesis, University of Cambridge, 2021, Section 4.5. https://api.repository.cam.ac.uk/server/api/core/bitstreams/49f56a79-35ca-4eec-9c22-106e681d52cd/content
