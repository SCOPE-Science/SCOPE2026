# Power-of-two oscillatory basins and a quarter-law in mixed adaptive threshold stars

## Finding

Consider the synchronous mixed adaptive threshold system of Chang, Cochran, Mortveit, Raval and Schroeder on the labelled star \(K_{1,m}\), for every integer \(m\ge1\). The hub has \(m\) leaves. Each vertex \(v\) has an opinion \(x_v\in\{0,1\}\) and a threshold \(k_v\in\{1,\ldots,d(v)+1\}\). At each update, every opinion becomes one if its **closed-neighborhood** sum reaches its current threshold; the threshold rises by one when the opinion changes from zero to one, falls by one when it changes from one to zero, and otherwise stays unchanged.

Every initial extended state becomes fixed or two-periodic after at most two synchronous updates: \(F^4=F^2\). This is sharp for \(m\ge2\) (for \(m=1\) one update suffices). There are exactly
\[
\operatorname{Fix}(F)=2(2m+3)3^{m-1},\qquad
\mathcal C_2=m3^{m-1}
\]
fixed extended states and primitive two-cycle **orbits**, respectively. For each \(1\le c\le m\), the number of primitive two-cycle orbits whose complete attraction basin contains **exactly** \(2^c\) initial extended states is
\[
\boxed{\binom mc 2^{m-c}c}.
\]
No other primitive two-cycle basin size occurs. Consequently the entire primitive-two attraction basin contains \(2m4^{m-1}\) initial extended states out of \(2(m+1)4^m\), and a uniform random extended state eventually oscillates with probability
\[
\boxed{\frac{m}{4(m+1)}\longrightarrow\frac14}.
\]
In contrast, its probability of **already** lying on a primitive two-cycle is \(\frac{m}{3(m+1)}(3/4)^m\), which decays exponentially.

Writing \(N_t\) for the number of initial extended states whose **least** entry time into a periodic orbit is \(t\), the exact full first-entry census is
\[
\begin{aligned}
N_0&=6(m+1)3^{m-1},\\
N_2&=m\left(2\cdot4^{m-1}-2^m\right),\\
N_1&=2(m+1)4^m-N_0-N_2,\\
N_t&=0\quad(t\ge3).
\end{aligned}
\]
For \(m=1\), the \(N_2\) term is zero; for every \(m\ge2\) it is positive.

## Assumptions and scope

The star is finite, simple, labelled, unweighted, with \(m\ge1\). All vertices update **simultaneously**, using old extended states, and threshold values lie in \(1,\dots,d(v)+1\). The initial-state distribution used for probabilities is independent uniform sampling over every legal opinion-threshold pair, not over opinions alone. A periodic orbit and a basin are in the full extended state space, including thresholds, not just the Boolean projection.

The exact rule for the old local extended state \((x_v,k_v)\) is
\[
 x'_v=\mathbf1\!\left\{\sum_{u\in N[v]}x_u\ge k_v\right\},\qquad k'_v=k_v+x'_v-x_v.
\]
The update preserves threshold admissibility. In particular the boundary threshold cannot leave its allowed interval under an opinion flip.

## Proof

