# Period-three rigidity of perfect edge domination on open ladders

## Finding
For every integer \(n\ge 2\), let \(L_n=P_2\square P_n\) denote the labelled two-row open ladder with \(n\) columns and \(3n-2\) edges. An edge subset \(F\subseteq E(L_n)\) is a *perfect edge dominating set* (PEDS) when every edge outside \(F\) shares an endpoint with exactly one edge in \(F\). Define its cardinality enumerator by
\[
\Phi_n(z)=\sum_{F\text{ a PEDS of }L_n}z^{|F|}.
\]
Then, with the two vertex rows and their left-to-right order fixed,
\[
\boxed{\Phi_n(z)=z^{3n-2}+\begin{cases}4z^n,&n\equiv2\pmod 3,\\2z^n,&n\equiv0,1\pmod3.\end{cases}}
\]
Thus every nontrivial PEDS has exactly \(n\) edges; precisely four such sets occur for \(n\equiv2\pmod3\), and precisely two otherwise. The remaining PEDS is the entire edge set. In particular the minimum PEDS cardinality is \(n\), and the ladder has no dominating induced matching.

Equivalently, the complete bivariate length/cardinality generating function is
\[
\boxed{\sum_{n\ge2}\Phi_n(z)t^{n-2}=\frac{z^4}{1-z^3t}+\frac{4z^2+2z^3t+2z^4t^2}{1-z^3t^3}.}
\]
The theorem also classifies every PEDS constructively by the six-state periodic automaton in the proof.

## Assumptions and scope
The graphs are undirected, finite, simple, and have labelled vertices \((i,r)\), with \(0\le i<n\) and \(r\in\{0,1\}\). The edges are the rungs \((i,0)(i,1)\) and the two horizontal edges \((i,r)(i+1,r)\) for \(0\le i<n-1\). The definition constrains only edges outside \(F\); adjacent selected edges are allowed. These sets are not to be confused with perfect matchings, perfect vertex dominating sets, or dominating induced matchings. The polynomial counts edge subsets, not symmetry classes.

## Proof
**1. Three vertex states.** For a candidate \(F\), write \(d_F(v)\) for its number of incident selected edges. On every omitted edge \(uv\), the PEDS condition is exactly \(d_F(u)+d_F(v)=1\). Assign a vertex state \(W\), \(Y\), or \(B\) according as \(d_F(v)=0\), \(d_F(v)=1\), or \(d_F(v)\ge2\). Since a vertex in state \(B\) cannot be incident with an omitted edge, the following conditions hold:

- Every neighbor of \(W\) is \(Y\).
- Every \(Y\) has exactly one neighbor in \(\{Y,B\}\), and all its other neighbors are \(W\).
- Every neighbor of \(B\) lies in \(\{Y,B\}\).

Conversely, any assignment of these three states satisfying these local conditions gives one PEDS: select exactly the edges whose endpoints both lie in \(\{Y,B\}\). Then \(W\) has selected degree zero, \(Y\) has selected degree one, and \(B\) has selected degree equal to its graph degree (at least two). Every omitted edge joins \(W\) and \(Y\) and therefore has exactly one adjacent selected edge. The reconstruction is unique, so the color assignments and PEDS are in bijection.

**2. Complete finite-state reduction.** A column state is an ordered top/bottom pair of elements of \(\{W,Y,B\}\), giving nine possibilities. An automaton state is an ordered pair \((a,b)\) of adjacent columns, giving \(81\) possibilities. It is an initial state when the two vertices of \(a\), whose graph degree is two, satisfy the three local conditions using the rung and their neighbor in \(b\). It is final when the same condition holds for \(b\) with its neighboring column \(a\). A transition \((a,b)\to(b,c)\) is permitted exactly when the two vertices in the middle column \(b\) satisfy the conditions using their rung and their horizontal neighbors in \(a,c\).

Direct application of these explicit three-valued predicates gives \(13\) initial states, \(13\) final states, \(15\) states reachable from an initial state, and \(15\) states that can reach a final state. To make that finite reduction transparent, writing \(a|b\) for the pair \((a,b)\), the forward-reachable state list is

`WY|YW, WY|YY, WY|YB, YW|WY, YW|YY, YW|BY, YY|WW, YB|WY, YB|WB, BY|YW, BY|BW, BB|YY, BB|YB, BB|BY, BB|BB`.

The backward-reachable list is

`WW|YY, WY|YW, WY|YB, WB|YB, YW|WY, YW|BY, YY|WY, YY|YW, YY|BB, YB|WY, YB|BB, BW|BY, BY|YW, BY|BB, BB|BB`.

