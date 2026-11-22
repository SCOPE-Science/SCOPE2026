# A seven-rung causal trigger and sharp five-update extinction on open ladders

## Finding
For every integer \(n\ge1\), consider the labelled open ladder \(L_n=P_n\square K_2\) with vertices \(u_1,\ldots,u_n\) and \(v_1,\ldots,v_n\). Under synchronous three-state Greenberg–Hastings dynamics requiring **two distinct excited neighbors** to excite a resting vertex, every initial configuration reaches all-rest by time five. The exact maximum first all-rest time is
\[
\max_x\tau(x)=\begin{cases}
2,&n=1,\\
3,&2\le n\le3,\\
4,&4\le n\le6,\\
5,&n\ge7.
\end{cases}
\]

More strongly, the configurations that require the fifth update have a **complete, length-seven local characterization**. Encode each initial rung by \(a_i=x(u_i)+3x(v_i)\in\{0,\ldots,8\}\), and define allowed symbol sets
\[
\mathcal S=(\{1,4,7\},\{3\},\{0,2\},\{3,4,5\},\{0,2\},\{3\},\{1,4,7\}).
\]
Let \(\sigma(a)=3(a\bmod3)+\lfloor a/3\rfloor\) exchange the upper and lower rung states. A seven-rung block is a *top trigger* if its successive entries belong to the seven corresponding sets in \(\mathcal S\); a *bottom trigger* if its entries after \(\sigma\) do so. Every top or bottom trigger has 108 possible seven-rung words, and the two sets of words are disjoint. The first all-rest time is **exactly five if and only if the initial rung word contains one of these 216 length-seven triggers as a contiguous block**.

Consequently there is an explicitly constructed \(204\)-state nonnegative integer transfer matrix \(M\) with
\[
\#\{x:\tau(x)=5\}=9^n-e_{\emptyset}^{\mathsf T}M^n\mathbf1.
\]
Here the states are the nonterminal proper-prefix states of the Aho–Corasick automaton of the 216 forbidden words, \(e_{\emptyset}\) is the empty-prefix start vector and each \(M_{ab}\) counts letters in the nine-symbol alphabet taking state \(a\) to nonterminal state \(b\). The constructive definition, including all failure links, is implemented with exact integer arithmetic in `verify_transfer.py`; no unexplained table is needed.

In particular the fifth-update populations for \(n=7,8,9,10\) are respectively \(216,3888,52488,629856\). For uniformly independent random initial vertex states, the probability of requiring all five updates tends to one exponentially, with the explicit bound
\[
\Pr(\tau=5)\ge1-\left(1-\frac4{3^{11}}\right)^{\lfloor n/7\rfloor}.
\]

## Assumptions and scope
At every integer time each vertex has state \(0\) (rest), \(1\) (excited), or \(2\) (refractory). States \(1\to2\to0\) evolve automatically. State \(0\to1\) occurs if and only if at least two **distinct open-neighborhood** vertices currently have state one; otherwise zero stays zero. All vertices update simultaneously and there is no external stimulation. Rungs join \(u_i\) to \(v_i\), while the rails join like-labelled vertices in consecutive columns. The endpoints are open, not cyclic. The hitting time \(\tau(x)\) includes time zero and is the least \(t\ge0\) with all vertices in state zero at time \(t\). The formula counts fully labelled states, not symmetry classes.

## Proof
**1. Finite local lemma with complete proof certificate.** A vertex's state at time three depends only on the initial states at graph distance at most three. If its column is at least three rungs from both endpoints, its entire dependency neighborhood lies in seven consecutive rungs. Exhaustively evaluating the exact three-step update on all \(3^{14}=4{,}782{,}969\) labelled states of the seven-rung ladder gives the following exact truth-table assertions, each explicitly asserted in `verify_all.cpp`: at time three the only possibly excited vertices are the two vertices in the central (fourth) rung; the upper central vertex is excited if and only if its seven rung symbols match \(\mathcal S\), and the lower central vertex if and only if they match the swapped sets. The product of the seven allowed-set cardinalities is \(3\cdot1\cdot2\cdot3\cdot2\cdot1\cdot3=108\). This is an exhaustive finite identity, not a sampling inference. A second complete enumeration of all shorter ladders \(1\le n\le6\) establishes that no vertex can be excited at time three on any of them.

To transfer the local identity to arbitrary \(n\), take any vertex in column \(j\). If \(j\) has at least three columns on both sides, use its seven-rung radius-three neighborhood, which is identical to the central radius-three neighborhood for the seven-rung ladder; edges beyond this neighborhood cannot affect its state by time three. If the vertex lies within three columns of an endpoint, its radius-three neighborhood is identical to one of the corresponding first or last three column neighborhoods in a seven-rung ladder (the other endpoint may be farther away but has no influence by time three). All such boundary vertices were proved unexcitable in the same seven-rung truth table. The separately checked smaller ladders handle \(n\le6\). Therefore, for *every* ladder length, the time-three excitation sites are precisely the centers of top and bottom triggers and there are no others.

**2. No time-four excitation.** The trigger sets forbid two time-three excited neighbors of the same vertex. It is enough to check a hypothetical upper target in column \(j\); the lower case follows by exchanging rails. Its three potential excited neighbors are the upper vertices in columns \(j-1\), \(j+1\), and the lower vertex in column \(j\). A top trigger centered at \(j-1\) requires the upper state at initial column \(j+2\) to be one, while a top trigger centered at \(j+1\) requires that same upper state to belong to \(\{0,2\}\). A top trigger centered at \(j-1\) or \(j+1\) requires the initial upper state in column \(j\) to belong to \(\{0,2\}\), whereas a bottom trigger centered at \(j\) requires that initial upper state to equal one. Thus each possible pair conflicts. If any required column is absent, the corresponding trigger is itself impossible. It follows that every vertex has at most one excited neighbor at time three. No resting vertex can become excited at time four; excited states from time three become refractory, so there is no excitation at time four at all.

