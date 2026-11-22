# Two-edge fault geometry changes the complete excitation clock census on cliques

## Finding
Fix an integer \(n\ge5\). From the labelled complete graph \(K_n\), delete exactly two edges. There are exactly two isomorphism types of deleted-edge patterns: **adjacent** edges \(\{0,1\},\{1,2\}\), or **disjoint** edges \(\{0,1\},\{2,3\}\). Under synchronous three-state Greenberg–Hastings excitation with states \(0\) (resting), \(1\) (excited) and \(2\) (refractory), let \(N_{t,p}\) count initial configurations having first periodic entry time \(t\) and eventual *least* period \(p\). Then **every** initial state is periodic by the fourth update, and the **entire exact all-order joint census** is:

| \((t,p)\) | Adjacent deleted edges | Disjoint deleted edges |
|---|---:|---:|
| \((0,1)\) | \(1\) | \(1\) |
| \((0,3)\) | \(3^n-6\cdot2^n+21\) | \(3^n-6\cdot2^n+15\) |
| \((1,1)\) | \(2^n-1\) | \(2^n-1\) |
| \((1,3)\) | \(2^n-14\) | \(2^n-16\) |
| \((2,1)\) | \(2^n+5\) | \(2^n+3\) |
| \((2,3)\) | \(2^n-12\) | \(2^n-8\) |
| \((3,1)\) | \(2^n\) | \(2^n-2\) |
| \((3,3)\) | \(2^n-12\) | \(2^n-8\) |
| \((4,1)\) | \(10\) | \(8\) |
| \((4,3)\) | \(2\) | \(8\) |

All other cells vanish. Consequently the adjacent-fault graph has **exactly two more primitive temporal three-cycle orbits** than the disjoint-fault graph, yet **six more initial configurations that ultimately extinguish**. Both effects hold at every \(n\ge5\):
\[
\begin{aligned}
Q_3^{\mathrm{adj}}&=3^{n-1}-2^{n+1}+7,&Q_3^{\mathrm{dis}}&=3^{n-1}-2^{n+1}+5,\\
E^{\mathrm{adj}}&=3\cdot2^n+15,&E^{\mathrm{dis}}&=3\cdot2^n+9.
\end{aligned}
\]
The terminal four-step shell, which is *sharp in both families*, has respectively \(10\) extinct and \(2\) three-periodic configurations for adjacent faults, versus \(8\) and \(8\) for disjoint faults. Thus edge-fault incidence changes both recurrence and the distribution of maximal delays, despite identical edge counts and asymptotically complete connectivity.

## Assumptions and scope
All graphs are simple, undirected, loopless, and labelled. In the adjacent case, the deleted edges meet at vertex \(1\); in the disjoint case their four endpoints are distinct. There are no other deleted edges. At every simultaneous update, \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) if and only if an *adjacent* vertex is currently in state \(1\); otherwise a resting vertex remains in state \(0\). Initial states are counted individually, without quotienting by graph automorphisms or spatial relabellings. The entry time \(t\) is the least nonnegative integer at which the full labelled state lies on a periodic orbit. A period-three orbit consists of three configurations; eventual period one means convergence to the all-rest state. Both graph families and the ten-row formula are asserted for all \(n\ge5\). The special four-vertex boundary is excluded because the disjoint-fault graph is \(C_4\) and has genuine four-periodic orbits.

## Proof
**1. A finite, multiplicity-invariant quotient.** Let \(r=3\) in the adjacent case and \(r=4\) in the disjoint case. Label the fault endpoints \(0,\ldots,r-1\). The other \(k=n-r\ge1\) vertices are *universal twins*: they form a clique and each is adjacent to every fault endpoint. Represent the state by the exact ternary word \(a\in\{0,1,2\}^{r}\) on the fault endpoints and the nonempty color support \(S\subseteq\{0,1,2\}\) present among the \(k\) universal twins. There are \(3^r(2^3-1)\) possible signatures: \(189\) or \(567\), respectively.

The next state on a fault endpoint depends on the ternary states of all fault endpoints and solely on whether color \(1\) occurs in \(S\). For a universal-twin vertex in state \(0\), an excited neighbor is present precisely when either a fault endpoint is excited or color \(1\) belongs to \(S\). Its values \(1,2\) advance unconditionally. Hence the update of **each existing twin color** is a deterministic common function of \((a,S)\), independent of its multiplicity. This proves that the signature has an exact deterministic successor and, more strongly, that its entire full-state temporal period and first-periodic-entry time can be read from the representative configuration containing **one twin of each color in \(S\)**. Indeed the representative tracks one copy of every possible color lineage, and copying any lineage does not alter any update condition or the equality of entire states at two times. Thus the temporal class \((t,p)\) is invariant under the numbers of twins assigned each represented color. This is a reduction of *all* \(3^n\) full states, not an approximation.

**2. Complete finite signature classification.** For each assignment \(a\in\{0,1,2\}^{r}\) and each nonempty subset \(S\), iterate the explicit local rule on the representative \(a\) followed by the sorted colors of \(S\), recording the first repeated labelled state. Its index is \(t\) and the repetition interval is \(p\). The following table displays, for each temporal cell, the exact number of signatures with support size \(|S|=1,2,3\). It is obtained by directly substituting the three-state truth table into all \(189\) or \(567\) finite representative trajectories; the complete enumerator and the assertions of every table entry are embedded in `verification/signature_certificate.py`.

