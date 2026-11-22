# A sharp height–leaf Pareto tradeoff in three-state unary–binary tree synchronization

## Finding

Let \(Q=\{0,1,2\}\), with a unary transition \(u:Q\to Q\) and an ordered binary transition \(b:Q^2\to Q\). A **full-context term** is a finite rooted term with these symbols at internal nodes and an independent, freely varying state variable at every leaf. It is **strongly synchronizing** if its root state does not depend on any leaf assignment. Let \(h\) denote its height (the greatest number of internal nodes on a root-to-leaf path) and \(\ell\) its number of independent leaves. Minimize \(h\) and \(\ell\) separately over all strongly synchronizing terms for a given automaton; if no such term exists, call it nonsynchronizing.

**Theorem (complete labeled census).** Among the exactly \(3^{12}=531441\) complete, labeled three-state automata with precisely this unary and this binary symbol, exactly \(242997\) strongly synchronize. For **exactly \(198\)** of them, no single term simultaneously minimizes height and leaf count; precisely \(18\) have Pareto-minimal pairs \(\{(1,2),(2,1)\}\), and precisely \(180\) have Pareto-minimal pairs \(\{(3,4),(4,3)\}\). Every other synchronizing automaton has just one Pareto-minimal height–leaf pair. Every synchronizing automaton has shortest height at most \(4\) and smallest leaf count at most \(4\), and both maxima occur. Among the \(8712\) automata whose minimum height is \(4\), precisely \(5220\) have minimum leaf count \(3\), and \(3492\) have minimum leaf count \(4\).

The **full distribution of the separately optimized** pair \((h_{\min},\ell_{\min})\) is:

| Minimum height | Minimum leaves | Number of labeled automata |
| ---: | ---: | ---: |
| undefined | undefined | 288444 |
| 1 | 1 | 59067 |
| 1 | 2 | 54 |
| 2 | 1 | 118080 |
| 2 | 2 | 14088 |
| 2 | 3 | 1572 |
| 2 | 4 | 1056 |
| 3 | 2 | 35448 |
| 3 | 3 | 3156 |
| 3 | 4 | 1764 |
| 4 | 3 | 5220 |
| 4 | 4 | 3492 |

The pair of separate minima need not be attained by a single term: that phenomenon is exactly the source of the \(198\) tradeoff cases. The full Pareto-frontier count is reproduced in `verify_pareto.cpp`.

## Assumptions and scope

States are labeled and symbols are not interchanged (their arities differ). Transitions are total, the binary operation is ordered, and there are no nullary symbols. At each leaf the full set \(Q\) of possible assigned states is available, independently of the other leaves. Images of terms are nonempty subsets of \(Q\); a term synchronizes if and only if its image is a singleton. There is no ground-term shortcut, no weak-context interpretation, and repeated variable labels are not allowed to impose dependencies. This is the strong/full-context notion of synchronization.

For nonempty \(A,B\subseteq Q\), define \(U(A)=\{u(a):a\in A\}\) and \(B(A,B)=\{b(a,c):a\in A,c\in B\}\). Independence of variables makes these exactly the image sets of unary and binary compositions.

## Proof

**Finite height bound.** Starting with \(Q\) at height zero, close the collection of attainable nonempty state-image subsets under \(U\) and \(B\). If one height step produces no new subset, the collection is closed and cannot grow later. Hence before the first singleton appears, each height adds at least one new nonsingleton subset. For three states there are precisely \(2^3-3-1=4\) nonempty nonsingleton subsets (the full set and three two-element sets). Since \(Q\) occurs at height zero, a singleton, when attainable, first occurs by height \(4\). This bound is over *all terms*, with no leaf restriction.

**Leaf-cost completeness.** On the seven nonempty image subsets maintain a cost equal to the smallest number of independent leaves producing that image. Initialize the cost of \(Q\) to one and others to infinity. Relax the unary rule \(c(U(A))\le c(A)\) and the binary rule \(c(B(A,B))\le c(A)+c(B)\) until no cost improves. Every finite relaxation is realized by a term with distinct fresh variables, so the final costs cannot underestimate the actual minimum. Conversely, induction on term size shows every possible term cost is bounded below by this relaxation's fixed point, so they cannot overestimate it. An improving relaxation always strictly decreases a positive integer, and the implementation explicitly checks convergence (the seven-state search is finite). Thus this computes the true **unrestricted** leaf minimum, not merely the minimum within a height cap.

**Complete parameter enumeration.** Every unary map has a unique three-digit base-three code; every ordered binary table has a unique nine-digit code. The two independent programs enumerate all \(3^3\cdot3^9\) choices. `verify_height_leaves.cpp` constructs all seven nonempty image masks for each table, exhaustively computes the first singleton height by closure, and computes minimum leaves by the unrestricted positive-cost relaxation above. It asserts every displayed histogram entry and the total \(531441\). `verify_pareto.cpp` independently decodes the tables, uses a different recurrence to enumerate *all* image masks attainable at height at most \(h\) with exactly \(\ell\) leaves for \(0\le h\le4\), \(1\le\ell\le4\), and derives the nondominated feasible pairs. The height argument and independently checked leaf-bound ensure that the bounded dynamic program loses no possible Pareto point; it asserts exactly the \(198\) two-point frontiers and that no third type occurs. Its mutually exclusive frontier counts add to \(242997\). This exhausts every labeled machine, not a sample.

