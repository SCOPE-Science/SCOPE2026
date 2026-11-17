# Exact first-recurrence clocks for rotor walks on equal-arm spiders

## Finding
Let \(S_{k,L}\) be the tree consisting of \(k\ge3\) internally disjoint paths of length \(L\ge2\) joined at a common hub. A single rotor walker starts at the hub; at each step it increments the rotor at its current vertex in the fixed cyclic order and follows that rotor. At every non-hub non-leaf vertex the rotor order is parent, child. The hub has any fixed cyclic order of its arms. The state includes the walker position and all rotor positions; its **entry time** \(\tau\) is the least nonnegative update count after which the state lies on a periodic orbit.

There is an exact per-configuration formula for \(\tau\), given below. In particular the sharp maximum over all initial rotors is
\[
\boxed{\tau_{\max}(k,L)=(L-1)\big((2k-1)L-1\big).}
\]
Exactly \(k\) of the \(k2^{k(L-1)}\) labelled hub-start rotor assignments attain this maximum. Every eventual orbit has primitive length exactly \(2kL\). With independent uniform initial rotors and fixed \(L\), as \(k\to\infty\),
\[
\frac{\tau}{k}\longrightarrow\frac32 L(L-1)
\quad\text{in probability and in mean},
\qquad
\Pr(\tau=\tau_{\max})=2^{-k(L-1)}.
\]

## Assumptions and scope
Write the arm vertices as \(v_{i,d}\), with \(1\le i\le k\) and depths \(1\le d\le L\), and \(v_{i,0}=h\). Leaf rotors have one position. At an internal arm vertex, index zero points toward the hub and index one points toward the tip. An initially **outward** pointer at depth \(d<L\) is a blocker. For each arm \(i\), list its blocker depths in increasing order:
\[d_{i,1}<\cdots<d_{i,b_i},\qquad 0\le b_i\le L-1.\]
Take the cyclic sequence \(i_1,\ldots,i_k\) of arms visited by the hub rotor, starting with the arm selected on its first increment. Define
\[
E_i(r)=\sum_{s=1}^{\min(r,b_i)}d_{i,s}+L\max(0,r-b_i),\qquad r\ge0.
\]
If \(B=\max_i b_i=0\), then \(\tau=0\). Otherwise let \(j_*\) be the **largest** index \(j\) for which \(b_{i_j}=B\). The exact all-configuration formula is
\[
\boxed{\tau=2\!\sum_{j<j_*}E_{i_j}(B)
+2\!\sum_{j>j_*}E_{i_j}(B-1)
+2\!\sum_{s=1}^{B-1}d_{i_{j_*},s}+d_{i_{j_*},B}.}
\]
The sums over empty index sets are zero. In particular, this formula is an explicit finite calculation directly from the initial rotors, not an eventual-cycle simulation.

## Proof
**Excursions from the hub.** When an arm is selected, the walker follows its path until encountering the shallowest blocker not already cleared. Each already-cleared internal rotor points toward the hub, so on entry it rotates outward; on the return it rotates toward the hub. At the first uncleared blocker, the initial outward rotor rotates toward the hub, sending the walker back. The entire excursion takes exactly twice the blocker depth and clears just that blocker. If there is no remaining blocker, the walker reaches the leaf and returns in \(2L\) steps. Therefore the \(r\)-th excursion down arm \(i\) has length \(2d_{i,r}\) for \(r\le b_i\) and length \(2L\) afterward. After any completed hub excursion, every internal rotor reached on that excursion points inward.

**Earliest recurrence.** On any finite undirected tree, a rotor state with walker on the unique directed two-cycle of its rotor arrows is periodic, traversing each oriented edge once in \(2|E|\) steps. Conversely a periodic one-walker rotor state is of this form. This follows from the usual Euler-tour argument: the rotor advances through all exits at every repeatedly visited vertex, connectivity forces every vertex to be visited, and leaf removal gives exactly one traversal of each oriented edge in a primitive tour. A directed rotor cycle on a tree can only consist of two mutually pointing neighboring vertices.

Before the last uncleared blocker is reached, either a separate outward-to-inward transition on another arm forms a second rotor two-cycle, or the walker lies strictly upstream of the remaining two-cycle. Consequently the state cannot yet be periodic. When the walker arrives at the last blocker, all other internal arm rotors point inward, the active path's already traversed rotors point toward that blocker, and the blocker points at its next vertex, which points back: there is a unique directed two-cycle containing the walker. Hence this arrival is exactly first periodic entry. Each arm before the final arm in the current hub round has completed \(B\) excursions; each arm after it has completed \(B-1\). The final arm has completed \(B-1\) excursions and the walker is \(d_{i_{j_*},B}\) edges into its last excursion. Adding these lengths proves the displayed formula.