| \((t,p)\) | Adjacent \((c_1,c_2,c_3)\) | Disjoint \((c_1,c_2,c_3)\) |
|---|---|---|
| \((0,1)\) | \((1,0,0)\) | \((1,0,0)\) |
| \((0,3)\) | \((6,33,27)\) | \((66,147,81)\) |
| \((1,1)\) | \((15,8,0)\) | \((31,16,0)\) |
| \((1,3)\) | \((2,8,0)\) | \((16,16,0)\) |
| \((2,1)\) | \((21,8,0)\) | \((35,16,0)\) |
| \((2,3)\) | \((4,8,0)\) | \((24,16,0)\) |
| \((3,1)\) | \((16,8,0)\) | \((30,16,0)\) |
| \((3,3)\) | \((4,8,0)\) | \((24,16,0)\) |
| \((4,1)\) | \((10,0,0)\) | \((8,0,0)\) |
| \((4,3)\) | \((2,0,0)\) | \((8,0,0)\) |

The coefficient totals are respectively \((81,81,27)\) and \((243,243,81)\), exactly the possible numbers of fault-word assignments times the \(3,3,1\) choices of nonempty supports of each size. The finite certificate enumerates **every** such signature, so no other period or transient depth can exist. The terminal cells are positive and their representatives already fit into a single-twin core, proving the sharp four-step bound at every admitted order.

**3. From signatures to all labelled states.** Fix a *specific* twin-support set \(S\) with \(|S|=j\). The number of length-\(k\) labelled twin colorings using every color of \(S\) is
\[
 w_1(k)=1,\qquad w_2(k)=2^k-2,\qquad w_3(k)=3^k-3\cdot2^k+3.
\]
These are exact surjection counts by inclusion–exclusion. Thus the full-state count for a temporal cell whose signature coefficient triple is \((c_1,c_2,c_3)\) equals \(c_1w_1(k)+c_2w_2(k)+c_3w_3(k)\). Substitute \(k=n-3\) or \(k=n-4\) into the displayed ten-row signature table and simplify. This gives **each entry** of the ten-row census in the Finding and proves that the entries sum to \(3^n\), with no double counting. Since the only primitive nontrivial period is three, division of the \((0,3)\) cell by three gives the exact orbit count. Summing the five period-one cells gives the extinction basin. Subtracting the two families proves both six-state and two-orbit differences and the contrasting terminal shells.

## Verification
The standalone integer-only program `verification/signature_certificate.py` constructs all \(756\) fault-word/support signatures directly from neighbor rules, determines the exact return times, checks every coefficient of the displayed finite table and the derived formulas for size parameters from five through thirty-four. Its success marker is `SIGNATURE_CERTIFICATE_OK`. A second program `verification/direct_enumeration.py` independently constructs the full labelled global update maps without using the finite-signature reduction, strips away transient vertices from each functional graph, and compares the entire \((t,p)\) joint histogram with the formulas for both graphs and every order from five through nine (\(58{,}806\) full graph-state pairs). Its success marker is `DIRECT_ENUMERATION_OK`. Both programs were executed from the embedded paths before delivery. The all-order proof is the multiplicity-invariant reduction and the exhaustive finite coefficient table; finite-size simulation alone is not presented as an infinite proof.

## Relationship to prior work
The three-state Greenberg–Hastings model goes back to Greenberg and Hastings (1978), with early systematic spatial studies by Durrett and Griffeath (1993). Gravner, Lyu and Sivakoff (2016), Theorem 3, already characterize eventual synchronization versus oscillation on arbitrary connected graphs through edge-cocycle winding and bound synchronization by graph diameter; those **qualitative** statements are not claimed new here. Doba (2018) gives a general maximum-cycle-density criterion for the excitation rate but no enumerated temporal entry-time distribution on these two defect families. Published exact results for a clique with a *perfect matching* removed determine a different edge-fault family; the graph with two adjacent removed edges is not a matching-deleted clique, and the two-disjoint-deletions graph has unpaired universal vertices for \(n\ge5\). Similarly, a published complete split-graph census covers the **one-missing-edge** graph, not the adjacent-two-edge graph; a separately published **three-color cyclic** automaton on matching-defected cliques uses a different update map. The exact ten-cell formulas and the matched adjacent-versus-disjoint comparison do not follow as special cases of these statements. This claim does not include priority for the general contour criterion or for the underlying finite-signature methodology. No proof of absolute historical novelty is asserted.

## Limitations
The result is for three-state deterministic threshold-one synchronous excitation on the two specific two-edge-defective cliques, with \(n\ge5\). It does not classify arbitrary missing-edge patterns, thresholds above one, stochastic excitation, attraction basins of individual nonzero orbits, or the exceptional four-vertex disjoint case. The equalities describe labelled-state populations, not independent external measurements. Historical overlap with unindexed, unpublished or inaccessible enumerations remains a risk. Independent external mathematical audit has not been performed.

## References
- J. M. Greenberg and S. P. Hastings, *Spatial patterns for discrete models of diffusion in excitable media*, SIAM J. Appl. Math. **34** (1978), 515–523, https://doi.org/10.1137/0134040 (publication month reported as May 1978; first day not independently established).
- R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first arXiv posting 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
- J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first posted 2016-10-24, https://arxiv.org/html/1610.07320v1.
- N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* **27** (2018), 101–126, https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf.
- *Three-state excitation on cocktail-party graphs: a sharp period transition and exact orbit count*, published comparison, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-three-state-excitation-on-cocktail-party-graphs-a-sharp-period-t--b65add71b337.
- *Four-phase entrance statistics for three-state excitation on complete split graphs*, published comparison, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-four-phase-entrance-statistics-for-three-state-excitation-on-com--86c3801557a2.
- *Linear orbit loss and quadratic delayed waves in matching-defected cliques*, three-color cyclic-automaton comparison, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-linear-orbit-loss-and-quadratic-delayed-waves-in-matching-defect--28a6bff0b607.