**3. Extinction and sharpness.** Since no time-four vertex is excited, time-five vertices cannot be newly excited; residual refractory states from time three recover by time five. Hence every state has become zero by time five. There is an excited vertex at time three precisely when a seven-rung trigger appears. This vertex remains refractory at time four, making the hitting time five; if there is no trigger, no vertex is excited at time three and all refractory states clear by time four. Therefore the exact trigger equivalence holds. Such words first fit at seven rungs. Any matching seven-rung block can be embedded in longer ladders, proving the sharp time-five bound for all \(n\ge7\). The complete small-size enumerations give sharp times \(2,3,3,4,4,4\) for lengths \(1,2,3,4,5,6\), respectively.

**4. Exact population and large-length law.** The forbidden-word set consists of the 108 upper and 108 lower triggers, all of length seven. Construct its prefix trie, add standard failure transitions to the longest suffix that is itself a prefix, and delete all states representing occurrence of a forbidden word. The resulting deterministic nine-letter automaton has 420 trie states, of which 204 are nonterminal. Its integer adjacency transfer \(M\) counts exactly the length-\(n\) words avoiding all triggers. Subtracting from \(9^n\) proves the stated population identity. For the probability bound, examine \(\lfloor n/7\rfloor\) disjoint seven-rung windows. In each, the probability of a top trigger is \(108/9^7=4/3^{11}\); independence of these disjoint windows bounds the chance of no trigger above by \((1-4/3^{11})^{\lfloor n/7\rfloor}\), giving exponential convergence.

## Verification
Compile `verify_all.cpp` with `g++ -O3 -std=c++17 verify_all.cpp -o verify_all` and execute `./verify_all`. It independently constructs every ladder of lengths one through eight, exhaustively iterates all \(48{,}427{,}560\) labelled states across those lengths, checks full trajectories through time five, verifies for **every state and every vertex** the asserted trigger equivalence at time three, and establishes exact small-length hitting-time maxima and fifth-update populations. The output must finish `EXHAUSTIVE_OK`. The exact enumeration of the seven-rung dependency truth table forms a finite lemma in the proof of the all-length result; it is not presented as proof merely from a few sampled ladder sizes.

Run `python3 verify_transfer.py` independently. It constructs the motif dictionary and the 204-state automaton without simulation, verifies the six pairwise trigger incompatibilities and the integer population counts through length twelve, and terminates `TRANSFER_OK`. Output of both programs is in `verification_output.txt`. The complete source is part of this package; its assertions and loop bounds are human-inspectable. Neither program requires network access, external datasets, or hidden assets.

## Relationship to prior work
The foundational Greenberg–Hastings and threshold-range literature [1,2] establishes the excitable-media model, not the seven-rung threshold-two ladder trigger. Gravner, Lyu and Sivakoff [3] establish detailed activity results on arbitrary graphs **at contact threshold one**; their published theorem does not imply the present two-contact dynamics. Existing exact results on the very same open ladders at threshold one [4] exhibit several persistent activity phases, whereas here every threshold-two trajectory dies out after at most five updates. This is a substantive contact-threshold change, not a reformulation of their rate classification. The finite-graph density criterion [5] does imply eventual extinction on open ladders, since their maximum induced edge density is strictly below two; however its general bound depends on graph size and it gives neither a universal five-step deadline, the exact seven-rung local characterization, nor its all-length population formula. A previously established five-update extinction result for **wheel graphs** [6] concerns a different adjacency structure and has a distinct minimum sharp circumference. Neither statement implies the causal motif for two-row open ladders. The available primary texts [3,4,5,6] were compared at statement and hypothesis level; historical-priority searches are not exhaustive.

## Limitations
The theorem concerns exactly three states, two-contact excitation, simultaneous update and the open two-row ladder. It does not address stochastic stimulation, other thresholds, more rails, cyclic ladders, or additional refractory stages. The exact population transfer has 204 nonterminal states; no claim is made that this representation is minimal. The result supplies an exponential probability bound but not a sharp exponential decay constant. The complete local table is verified by executable exhaustive enumeration rather than being replaced by a short hand-derived case distinction. No independent external mathematical validation or absolute priority certification is claimed.

## References
[1] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, public preprint dated 1993-03-22. https://arxiv.org/abs/patt-sol/9303002

[2] R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001, public preprint dated 1993-04-02. https://arxiv.org/abs/patt-sol/9304001

[3] J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, public preprint dated 2016-10-24, Sections 1–4. https://arxiv.org/html/1610.07320v1

[4] *Exact three-rate excitation census on open square ladders*, 2026-11-08, full result. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-three-rate-excitation-census-on-open-square-ladders--9fa61fb1a7f9/RESULT.md

[5] *A densest-subgraph threshold and finite excitation budget for three-state graph dynamics*, 2026-10-25, full result. https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-a-densest-subgraph-threshold-and-finite-excitation-budget-for-th--352367f51e91/RESULT.md

[6] *Sharp five-step extinction for threshold-two excitation on wheel graphs*, 2026-10-26, full result. https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-sharp-five-step-extinction-for-threshold-two-excitation-on-wheel--58917bc0decb/RESULT.md
