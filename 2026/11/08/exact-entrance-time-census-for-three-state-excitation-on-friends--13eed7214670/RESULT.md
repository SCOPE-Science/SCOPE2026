# Exact entrance-time census for three-state excitation on friendship graphs

## Finding
For each integer \(r\ge1\), let \(W_r\) be the friendship graph made by identifying one vertex of \(r\) copies of the triangle. Its vertices consist of a common hub \(h\) and \(r\) *labelled pairs* \((u_j,v_j)\), where \(u_jv_j\), \(hu_j\), and \(hv_j\) are the only edges. Apply synchronous three-state Greenberg–Hastings excitation: excited \(1\) becomes refractory \(2\), refractory \(2\) becomes resting \(0\), and resting \(0\) becomes \(1\) exactly when an adjacent vertex is in state \(1\).

Let \(T(x)\) be the smallest nonnegative integer for which the iterate \(F^{T(x)}(x)\) is periodic, and let \(P(x)\) be its least period. Let \(N_{t,p}(r)=|\{x:T(x)=t,\ P(x)=p\}|\), counting all \(3^{2r+1}\) labelled initial colorings. **The complete census** is

| \(t\) | \(p\) | \(N_{t,p}(r)\) |
|---:|---:|---:|
| 0 | 1 | \(1\) |
| 0 | 3 | \(3\cdot3^r-3\) |
| 1 | 1 | \(2\cdot4^r-1\) |
| 1 | 3 | \(6^r-4^r-3^r+1\) |
| 2 | 1 | \(7^r\) |
| 2 | 3 | \(9^r-7^r-3^r+1\) |
| 3 | 1 | \(7^r-4^r+3^r\) |
| 3 | 3 | \(9^r-7^r-3^r+1\) |
| 4 | 1 | \(7^r-4^r-3^r\) |
| 4 | 3 | \(9^r-7^r-6^r+4^r\) |

All other classes are empty. Consequently, \(F^7=F^4\) for every \(r\ge1\); the sharp maximum entry time is \(3\) when \(r=1\), and \(4\) for every \(r\ge2\). There is exactly one fixed point (all resting) and exactly \(3^r-1\) distinct primitive three-cycle orbits. The exact attraction-basin totals are \(3\cdot7^r\) for the fixed point and \(3(9^r-7^r)\) for the three-cycles.

For independent uniform initial states, \(\Pr(P=3)=1-(7/9)^r\). Conditioned on \(P=3\), the time of first periodic entry converges to the uniform distribution on \(\{2,3,4\}\): for each \(t\in\{2,3,4\}\),
\[
\lim_{r\to\infty}\Pr(T=t\mid P=3)=\frac13.
\]
The equality \(N_{2,3}(r)=N_{3,3}(r)\) holds for every \(r\ge1\).

## Assumptions and scope
The graph is finite, undirected and simple; petals are distinguishable and the two vertices in each petal are distinguishable in the labelled state count. The excitation threshold is one, updates are parallel, and no spontaneous excitation is permitted. The result is valid for all \(r\ge1\), with no assertion for other update rules or graphs.

## Proof
**Exact support reduction.** At time \(s\), write the two petal states in unordered form as one of the six types \(00,01,02,11,12,22\). For a given hub state, the next *unordered* petal type depends only on its old type, because each petal vertex sees just the hub and its partner. In this type order, the transition tables are

| Old hub state | Image indices for types \(00,01,02,11,12,22\), indexed \(0\) through \(5\) |
|---|---|
| \(0\) | \((0,4,0,5,2,0)\) |
| \(1\) | \((3,4,1,5,2,0)\) |
| \(2\) | \((0,4,0,5,2,0)\) |

The next hub state is \(2\) from state \(1\), \(0\) from state \(2\), and from state \(0\) is \(1\) precisely when at least one present petal type contains an excited vertex. Thus the hub and the nonempty *support* \(S\subseteq\{00,01,02,11,12,22\}\) form a deterministic quotient with exactly \(3(2^6-1)=189\) states. Identical type classes remain identical, so this quotient is exact for the evolution of the support.

**Finite dynamical lemma.** Direct composition of the displayed six-type transition maps for the 189 possible hub/support pairs gives exactly the following signature counts, in the same order as the ten rows above:
\[
(1,6,13,6,31,30,27,30,21,24).
\]
Every quotient trajectory reaches a cycle within four steps, and every such cycle has period one or three. This is a *finite exhaustive statement*, not a statistical computation. Its complete 189-row transition and classification certificate is supplied in `state_certificate.csv`; the stand-alone `verify_friendship.py` recomputes every transition and every first-entry time directly from the displayed rule. To exclude the possibility that forgetting the order inside each petal hides an extra period or changes entry time, that checker also composes the **ordered** pair transition through the full period of every recurrent quotient signature and verifies that each ordered petal state returns unchanged. Equivariance under swapping the two vertices handles the other orientation. Because a labelled periodic state necessarily has periodic quotient, this proves equality of labelled and quotient entry times and least periods for every initial state.

