# A sharp three-slide code-relaxation detour on the Grötzsch graph

## Finding

Let \(G=\mu(C_5)\) be the labelled 11-vertex Grötzsch graph. Its minimum locating-total dominating sets and minimum radius-one identifying codes both have cardinality five. There are exactly 110 minimum locating-total sets and 191 minimum identifying codes, and **every one of the 110 minimum locating-total sets is an identifying code**.

For two minimum locating-total configurations \(S,T\), let \(d_{\mathrm{LT}}(S,T)\) be their shortest reconfiguration distance with every intermediate five-set locating-total, and let \(d_{\mathrm{IC}}(S,T)\) allow every intermediate five-set to be identifying. Both distances are defined using the same move rule, and both configuration graphs are connected.

For **token slides**, where one removed detector must be adjacent in \(G\) to the inserted detector, the precise distribution over the \(\binom{110}{2}=5995\) unordered pairs is:

| \(d_{\mathrm{LT}}-d_{\mathrm{IC}}\) | Number of pairs |
|---:|---:|
| 0 | 4135 |
| 1 | 1440 |
| 2 | 360 |
| 3 | 60 |

Thus 1860 pairs obtain a strictly shorter relocation by temporarily relaxing locating-total observation to identification, without adding detectors. The maximum saving is **exactly three slides**, attained by precisely 60 unordered pairs.

For **token jumps**, where the exchanged vertices need not be adjacent, the difference distribution is \(5725\) pairs at zero and \(270\) pairs at one. The complete optimum-state metrics are:

| Property | Locating-total jumps | Identifying jumps | Locating-total slides | Identifying slides |
|---|---:|---:|---:|---:|
| Minimum configurations | 110 | 191 | 110 | 191 |
| Legal undirected transitions | 520 | 1405 | 190 | 555 |
| Radius | 4 | 4 | 6 | 5 |
| Diameter | 5 | 5 | 8 | 6 |

Under the natural order-ten dihedral symmetry of \(C_5\), the 110 locating-total configurations fall into 13 orbits (nine of length ten and four of length five); the 191 identifying configurations fall into 24 orbits (15 of length ten, eight of length five, and one singleton). All these assertions concern **this one finite graph**, not a family of Mycielski graphs.

## Assumptions and scope

The graph has vertices \(v_i,u_i\) for \(i\in\mathbb{Z}/5\mathbb{Z}\), and an apex \(w\). Its 20 edges are the five \(v_iv_{i+1}\), the ten \(v_iu_{i-1}\) and \(v_iu_{i+1}\), and the five \(u_iw\), with indices interpreted modulo five. No loops or multiple edges occur.

A code \(S\subseteq V(G)\) is **identifying (IC)** when the 11 sets \(N[x]\cap S\) are nonempty and pairwise distinct for all \(x\in V(G)\). A set \(S\) is **locating-total (LT)** when every \(N(x)\cap S\) is nonempty and the sets \(N(x)\cap S\) for the six vertices outside \(S\) are pairwise distinct. The closed-neighborhood identifying condition and the open-neighborhood locating-total condition are not treated as interchangeable.

The optimal configuration graphs have one vertex per feasible five-set. Two states are adjacent under jumping exactly when their symmetric difference has two vertices. Under sliding those two vertices must additionally be adjacent in \(G\). Distances are ordinary graph shortest-path distances, so no intermediate invalid or larger configuration is permitted. The comparing pairs \(S,T\) always belong to the LT family; they are also IC configurations by the inclusion assertion.

## Proof

This is an exhaustive finite proof with standalone verifiers, not an inference from a sample. It has four stages, each reconstructed by two distinct implementations.

