# Sharp rank-four logical visibility of carousel tournaments

## Finding

For every positive odd integer \(n\), let \(R_n\) be the finite carousel tournament on \(\mathbb Z/n\mathbb Z\), with directed edge \(x\to y\) precisely when \(1\le (y-x)\bmod n\le(n-1)/2\). Write \(R_n\equiv_q R_{n'}\) when the two tournaments satisfy the same first-order sentences of quantifier rank at most \(q\), in the language consisting of a directed-edge relation and equality.

**Theorem.** For all positive odd integers \(n,n'\),
\[
 R_n\equiv_4 R_{n'}\quad\Longleftrightarrow\quad
 \bigl(n=n'\le13\bigr)\ \text{or}\ \bigl(n\ge15\ \text{and}\ n'\ge15\bigr).
\]
Thus the family has exactly eight rank-four first-order theories: seven singleton-size classes at orders \(1,3,5,7,9,11,13\) and one infinite class beginning at order \(15\). More generally, for every integer \(q\ge1\), all positive odd \(n,n'\ge2^q-1\) satisfy \(R_n\equiv_q R_{n'}\).

## Assumptions and scope

The language has no order, arithmetic, constants, or counting quantifiers. The structure \(R_1\) has one vertex and no edges. Quantifier rank counts the maximum number of nested first-order quantifiers, not the total number of quantifiers or the number of distinct variables. The equivalence claimed is restricted to the specified carousel family, not to all tournaments.

## Proof

**Antipodal circular representation.** For each odd \(n\), make a circle of \(2n\) equally spaced sites labelled by \(\mathbb Z/(2n)\mathbb Z\); the even sites are *vertices*, and the odd sites are *gaps*. The antipodal involution \(a\mapsto a+n\) interchanges the two kinds. Associate to a vertex \(x\in\mathbb Z/n\mathbb Z\) the even site \(2x\) and its antipodal gap \(2x+n\). For distinct vertices \(x,y\), the edge \(x\to y\) holds exactly when site \(2y\) lies clockwise strictly between \(2x\) and \(2x+n\). Indeed, the positive clockwise difference is an even integer at most \(n-1\) exactly for forward vertex distances \(1,\ldots,(n-1)/2\).

**Paired-interval extension lemma.** Suppose finitely many previously selected vertices in two such circles have been bijectively matched. Mark each selected vertex site and its antipodal gap. Assume the matching of marked sites preserves clockwise cyclic order, site kind (vertex/gap), and antipodes. Between every two consecutive marked sites, let \(L\) be the number of unmarked *sites* strictly inside that interval. Given \(r\ge0\), assume that corresponding intervals either have exactly equal \(L\), or both have \(L\ge T_r\), where \(T_0=0\) and \(T_r=2T_{r-1}+2=2^{r+1}-2\). Then the second player can respond to \(r\) further arbitrary vertex selections so as to preserve the edge/equality diagram of all selected vertices.

Proof is by induction on \(r\). A repeated selection receives the already matched response. For a new selected vertex site in an interval of length \(L\), its antipode lies in the distinct, paired opposite interval, and both insertions split those intervals in corresponding positions. When corresponding lengths are equal, choose exactly the same offset. Otherwise both lengths are at least \(2T_{r-1}+2\). Let \(a,b\) be the numbers of unmarked sites to the left and right of the selected site, so \(a+b+1=L\). If \(a<T_{r-1}\), match \(a\) exactly; the other residual lengths are both at least \(T_{r-1}\). Do the analogous thing if \(b<T_{r-1}\); the two cases cannot occur simultaneously in a large interval. If both \(a,b\ge T_{r-1}\), choose a response whose two residual lengths are at least \(T_{r-1}\). In this last case there are two consecutive admissible positions, because the receiving interval has length at least \(2T_{r-1}+2\); one position is an even vertex site, the other an odd gap, so a vertex site can always be chosen. In the other cases exact offset from one endpoint preserves the site's kind, because corresponding endpoints have equal kinds and all sites alternate. The antipodal insertion automatically realizes the identical split in the partner interval. Thus the invariant persists with \(r-1\) moves remaining. At \(r=0\), the cyclic order and antipodal-mark matching determine all directed edges and all equalities, proving the lemma.

**Uniform collapse.** If \(q\ge1\), after the first vertex move any two carousel tournaments have a matched pair of marked sites (the played vertex and its antipodal gap). Each of the two intervening circular intervals has exactly \(n-1\) unmarked sites on its side, and correspondingly \(n'-1\) on the other circle. If \(n,n'\ge2^q-1\), both lengths are at least \(2^q-2=T_{q-1}\). Apply the extension lemma to the remaining \(q-1\) moves. The first-order Ehrenfeucht–Fraïssé theorem yields \(R_n\equiv_q R_{n'}\). For \(q=4\), this gives the entire tail starting at \(n=15\).

**Sharp finite boundary.** It remains to prove pairwise nonequivalence of the eight representatives \(R_1,R_3,\ldots,R_{15}\). This is an exact finite computation over the small tournaments, *not* extrapolation to infinitely many orders. The standalone file `verify_carousel.py` implements the following exhaustive logical recursion. For a tuple \(\bar a\), its depth-zero type is the complete equality/directed-edge atomic diagram. At depth \(r+1\), its type is its atomic diagram together with the *set* of depth-\(r\) types obtained by appending every possible vertex. Inductively, two pointed structures receive the same recursively constructed type exactly when they satisfy the same formulas of quantifier rank at most \(r\): an existential quantifier tests membership among appended types, universal quantification is its negation dual, and Boolean combinations test subsets of these types. The algorithm enumerates every tuple at depths up to four, interns full keys without hash-only comparisons, and identifies eight different empty-tuple depth-four types for the eight representative orders. Its printed identifiers, in increasing order of \(n\), are \(5,45,136,199,229,243,249,253\); it also obtains identifier \(253\) for orders \(17\) and \(19\), which are independent finite spot checks. The general interval lemma, not these checks, covers every larger odd order. Each distinct recursive type implies the existence of a distinguishing rank-four first-order sentence by the same inductive characteristic-formula construction.

Together the infinite collapse and exact finite separation prove the theorem.

## Verification

Run `python3 verify_carousel.py` with Python 3. The run compares all representatives of odd orders \(1\) through \(19\); it prints `EXACT_SMALL_CASE_CHECK_PASS` only when all eight claimed finite rank-four types are distinct and the checked tail instances match. The program implements full tuple equality/orientation diagrams, including repeated variables. The infinite tail follows from the proved paired-interval extension lemma, not from a finite experiment. The recurrence \(T_r=2^{r+1}-2\) is proved algebraically by induction.

## Relationship to prior work

Coregliano's *Quasi-Carousel Tournaments* (arXiv:1503.04124, first version March 13, 2015, Section 1) defines the same family and studies density limits and local transitivity, not bounded-quantifier-rank equivalence. Goodall, Nešetřil, and Ossona de Mendez, *Strongly Polynomial Sequences as Interpretations* (December 15, 2015, Section 5.1.11) establish polynomial homomorphism counts for the carousel sequence; polynomiality of those counts does not itself give the exact rank-four equivalence cutoff. Pikhurko and Verbitsky's *Logical Complexity of Graphs: A Survey* (arXiv:1003.4865, March 25, 2010, Section 3) reviews Ehrenfeucht–Fraïssé games and logarithmic depth phenomena but does not establish this carousel-family classification. Related exact depth bounds for finite directed paths concern a successor digraph, whose binary relation is not the half-circle orientation relation of a carousel tournament; that path result therefore does not imply this statement by a signature-preserving reduction known here.

## Limitations

The sharpness proof is specific to quantifier rank four; the general statement is an upper stabilization bound, not a claimed sharp threshold for all quantifier ranks. The finite portion depends on a small, fully enumerated computation with openly supplied code; no unperformed independent audit or formal proof-assistant verification is claimed. Exhaustive search of all possible earlier publications is impossible; a previously unnoticed theorem about first-order interpretations of antipodal circular orders could subsume some or all of the claim. The claim concerns model-theoretic distinguishability, not an algorithm for recognizing carousel tournaments among arbitrary directed graphs.

## References

1. L. N. Coregliano, *Quasi-Carousel Tournaments*, arXiv:1503.04124 (initially posted 2015-03-13), https://arxiv.org/abs/1503.04124 ; definition on pp. 1–2 and results on asymptotic densities.
2. A. J. Goodall, J. Nešetřil, P. Ossona de Mendez, *Strongly Polynomial Sequences as Interpretations*, preprint dated 2015-12-15, https://iti.mff.cuni.cz/series/2015/631.pdf ; §5.1.11, Proposition 5.4.
3. O. Pikhurko, O. Verbitsky, *Logical Complexity of Graphs: A Survey*, arXiv:1003.4865 (initially posted 2010-03-25), https://arxiv.org/abs/1003.4865 ; §3.
4. Standard Ehrenfeucht–Fraïssé equivalence theorem for bounded quantifier rank, as reviewed in Reference 3.
