# A sharp \(2q+1\) threshold for two-variable logic on once-marked directed cycles

## Finding
For every integer \(q\geq2\) and positive integers \(n,m\), let \(C_n\) and \(C_m\) be directed cycles with a single marked vertex, in the relational signature \(\{S,P,=\}\), as defined below. They satisfy exactly the same first-order sentences using only the variable names \(x,y\), of quantifier rank at most \(q\), **if and only if**
\[
(n=m\leq 2q)\quad\text{or}\quad(n,m\geq 2q+1).
\]
Thus the family has exactly \(2q+1\) distinct sentence theories at rank \(q\), and the sharp maximum size of a smallest representative is \(2q+1\). At rank zero every such cycle is equivalent; at rank one the two classes are \(\{C_1\}\) and \(\{C_n:n\geq2\}\).

## Assumptions and scope
For each integer \(n\geq1\), the universe of \(C_n\) is \(\mathbb Z/n\mathbb Z\). The binary predicate \(S(a,b)\) holds precisely when \(b\equiv a+1\pmod n\), and the unary predicate \(P\) holds precisely at residue zero. In particular, \(C_1\) has one directed loop. The order, transitive closure of \(S\), additional constants, and counting quantifiers are **not** in the language. Quantifier rank is the maximum nesting depth of quantifiers, and \(\mathrm{FO}^{2}\) permits reuse of only \(x,y\).

## Proof
**1. Rank-\(q\) lower bounds, for each finite length through \(2q\).** Define two-variable unary formulas \(F_j(z)\), \(B_j(z)\) inductively, with \(z\) standing for whichever of the two variable names is free. Set \(F_0(z)=B_0(z)=P(z)\). For \(j\geq0\), set
\[
F_{j+1}(z):=\exists w\,(S(w,z)\land F_j(w)),\qquad
B_{j+1}(z):=\exists w\,(S(z,w)\land B_j(w)),
\]
where \(w\) denotes the other variable name and bound variables inside the recursive subformula are consistently renamed. Each formula uses only two variable names and has quantifier rank \(j+1\). On \(C_n\), \(F_j\) identifies the vertex at forward directed distance \(j\) from the mark, and \(B_j\) identifies the vertex at backward directed distance \(j\). Let \(A_r(z):=\bigvee_{j=0}^{r}(F_j(z)\lor B_j(z))\), which has rank \(r\) and identifies the radius-\(r\) undirected ball around the marked point.

For odd \(k=2r+1\), \(r\geq1\), the rank-\(r+1\) sentence \(\forall x\,A_r(x)\) holds on \(C_n\) precisely for \(n\leq k\), since the marked ball has at most \(2r+1\) elements. The case \(k=1\) is given by \(\forall x\,P(x)\), of rank one.

For every even \(k=2r+4\), \(r\geq0\), the rank-\(r+2\) sentence
\[
\exists x\,\forall y\;\bigl(A_r(y)\lor x=y\lor S(x,y)\lor S(y,x)\bigr)
\]
holds on \(C_n\) precisely for \(n\leq k\). If the marked radius-\(r\) ball does not already cover the cycle, its complement is one consecutive directed arc, of length \(n-(2r+1)\). That complementary arc fits into the closed one-step neighborhood of a suitable \(x\) exactly when it has at most three vertices. Conversely the union of the marked ball and such a neighborhood has at most \((2r+1)+3=k\) points. For \(k=2\), use the rank-two sentence \(\forall x\,\forall y\,(S(x,y)\leftrightarrow S(y,x))\), which holds exactly for cycles of lengths one or two. Consequently, for every \(1\leq k\leq 2q\) there is a sentence of rank at most \(q\) expressing \(n\leq k\) on this family. Any two different lengths of which the smaller is at most \(2q\) can therefore be distinguished.

**2. Uniform upper bound via a two-pebble game.** Fix \(q\geq2\) and \(n,m\geq2q+1\). For \(0\leq t\leq q-1\) label the vertices of either cycle by \(0\) at the marked vertex, by \(R_i\) at the vertex \(i\) steps forward for \(1\leq i\leq t\), by \(L_i\) at the vertex \(i\) steps backward for \(1\leq i\leq t\), and by \(M\) at all remaining vertices. These labels are disjoint because the cycle lengths are at least \(2t+3\). The two cycles realize exactly the same labels at each such radius.

