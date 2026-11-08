# Twenty-one rank-three theories of finite rectangular grid posets

## Finding

Let \(G_{a,b}\) be the finite product-order poset on \([a]\times[b]\), with \(1\leq a\leq b\). For finite relational structures write \(P\equiv_3 Q\) when they satisfy exactly the same first-order sentences of quantifier rank at most three in the pure vocabulary \(\{\leq\}\) with equality.

**Theorem.** Exactly **21** distinct \(\equiv_3\)-classes occur among all nonempty finite rectangular grid posets. They are classified completely by the following disjoint parameter cases:

| Smaller side \(a\) | Distinct classes, indexed by \(b\) | Count |
| --- | --- | ---: |
| \(a=1\) | \(b=1,2,3,4,5,6\), or \(b\geq7\) | 7 |
| \(a=2\) | \(b=2,3,4,5\), or \(b\geq6\) | 5 |
| \(a=3\) | \(b=3,4,5\), or \(b\geq6\) | 4 |
| \(a=4\) | \(b=4,5\), or \(b\geq6\) | 3 |
| \(a\geq5\) | \((a,b)=(5,5)\), or \(b\geq6\) | 2 |

Consequently, among rectangular grid posets the terminal class has the unique smallest representative
\[
G_{5,6},\qquad |G_{5,6}|=30,
\]
and contains every \(G_{a,b}\) with \(5\leq a\leq b\) and \(b\geq6\). In contrast \(G_{5,5}\not\equiv_3 G_{5,6}\), so the sharp boundary occurs between 25 and 30 points within this natural family.

## Assumptions and scope

Here \([n]=\{0,\ldots,n-1\}\) and
\[
(i,j)\leq_{\mathrm{prod}}(i',j')
\quad\Longleftrightarrow\quad i\leq i'\text{ and }j\leq j'.
\]
Only the binary order symbol and logical equality are available; no named least/greatest elements, coordinate predicates, lattice operations, counting quantifiers, or second-order quantifiers are part of the language. Side lengths are strictly positive. Coordinate exchange allows the normalization \(a\leq b\). Rank-three equivalence does not assert isomorphism or complete elementary equivalence.

## Proof

**1. Factorwise finite reduction.** The standard three-move Ehrenfeucht–Fraïssé interval strategy on finite linear orders shows that any two chains with at least seven points are \(\equiv_3\)-equivalent. More generally, for \(r\) remaining moves, Duplicator maintains that corresponding open intervals between selected points have either equal size below \(2^r-1\) or both sizes at least \(2^r-1\). When Spoiler chooses a point in a large interval, the reply can preserve whichever new subinterval is small, or make both new subintervals large, because \(2^r-1=2(2^{r-1}-1)+1\). The base \(r=0\) preserves all selected pair comparisons. Therefore every finite chain \([n]\) is \(\equiv_3\)-equivalent to \([\min(n,7)]\).

Run two such chain strategies simultaneously when Spoiler plays a grid point. Answer with the ordered pair of the two coordinate responses. Since order of points in a product is exactly the conjunction of the coordinate comparisons, and equality is likewise conjunction of coordinate equalities, the resulting pairing is a partial isomorphism after three moves. This proves
\[
G_{a,b}\equiv_3G_{\min(a,7),\min(b,7)}
\]
for every pair of positive integers. It suffices to distinguish the 28 pairs \(1\leq a\leq b\leq7\).

**2. An exact signature for the remaining finite cases.** For two points define their comparison label \(R(x,y)\) to be 0 when equal, 1 when strictly below, 2 when strictly above, and 3 when incomparable. The complete atomic type of an ordered triple is the three-label vector
\[
A(x,y,z)=\bigl(R(x,y),R(x,z),R(y,z)\bigr).
\]
Define
\[
U(x,y)=\left(R(x,y),\,\{A(x,y,z):z\in G\}\right),
\quad V(x)=\{U(x,y):y\in G\},
\quad \Sigma_3(G)=\{V(x):x\in G\}.
\]
The full atomic types of one and two points are automatically determined by these labels. The usual back-and-forth induction shows:
\[
G\equiv_3H\quad\Longleftrightarrow\quad
\Sigma_3(G)=\Sigma_3(H).
\]
For clarity, the induction starts with the equivalence of atomic types after no moves; one further move requires equality of the sets of possible descendant types on both sides. Repeating this operation twice for the selected first point and once at the empty tuple gives precisely the nested sets defining \(\Sigma_3\). Conversely, every missing descendant type can be expressed by a distinguishing formula using one more existential quantifier (or its negation), so unequal signatures give a first-order sentence of rank at most three.

