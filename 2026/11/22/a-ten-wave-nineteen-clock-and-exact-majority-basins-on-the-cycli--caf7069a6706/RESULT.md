# A ten-wave nineteen-clock and exact majority basins on the cyclic tournament of order nineteen


## Finding
Let \(T\) be the cyclic tournament on \(\mathbb Z/19\mathbb Z\) with arcs from \(i\) to the nine vertices \(i+1,\ldots,i+9\). In synchronous binary out-neighbor majority dynamics, **every one of the \(2^{19}=524{,}288\) labelled states becomes periodic within four updates**, sharply:
\[
F^{23}=F^4,\qquad F^{22}\ne F^3.
\]
There are exactly two fixed points (the unanimous states) and exactly **ten primitive temporal cycles, all of length nineteen**. These cycles are the rotations of the ten one-block words \(1^k0^{19-k}\) for \(5\le k\le14\), one cycle for each \(k\). Every such word shifts by five sites per update, in the direction corresponding to \(i\mapsto i+5\) in the updated coordinate rule. No primitive two-, four-, or other cycles occur.

Each unanimous fixed point has an attraction basin of **137,903** labelled initial configurations. The complete basin size of each length-nineteen *temporal orbit* is:

| Number of ones \(k\) in a rotating block | Full attraction-basin size |
|---:|---:|
| 5 | 13,376 |
| 6 | 18,202 |
| 7 | 24,947 |
| 8 | 34,200 |
| 9 | 33,516 |
| 10 | 33,516 |
| 11 | 34,200 |
| 12 | 24,947 |
| 13 | 18,202 |
| 14 | 13,376 |

The two consensus basins together contain 275,806 states; the ten rotating-wave basins together contain 248,482. The exact first-periodic-entry distribution is:

| Least first-entry update | Eventually fixed | Eventually period nineteen |
|---:|---:|---:|
| 0 | 2 | 190 |
| 1 | 90,744 | 161,120 |
| 2 | 142,956 | 85,272 |
| 3 | 38,798 | 1,900 |
| 4 | 3,306 | 0 |

These rows sum to 524,288; exactly **3,306 states** require the fourth update, and state mask 21391 is an explicit example.

The numerically comparable, but dynamically distinct, Paley tournament of order nineteen (quadratic-residue offsets) was already classified in prior work: it has two fixed states, 342 primitive period-four cycles and eighteen primitive period-nineteen cycles, with sharp entry depth seven and consensus-basin population 516,764. Thus two vertex-transitive, regular nineteen-vertex tournaments with identical out-degree nine have sharply different periodic spectra and vastly different consensus attraction. **The Paley counts are quoted as prior work, not a new finding.**

## Assumptions and scope
The graph has vertices \(i\in\mathbb Z/19\mathbb Z\), with one arc \(i\to i+j\) for every \(j\in\{1,2,\ldots,9\}\). For every pair of distinct vertices exactly one of the two possible arcs occurs, so this is a loopless regular tournament with out-degree nine. A configuration is \(x\in\{0,1\}^{19}\), and its synchronous update is
\[
F(x)_i=\begin{cases}1,&\sum_{j=1}^9x_{i+j}\ge5,\\0,&\sum_{j=1}^9x_{i+j}\le4,\end{cases}
\]
with subscripts modulo nineteen. All out-degrees are odd, so tie-handling is irrelevant. Encode \(x\) as the integer \(\sum_{i=0}^{18}2^ix_i\); every such integer from zero through 524,287 is included. A **primitive period** is the least positive iterate returning an already periodic configuration to itself. The **first-entry time** is the least nonnegative iterate at which any periodic state is reached. Each attraction basin counts all starting states eventually entering one *temporal orbit*, including all nineteen phases of that orbit; there are no spatial-symmetry or complement quotients in basin sizes.

For comparison, the Paley tournament has offset set \(Q=\{1,4,5,6,7,9,11,16,17\}\) of nonzero quadratic residues modulo nineteen, also with nine out-neighbors per vertex. Distinct edge sets mean the two state-update operators are not identified.

