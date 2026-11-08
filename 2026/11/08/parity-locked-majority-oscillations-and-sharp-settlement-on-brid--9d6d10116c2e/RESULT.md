# Parity-locked majority oscillations and sharp settlement on bridge barbells

## Finding
Let \(B_{m,n}\), for integers \(m,n\ge3\), consist of two disjoint labelled cliques \(K_m\) and \(K_n\) joined by exactly one bridge between specified hubs. Update every binary vertex opinion synchronously to the strict majority among its open neighbors, keeping its previous opinion on a tie. Denote the update by \(F\), the first periodic-entry time by \(\tau(x)=\min\{t\ge0:F^{t+p}(x)=F^t(x)\text{ for some }p\ge1\}\), and the eventual least period by \(p(x)\).

**Theorem.** All \(2^{m+n}\) initial configurations become fixed or two-periodic. There are exactly four fixed configurations, namely one unanimous opinion for each clique. Primitive two-cycles exist **if and only if both clique orders are even**, in which case their number is
\[
C_{m,n}=\binom{m-1}{m/2}\binom{n-1}{n/2}.
\]
Exactly \(2C_{m,n}\) labelled configurations belong to such two-cycles, and **no initially nonperiodic configuration ever enters one**: \(p(x)=2\Rightarrow\tau(x)=0\). The sharp first-entry bound is
\[
\max_x\tau(x)=\begin{cases}2,&m,n\text{ both odd},\\4,&m,n\text{ both even},\\5,&m,n\text{ of opposite parity}.\end{cases}
\]
Thus every other configuration reaches one of the four fixed configurations at the stated finite bound. For independent uniformly random initial bits, when \(m,n\) are even,
\[
\Pr(p(x)=2)=\frac{2\binom{m-1}{m/2}\binom{n-1}{n/2}}{2^{m+n}}\sim\frac{1}{\pi\sqrt{mn}}
\]
as both even clique orders grow. If either order is odd, this probability is zero.

## Assumptions and scope
Vertices are labelled: within each clique, one designated hub is incident to the bridge. The cliques have orders at least three, there are no self-loops or multiple edges, and updates are deterministic and **simultaneous**. An open-neighbor tie leaves the vertex unchanged. The probability assertion refers to the uniform measure on all \(2^{m+n}\) binary configurations, not random graph sampling. Statements about asymptotic probability are along even \(m,n\to\infty\), with no requirement on their ratio.

## Proof
**1. Reduction to clique counts.** For a clique of order \(k\), let \(a\in\{0,\dots,k-1\}\) count occupied nonhub vertices, let \(x\in\{0,1\}\) be its hub, and let \(y\) be the opposite hub. Its hub sees \(a+y\) occupied vertices and has degree \(k\). An occupied nonhub sees \(a+x-1\) occupied neighbors; an unoccupied nonhub sees \(a+x\), each of degree \(k-1\). Consequently the new nonhub count is
\[
a'=a\mathbf1_{\{2(a+x-1)\ge k-1\}}+(k-1-a)\mathbf1_{\{2(a+x)>k-1\}},
\]
while its hub is updated according to
\[
x'=\mathbf1_{\{2(a+y)>k\}}+x\mathbf1_{\{2(a+y)=k\}}.
\]
These formulas also determine which labelled nonhub vertices change: a nonhub's new bit depends only on its old bit and on \(a+x\).

**2. An odd clique becomes locally frozen.** If \(k=2h+1\), \(h\ge1\), all its nonhubs become 1 when \(a+x\ge h+1\), and all become 0 otherwise. Once nonhubs are unanimous, they never change, and the hub takes their opinion at the next update, regardless of the opposite hub. Hence an odd clique's nonhubs are permanently unanimous from update 1 and the whole clique is frozen by update 2. In particular, an odd clique cannot participate in an eventual two-cycle.

**3. An even clique has exactly two critical count states.** Put \(k=2h\), \(h\ge2\). If \(a+x\le h-1\), the entire clique becomes 0 at the next update; if \(a+x\ge h+1\), it becomes entirely 1. For example, in the first case \(a+y\le h\) when \(x=0\), and \(a+y<h\) when \(x=1\); the hub therefore becomes 0. The other case is symmetric. Both unanimous clique states are permanent, regardless of its external hub. The only exception is the **critical** condition \(a+x=h\). Then
\[
(a',x')=(2h-1-a,y).
\]
In particular all \(2h-1\) nonhub bits **flip**. The clique remains critical at the following time if and only if \(x+y=1\) at the previous time. Its hub then also flips. In the critical states \((a,x)=(h,0)\) and \((h-1,1)\), a failed critical condition immediately produces a noncritical state, which becomes unanimous on the next update.