1. **Exhaust the candidate sets.** Enumerate every subset of cardinality at most five, a total of \(\sum_{j=0}^{5}\binom{11}{j}=1024\) subsets, by cardinality. For each subset compute the actual open and closed neighborhood traces. The predicate definitions above are necessary and sufficient by definition. Both algorithms find no qualifying set of size at most four; among the \(\binom{11}{5}=462\) five-subsets they find precisely 110 LT and 191 IC, and verify set inclusion \(\mathcal L\subset\mathcal I\). The bitmask checker and a separately built tuple-of-vertices checker use different set representations and graph implementations.
2. **Exhaust the legal transitions.** For each unordered pair of feasible five-sets, test whether the intersection has size four, and under sliding also whether the exchanged endpoints form an original edge. This criterion is equivalent to exactly one legal detector move. Every qualifying pair is inserted once as an undirected transition. The edge totals are the numbers in the table.
3. **Exhaust the shortest paths.** Breadth-first search from each state on each of the four finite configuration graphs yields the exact unweighted distances; in every case all vertices are reached. Compute all eccentricities for radii and diameters. For each of the 5995 unordered pairs from \(\mathcal L\), subtract its shortest distance measured inside \(\mathcal I\) from its shortest distance inside \(\mathcal L\), separately for jumps and slides. The two programs give the identical histograms stated above. These loops cover *all* legal configuration vertices and edges, not only reachable sampled paths.
4. **Check symmetry and an extremal witness.** Rotation and reflection \(i\mapsto a\pm i\pmod5\) act on both \(v\)- and \(u\)-labels, fixing \(w\); orbit enumeration gives the stated sizes. An actual maximum-saving pair is
\[
S=\{v_0,v_1,v_2,u_0,u_3\},\qquad T=\{v_1,v_2,v_3,u_0,u_3\}.
\]
The shortest LT-only path has five slides:
\[
\begin{aligned}
&\{v_0,v_1,v_2,u_0,u_3\}\\
\to{}&\{v_0,v_1,v_2,v_4,u_3\}\\
\to{}&\{v_0,v_1,v_2,v_3,u_3\}\\
\to{}&\{v_1,v_2,v_3,u_3,u_4\}\\
\to{}&\{v_1,v_2,v_3,u_3,w\}\\
\to{}&\{v_1,v_2,v_3,u_0,u_3\}.
\end{aligned}
\]
The IC-only shortest path instead has two slides:
\[
S\to\{v_1,v_2,u_0,u_3,u_4\}\to T.
\]
The middle five-set is identifying but not locating-total, because \(u_4\) has no open-neighbor selected in that set. The verifier checks both actual paths are legal and uses BFS to establish lengths five and two are shortest. This witnesses the three-move saving; the exhaustive histogram proves it is sharp and occurs exactly 60 times.

## Verification

Run `python3 verification_a.py` and `python3 verification_b.py` from a directory containing the two accompanying Python 3 files. Both require only the Python standard library and construct the entire finite graph afresh. The first uses 11-bit masks and explicit one-move generation; the second uses labelled tuples and pairwise set intersections. Each independently checks the two optimum families, the four transition counts, and all 5995 pairwise distance differences; the first also checks the four radii and diameters and the second independently checks orbit sizes and the displayed witness. The complete expected output and scope are described in `VERIFICATION.md`.

## Relationship to prior work

Shaminejad, Vatandoost and Mirasheh (2022), Theorem 2.4, give an upper bound of five for identifying codes of Mycielskian five-vertex bases satisfying their stated degree and neighborhood hypotheses. This applies to \(C_5\), but it does not supply an exact count of minimum codes, locating-total structure, inclusion, reconfiguration distances or the three-slide detour. Chakraborty and collaborators (first arXiv public version 25 November 2022) develop general locating-total domination bounds in specified graph classes; their results do not imply these exact configuration metrics of \(\mu(C_5)\). Mynhardt and Teshima (2017) define and study code-based minimum-solution slide graphs at a general level, not this exact code-family comparison.

Relevant previously indexed results for the Pappus graph, cycle graphs, the dodecahedral graph and Cartesian grids concern different graph instances or different neighborhood predicates. No equivalent exact Grötzsch cross-predicate histogram was found in the consulted indexed records or inspected primary sources; this is not a guarantee that an unindexed equivalent does not exist.

## Limitations

The conclusion is a computer-assisted, exhaustive theorem **only for the labelled 11-vertex Grötzsch graph**. It does not give a universal relation between locating-total sets and identifying codes, nor a bound on detours for arbitrary graphs. The result is a self-reviewed candidate; no independent mathematical audit has been carried out. An unindexed or inaccessible historical table with equivalent numbers remains a priority uncertainty. All code and trace checks use finite exhaustive enumeration; no claim about infinite families follows from the enumeration.

## References

1. D. Chakraborty, F. Foucaud, A. Hakanen, M. A. Henning, A. K. Wagler, *Progress towards the two-thirds conjecture on locating-total dominating sets*, 2022, first posted 2022-11-25, arXiv:2211.14178, https://arxiv.org/abs/2211.14178.
2. A. Shaminejad, E. Vatandoost, K. Mirasheh, *The identifying code number and Mycielski's construction of graphs*, Transactions on Combinatorics 11(4) (2022), 309–316, doi:10.22108/TOC.2021.126368.1794, https://toc.ui.ac.ir/article_26088_858b032cc710d026f084d95cbe679621.pdf.
3. C. M. Mynhardt, L. E. Teshima, *A note on some variations of the gamma graph*, arXiv:1707.02039, https://arxiv.org/abs/1707.02039.