## Proof
**1. Finite exhaustive decomposition.** `verify_functional.py` independently constructs the successor of every integer state \(x\in\{0,\ldots,2^{19}-1\}\), using nine-bit neighborhood masks and integer bit counts. It traverses every component of the deterministic functional graph with a path dictionary, detects each cycle by the first repeated state, propagates the least first-entry depth and exact primitive period backward, and records the root cycle for every state. Every input is assigned to exactly one cycle or to its transient predecessor tree; the algorithm has no sampling, depth cutoff or unexamined boundary state. The `cycles_by_period` dictionary is exactly `{1: 2, 19: 10}`. The complete output `output_functional.json` records every entry-depth/period population, the ten individual basin sizes, and the minimal mask of maximum-depth states. As a finite proof for this exactly specified nineteen-vertex system, exhaustive enumeration is conclusive; it asserts nothing unproved about arbitrary orders.

**2. Shape of all oscillations.** Let \(R_s\) act by \((R_sx)_i=x_{i+s}\), and write \(a_k=1^k0^{19-k}\) for the first \(k\) sites in opinion one and remaining sites in opinion zero. For each \(k\in\{5,\ldots,14\}\) and each phase \(s\in\mathbb Z/19\mathbb Z\), direct evaluation of the nine terms in the defining majority sum gives
\[
F(R_sa_k)=R_{s+5}a_k.
\]
The checker verifies this identity for all 190 pairs \((k,s)\) rather than inferring it from a short simulation. Because nineteen is prime and \(a_k\) is nonunanimous, \(R_5\) has exact order nineteen on these words. Thus each \(k\) yields one distinct temporal nineteen-cycle. The finite functional-graph enumeration proves **exhaustively** that these ten cycles and the two unanimous equilibria are all recurrent configurations. No unlisted oscillation can be hidden by period testing.

**3. Sharp cutoff and attraction basins.** In the independent C++ implementation `verify_direct.cpp`, every transition is recomputed through nine separate vertex-bit tests, rather than reusing the Python masks or its functional-graph traversal. For every one of the 524,288 input masks, that program tests at each step from zero through four whether the current state returns after nineteen more updates. It verifies \(F^{23}(x)=F^4(x)\) for all inputs and finds **3,306** for which \(F^{22}(x)\ne F^3(x)\), proving the exact global cutoff of four. It independently assigns every state to one of the two unanimous states or one of the ten block-length nineteen-cycles, counts the full orbit basins, and recovers every entry-time/period row listed above. Since every input is examined, the total-basin partition is complete. The two consensus basin sizes agree by global bit-complement symmetry, and the listed ten wave sizes occur in complement pairs \(k\) and \(19-k\).

**4. Structural relationship to the centered rule.** If \(M\) is the ordinary centered majority rule with radius four, \(M(x)_i=\operatorname{maj}(x_{i-4},\ldots,x_{i+4})\), then \(F=R_5M=MR_5\). Hence \(F^t=R_{5t}M^t\). This gives a genuine equivalence to a rotating-frame majority automaton and is explicitly accounted for when comparing related published cellular-automaton theorems. In particular, a spatially fixed nonunanimous block under \(M\) becomes a travelling nineteen-cycle under \(F\), not a new type of nonlinear rule. The **exact recurrent set, sharp finite entry cutoff and full attraction basins at this natural parameter** are the precise assertions being established; a mere reinterpretation of the centered rule is not offered as the finding.

**5. Published baseline.** The second independent program additionally reconstructs the Paley offsets as quadratic residues and recomputes from all 524,288 states the previously published consensus population 516,764, the period-four basin population 6,156, the period-nineteen population 1,368, and the sharp seven-step cutoff. It counts the 1,368/4=342 period-four and 342/19=18 period-nineteen primitive cycles. This is a statement-to-statement comparison with prior work, not part of the cyclic-tournament originality claim.