Their intersection has exactly seven states. Its complete directed transition graph is the isolated loop \((BB,BB)\to(BB,BB)\), together with this directed six-cycle:
\[
\begin{aligned}
&(WY,YB)\to(YB,WY)\to(WY,YW)\\
&\quad\to(YW,BY)\to(BY,YW)\to(YW,WY)\to(WY,YB).
\end{aligned}
\]
On that six-cycle, precisely the positions \(0,1,3,4\) (numbered in the displayed order) are initial, and precisely the same four positions are final. The loop \((BB,BB)\) is both initial and final. The exhaustive \(81\)-state computation and the exact seven-state transition check are reproduced from the local predicates in the accompanying self-contained verifier; this is a finite exhaustive lemma, not an inference from a bounded sample of ladder lengths.

**3. Count and weight.** A ladder of length \(n\) corresponds to a walk of \(n-2\) transitions from an initial pair to a final pair. The \((BB,BB)\) loop gives the all-black coloring, hence the full edge set of cardinality \(3n-2\). A proper coloring is uniquely determined by its starting position \(i\in\{0,1,3,4\}\) on the six-cycle and is permitted if \(i+n-2\pmod6\) also belongs to that set. Counting these possibilities gives four when \(n\equiv2\pmod3\) and two in the other two congruence classes.

Each proper coloring selects exactly \(n\) edges. Indeed, for each of the four possible initial phases, direct application of the edge-selection rule to the six initial lengths \(n=2,3,4,5,6,7\) (when the phase is terminal) gives \(|F|=n\). Extending any of these walks by a full six-period block adds exactly six selected edges, as is checked using the six displayed column states and their horizontal and rung edges. Every possible longer walk is obtained this way. This proves the cardinality assertion at all lengths, and summing the resulting period-three counts gives the displayed generating function.

Finally, every nontrivial walk starts at one of the four two-column pairs containing a \(B\) vertex. Its selected edges therefore contain adjacent edges at that vertex, so none is a dominating induced matching. The full edge set is not an induced matching either. The minimum \(n\) is strictly below \(3n-2\) for all \(n\ge2\).

## Verification
Run `python3 artifacts/verify.py` using only the Python standard library. The verifier directly constructs the \(81\)-state automaton from the three local rules, obtains the exact reachable/co-reachable seven-state reduction and six-cycle, and checks the six-column selected-edge increment for every allowed phase. As an independent check of the state interpretation, it exhaustively examines every subset of the \(3n-2\) edges at \(2\le n\le7\), evaluates the PEDS condition directly, and compares the complete cardinality distribution. Larger calculated lengths are corroboration only; the all-parameter proof is the finite-state argument above.

## Relationship to prior work
Lin, Lozin, Moyano, and Szwarcfiter (2017/2018) established the three-state vertex characterization of perfect edge domination, used here as a starting point, and studied complexity and solvable graph classes. Grippo, Lin, Moyano, and Vera (2026) investigate counting PEDS in several graph classes and provide general algorithms on generalized series-parallel graphs, a class that contains ladders. A general counting algorithm does not by itself state the present explicit three-periodic coefficient formula, the classification of every subset, or the absence of an efficient edge dominating set. The existing results and methods are credited, not claimed as new.

The theorem is specific to the **open** ladder. A previously obtained calculation for **cyclic** ladders concerns a different graph family; deleting the closing horizontal edges changes the PEDS condition on boundary edges and does not logically turn that cyclic calculation into the open-boundary theorem.

## Limitations
No classification is asserted for wider grids, twisted closures, weighted edges, or arbitrary series-parallel graphs. The closest 2026 counting preprint's full text could not be inspected here; a differently worded special-case derivation within it remains a historical-priority risk.

## References
1. M. C. Lin, V. Lozin, V. A. Moyano and J. L. Szwarcfiter, *Perfect Edge Domination: Hard and Solvable Cases*, arXiv:1705.08379 (first public 2017-05-23), published in *Annals of Operations Research* (2018). Open full text: https://wrap.warwick.ac.uk/id/eprint/92507/13/WRAP-perfect-edge-domination-hard-solvable-cases-Lozin-2017.pdf.
2. L. N. Grippo, M. C. Lin, V. Moyano and C. Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894 (first public 2026-07-04), https://arxiv.org/abs/2607.03894.
3. L. N. Grippo, M. C. Lin and C. Vera, *Perfect Edge Domination in \(P_6\)-free Graphs and in Graphs Without Efficient Edge Dominating Sets*, arXiv:2509.04598 (first public 2025-09-04), https://arxiv.org/abs/2509.04598.
