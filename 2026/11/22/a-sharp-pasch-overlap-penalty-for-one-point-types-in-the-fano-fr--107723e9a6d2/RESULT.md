# A sharp Pasch-overlap penalty for one-point types in the Fano-free homogeneous hypergraph

## Finding
Let \(\mathcal M\) be the countable homogeneous universal **Fano-free** symmetric, irreflexive \(3\)-uniform hypergraph: its age consists of finite hypergraphs with no (not necessarily induced) copy of the seven-line Fano plane. Let \(A\subset\mathcal M\) be any finite, pointwise named partial Steiner triple system (PSTS), meaning each old pair belongs to at most one old triple. Set \(n=|A|\), \(N=\binom n2\), and let \(t(A)\) be the number of nonalgebraic complete one-point types over the named base.

A **Pasch** is a six-point, four-triple subconfiguration isomorphic to the Fano plane with one point and its three incident triples deleted. Its **opposite matching** consists of the three disjoint old pairs that occur in no triple of the Pasch. Let \(\mathcal P(A)\) be the set of these opposite matchings for Pasches inside \(A\); this set has no repetitions for a PSTS.

**Theorem (sharp first and second obstruction penalties).** Every one-point type corresponds to a link \(X\subseteq\binom A2\), and exactly those links avoiding complete containment of every \(M\in\mathcal P(A)\) are realized. Consequently:

1. If \(\mathcal P(A)=\varnothing\), then \(t(A)=2^N\); conversely, equality to \(2^N\) forces \(A\) to be Pasch-free.
2. If \(|\mathcal P(A)|\ge1\), then \(t(A)\le (7/8)2^N\), with equality **if and only if** exactly one Pasch occurs.
3. If \(|\mathcal P(A)|\ge2\), then
   \[
   \boxed{t(A)\le\frac{25}{32}2^N.}
   \]
   Equality holds **if and only if** there are exactly two Pasches and their opposite matchings have one pair in common. Distinct Pasches sharing an opposite pair have no other old vertex in common; hence equality is impossible when \(n\le9\), and is attained for every \(n\ge10\).
4. If \(6\le n\le9\) and at least two Pasches occur, the stronger bound \(t(A)\le(49/64)2^N\) holds. For unrestricted \(n\) it also holds whenever every pair of opposite matchings is disjoint. It is attained by the disjoint union of two Pasches and any isolated points (\(n\ge12\)).

In particular, six points are necessary and sufficient for a deficit from the unrestricted one-point count; the six-point Pasch has \(t(A)=28{,}672\). A ten-point witness has \(t(A)=27{,}487{,}790{,}694{,}400\).

## Assumptions and scope
A copy of the Fano plane is forbidden as an ordinary hypergraph substructure, not merely as an induced substructure. A finite PSTS is used only as a **parameter base** inside the Fano-free homogeneous hypergraph. The one-point extension is not required to remain a PSTS: each of its \(\binom n2\) possible new triples \(\{x,a,b\}\) is independently available unless it completes a Fano copy. The PSTS hypothesis is essential to the uniqueness and overlap-rigidity statements. All old vertices are individually named, and only types realized outside \(A\) are counted. For \(n=0,1\) use the usual empty-set conventions.

## Proof
**A. Fraïssé and type reduction.** The seven-point Fano hypergraph is *pair-irreducible*: each pair of its vertices lies on one of its lines. Thus a free amalgam of finite Fano-free \(3\)-hypergraphs cannot introduce a forbidden copy meeting both new sides. The hereditary class has the joint embedding, amalgamation, and countability properties, so it has a homogeneous Fraïssé limit. Every admissible finite one-point diagram occurs in that limit, and distinct link sets yield distinct complete types by homogeneity/quantifier elimination. By freely amalgamating multiple such extensions, every type outside \(A\) is nonalgebraic.

**B. Exact Pasch obstruction.** Delete a point \(x\) from a Fano plane. Four lines remain among the six old points and form the Pasch; the three deleted lines are \(\{x,a,b\}\) for the three opposite pairs \(ab\) of that Pasch. Conversely, these four old triples plus the three indicated new triples reproduce the Fano plane (the seven-line incidence design). As the old base itself is Fano-free, every forbidden copy after adjoining \(x\) must contain \(x\). Hence its link \(X\) is legal exactly if \(M\not\subseteq X\) for every \(M\in\mathcal P(A)\), proving the exact formula
\[
 t(A)=\#\{X\subseteq\binom{A}{2}:\; M\not\subseteq X\text{ for every }M\in\mathcal P(A)\}.
\]
Under uniform independent Bernoulli \(1/2\) indicators for the \(N\) old-pair coordinates, \(t(A)/2^N\) is exactly the probability of satisfying all Pasch clauses.

**C. Rigidity of opposite matchings in a PSTS.** Each of the six Pasch points belongs to exactly two of its four triples, and the opposite matching is the set of three pairs not used by any of those triples. Relative to its opposite pairs \(\{a,b\},\{c,d\},\{e,f\}\), the four triples, after relabeling, are
\[
 ace,\qquad adf,\qquad bcf,\qquad bde.
\]
A PSTS cannot carry two distinct Pasches with the same opposite matching: the four cross pairs between \(\{a,b\}\) and \(\{c,d\}\) uniquely determine their third vertices, so the four triples and the other opposite pair are determined. More strongly, suppose two Pasches share the opposite pair \(\{a,b\}\) and some other vertex \(c\). In either Pasch, \(c\) lies in exactly one block with \(a\) and one with \(b\). Uniqueness of old blocks through the pairs \(ac\) and \(bc\) forces the same further vertices \(e,f\) into both Pasches. Applying the same argument to \(e\) forces the last vertex \(d\); all four blocks and all six vertices coincide. Thus distinct Pasches with a common opposite pair have **no further common vertex**, and in particular two distinct opposite matchings intersect in at most one pair. Their union then has five pair-coordinates if they overlap, and six otherwise. Sharing one opposite pair requires at least ten old vertices.

