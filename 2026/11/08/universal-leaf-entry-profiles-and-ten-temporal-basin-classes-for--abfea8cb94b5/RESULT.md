# Universal leaf-entry profiles and ten temporal basin classes for three-state excitation on pineapple graphs

## Finding

Consider the pineapple graph formed from a clique on \(r+1\) vertices by adjoining \(s\) leaves to one distinguished clique vertex, with \(r\ge2\) and \(s\ge1\). Evolve the synchronous three-state Greenberg–Hastings model described below. For each labelled initial state \(x\), let \(T(x)\) be its first time on its eventual periodic orbit and \(p(x)\) the least period of that orbit. Let \(N_{t,p}(r,s)\) count the states with \(T=t\) and \(p(x)=p\).

Write
\[
 R=2^r,\qquad S=2^s,\qquad P=3^s,\qquad Q=3^r-2^{r+1}+1.
\]
Then **all ten nonzero first-entry populations** are exactly

| First entry \(t\) | Fixed-point basin \(N_{t,1}\) | Three-cycle basins \(N_{t,3}\) |
|:--:|:--|:--|
| \(0\) | \(1\) | \(3Q\) |
| \(1\) | \(2RS-1\) | \((S-1)Q\) |
| \(2\) | \((2R-1)P\) | \((P-1)Q\) |
| \(3\) | \((2R-1)P-RS+R-1\) | \((P-1)Q\) |
| \(4\) | \((2R-1)P-RS-R+1\) | \((P-S)Q\) |

Every other \((t,p)\) population is zero. In particular, the global map \(F\) obeys \(F^7=F^4\), and \(4\) is the sharp universal first-entry bound for **every** admissible \((r,s)\). There is exactly one fixed state, the all-rest state, and exactly \(Q\) primitive three-cycle orbits.

The stronger orbit-by-orbit statement is that **each individual primitive three-cycle has precisely the same temporal attraction profile**:
\[
\bigl(B_0,B_1,B_2,B_3,B_4\bigr)
 =\bigl(3,\ 2^s-1,\ 3^s-1,\ 3^s-1,\ 3^s-2^s\bigr).
\]
Here \(B_t\) counts initial labelled states first entering this particular orbit at step \(t\). Thus its full basin contains \(3^{s+1}\) states. The conditional law of \(T\), given eventual least period three, is **independent of the clique size \(r\)**. For fixed \(r\), as \(s\) tends to infinity, its probability concentrates equally on the three entry times \(2,3,4\).

The all-rest basin contains \(3^{s+1}(2^{r+1}-1)\) states. The orbit-versus-extinction partition itself also follows from the previously known finite-graph circulation criterion; the new contribution asserted here is the complete first-entry census and the individual orbit's five-layer basin profile.

## Assumptions and scope

Let \(v_0\) be the distinguished clique vertex, \(v_1,\ldots,v_r\) its ordinary clique companions, and \(w_1,\ldots,w_s\) the leaves, each adjacent only to \(v_0\). The graph is simple, loopless, undirected, with fixed labelled vertices. The state of each vertex is in \(\{0,1,2\}\): rested \(0\), excited \(1\), and refractory \(2\). All updates occur simultaneously. If a vertex has state \(1\), it changes to \(2\); if it has state \(2\), it changes to \(0\); a rested vertex changes to \(1\) exactly when at least one neighbor is currently excited, and otherwise stays at \(0\).

An initial state is counted once per labelled vertex assignment. Its first-entry time is the smallest nonnegative integer \(t\) for which \(F^t(x)\) lies on a cycle of the finite deterministic state map. In particular, a state which first becomes all-rest at time \(t\) has \(p=1\), while a recurrent oscillatory state has \(p=3\). Statements concern deterministic finite graphs with \(r\ge2,s\ge1\); no asynchronous update, random graph, positive excitation threshold greater than one, or more-than-three-state rule is included.

## Proof

