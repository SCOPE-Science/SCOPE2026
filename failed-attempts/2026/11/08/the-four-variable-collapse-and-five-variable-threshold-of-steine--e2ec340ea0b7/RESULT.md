# The four-variable collapse and five-variable threshold of Steiner quadruple systems

## Finding
Let \(\mathcal Q=(V,B)\) be any *nontrivial finite Steiner quadruple system* (SQS): \(V\) is finite with \(|V|\ge8\), and \(B\) is the symmetric four-ary relation holding exactly on four pairwise distinct points which constitute a block. Every three distinct points occur in exactly one block. No further relations, constants, counting quantifiers, or function symbols are present.

For all SQSs \(\mathcal Q,\mathcal Q'\), with orders \(v,w\), and ordinary counting-free finite-variable first-order logic at unrestricted quantifier depth:

\[
\mathcal Q\equiv_{\mathrm{FO}^{k}}\mathcal Q'\quad\text{for every }1\le k\le4,
\]
\[
\boxed{\mathcal Q\equiv_{\mathrm{FO}^{5}}\mathcal Q'\ \Longleftrightarrow\ (v=8\ \Longleftrightarrow\ w=8).}
\]

Thus the class has exactly one theory at each of widths one through four, and exactly two at width five: the order-eight theory and the common theory of *all* orders at least ten. This classification is independent of whether a system has many automorphisms or has no transitive automorphism group. It is a statement about the pure point/block relation, not a quasigroup operation or a two-sorted incidence expansion.

## Assumptions and scope
For \(v\ge8\), an SQS of order \(v\) is a pair \((V,\mathscr B)\) with \(\mathscr B\subseteq\binom V4\) such that every \(T\in\binom V3\) belongs to precisely one \(C\in\mathscr B\). The relation \(B(a,b,c,d)\) is true iff \(\{a,b,c,d\}\in\mathscr B\) and those four arguments are distinct. Arguments of \(B\) may be permuted. Existence of orders eight and ten follows from explicit systems (verified below), and the classical existence theorem gives infinitely many orders \(v\equiv2,4\pmod6\) with \(v\ge8\). The classification is quantified over all systems of such orders, including nonisomorphic systems of the same order.

\(\mathrm{FO}^{k}\) denotes all first-order formulas using at most \(k\) distinct variable names, reused as often as desired, with equality and \(B\) but without counting quantifiers. Equivalence means agreement on every sentence of this fragment, with no quantifier-depth bound.

## Proof
**Completion geometry.** For every three-element set \(T\subseteq V\), write \(c(T)\in V\setminus T\) for the unique fourth point with \(T\cup\{c(T)\}\in\mathscr B\). If \(A\subset V\) consists of four distinct points, then either:

(i) \(A\) is a block, in which case all four triples \(T\in\binom A3\) are completed by the fourth member of \(A\); or

(ii) \(A\) is not a block, in which case the four points \(c(T)\), for \(T\in\binom A3\), lie outside \(A\) and are pairwise distinct.

For (ii), no completion can belong to \(A\), since that would make \(A\) a block. If two different triples of \(A\) shared a completion \(x\), the resulting two blocks would have three points in common (the two shared points of those triples together with \(x\)). Their common triple would then occur in two different blocks, contrary to uniqueness.

**Permanent four-pebble strategy.** Consider two arbitrary systems of order at least eight. Maintain a pebble map preserving equality and every atomic occurrence of \(B\), including its negation. On moving one of four pebbles, at most three fixed pebbles remain. If at most two distinct fixed points remain, any choice of a fresh point has the same atomic behavior, since \(B\) requires four distinct arguments. If exactly three distinct fixed points \(a,b,c\) remain, a fresh point can be either the unique completion \(c(\{a,b,c\})\) or a point different from that completion and the three fixed points. Both choices exist because \(v\ge8\). If the moving pebble is placed on a fixed point, match the corresponding equality instead. Consequently the current partial isomorphism can always be preserved. Starting with empty placements gives an infinite winning four-pebble strategy, and hence equivalence in \(\mathrm{FO}^{4}\), which implies equivalence in smaller widths.

**Permanent five-pebble strategy within each regime.** First suppose both orders are at least ten. Maintain exactly the same invariant for five pebbles. When one pebble is moved, at most four distinct points remain fixed. The cases of zero to three fixed points were covered above. Suppose there are exactly four distinct fixed points \(A\). Their images have the same block/nonblock status by the invariant. If \(A\) is a block, no fresh fifth point can complete any of the four fixed triples; hence every fresh point has the same atomic behavior and at least one is available. If \(A\) is a nonblock, the completion geometry supplies exactly four distinct fresh points, each completing precisely one of the four fixed triples. All remaining fresh points complete none of those triples. There are \(v-8\ge2\) such generic points at either order. Each of these five possible fresh-point atomic profiles therefore occurs in both structures. If instead both systems have order eight, the identical argument applies except that the generic type is absent on both sides; the four distinct completion types and all equality types still match. Equalities are also matched. The permanent strategy in either equal-regime case gives equivalence at unrestricted depth.

**Sharp five-variable separation.** With exactly five variable names \(a,b,c,d,e\), consider the sentence

\[
\begin{aligned}
\Phi:=\exists a\,\exists b\,\exists c\,\exists d\,\exists e\;[&\bigwedge_{x\ne y\in\{a,b,c,d,e\}}x\ne y\;\wedge\;\neg B(a,b,c,d)\\
&\wedge\neg B(a,b,c,e)\wedge\neg B(a,b,d,e)\\
&\wedge\neg B(a,c,d,e)\wedge\neg B(b,c,d,e)].
\end{aligned}
\]

Here \(\bigwedge_{x\ne y\in\{a,b,c,d,e\}}x\ne y\) abbreviates the ten unordered pairwise inequalities, not quantification over additional variables. A nonblock \(A=\{a,b,c,d\}\) always exists: fix any triple and choose a fourth point other than its unique completion. By (ii), precisely four points outside \(A\) complete one of its four triples. Therefore the number of points outside \(A\) satisfying the four displayed negations is exactly \(v-8\). Hence \(\mathcal Q\models\Phi\) iff \(v\ge10\), while order eight fails \(\Phi\). Combined with the five-pebble strategy, this proves both directions and exhausts the possible five-variable theories.

## Verification
The standalone file `verify.py` constructs SQSs of orders eight and sixteen from four-point sets with vanishing bitwise XOR, and constructs the order-ten SQS from the affine lines and anisotropic circles over \(\mathbb F_3^2\), adjoining a point at infinity for the affine lines. It independently checks that every triple has exactly one completing block. For each ordered tuple of length up to four, allowing repeated entries, the program exhaustively computes the equality/block atomic profile and the set of profiles obtainable after one fresh pebble move. The extension catalogues agree for all three sampled systems at width four and agree for orders ten and sixteen—but not eight—at width five. In the exceptional nonblock-four configuration, order eight has eight extension profiles (four equalities and four completions), whereas orders ten and sixteen have nine (one additional generic type).

The output in `verification_output.txt` is reproducible using `python3 verify.py` with Python's standard library. Exhaustive checks over three concrete finite designs are corroboration only; the unrestricted and all-orders statements are proved by the preceding completion argument and permanent pebble strategies. Neither script nor finite enumeration asserts novelty or independence.

## Relationship to prior work
The characterization of counting-free finite-variable equivalence by permanent \(k\)-pebble strategies is classical and is explicitly discussed by Grohe and Otto in *Pebble Games and Linear Equations*, Section 2, Theorem 2.1 (arXiv:1204.1990; initially submitted 2012-04-09). Their Section 5.3 investigates Boolean linear-equation representations, not Steiner-quadruple order thresholds. Horan and Hurlbert, *Overlap Cycles for Steiner Quadruple Systems* (arXiv:1204.3215; initially submitted 2012-04-14), establish the SQS definition, admissible orders, and block-ordering constructions, but do not address this bounded-variable theory. Huber's *Classification of flag-transitive Steiner quadruple systems* (arXiv:math/0401117) concerns automorphism classifications; its abstract was available, but its complete text was not inspected.

Direct published-record and literature searches for SQS block-relation logical equivalence, four- and five-variable theories, pebble games, and stronger general-design coverage did not identify this exact classification. This negative search is not a proof of historical priority: an unstated consequence of a more general theorem on relational designs could cover the claim. The proof here is independent of any assertion of priority.

## Limitations
No claim is made for six or more variables. The result fails as an automatic statement for counting logic, for two-sorted point/block incidence structures, or for algebraic expansions with a ternary completion operation. The full historical literature has not been exhaustively inspected, and independent mathematical validation has not been performed. The finite check covers the named orders eight, ten, and sixteen, not all admissible orders.

## References
1. Martin Grohe and Martin Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, first version 2012-04-09, https://arxiv.org/abs/1204.1990 .
2. Victoria Horan and Glenn Hurlbert, *Overlap Cycles for Steiner Quadruple Systems*, arXiv:1204.3215, first version 2012-04-14, https://arxiv.org/abs/1204.3215 .
3. Michael Huber, *Classification of flag-transitive Steiner quadruple systems*, arXiv:math/0401117, first version 2004-01-12, https://arxiv.org/abs/math/0401117 .