**D. Exact bounds and equality.** For a Pasch matching \(M\), let \(E_M\) denote the event that all its three link indicators equal one. Then \(\Pr(E_M)=1/8\). One such forbidden event leaves a fraction \(7/8\). If distinct \(M,M'\) share one pair, \(\Pr(E_M\cap E_{M'})=1/32\); if they share none, this probability is \(1/64\). Inclusion–exclusion therefore gives the legal fractions \(25/32\) and \(49/64\), respectively, for exactly two Pasches. Any third distinct matching imposes a **strictly** additional condition: choosing exactly its three coordinates and no others makes \(E_{M''}\) true while leaving both earlier events false. It follows that the upper bounds and their stated equality criteria hold without any independence assumption. The six-point threshold follows from the size of a Pasch.

**E. Attaining the constants.** Use old points \(0,\ldots,9\) and these eight old triples:
\[
\begin{array}{llll}
024,&035,&125,&134,\\
068,&079,&169,&178.
\end{array}
\]
The first four make a Pasch with opposite matching \(\{01,23,45\}\); the other four make a Pasch with matching \(\{01,67,89\}\). Every old pair lies in at most one triple. The only common old vertices between the two Pasch blocks are \(0,1\), and cross-block triples have no pairs connecting exclusive vertices, so the union is Fano-free. Every two blocks from a Pasch intersect; for a mixed four-block Pasch, pairs of blocks from both halves would have to meet in one point, which is impossible unless all four blocks pass through the same common point, contradicting the Pasch's degree-two condition. Thus there are exactly two Pasches. Their two link constraints involve five pair-bits and leave a fraction \(25/32\), yielding \(25\cdot 2^{40}=27{,}487{,}790{,}694{,}400\) types. Adjoining isolated old vertices preserves the obstruction set and scales the count by the added free pair-bits. One six-point Pasch gives \((7/8)2^{15}=28{,}672\); two vertex-disjoint Pasches give \((49/64)2^{66}\) on twelve points, with isolated padding for all larger orders.

## Verification
The provided `verify.py` uses two separate finite descriptions: it generates the \(30\) distinct Fano planes on seven fixed labels from the vector-space model over \(\mathbb F_2\), and it detects Pasches by their six-point, four-block incidence signature. For each explicit witness the two methods independently obtain the same forbidden link matchings. It checks the partial Steiner property, reproduces the fractions \(7/8,25/32,49/64\), enumerates all \(2^{15}\) one-point link assignments for the six-point witness, and tests all locally compatible second-Pasch configurations through ten points, finding no common-opposite-pair example before ten. Run with `python3 verify.py`; its last line must be `ALL CHECKS PASSED`. These finite checks independently corroborate, but do not replace, the universal combinatorial argument in parts C–D.

## Relationship to prior work
The free-amalgamation/Fraïssé framework, the Fano plane's seven-line geometry, its four-line Pasch deletion and the definition of a partial Steiner triple system are pre-existing mathematics. Conant's *An axiomatic approach to free amalgamation* establishes relevant general background; Král' et al. describe the Pasch as a point-deleted Fano configuration. Previously published work on extension spectra of **partial Steiner systems** requires the *new* structure also to be a PSTS and therefore counts matchings in a leave; it does not count arbitrary Fano-free new links. A published sharp overlap-matching inequality for **tetrahedron-free** \(3\)-hypergraphs uses one obstruction for each old triple, a different forbidden configuration and different parameters. Neither yields the stated Pasch-rigidity and sharp \(7/8\), \(25/32\) bounds. Literature search may still have missed a classical equivalent formulation in design enumeration or hypergraph property testing.

## Limitations
Only Fano-free \(3\)-hypergraphs with **partial-Steiner old parameter bases** are covered. For general Fano-free old bases, multiple Pasches can share the same opposite matching, so the uniqueness and equality claims need not hold. No universal exact closed form purely in the number of Pasches is asserted: higher overlaps influence the count. The probability normalization is over link diagrams/types, not random vertices of the infinite structure. Independent external mathematical validation and an exhaustive historical priority determination are not claimed.

## References
1. G. Conant, *An axiomatic approach to free amalgamation*, arXiv:1505.00762, first posted 2015-05-04, Sections 3 and 7. https://arxiv.org/abs/1505.00762
2. D. Král', E. Máčajová, O. Pangrác, A. Raspaud, J.-S. Sereni, M. Škoviera, *Projective, affine, and abelian colorings of cubic graphs*, preprint, Section 2 (Pasch/Fano point deletion). https://irma.math.unistra.fr/~sereni/Articles/KMP%2B08.pdf
3. *Real-rooted one-point extension spectra of partial Steiner triple systems*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-real-rooted-one-point-extension-spectra-of-partial-steiner-tripl--9599713a6632
4. *Sharp overlap-matching bounds for one-point types of the generic tetrahedron-free 3-hypergraph*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-overlap-matching-bounds-for-one-point-types-of-the-generic--5ae2c90229c3
