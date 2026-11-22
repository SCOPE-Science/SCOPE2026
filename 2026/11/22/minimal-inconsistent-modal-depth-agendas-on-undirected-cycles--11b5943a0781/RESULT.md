# Minimal inconsistent modal-depth agendas on undirected cycles

## Finding

**Theorem (complete three-premise spectrum).** Let \(n\ge3\), let \(C_n\) be the loopless undirected cycle on \(\mathbb Z/n\mathbb Z\), and use ordinary Boolean Kripke semantics for its symmetric adjacency relation. Fix the world \(0\), a single propositional letter \(p\), and the genuinely modal signed agenda
\[
\Gamma_n=\{P_j,\neg P_j:1\le j\le n-1\},\qquad P_j:=\Box^j p.
\]
A set of signed formulas is *minimally inconsistent* if no valuation satisfies all of it, but every proper subset is satisfiable.

Every minimally inconsistent subset of \(\Gamma_n\) has size two or three. The size-two subsets are exactly \(\{P_i,\neg P_j\}\) for which the original cycle's length-\(j\) walk endpoint set is contained in its length-\(i\) endpoint set.

For even \(n\), there are **no** minimally inconsistent triples. For odd \(n=2r+1\), the complete list of minimally inconsistent triples consists of
\[
\{P_{2a},P_{2b+1},\neg P_k\}
\]
for the integers
\[
1\le a\le r-1,\quad 0\le b\le r-1,\quad a+b\ge r-1,
\]
with \(1\le k\le2r\) satisfying either \(k\) even and \(k>2a\), or \(k\) odd and \(k>2b+1\). Each triple occurs exactly once in this parameterization. Consequently their exact number is
\[
\boxed{H(C_{2r+1})=\frac{r(r-1)(2r+5)}6},\qquad r\ge1.
\]
In particular, there are no such triples at \(n=3\), and the counts for odd cycle lengths \(5,7,9,11,13\) are \(3,11,26,50,85\). For \(r\ge2\), the smallest modal-depth bound admitting any minimally inconsistent triple is exactly \(r+1=(n+1)/2\).

## Assumptions and scope

The accessibility relation is symmetric and irreflexive: \(iRj\) exactly when \(j=i+1\) or \(j=i-1\) modulo \(n\). This is **not** the one-way successor cycle, nor a reflexive epistemic frame. A valuation is any subset \(V\subseteq\mathbb Z/n\mathbb Z\) marking the worlds where \(p\) holds. The expression \(\Box^j p\) is interpreted at the fixed root \(0\), with a path of precisely \(j\) accessibility steps, backtracking allowed. Each signed formula is an element of a set, with no repeated copies counted.

The depth cut-off \(n-1\) is sufficient for the complete family of distinct endpoint supports on odd cycles: for \(j\ge n-1\) that support is all of \(V(C_n)\). In even cycles the same-parity endpoint families also stabilize, and extending the agenda to arbitrary positive depths cannot create a minimally inconsistent triple. Counts here distinguish syntactically indexed signed formulas in the explicitly displayed finite agenda, not all formulas of Boolean modal logic and not all possible frames. The unique fixed root is harmless by cycle vertex-transitivity.

Let
\[
B_j=\{v\in\mathbb Z/n\mathbb Z:\text{there is a walk of length }j\text{ from }0\text{ to }v\}.
\]
Then \(P_j\) holds exactly when \(B_j\subseteq V\), and \(\neg P_j\) holds exactly when \(B_j\not\subseteq V\). All \(B_j\) are nonempty.

## Proof

**1. Walk supports and covers.** Every length-\(j\) walk on the cycle consists of some clockwise and some anticlockwise steps. Its endpoint is the sum of \(j\) signs, hence
\[
B_j=\{j-2t\pmod n:0\le t\le j\}.
\]
Because backtracking two steps is allowed, \(B_j\subseteq B_{j+2}\). Accordingly, for each parity the supports form a nested chain. A set of positive premises \(\{P_i:i\in I\}\) forces \(p\) true on \(U=\bigcup_{i\in I}B_i\). Adjoining negative premises \(\{\neg P_j:j\in J\}\) is consistent exactly if each \(B_j\) has a vertex outside \(U\): take the valuation \(V=U\). This proves the stated set-cover test, and in particular the pair classification.

