# Sharp five-step entry and exact six-cycle basins in four-colour bipartite cyclic dynamics

## Finding

Let \(m,n\ge1\). Colour the labelled vertices of the complete bipartite graph \(K_{m,n}\) with values in \(\mathbb Z/4\mathbb Z\). At each synchronous update a vertex of colour \(c\) changes to \(c+1\pmod4\) if and only if at least two **distinct** neighbours currently carry that successor colour; otherwise it retains \(c\). Write \(F\) for this deterministic map, and let \(\tau(x)\) be the least nonnegative time at which \(F^{\tau(x)}(x)\) is periodic.

**Theorem.** For every \(m,n\ge1\):

1. \(F^{17}=F^5\). Every orbit enters a cycle by the fifth update, and the eventual least period belongs to \(\{1,4,6\}\). The entry-time bound five is attained on \(K_{5,6}\).
2. Eventual period six occurs if and only if \(m,n\ge6\). Every state whose eventual period is six has \(\tau(x)\in\{0,1\}\): the six-cycle basin has no chains of length two or longer.
3. Put \(H(z)=e^z-1-z\), and for every nonnegative integer \(s\) define
   \[
   U_s=s![z^s]H(z)^3,\qquad
   V_s=s![z^s]zH(z)^3,\qquad
   W_s=s![z^s]z^2H(z)^2.
   \]
   Exactly
   \[
   \boxed{N_6(m,n)=4(U_m+V_m)(U_n+V_n)+4W_mW_n}
   \]
   labelled configurations eventually enter a primitive six-cycle. Exactly \(4U_mU_n\) are *already* on six-cycles, giving exactly \(\frac23U_mU_n\) distinct primitive six-cycles.

For instance, on \(K_{6,6}\) the period-six basin contains exactly \(162{,}000\) configurations, of which \(32{,}400\) lie on the \(5{,}400\) primitive six-cycles. With two equal shores of size \(s\), uniform initial colours satisfy
\[
\Pr(\text{eventual least period }6)\sim\frac49 s^2\left(\frac9{16}\right)^s.
\]
This exponentially small basin, despite period-six existence for all \(m,n\ge6\), contrasts with more commonly observed oscillatory attraction regimes in cyclic-colour networks.

## Assumptions and scope

The graph is undirected and simple. Shore sizes are arbitrary positive integers; vertices are labelled and count as distinct initial configurations even if their colour counts agree. Updating is simultaneous. A neighbour is counted once, and the threshold is two. No randomness enters the update map. A period-six basin includes any configuration whose *eventual least* period is six, not just a periodic configuration. All powers of \(F\) act on the full labelled-state space, not merely on colour-population vectors.

## Proof

**Step 1: an exact finite reduction.** Let \(a_c\) and \(b_c\) be the numbers of shore vertices initially coloured \(c\), with \(c=0,1,2,3\). Set \(\bar a_c=\min(2,a_c)\) and \(\bar b_c=\min(2,b_c)\). All decisions made by vertices on one shore depend only on the four clipped counts on the opposite shore. Moreover, every vertex belonging to the same *initial* colour class on a shore remains in the same colour at all subsequent times, by induction: it has identical neighbours and the same present colour as the other vertices of its class.

The complete labelled dynamics therefore factors through a finite state consisting of eight clipped counts and eight initially tagged colour-class positions. An absent class has sentinel \(-1\). Given \(a,b\), define \(\sigma_b(c)=(c+1)\bmod4\) when \(b_{(c+1)\bmod4}=2\), and \(\sigma_b(c)=c\) otherwise, and similarly \(\sigma_a\). The one-step clipped-count update is
\[
 a'_d=\min\!\left(2,\sum_{c:\sigma_b(c)=d}a_c\right),\qquad
 b'_d=\min\!\left(2,\sum_{c:\sigma_a(c)=d}b_c\right),
\]
where the sums use *clipped* inputs. Tag positions are updated with the same shore-specific \(\sigma\), while absent tags remain absent. This reduction is **exact** for arbitrary shore sizes because clipping commutes with the threshold and with these nonnegative sums. A return of the tagged states is equivalent to a return of the original labelled configuration: present tagged classes partition the vertices, and the tags record the colour of every member of each class.

There are exactly \((3^4-1)^2=6400\) possible nonempty pairs of clipped shore vectors. Every one is realizable by some graph with positive shore sizes. Thus a finite exhaustive check of all of them proves a result for all \(m,n\ge1\), not merely for a finite selection of graph sizes.

**Step 2: full finite-state lemma.** The standalone `verify_symbolic.py` executes precisely the update above on all \(6400\) initial signatures and independently checks the tagged state at times five and seventeen. The observed return periods of the tagged states are distributed as follows: \(6141\) initial signatures eventually have period one, \(239\) have period four, and \(20\) have period six. The numbers of signatures with entry times \(0,1,2,3,4,5\) are, respectively, \(1032,1628,1880,1364,448,48\). All \(6400\) exact identities \(F^{17}=F^5\) hold for both clipped populations and all present labelled colour tags. This is an exhaustive finite certificate, not sampling; the complete executable loop and exact assertions are included.