**Invariant reduction and leaf types.** Set \(h_v=k_v-x_v\). This quantity is invariant because \(k'_v-x'_v=k_v-x_v\). The opinion rule becomes \(x'_v=\mathbf1\{\sum_{u\sim v}x_u\ge h_v\}\). For a leaf of degree one, there are precisely three invariant classes: \(A\), \(h=0\), necessarily opinion one; \(B\), \(h=2\), necessarily opinion zero; and \(C\), \(h=1\), whose opinion after each update equals the hub's preceding opinion. For the hub, \(h\in\{0,\ldots,m+1\}\). Opinion one is the only admissible hub opinion if \(h=0\), opinion zero the only one if \(h=m+1\), and both are admissible for \(1\le h\le m\).

**Hub recurrence.** Let \(a,b,c\) be the counts of leaf types \(A,B,C\), with \(a+b+c=m\). Let \(H_t\) be the hub opinion at update \(t\), and let \(J\) be the number of initially active \(C\)-leaves. At the first update,
\[
H_1=\mathbf1\{a+J\ge h\}.
\]
For every \(t\ge1\), all \(C\)-leaves have opinion \(H_{t-1}\) at time \(t\), so
\[
H_{t+1}=g(H_{t-1}),\quad
 g(0)=\mathbf1\{a\ge h\},\quad
 g(1)=\mathbf1\{a+c\ge h\}.
\]
If \(h\le a\), then \(g\equiv1\) and \(H_1=1\) for every possible \(J\); if \(h>a+c\), then \(g\equiv0\) and \(H_1=0\). In either case all hub and leaf opinions become fixed by time two. In the remaining central interval \(a<h\le a+c\), \(g\) is the identity: \(H_{t+1}=H_{t-1}\), and the flexible leaves copy the preceding hub. At time one the state is already fixed or two-periodic. Thus every state is periodic by time two, as asserted.

**Two-cycle classification and basins.** For each labelled assignment of leaf types with \(c\ge1\), there are precisely \(c\) central integer hub thresholds. At each such threshold there is exactly one primitive two-cycle orbit: the hub alternates, all \(C\)-leaves alternate in the opposite phase, and \(A,B\) stay fixed. For this orbit, each of the \(2^c\) arbitrary initial words on the \(C\)-leaves permits exactly one initial hub opinion for which \(H_1\ne H_0\), because \(H_1\) is fixed by that word. This yields an exact full basin of \(2^c\) extended states, including the two periodic states. There are \(\binom mc2^{m-c}\) labelled leaf-type assignments with \(c\) flexible leaves, hence \(\binom mc2^{m-c}c\) distinct two-cycle basins of that size. Summing their counts gives
\[
\mathcal C_2=\sum_{c=1}^m\binom mc2^{m-c}c=m3^{m-1},\quad
B_2=\sum_{c=1}^m\binom mc2^{m-c}c2^c=2m4^{m-1}.
\]

**Fixed states.** Given any leaf-type assignment, a fixed hub zero has exactly \(m+1-a\) possible hub invariants \(h\), while a fixed hub one has \(a+c+1\). Each choice forces all \(C\)-leaf opinions to match the hub. This makes \(m+c+2\) fixed states per assignment. Sum across \(\binom mc2^{m-c}\) assignments to obtain
\[
\operatorname{Fix}(F)=\sum_{c=0}^m\binom mc2^{m-c}(m+c+2)=2(2m+3)3^{m-1}.
\]

**Entrance-time census and sharpness.** There are \(2(m+1)4^m\) legal initial states. Already-periodic states consist of fixed states and both phases of all primitive two-cycles, giving \(N_0\). An initial state needs exactly two updates precisely when \(c\ge1\), the hub invariant is outside the central interval, and the initial hub differs from the eventually forced constant. With leaf-type counts \((a,b,c)\), there are \(a+b\) such admissible choices of the hub invariant, and \(2^c\) possible initial flexible-leaf words. Consequently
\[
N_2=\sum_{c=1}^m\binom mc2^{m-c}(m-c)2^c=m(2\cdot4^{m-1}-2^m).
\]
For \(m\ge2\), take two leaves, one permanently active and one flexible, a hub invariant forcing permanent activation, and initially inactive hub: this provides a two-update witness. The remaining \(N_1\) follows by subtraction and includes no unclassified orbit because of the universal two-update bound.

## Verification

Two supplied standalone Python scripts can be executed with Python 3 and its standard library. `verify_exhaustive.py` enumerates **all 72,816 legal extended states** across \(m=1,\ldots,6\), follows each entire orbit, independently identifies each primitive attractor and its full basin, and checks each predicted orbit-size bin and entrance-time count. `verify_formula.py` independently sums the leaf-type multinomial decomposition for \(m=1,\ldots,30\), including the boundary \(m=1\). Both programs passed. The finite tests are checks of the all-size symbolic proof, not substitutes for it.

## Relationship to prior work

Chang, Cochran, Mortveit, Raval, and Schroeder (2013) introduce precisely this mixed extended-threshold rule and prove that synchronous systems on arbitrary graphs have only fixed points and two-cycles (Theorem 3.1); they also provide fixed-state enumeration tools for trees (Theorem 4.7). Those results establish general orbit-length restrictions and allow fixed-state counts, but their inspected sections do not give the oscillatory basin-size spectrum, uniform initial-state attraction probability, or sharp first-entry histogram for the star. The current result specializes to an intrinsically meaningful two-level network and quantitatively separates the rarity of recurrent oscillatory configurations from the large basins they attract. Related published work on **static** or sequential bi-threshold maps uses different dynamics and does not imply the invariant and exact mixed-rule basin spectrum.

## Limitations

The proof is limited to synchronous mixed adaptive thresholds on stars, with threshold and opinion both included in the state; it does not cover increasing-only, decreasing-only, or sequential updates, nor arbitrary trees. Uniform probabilities require sampling legal extended states rather than an externally specified distribution of opinions. Priority comparison used the publicly available primary manuscript, related source descriptions and targeted published-record searches; an unindexed or otherwise undiscovered equivalent enumeration could change priority assessment. Independent mathematical audit has not been performed.

## References

1. L. Chang, J. Cochran, H. S. Mortveit, S. Raval, M. Schroeder, *Adaptive Complex Contagions and Threshold Dynamical Systems*, arXiv:1305.4599v1 (first public submission 2013-05-20), https://arxiv.org/abs/1305.4599 ; accessible complete HTML https://ar5iv.labs.arxiv.org/html/1305.4599 . See Definitions 2.1–2.2, Theorem 3.1, and Section 4, especially Theorem 4.7.
2. E. Goles and J. Olivos, *Periodic behavior in generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, as cited in reference [7] of Chang et al. The classical theorem concerns possible period lengths, not this star-level mixed adaptive basin census.