**4. Periodic states and their exact count.** A periodic state containing an odd clique cannot oscillate there (Step 2). An even clique cannot oscillate unless it is critical at every time; otherwise it becomes unanimously frozen (Step 3). A pair of even cliques remains simultaneously critical exactly when their hubs disagree, and then both hubs and all nonhub bits flip on each update. Conversely, whenever both cliques are critical with opposite hub bits, every vertex flips at every update, giving a primitive two-cycle. There are exactly
\(\binom{m-1}{m/2}\binom{n-1}{n/2}\)
choices for the labelled occupied nonhubs in the orientation (left hub 0, right hub 1); the reverse orientation gives the other member of each cycle. The four unanimous-by-clique states are exactly the fixed configurations. Finally, a noncritical even clique has only unanimous outputs, and a critical output with a mixed nonhub set can only come from a critical input. Every predecessor of a two-cycle state must therefore already have both cliques critical with opposite hubs, and is its other two-cycle state. This proves that the two-cycle basin contains only its periodic configurations.

**5. Uniform settlement bounds.** If both clique orders are odd, Step 2 freezes the whole graph by update 2. For an even clique, the critical condition can survive from one time to the next only if the two hub bits were opposite; in that event its own hub copies the external hub. If both cliques are even and initially critical, opposite hub bits give a two-cycle; equal hub bits cause both cliques to become noncritical after one update and unanimous after the next, hence fixed by update 2. If neither even clique is initially critical, both are fixed after one update. If just one is initially critical, the other becomes unanimous at update 1. The surviving critical clique can remain critical through update 2 but not beyond: the other hub is constant from update 1 onward, so successive critical steps would require it to alternate. If it is still critical at update 2, its hub equals the now-constant external hub; at update 3 it becomes noncritical, and at update 4 it becomes unanimous in the same opinion as that hub. Thus every even-even configuration is periodic by update 4.

If one clique is odd and the other even, the odd clique is fixed by update 2. Its hub may change over the first two updates but is constant thereafter. The even clique can be critical through update 3; if it is, its hub at update 3 equals the stable opposite hub. It therefore becomes noncritical at update 4 and unanimous at update 5. Otherwise it settles earlier. This proves the upper bound of 5. Cases in which a critical even clique becomes noncritical sooner only improve the bound.

**6. Explicit sharp witnesses.** Write the initial state as \((a,x,b,y)\), where \(a,b\) count occupied nonhubs and \(x,y\) are hub bits. When \(m,n\) are odd, \((0,0,(n-1)/2,1)\) has first-entry time 2. For even \(m,n\), \((0,1,n/2,0)\) has first-entry time 4. For odd \(m\) and even \(n\), \(((m-1)/2,0,n/2-1,1)\) has first-entry time 5; for even \(m\) and odd \(n\), \((m/2-1,1,(n-1)/2,0)\) has first-entry time 5. These are legal states for every stated order, and substitution into the two exact update formulas confirms each time claim. Thus all bounds are sharp.

**7. Probability.** There are \(2^{m+n}\) equally likely initial configurations. Divide the precise period-two population by this value. For even \(m,n\), use \(\binom{m-1}{m/2}=\frac12\binom m{m/2}\) and Stirling's central-binomial asymptotic \(\binom m{m/2}/2^m\sim\sqrt{2/(\pi m)}\). This gives the asserted constant \(1/(\pi\sqrt{mn})\).

## Verification
The accompanying standalone `direct_states.py` checks every labelled configuration on all \(21\) pairs \(3\le m\le n\le8\), testing exact periods, first-entry bounds, four fixed states, and the period-two formula; it traverses \(170688\) labelled initial states. The independent `class_states.py` iterates over all \(4mn\) count/hub states for each ordered \((m,n)\in[3,50]^2\), weighting each by \(\binom{m-1}{a}\binom{n-1}{b}\). The `witnesses.py` program independently evaluates each explicit sharp witness for \(9604\) ordered pairs \((m,n)\in[3,100]^2\). The captured output files report successful completion. Finite computations corroborate but do not replace the uniform symbolic proof.

## Relationship to prior work
Goles and Olivos (1980) established eventual period at most two for symmetric threshold dynamics; this proof uses that setting but independently proves the stronger uniform bounds. Benjamini et al. (arXiv:1405.2486v1, submitted May 11, 2014) study convergence and period-two behavior on unimodular and random graphs, rather than a full exact barbell classification. Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519v1, submitted August 14, 2015) introduce graph-module-based general voting-time bounds; their clique-module results motivate the two dense communities here, but their theorems do not specify this exact 2/4/5 sharp trichotomy, the labelled cycle count, or the zero transient basin of those cycles. A general 2020 dense-random-graph stabilization theorem likewise does not imply a sharp theorem for two bridge-connected deterministic cliques. The barbell graph is a standard example of weakly linked dense communities; the structure itself is not claimed as new.

## Limitations
The result is restricted to a single bridge joining cliques of orders at least three, synchronously updated binary majority, and the stated tie rule. It counts all recurrent orbits and their total basin sizes but does **not** give separate exact basin counts for each of the four fixed configurations or the full distribution of individual transient-entry times. The novelty assessment compares accessible literature and the identified exact statements, not all unindexed historical work. No independent external audit or formal certification was performed.

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (May 11, 2014), https://arxiv.org/abs/1405.2486.
3. D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1 (August 14, 2015), https://arxiv.org/html/1508.03519v1.
4. N. Fountoulakis, M. Kang, T. Makai, *Resolution of a conjecture on majority dynamics: Rapid stabilization in dense random graphs*, Random Structures & Algorithms 57 (2020), 1134–1156. DOI: 10.1002/rsa.20970.