Every minimally inconsistent set must contain exactly one negative premise. Indeed, if it were inconsistent with multiple negatives, one of them by itself would be contradicted by the positive union, and deleting every other negative would leave an inconsistent proper subset. It must contain at least one positive, since all negatives are jointly true at the empty valuation. At most one positive of each parity can occur: two positives of the same parity have nested supports, and the one with smaller support is redundant. Thus every minimally inconsistent set has at most three formulas, and every triple has exactly two opposite-parity positives and one negative.

**2. Even cycles.** In an even cycle, \(B_j\) lies entirely in the bipartition shore whose parity agrees with \(j\). The two positive supports in a prospective triple are therefore disjoint, and the negative support lies in one shore. If the negative support is covered by their union, it is covered by the positive support of its own parity alone. Hence no triple can be minimally inconsistent.

**3. Odd cycles: the exact two-support criterion.** Put \(n=2r+1\). For \(0\le j\le n-1\), the residues \(j-2t\), \(0\le t\le j\), are all different: a repetition would imply \(n\mid(t-t')\), impossible when \(0<|t-t'|<n\). Therefore \(|B_j|=j+1\), \(B_{n-1}=\mathbb Z/n\mathbb Z\), and all larger depths yield the same full set.

Write the positive levels as \(e=2a\) and \(o=2b+1\). A genuine minimal triple must have \(e\ge2\), \(e\le n-3\), and \(1\le o\le n-2\): the last even level \(n-1\) is already the full universe and makes every other positive redundant.

The sets \(B_e,B_o\) have no common element when \(e+o<n\). An integer endpoint of parity \(e\) and one of parity \(o\) differ by an odd number; if they agree modulo odd \(n\), their difference has absolute value at least \(n\), whereas their absolute endpoint values total at most \(e+o\). Thus, when \(e+o=n-2\), these sets are disjoint and their sizes add to \(n\), so they partition the universe. Increasing either depth by two only expands its set. Consequently
\[
e+o\ge n-2\quad\Longrightarrow\quad B_e\cup B_o=\mathbb Z/n\mathbb Z.
\]
Conversely, suppose \(e+o<n-2\). If a negative level \(k\) has even parity and \(k>e\), then \(B_{e+2}\subseteq B_k\) contains \(e+2\pmod n\). This vertex is not in \(B_e\), and it is not in \(B_o\): the shortest odd-length walk to it has length \(n-e-2>o\). Hence \(B_k\not\subseteq B_e\cup B_o\). Symmetrically, when \(k\) is odd and \(k>o\), the new vertex \(o+2\) is absent from both positives because its shortest even-length walk has length \(n-o-2>e\). If \(k\) is not larger than its same-parity positive level, the negative support is contained in that positive alone and minimality fails. This proves that a triple requires \(e+o\ge n-2\).

If \(e+o\ge n-2\), the union of positive supports is the universe. For even \(k>e\), nesting is strict because \(|B_k|=k+1>|B_e|\), while \(0\in B_k\setminus B_o\) since no odd walk shorter than \(n\) closes at \(0\). Thus neither positive alone covers \(B_k\). For odd \(k>o\), nesting is strict and \(1\in B_k\setminus B_e\): reaching \(1\) in even length needs at least \(n-1\) steps, but \(e\le n-3\). These are precisely the cases in the theorem, proving the necessary-and-sufficient classification.

**4. Counting and first depth.** Substitute \(e=2a\), \(o=2b+1\). The covering condition is \(a+b\ge r-1\). The possible even negatives strictly beyond \(e\) number \(r-a\); the odd negatives strictly beyond \(o\) number \(r-1-b\). Summing gives
\[
\begin{aligned}
H(C_{2r+1})
&=\sum_{a=1}^{r-1}\sum_{b=r-1-a}^{r-1}(2r-1-a-b)\\
&=\frac12\sum_{a=1}^{r-1}(a+1)(2r-a)
=\frac{r(r-1)(2r+5)}6.
\end{aligned}
\]
When \(r=1\) this is the empty sum. If all depths were at most \(r\), two opposite-parity positive levels satisfying \(e+o\ge2r-1\) would have to be \(r-1,r\), but no allowed negative level exceeding one of them by two would remain at depth at most \(r\). Conversely the three depths \(r-1,r,r+1\), with positives at the first two and negative at the last, realize an inconsistent minimal triple for every \(r\ge2\). This proves the sharp threshold.

## Verification

The standalone `verify.py` independently generates all exact-length endpoint sets by graph-adjacency recurrence rather than the modular arithmetic formula, and compares every minimal-cover triple with the theorem's parameterization. It checks every cycle order from \(3\) through \(61\), counts the triples, and verifies the sharp first depth.

For every order from \(3\) through \(15\), it separately evaluates all \(2^n\) Boolean valuations, constructs the truth sets of every positive and negative signed modal literal, and enumerates **all** inclusion-minimal inconsistent three-formula subsets, including every sign configuration. It verifies that precisely the predicted two-positive/one-negative triples occur. The executable reports `VERIFY_OK walk_orders=59 exhaustive_valuations_orders=13`. These tests are finite checks; the preceding proof establishes the unrestricted finite-order claim.

To reproduce: run `python3 verify.py` with Python 3; no third-party packages, external services, or input files are required. All formulas and data necessary for checking are in this package.

## Relationship to prior work

Nagai and Ono (2026) study minimal inconsistency in genuinely modal judgment agendas and give a general covering criterion, with specific impossibility results for directed cyclic constructions and a different iterated modal pattern. Their Proposition 4.1 supplies a related semantic covering viewpoint, but their cyclic frames are not the present irreflexive symmetric cycle with the pure positive-depth necessity agenda, and their results do not state the exact all-cycle triple classification, cubic count, or first-depth threshold proved here.

A separate published result, *Sharp half-circumference modal stabilization on two-colored cycles*, examines pointed modal equivalence, dihedral color orbits and Boolean modal-algebra generation on the same underlying undirected graphs. Its full result concerns which **worlds** are modally indistinguishable under a fixed valuation; it does not classify which combinations of **signed depth formulas** admit a common valuation at a fixed root. The full result *Reachability normal form for multiple modal reductions in pure necessitation* concerns derivability in a weaker abstract proof system, not frame-relative Boolean signed-agenda consistency. *Noncontingency on finite paths* studies a different modality and path frames. These are distinct objects and none of the inspected statements directly yields the exact count here.

The original covering criterion and the walk representation are credited as background tools, not claimed as new. The contribution assessed here is the odd/even obstruction dichotomy with an exact parameterization, all-length cubic census and sharp genuinely modal depth threshold. Earlier unindexed equivalent results in modal judgment aggregation or cyclic hypergraph containment remain a priority risk.

## Limitations

The theorem is restricted to one fixed root on symmetric cycle frames, one propositional variable, ordinary Boolean \(\Box\), and the displayed signed single-operator agenda; it does not establish a new Arrow-type dictatorship theorem or classify arbitrary Boolean combinations of modal formulas. The complete count uses indexed depths at most \(n-1\), so it is not an enumeration over infinitely many syntactic repetitions of an eventually equivalent formula. The all-length proof is self-contained but has not been independently peer-reviewed. Source comparisons establish best-knowledge noncoverage, not global novelty.

## References

1. Y. Nagai and H. Ono, *Arrow-Type Impossibility for Genuinely Modal Judgments*, arXiv:2605.23321 (first public version 2026-05-22), especially the cyclic-frame definitions, Theorem 3 and Proposition 4.1. https://arxiv.org/abs/2605.23321 ; accessible author-posted full text: https://www.researchgate.net/publication/405221506_Arrow-Type_Impossibility_for_Genuinely_Modal_Judgments
2. *Sharp half-circumference modal stabilization on two-colored cycles*, published result, 2026-10-12. https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-sharp-half-circumference-modal-stabilization-on-two-colored-cycl--eac9243128cc
3. *Reachability normal form for multiple modal reductions in pure necessitation*, published result, 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-reachability-normal-form-for-multiple-modal-reductions-in-pure-n--f7b79fec74bf
4. *Noncontingency on finite paths: exact small-frame algebras and an unbounded depth hierarchy*, published result, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-noncontingency-on-finite-paths-exact-small-frame-algebras-and-an--73acc7ce4a63