For period six, the complete list of \(20\) initial signatures consists of all four simultaneous colour rotations of the five seed pairs
\[
\begin{array}{c|c}
(0,2,2,2)&(2,2,0,2)\\
(0,2,2,2)&(2,2,1,2)\\
(1,2,2,2)&(2,2,0,2)\\
(1,2,2,2)&(2,2,1,2)\\
(1,1,2,2)&(2,2,1,1).
\end{array}
\]
The first seed's four rotations are already periodic. The other sixteen signatures enter a six-cycle after exactly one update. No further six-cycle predecessors exist, as the exhaustive classification of *all initial signatures* establishes.

**Step 3: sharpness and existence.** The clipped shore vectors \((0,1,2,2)\) and \((2,2,1,1)\), realized by exactly five and six vertices, first enter a fixed state at time five; the direct labelled update independently reproduces this witness. Each of the twenty period-six signatures requires at least six vertices on each shore. Conversely, the first seed pair realizes a six-cycle on \(K_{6,6}\), and increasing any clipped count two leaves all transition decisions unchanged. Hence six-cycles exist if and only if both sizes are at least six.

**Step 4: exact counting.** The exponential-generating-function coefficient \(U_s\) counts assignments of \(s\) labelled vertices to three *specified* colours, each occupied by at least two vertices, while the fourth specified colour is absent. The coefficient \(V_s\) counts one prescribed singleton colour and three prescribed colours each with multiplicity at least two. The coefficient \(W_s\) counts two prescribed singleton colours and two prescribed colours each with multiplicity at least two. These are counts for *specified positions*, not sums over colour rotations.

Four of the twenty period-six signatures correspond to each of the four paired choices \(U_mU_n\), \(U_mV_n\), \(V_mU_n\), and \(V_mV_n\). The remaining four correspond to \(W_mW_n\). Distinct signatures are disjoint. Multiplying and summing gives the asserted formula for \(N_6\). The four signatures already on cycles use the \(U_mU_n\) term alone. Dividing the number of periodic labelled states by six counts primitive orbits without overcounting.

**Step 5: asymptotic.** Standard finite-alphabet occupancy bounds give \(U_s=3^s+O(s2^s)\) and \(V_s=s3^{s-1}+O(s^2 2^s)\); also \(W_s=O(s^2 2^s)\). Thus \(N_6(s,s)\sim\frac49s^2 9^s\). Division by the total \(4^{2s}=16^s\) labelled configurations gives the displayed probability asymptotic.

## Verification

Run `python3 verify_symbolic.py` and `python3 verify_vertices.py` with the Python standard library. Captured verified outputs are included as `verify_symbolic.out` and `verify_vertices.out`. The first program is an exhaustive proof certificate over the exact \(6400\)-signature reduction; it checks the global identity, the complete period-six signature classification and independent multinomial enumerations for \((m,n)=(6,6),(6,7),(7,7),(8,9)\). The second uses the original vertex-level rule without the symbolic reduction; it exhaustively checks five smaller graph sizes, two six-cycle witnesses and the sharp entry-time witness.

## Relationship to prior work

Durrett and Griffeath (1993) introduced and studied contact-threshold cyclic colour dynamics primarily in spatial lattice contexts; their readily accessible abstract does not report this complete-bipartite four-colour basin census. Matamala and Goles (1995; 1997) studied cyclic automata on finite graphs and established graph-dependent bounds, an important and unusually close predecessor. Accessible abstracts describe general period/transient bounds, not the twenty-signature classification or exact labelled six-cycle basin formula. Their full texts could not be retrieved, so this comparison is incomplete and publication priority remains uncertain. Bello and Sivakoff (2021) study an infinite regular-tree setting and do not state finite complete-bipartite basin formulas in their accessible abstract. The finite-signature method and present exact enumerative specialization should not be confused with a claim of novelty for the cyclic update rule itself.

## Limitations

The theorem concerns exactly four colours, contact threshold two, synchronous updates, and complete bipartite graphs. It neither classifies every labelled four-cycle basin by formula nor extends automatically to other colour counts or arbitrary graphs. The exhaustive finite reduction is a machine-checkable finite proof, not a formal proof-assistant certification; no independent mathematical audit has been performed. The relevant 1995 and 1997 finite-graph primary texts remain inaccessible, creating a residual priority risk.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata* (first public arXiv posting 1993-03-22), https://arxiv.org/abs/patt-sol/9303002.
2. M. Matamala and E. Goles, *Cyclic Automata Networks on Finite Graphs*, LATIN 1995, pp. 398–410, https://doi.org/10.1007/3-540-59175-3_105.
3. M. Matamala and E. Goles, *Dynamic Behavior of Cyclic Automata Networks*, Discrete Applied Mathematics 77 (1997), pp. 161–184, https://doi.org/10.1016/S0166-218X(97)84104-2.
4. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg-Hastings Models on Regular Trees*, first public arXiv posting 2021-08-13, https://arxiv.org/abs/2108.06404.