More explicitly, writing \(\mathcal S_{h,\ell}\) for all images realizable at height at most \(h\), with exactly \(\ell\) leaves, the initial conditions are \(\mathcal S_{0,1}=\{Q\}\), \(\mathcal S_{0,\ell}=\varnothing\) for \(\ell>1\), and the exhaustive recurrence is
\[
\mathcal S_{h+1,\ell}=\mathcal S_{h,\ell}\cup U(\mathcal S_{h,\ell})\cup\bigcup_{i=1}^{\ell-1} B(\mathcal S_{h,i},\mathcal S_{h,\ell-i}).
\]
The operations on collections apply \(U\) or \(B\) to all constituent subsets. The recursive equation holds in both directions by inspecting the root operation of any term and by combining terms on disjoint fresh variables.

**Explicit strict height–leaf tradeoff.** Put
\[
u=(2,2,1),\qquad
b=\begin{pmatrix}0&1&0\\1&2&0\\0&0&0\end{pmatrix}.
\]
This automaton has the two strongly synchronizing full-context terms
\[
T=b(b(u(x_1),u(x_2)),b(u(x_3),u(x_4)))
\quad\text{and}\quad
V=u(b(x_1,b(u(x_2),u(x_3)))).
\]
The first has image \(\{0\}\), height \(3\), and four leaves; the second has image \(\{2\}\), height \(4\), and three leaves. The complete recurrence establishes that there is **no** synchronizing term with height at most \(3\) and at most three leaves, nor any with fewer than three leaves or height below three. This witness is among the \(180\) deep tradeoff automata.

**First state-size boundary.** With one state, the leaf term already synchronizes. With two states, a nonconstant unary map is a permutation and sends the full set to itself; a nonconstant binary map has full image. Thus unless the unary or binary operation itself has a singleton image, every full-context image remains the entire state set, and no synchronization occurs. When a basic operation is constant, a height-one term synchronizes; a unary constant uses one leaf and dominates every other term, while a binary constant uses two leaves and no nonconstant unary can reduce leaf count. No two-state machine exhibits a height–leaf conflict. The three-state witness proves that three is the first possible state size.

## Verification

Both standalone C++17 files compile with any conforming compiler, require only the standard library, and are independent implementations:

```sh
g++ -O2 -std=c++17 verify_height_leaves.cpp -o verify_height_leaves
./verify_height_leaves
g++ -O2 -std=c++17 verify_pareto.cpp -o verify_pareto
./verify_pareto
```

Expected assertions finish with `HEIGHT_LEAVES_OK total=531441 synchronizing=242997 height4=8712` and `PARETO_OK total=531441 nonsync=288444 conflict=198 deep=180`. Both enumerate every complete labeled operation pair; neither calls outside libraries or uses randomized sampling. The arithmetic bound and recursive closure make these terminating computations exhaustive certificates for the finite theorem. They do not imply a formula for larger state sets or more symbols.

## Relationship to prior work

Blažej, Janoušek and Plachý give the general strong-synchronization height upper bound \(2^n-n-1\) and constructions over larger ranked alphabets. This known upper bound immediately yields the height-four **upper bound** when \(n=3\), but does not determine this complete small-ranked-alphabet census, the minimum numbers of independent leaves, or the existence and number of incompatible minima. A later published four-state, one-unary/one-binary example attains height eleven, but its four-state extremal height does not imply a three-state height–leaf Pareto classification. Herrmann and Mörbitz (first posted 1 September 2026) investigate small constant ranked alphabets and establish subexponential reset-height lower bounds; the accessible abstract concerns growth in state count, not the finite distribution or leaf-count objective. The full text of that recent manuscript was not available for a complete priority comparison. The novelty claim is confined to the joint three-state Pareto classification and explicit first state-size tradeoff, not to the previously known universal bound.

## Limitations

The statistics count labeled unary/binary operation tables, not isomorphism classes. The results are exact only for three states and this ranked signature; the two-state nonexistence boundary is an auxiliary elementary proof. The theorem does not classify optimal term shapes, nor provide asymptotics, complexity bounds for arbitrary state sizes, or an independent outside audit. An unindexed equivalent census or an unavailable part of the recent primary manuscript could affect historical priority; neither is claimed ruled out.

## References

1. L. Herrmann and R. Mörbitz, *On smallest synchronizing terms over constant alphabets*, arXiv:2609.01184, first posted 1 September 2026. https://arxiv.org/abs/2609.01184
2. V. Blažej, J. Janoušek and Š. Plachý, *On the Smallest Synchronizing Terms of Finite Tree Automata*, International Journal of Foundations of Computer Science 37 (2026), 215–239, DOI: 10.1142/S0129054125410096. https://wrap.warwick.ac.uk/id/eprint/193962/
3. *Sharp four-state tree synchronization over two ranked symbols*, publicly accessible mathematical research record, 26 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-four-state-tree-synchronization-over-two-ranked-symbols--5734bc809a8e