## Verification
With Python 3, run `python3 verify_functional.py --json output_functional.json` in a directory containing the extracted package files; the program prints its complete independently generated census. With a C++17 compiler, run `c++ -std=c++17 -O2 -Wall -Wextra verify_direct.cpp -o verify_direct && ./verify_direct`. `output_direct.txt` records the second program's expected standard output. Both programs were replayed directly from their embedded source contents. The Python path checker assigns all 524,288 labelled inputs; the C++ state checker independently inspects every input and verifies the global iterate identity and its sharp predecessor failure. Scientific checks do not rely on interpreting log messages alone: the source code implements the exact transitions, coverage loops, basin classification and assertions. The machine-readable table in `output_functional.json` is a cross-check, not a substitute for the programs.

## Relationship to prior work
The natural baseline is [1], which proves a no-two-cycle theorem for every tournament and exhaustively classifies majority dynamics on **Paley** tournaments of orders three, seven, eleven and nineteen. Its full text was compared: it does not classify the distinct **consecutive-offset cyclic tournament** at order nineteen, and indeed its Paley-19 period-four recurrent population is nonzero, whereas the consecutive-offset system has none. Its general no-two-cycle lemma and regular-tournament unanimity lemma do imply parts of the present outcome; these are credited and not claimed new.

The broader one-dimensional majority cellular-automaton theory of Nakar and Ron [2] proves structural restrictions on eventual fixed points and two-cycles of centered radius-\(r\) majority. Our rotating-frame identity shows why that literature is directly relevant. Their paper does not give the exact all-state first-entry histogram, the ten full basin populations or the published-Paley contrast for the radius-four, nineteen-site consecutive-offset tournament. An earlier published one-sided *three-tap* majority study [3] gives complete recurrent formulas at different neighborhood width; it does not specialize to this **nine-tap** rule. The symmetric majority preimage result [4] concerns predecessor multiplicities of two-cycles at radius three and does not supply these radius-four basin counts. Benjamini et al. [5] concern **undirected** majority graphs and their eventual periods and cannot rule out directed nineteen-cycles. Jørgensen [6] concerns algebraic structure of normally regular digraphs and the Paley tournament, not these dynamical basins.

The consecutive-offset tournament is a classical canonical regular tournament, rather than an arbitrary selected finite graph; its contrast with the equally regular Paley tournament motivates the exact order-nineteen case. This is not a general theorem for all odd orders or all shifted majorities.

## Limitations
The exhaustive results are confined to the directed, unweighted, nineteen-site, nine-out-neighbor rule precisely defined above; they do not prove an analogous ten-cycle classification for any other order, nor that the consensus-versus-wave effect persists asymptotically. They do not establish priority against unpublished, unindexed or inaccessible older computations. Most importantly the rotating-frame identity and general qualitative properties are already known in wider majority-automaton theory; the claim of originality is restricted to the **exact** order-nineteen oscillation-basin/entry-time census and the explicit graph-structure contrast with Paley-19. Independent mathematical validation has not been performed.

## References
[1] *A forbidden two-clock and the Paley-19 revival of majority oscillations*, publicly archived finding (2026-11-17). https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-forbidden-two-clock-and-the-paley-19-revival-of-majority-oscil--13a06d889156

[2] Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, first arXiv version 2022-05-18; Sections 1–3 and theorem statement. https://arxiv.org/abs/2205.08972

[3] *Missing maximal individual periods in one-sided majority waves on binary rings*, published result (2026-11-17). https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-missing-maximal-individual-periods-in-one-sided-majority-waves-o--57acbeca82a7

[4] *Sharp radius-three onset of transient attraction to majority-automaton two-cycles*, published result (2026-11-01). https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-radius-three-onset-of-transient-attraction-to-majority-aut--624ce6cd08d3

[5] I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first public arXiv version 2014-05-11. https://arxiv.org/abs/1405.2486

[6] L. K. Jørgensen, *Normally Regular Digraphs*, first public arXiv version 2014-10-30, Section 1. https://arxiv.org/abs/1410.8424