**Lifting from support types to labelled configurations.** The six unordered types have respectively \(w=(1,2,2,1,2,1)\) labelled realizations per petal. For any nonempty support \(S\), the number of length-\(r\) ordered sequences of petal states using *exactly* that support is the exact inclusion–exclusion formula
\[
 A_r(S)=\sum_{U\subseteq S}(-1)^{|S|-|U|}\Bigl(\sum_{a\in U}w_a\Bigr)^r.
\]
The hub itself has one specified state in each quotient signature. Sum \(A_r(S)\) over signatures in each temporal class. The supplied checker evaluates this finite sum symbolically, collecting coefficients of \(k^r\) for \(1\le k\le9\), and obtains precisely the ten expressions in the theorem. This establishes them simultaneously for **every positive integer \(r\)**; enumeration of a few graph sizes is not used as an infinite-family argument. The ten expressions sum to \(3\cdot9^r\).

All recurrent signatures with period one reduce to the all-rest configuration, so there is one fixed state. The number of period-three states is \(3(3^r-1)\), hence the number of primitive three-cycle orbits is \(3^r-1\). The formulas give positive four-step classes when \(r\ge2\), establishing sharpness; at \(r=1\) both four-step classes vanish and a three-step class is nonempty. The relation \(F^7=F^4\) follows from the common period divisor three and the four-step bound.

**Asymptotics.** Adding the five period-one formulas yields exactly \(3\cdot7^r\). Among period-three initial states, each of the classes at times two, three and four has leading term \(9^r\), whereas times zero and one have lower exponential bases. Dividing by \(3(9^r-7^r)\) gives the asserted limiting conditional probabilities.

## Verification
`verify_friendship.py` is a deterministic standard-library proof checker over all 189 quotient states. It reconstructs `state_certificate.csv`, checks the exact symbolic coefficient identities, and verifies ordered-pair lifting on every recurrent quotient signature. Its captured output is `proof_log.txt`. `check_graph.py` independently constructs adjacency lists and evolves every labelled initial coloring for \(r=1,2,3,4,5\), totaling 199,287 configurations; its output is `graph_log.txt`. The latter is a corroborating check, not an infinite proof.

Reproduce by running `python3 verify_friendship.py` followed by `python3 check_graph.py` in the folder containing the bundled artifacts. The proof's finite state transitions and inclusion–exclusion are exact. No external data, random inputs, or third-party packages are required.

## Relationship to prior work
Gravner, Lyu and Sivakoff (arXiv:1610.07320v1, 2016, Theorems 3 and 5) already characterize synchronization through the circulation of initial colors around graph cycles and prove a general diameter-bound for synchronized states; their upper bound \((7/9)^r\) on synchronization probability specializes to the friendship graph. In fact, their Theorem 3 together with the triangular block structure already implies the aggregate eventual-basin sizes \(3\cdot7^r\) and \(3(9^r-7^r)\). **These aggregate counts and the general circulation criterion are not claimed as novel.** The added assertion is the ten-class exact first-entry-time distribution, including the sharp positive fourth-entry layers and the conditional one-third entrance law. The paper's full text was checked for friendship/windmill and exact first-entry formulas, and its relevant theorems and proofs were inspected.

Durrett and Griffeath (arXiv:patt-sol/9303002, originally submitted 1993-03-22) study excitable cellular automata and phase transitions on spatial lattices rather than this labelled friendship-graph entrance-time census; only the accessible abstract was material for this comparison. Prior classifications for wheel graphs, complete tripartite graphs, and one-hub pineapple graphs address different underlying graph families and do not imply these ten formulas by graph specialization. Absence of a matching searchable claim is not a proof of historical novelty.

## Limitations
The general synchronization mechanism and aggregate basin totals are established prior mathematics. The contribution is limited to a sharply defined graph family and exact transient census. The finite exhaustive lemma is independently reproducible but not externally certified. A previously unindexed source may contain an equivalent formula; independent literature audit has not been performed.

## References
1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (public 2016-10-24), especially Theorems 3 and 5; https://arxiv.org/pdf/1610.07320.
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (submitted 1993-03-22); https://arxiv.org/abs/patt-sol/9303002.