**3. Finite exact certificate.** The standalone `checker.py` constructs all 28 order matrices and computes every \(\Sigma_3(G_{a,b})\) using integer comparison labels and finite sets. It compares all \(28^2=784\) ordered pairs of signatures against the claimed piecewise classification. The output contains precisely 21 distinct signatures, with the terminal class represented among bounded cases by
\[
(5,6),(5,7),(6,6),(6,7),(7,7)
\]
and \((5,5)\) in its own class. As a separate computation, an explicit recursive Spoiler/Duplicator minimax implementation checks 55 unordered pairs (with repetition) among the ten grids with \(1\leq a\leq b\leq4\); its results agree exactly with the atomic-type signature method. All computations use exhaustive finite iteration, not random sampling or numerical approximation.

The factorwise reduction of Step 1 and the complete, independently rerunnable finite signature certificate of Steps 2–3 establish the claimed classification for *all* finite side lengths. Within the terminal class the least possible side lengths are 5 and 6, so its minimum cardinality is exactly 30 and is attained uniquely, up to product-grid isomorphism, by \(G_{5,6}\).

## Verification

Extract `checker.py` from this package and run `python3 checker.py` using a standard Python 3 interpreter. Expected terminal message:

`GRID_RANK3_CERTIFICATE_OK cases=28 classes=21 pair_checks=784 direct_games=55 terminal_minimum=30`

The certificate enumerates only 28 grids, but Step 1 rigorously reduces every remaining grid to one of them. The independent direct-game comparisons are a cross-check, not the sole correctness argument. No external proof assistant or independent expert audit has been performed.

## Relationship to prior work

Kurilić's 2026 paper establishes deep **full elementary-theory** structure for finite products of chains, including factorwise characterizations and definability of the classes of products. The inspected complete arXiv HTML text, particularly Theorem 1.1 and its introductory and concluding remarks, does not state this bounded rank-three 21-class calculation or the sharp 30-point representative. The implication from factorwise equivalence is related to the easy reduction in Step 1; it does not settle the exact identification of the 28 bounded cases.

Sankaran's 2016 dissertation treats first-order equivalent bounded substructures for products and explicitly discusses two-dimensional grid posets in Chapters 10–11. That provides general background but not the precise rank-three class partition here. Mwesigye and Truss's work on three-move equivalence of *coloured linear orders* offers a related finite-model-theoretic framework for the factors, but does not classify product-order grids.

## Limitations

This is a classification **within the family of finite rectangular products of two finite chains** in the pure order vocabulary. The 30-point minimality assertion is *not* a minimum over all finite partial orders or all finite distributive lattices of the same rank-three theory. Higher quantifier ranks, products of three or more factors, and expansions of the signature are outside the theorem. Source priority is assessed relative to the literature actually inspected; undiscovered equivalent earlier work remains a historical-priority risk. The finite computation is covered by a transparent exhaustive certificate, not an independent formal proof.

## References

1. Miloš S. Kurilić, *Model Theory of Products of Chains*, arXiv:2610.24683, publicly posted 17 October 2026. https://arxiv.org/abs/2610.24683.
2. Abhisekh Sankaran, *A Generalization of the Łoś–Tarski Preservation Theorem*, doctoral dissertation, IIT Bombay, 2016, especially Chapters 10–11. https://abhisekhs.github.io/Papers/abhisekh-dissertation.pdf.
3. F. Mwesigye and J. K. Truss, *On Optimal Representatives of Finite Coloured Linear Orders*, *Order* 36 (2019), 107–117; published online 2 May 2018. https://doi.org/10.1007/s11083-018-9458-3.