**1. An exact 147-signature quotient.** For a state write \(h\in\{0,1,2\}\) for the color of \(v_0\), \(A\subseteq\{0,1,2\}\) for the set of colors represented among \(v_1,\ldots,v_r\), and \(B\subseteq\{0,1,2\}\) for the colors represented among the leaves. Both \(A\) and \(B\) are nonempty. Define \(\phi(c,e)\) by \(\phi(0,e)=1\) if \(e\) is true and \(\phi(0,e)=0\) otherwise, \(\phi(1,e)=2\), and \(\phi(2,e)=0\). The synchronous update induces exactly
\[
\begin{aligned}
 h'&=\phi\bigl(h,\ 1\in A\cup B\bigr),\\
 A'&=\{\phi(c,\ (h=1)\lor(1\in A)):c\in A\},\\
 B'&=\{\phi(c,\ h=1):c\in B\}.
\end{aligned}
\]
Every pair of ordinary clique vertices with the same initial color has identical inputs at all future steps, as does every pair of equally colored leaves. Conversely, the signature recurrence determines the future of every initially occupied color class. Consequently, this is an exact reduction for the full labelled dynamics, not an approximation to a mean-field model. There are \(3(2^3-1)^2=147\) possible signatures before imposing the minimum numbers of labelled vertices needed for each support.

**2. Oscillatory core and exact individual basins.** If all three colors occur initially on the clique, then each rested clique vertex has an excited neighbor, so all clique colors advance by one modulo three at every update. Thus the clique is already in a primitive three-cycle. Conversely, if the initial clique uses at most two colors, it can never acquire all three: the possible nonempty two-color supports map through \(\{0,1\}\to\{1,2\}\to\{0,2\}\to\{0,1\}\) or their subsets, with any extra excitation of the hub leaving the support size at most two. The finite recurrence in Step 3 proves that all such configurations reach the all-rest state by step four.

The number of three-colorings of the \(r+1\) clique vertices using all three colors is \(3^{r+1}-3\cdot2^{r+1}+3=3Q\). Every such configuration rotates through three distinct phases; hence there are \(Q\) primitive clique cycles. In an oscillating clique orbit the hub's color is \(h_t=h_0+t\pmod3\). Every attached leaf eventually follows the unique forced phase \(\ell_t=h_t-1\pmod3\). For one leaf, the least time from which its actual path agrees forever with this phase depends on initial hub color \(h_0\) and leaf color \(\ell_0\) as follows:

| \(h_0\) | \(\ell_0=0\) | \(\ell_0=1\) | \(\ell_0=2\) |
|:--:|:--:|:--:|:--:|
| \(0\) | \(1\) | \(4\) | \(0\) |
| \(1\) | \(0\) | \(3\) | \(3\) |
| \(2\) | \(2\) | \(0\) | \(2\) |

This table follows by iterating the three elementary state changes \(0\to 1\) (only when the hub is excited), \(1\to2\), and \(2\to0\) against the periodic hub. For \(s\) independent leaves the full configuration enters its periodic orbit when the last leaf has settled. Summing the cumulative numbers of admissible initial leaf colors across the three clique phases gives
\[
 3,\quad 2^s+2,\quad 3^s+2^s+1,\quad 2\cdot3^s+2^s,\quad 3\cdot3^s
\]
for the numbers with entry time at most \(0,1,2,3,4\), respectively, within **each fixed three-cycle basin**. Adjacent differences give exactly the claimed \(B_t\)'s. Notice that this argument is orbit-by-orbit and does not use a quotient that identifies different labelled clique phases.

**3. Exact extinction-layer census.** For clarity, the finite-signature calculation can be condensed into the following table. Let \(C_{t,a,b}\) be the number of triples \((h,A,B)\) with \(|A|=a\), \(|B|=b\), whose labelled descendants first reach the all-rest state at time \(t\). The six columns cover \(a\in\{1,2\}\), \(b\in\{1,2,3\}\); entries with \(a=3\) never reach the all-rest state.

| \(t\) | \(C_{t,1,1}\) | \(C_{t,1,2}\) | \(C_{t,1,3}\) | \(C_{t,2,1}\) | \(C_{t,2,2}\) | \(C_{t,2,3}\) |
|:--:|--:|--:|--:|--:|--:|--:|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 7 | 4 | 0 | 4 | 2 | 0 |
| 2 | 9 | 9 | 3 | 6 | 6 | 2 |
| 3 | 6 | 7 | 3 | 5 | 5 | 2 |
| 4 | 4 | 7 | 3 | 3 | 5 | 2 |

This is an exact finite case analysis: applying the displayed recurrence to all \(147\) nonempty \((h,A,B)\) signatures gives one fixed signature \((0,\{0\},\{0\})\), two three-cycles of signatures, and the stated first-entry table. All other signatures flow into one of these by at most four updates. The recurrence and the table are fully specified above and independently replayable by `code/verify_signatures.py`; the fact that each listed nonoscillating signature reaches the **all-rest labelled state** means the quotient cannot spuriously shorten a labelled period or transient.