**One-step matching lemma.** Suppose stationary pebbles \(a\) and \(a'\), in the two cycles respectively, carry the same radius-\(t\) label, where \(1\leq t\leq q-1\). Given any proposed placement \(b\) of the other pebble in the first cycle, a matching placement \(b'\) can be chosen in the second cycle that has the same radius-\((t-1)\) label and preserves the atomic relations \(a=b\), \(S(a,b)\), and \(S(b,a)\). If \(b\) has a boundary label, its unique counterpart has exactly those relations to \(a'\), because the radius-\(t\) label of \(a\) determines every equality or directed adjacency with a vertex within \(t-1\) of the marked point. If \(b\) is labelled \(M\) and equals \(a\), use \(a'\); if it is a directed neighbor of \(a\), use the corresponding directed neighbor of \(a'\). In each case the selected point has the required \(M\) label: the radius-\(t\) class of the stationary pebble determines whether its neighbors lie outside the smaller marked ball. Otherwise choose any \(M\)-labelled point unequal and nonadjacent to \(a'\). The radius-\((t-1)\) interior contains at least
\[
n-\bigl(1+2(t-1)\bigr)=n-2t+1\geq4
\]
points in either cycle; at most three are excluded by the stationary point and its two directed neighbors, so this choice exists. The argument is symmetric in the two cycles.

In the standard \(q\)-round two-pebble Ehrenfeucht–Fraïssé game, after the first move choose the counterpart with the same radius-\((q-1)\) label. With \(t\) rounds remaining, preserve the matching radius-\(t\) labels of all currently placed pebbles and all atomic relations between them. At every subsequent move, keep the stationary pebble and apply the one-step lemma, reducing the radius to \(t-1\). The atomic partial isomorphism is preserved after every move, so Duplicator wins. The two-pebble game theorem then yields agreement on every \(\mathrm{FO}^{2}\) sentence of rank at most \(q\).

Combining the separating sentences in step 1 with Duplicator's strategy in step 2 proves the claimed equivalence classes. At rank one, the only relevant one-element existential properties distinguish a self-loop/all-red singleton from the cycles with a single red point and at least one nonred point; all lengths at least two agree. Rank-zero sentences cannot inspect any vertex in this constant-free vocabulary.

## Verification
An independent, exhaustive finite type-refinement computation using the complete atomic diagrams of zero-, one-, and two-pebble assignments agrees with the classification for ranks \(0\) through \(7\) and cycle lengths \(1\) through \(20\). The explicit odd/even threshold sentences were separately evaluated on lengths \(1\) through \(34\), for thresholds \(1\) through \(14\). Run `python checker.py` (Python standard library only). The uniform mathematical proof above, not these finite tests, establishes the infinite quantifiers over all ranks and lengths.

## Relationship to prior work
Michaliszyn–Witkowski (2026) and Jeż–Michaliszyn–Witkowski (2026) establish decision and finite-model bounds for two-variable logic with exact successors of **linear orders**, hence acyclic spanning paths. The present structures are instead directed cycles, with one named unary colour and no available order, and the invariant is an exact rank-sensitive classification rather than satisfiability complexity. The full first-order rank profile of one-red linear orders and the rank profile of unmarked finite directed paths are nearby but do not imply this precise marked-cycle \(\mathrm{FO}^{2}\) threshold: each changes both the structure/language or the available number of variables. Classical work on two-variable logics of words and rankers remains a priority risk; no universal novelty claim is made.

## Limitations
The theorem is only about a single cycle with exactly one marked point, without counting quantifiers, an order relation, or additional colours. It does not classify arbitrary disjoint unions of cycles or marked words with multiple distinguished points. Targeted searches did not locate an equivalent statement, but cannot establish absolute priority. No independent mathematical audit was performed.

## References
- J. Michaliszyn and P. Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758v1, first posted 2026-10-07, https://arxiv.org/html/2610.09758v1.
- A. Jeż, J. Michaliszyn and P. Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943v1, first posted 2026-10-14, https://arxiv.org/html/2610.19943.
- K. Etessami, M. Y. Vardi and T. Wilke, *First-order logic with two variables and unary temporal logic*, Information and Computation 179 (2002), 279–295.
- P. Weis and N. Immerman, *Structure Theorem and Strict Alternation Hierarchy for FO2 on Words*, arXiv:0907.0616, 2009.