**Extremal time and equality.** Fix \(B\ge1\), and suppose the terminal arm is the \(j_*\)-th in cyclic order. Every completed excursion takes at most \(2L\) steps, while the terminal arm has exactly \(B\) distinct blocker depths in \(\{1,\ldots,L-1\}\). Its contribution is maximized when those depths are the \(B\) deepest allowed positions. Thus
\[
\tau\le 2(j_*-1)BL+2(k-j_*)(B-1)L
+(B-1)(2L-B-2)+(L-1).
\]
For fixed \(B\), the right side strictly increases with \(j_*\), so \(j_*=k\) maximizes it. The resulting bound
\[
H(B)=2(k-1)BL+(B-1)(2L-B-2)+L-1
\]
strictly increases for \(1\le B\le L-1\), since \(H(B+1)-H(B)=2(k-1)L+2(L-B-1)>0\). It is largest at \(B=L-1\), giving \(H(L-1)=(L-1)((2k-1)L-1)\). Equality forces all earlier arms to have **no** outward pointers and the final arm to have **all** its \(L-1\) internal pointers outward. For each of the \(k\) hub rotor positions there is exactly one such assignment. This proves the maximum and the extremizer count.

**Typical clock.** For random independent fair internal rotors, the number of blockers on each arm is a binomial random variable with parameters \((L-1,1/2)\). The probability of an all-blocker arm is \(p=2^{-(L-1)}>0\). For fixed \(L\), the maximal blocker count \(B=L-1\) therefore occurs with probability approaching one, while the number of arms after the last all-blocker arm is tight (geometric tail \((1-p)^r\)). Each other arm contributes, up to this last arm, the bounded independent quantity \(2E_i(L-1)\). Since
\[
\mathbb E E_i(L-1)=\frac12\sum_{d=1}^{L-1}d+\frac L2(L-1)=\frac34L(L-1),
\]
the law of large numbers gives \(\tau/k\to3L(L-1)/2\) in probability. The uniform deterministic bound \(\tau/k\le2L(L-1)\) yields convergence in mean. The extremal probability follows from the exact count of extremizers divided by \(k2^{k(L-1)}\).

## Verification
The standalone program `verify.py` independently constructs each finite-state rotor transition and computes the exact first-repeated-state index, and compares it with the direct blocker-depth formula. It exhaustively checked all 24,344 labelled hub-start assignments for \((k,L)\in\{(3,2),(3,3),(3,4),(4,2),(4,3),(4,4),(5,3)\}\), including the primitive period and extremal multiplicity. Run `python3 verify.py`; the captured summary is in `verification_output.txt`. The infinite-parameter assertions follow from the proof, not from this finite test.

## Relationship to prior work
Classic finite-graph rotor-router theory establishes eventual Euler tours and general bounds on stabilization and exploration; see Chalopin et al. (arXiv:1407.3200, especially Sections 1 and 5.1) and Bampas et al. (DOI below, especially introduction and lock-in bounds). These results do not state the present hub-start first-periodic-entry formula, its exact extremizers, or its random-initialization limit on equal-arm spiders. In particular, the *first periodic state* studied here need not coincide with a paper's differently defined *completion time of an Euler tour*. Menc et al. address optimal exploration time on paths, not equal-arm spiders with at least three arms. The rotor-tree work of Landau and Levine concerns rotor growth and escape on infinite regular trees.

## Limitations
The theorem assumes one walker starting at the hub, undirected equal-length arms, deterministic cyclic rotor order, and all internal arm orders parent-to-child. It does not classify walkers started off the hub, heterogeneous arm lengths, arbitrary tree branching, or Euler-tour *completion* time. Historical priority outside inspected and indexed sources has not been independently established. The reproducibility check is finite and cannot replace the proof or an independent audit.

## References
1. Landau, I., and Levine, L., *The Rotor-Router Model on Regular Trees*, arXiv:0705.1562, first posted 2007-05-10, https://arxiv.org/abs/0705.1562.
2. Chalopin, J., Das, S., Gawrychowski, P., Kosowski, A., Labourel, A., and Uznański, P., *Lock-in Problem for Parallel Rotor-router Walks*, arXiv:1407.3200, first posted 2014-07-10, https://arxiv.org/abs/1407.3200.
3. Bampas, E. et al., *Robustness of the Rotor-Router Mechanism*, Algorithmica 78, 869–895, DOI:10.1007/s00453-016-0179-y, public author manuscript https://livrepository.liverpool.ac.uk/3003004/1/rotorjv.pdf.
4. Menc, A., Pająk, D., and Uznański, P., *Time and space optimality of rotor-router graph exploration*, arXiv:1502.05545, first posted 2015-02-19, https://arxiv.org/abs/1502.05545.