For a fixed \(a\)-color support on \(r\) labelled ordinary vertices, the number of assignments using every color in that support is
\[
 W_r(a)=\sum_{j=0}^{a}(-1)^j\binom aj(a-j)^r.
\]
In particular, \(W_r(1)=1\), \(W_r(2)=2^r-2\), and \(W_r(3)=3^r-3\cdot2^r+3\), with analogous formulas for the leaves. Thus
\[
 N_{t,1}(r,s)=\sum_{a=1}^{2}\sum_{b=1}^{3}C_{t,a,b}\,W_r(a)W_s(b).
\]
Substituting the five displayed coefficient rows and simplifying yields precisely the five \(N_{t,1}\) formulas in the Finding. Since each oscillatory clique cycle has the \(B_t\) distribution from Step 2, \(N_{t,3}=Q B_t\), which establishes the remaining five formulas.

**4. Exhaustion, sharpness, and conditional law.** Summing all ten formulas gives \(3^{r+s+1}\), the complete state-space size. For \(r\ge2\), \(Q=3^r-2^{r+1}+1>0\), and for \(s\ge1\), \(3^s-2^s>0\). Thus at least one primitive-three-cycle basin has configurations with \(T=4\); the coefficient table also gives nonoscillatory examples with \(T=4\). The global sharp bound follows. Dividing \(B_t\) by \(3^{s+1}\) proves the conditional law and its three-way limit for \(t\in\{2,3,4\}\). There are no other periods or first-entry times, so \(F^7=F^4\).

## Verification

Run `python3 code/verify_signatures.py` with Python 3 to enumerate the entire \(147\)-signature space, check the ten coefficient matrices and compare the symbolic weighted count formulas for \(2\le r\le12\) and \(1\le s\le12\). Run `python3 code/verify_direct.py` to generate graph adjacency lists from their definition, evolve every labelled initial state for \(20\) graph sizes, and check orbit representatives and individual entry-basin populations without using the support quotient. The direct checker examines \(392,040\) labelled configurations. Captured output is `checks/verification_output.txt`.

These finite checks independently corroborate the finite recurrence and arithmetic. The infinite-parameter conclusion is justified by the exact support-class proof, the algebraic surjection counts, and the separate forced-leaf calculation; the checks are not extrapolated as an infinite proof.

## Relationship to prior work

Gravner, Lyu, and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (first publicly posted 2016-10-24), establish general circulation/irrotationality criteria for three-state Greenberg–Hastings dynamics and cyclic contact dynamics, and consider arbitrary finite graphs as well as random graphs and infinite trees. Those general criteria already distinguish possible fixation from persistent excitation in the graph family here, and this basic orbit-versus-extinction separation is **not** asserted to be a new discovery.

The present statement is more specific in a different dimension: exact labelled first-entry populations at each of five times, the **individual** three-cycle basin profile, and its invariance under changing clique size while keeping the number of leaves fixed. The cited primary paper does not state those formulas or an implication computing them. Results for other graph families or different three-color/majority rules do not automatically transfer the required clock-resolved counts to Greenberg–Hastings excitation on this pineapple family. The literature searches and comparison do not establish historical priority; equivalent unindexed treatments remain possible.

## Limitations

Only labelled pineapple graphs with \(r\ge2\) ordinary clique vertices and \(s\ge1\) leaves, synchronous updates, one excited-neighbor threshold, and exactly three states are covered. The theorem does not provide exact temporal counts for arbitrary tree grafts, general complete multipartite graphs, or asynchronous dynamics. The fixed-versus-oscillatory partition is already implied by established circulation theory; the claimed contribution is the finer first-entry census and individual orbit-basin layer law. Published-equivalence searches are not a proof of priority, and the result has no independent expert or external audit.

## References

1. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, 2016-10-24, https://arxiv.org/abs/1610.07320 (in particular model definition and Theorem 3; full text available at https://arxiv.org/html/1610.07320v1).
2. J. M. Greenberg and S. P. Hastings, *Spatial patterns for discrete models of diffusion in excitable media*, SIAM Journal on Applied Mathematics 34 (1978), 515–523 (model origin; bibliographic reference in the preceding primary source).
