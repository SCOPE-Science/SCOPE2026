# One odd clique blade pins the hub: exact attractors of asynchronous minority on clique bouquets

## Finding

Let \(m\ge2\), let \(r_1,\ldots,r_m\ge1\) be arbitrary integers, and let \(G\) be the graph formed by taking cliques of orders \(r_i+1\) and identifying exactly one vertex, denoted \(h\), among all of them. Every other vertex lies in exactly one clique blade. At each discrete step a uniformly chosen vertex adopts the minority binary opinion in its **closed** neighborhood (the selected vertex is included); in a tie it keeps its opinion. Define
\[
 a_i=\left\lfloor\frac{r_i}{2}\right\rfloor,
 \qquad w_i=\binom{2a_i+1}{a_i},
 \qquad N=1+\sum_{i=1}^m r_i.
\]

**Theorem.** From every initial binary configuration the chain almost surely reaches its set of global maximum-cut configurations. This set is exactly the union of its recurrent communicating classes and has
\[
 R=2\prod_{i=1}^m w_i
\]
labelled configurations. Its recurrent-class decomposition is determined completely by blade parity.

If **every** \(r_i\) is even, all \(R\) states communicate in **one** recurrent class. The hub changes opinion under stationary dynamics with exact one-step probability
\[
 p_h=\frac1N\prod_{i=1}^m\frac{a_i+1}{2a_i+1}>0.
\]
For the discrete-time chain restricted to that class, the total-variation mixing time satisfies
\[
 t_{\mathrm{mix}}(1/4)\ge
 \left\lceil\frac{N}{4}\prod_{i=1}^m\frac{2a_i+1}{a_i+1}\right\rceil.
\]
The stationary mean number of updates between consecutive hub changes is \(1/p_h\).

If **at least one** \(r_i\) is odd, the hub is permanently frozen after the recurrent set is reached, and the number of recurrent classes is
\[
 K=2\prod_{i:\,r_i\ \mathrm{odd}}\binom{r_i}{(r_i-1)/2}.
\]
Every class has the same size
\[
 S=\prod_{i:\,r_i\ \mathrm{even}}\binom{r_i+1}{r_i/2},
\]
with the empty product interpreted as \(1\). Each class is irreducible and has the uniform stationary law; if all blades are odd, every recurrent class is an absorbing singleton.

**One-vertex parity switch.** If at least two blades are present and all \(r_i\) are even, enlarging exactly one blade from \(r_j=2a\) to \(r_j=2a+1\) by adding a vertex adjacent precisely to that clique changes neither the total recurrent-state count \(R\) nor the maximum-cut character of the recurrent set. It changes the number of recurrent classes from \(1\) to \(2\binom{2a+1}{a}\), and prevents the hub from changing opinion within any recurrent class.

For instance, the blades \((4,4)\) give \(R=200\) recurrent states in one class, whereas blades \((4,5)\) give the same \(R=200\) recurrent states divided into \(20\) classes of \(10\) states. These are different labelled graphs, with nine and ten vertices respectively, and the statement concerns their recurrent-state **populations**, not a state-preserving bijection of trajectories.

## Assumptions and scope

All graphs are finite, simple and undirected; vertex labels and the blade partition are fixed. There are no edges between private vertices of different blades. The only common vertex is \(h\). Every \(r_i\ge1\) is allowed, so a blade may be a single pendant edge. The update is uniform, sequential, binary and closed-neighborhood minority with tie retention. The stated mixing time concerns the unique recurrent class in the all-even case, not the transient full-state chain or any nonergodic mixed-parity chain. The initial state may be arbitrary.

Write \(k_i\) for the number of private vertices in blade \(i\) agreeing with the hub's current opinion. If \(r_i=2a_i\), define the admissible levels \(k_i\in\{a_i-1,a_i\}\). If \(r_i=2a_i+1\), the sole admissible level is \(k_i=a_i\).

## Proof

**1. Cut monotonicity and blade reduction.** Consider an update at a vertex of open degree \(d\). Let \(s\) count its agreeing **open** neighbors and \(d-s\) its disagreeing open neighbors. Including the vertex itself, the minority rule flips the vertex precisely when \(2(s+1)>d+1\), equivalently when \(2s\ge d\). If the vertex flips, the change in the number of cut edges is \(s-(d-s)=2s-d\ge0\). Thus every transition has nondecreasing cut size; strict cut increase cannot occur along a recurrent cycle.

For a private vertex of blade \(i\), its closed neighborhood is exactly the clique of order \(r_i+1\). With the hub opinion held fixed, the hub side of the clique has \(k_i+1\) vertices and the opposite side has \(r_i-k_i\). A private vertex agreeing with the hub flips if and only if
\[
 2(k_i+1)>r_i+1,
\]
whereas a disagreeing private vertex flips to the hub opinion if and only if
\[
 2(r_i-k_i)>r_i+1.
\]
If \(r_i=2a_i+1\) is odd, these rules strictly increase the blade cut until \(k_i=a_i\), where no private vertex is active. If \(r_i=2a_i\) is even, they strictly increase the blade cut until \(k_i\in\{a_i-1,a_i\}\); at those two adjacent levels, private updates may occur, but preserve the cut and move only between those levels. From any state and while avoiding updates of \(h\), choosing out-of-range private vertices successively reaches all admissible levels after at most \(\sum_i r_i\) actual flips.

**2. These and only these states are global maximum cuts.** Every edge belongs to one clique blade. For a clique of order \(r_i+1\), the largest possible cut is \(\lfloor(r_i+1)^2/4\rfloor\), achieved exactly by the two as-equal-as-possible color-class sizes. For a specified hub spin these are precisely the admissible \(k_i\) from Step 1. Because all blade choices can be realized simultaneously for either hub spin, the maximum cut of \(G\) is the sum of the individual clique maxima; its complete maximizing set \(\mathcal M\) consists of the admissible states.

**3. The set \(\mathcal M\) is closed and accessible.** At every state of \(\mathcal M\), private updates remain within \(\mathcal M\). The hub's closed neighborhood contains all \(N\) vertices. It flips precisely when
\[
 1+2\sum_{i=1}^m k_i>\sum_{i=1}^m r_i.
\]
An odd blade contributes \(2k_i-r_i=-1\); an even blade contributes \(-2\) at its lower admissible level and \(0\) at its upper level. Consequently the hub can flip at an admissible state if and only if **all** blades are even and **all** \(k_i=a_i\). In that case, changing the hub opinion leaves each new \(k_i=r_i-a_i=a_i\), and therefore remains in \(\mathcal M\). If an odd blade exists, the hub cannot flip anywhere in \(\mathcal M\). Hence \(\mathcal M\) is closed. From any initial state there is a finite permitted sequence of private-only updates into \(\mathcal M\), by Step 1. Since the state space is finite and every selected vertex has positive probability, the hitting time of this accessible closed set is finite almost surely.

**4. Communicating classes.** For an even blade \(r_i=2a_i\), with the hub held fixed, the admissible private configurations are the subsets of \(2a_i\) private vertices of sizes \(a_i-1\) and \(a_i\). A permitted private update inserts or removes one private vertex, moving along edges of the two adjacent Boolean-lattice layers. That bipartite inclusion graph is connected: to exchange an element in a lower-level subset, first insert the desired new element and then delete an undesired one; the upper layer is linked to the lower layer. Its total number of vertices is
\[
 \binom{2a_i}{a_i-1}+\binom{2a_i}{a_i}
 =\binom{2a_i+1}{a_i}=w_i.
\]
For an odd blade \(r_i=2a_i+1\), a fixed-hub admissible private configuration has exactly \(a_i\) agreeing vertices; all private vertices are inactive. There are \(\binom{2a_i+1}{a_i}=w_i\) such frozen choices.

With the hub fixed, the transition graph of \(\mathcal M\) is the Cartesian product of all even-blade inclusion graphs, with separate components indexed by the fixed choices of all odd blades. If any odd blade exists, the hub never moves and these are exactly the recurrent classes, giving the stated number and sizes. If every blade is even, each hub-spin half is connected, and the all-upper-level configurations provide hub-flip edges joining the two halves. Therefore the entire \(\mathcal M\) is one communicating class. Every permitted nontrivial transition in \(\mathcal M\) is reversible by updating the same vertex once more and has transition probability \(1/N\) in either direction. Hence the uniform law on each recurrent class is stationary and unique. Each class contains a self-loop with positive probability: e.g. selecting an inactive vertex; in the all-even case there are also boundary states with inactive hub or private vertices. The chain is thus aperiodic in each recurrent class.

Counting \(w_i\) admissible private choices for each of the two hub opinions gives \(R=2\prod_i w_i\), completing the census.

**5. Hub flux and mixing.** Assume all \(r_i=2a_i\) are even. Conditional on a fixed hub opinion under the uniform stationary law, blade choices are independent and uniform over their \(w_i\) admissible private configurations. The hub may flip only when all blades occupy their upper layers. In blade \(i\), the fraction of upper-layer configurations is
\[
 \frac{\binom{2a_i}{a_i}}{\binom{2a_i+1}{a_i}}=
 \frac{a_i+1}{2a_i+1}.
\]
Since the hub is selected with probability \(1/N\), the exact stationary flip probability per update is \(p_h\) as stated. The stationary flux gives mean inter-flip time \(1/p_h\).

To obtain the total-variation bound, start from the stationary distribution conditioned on the hub opinion \(0\). This initial law has density at most \(2\) with respect to stationarity, and that domination persists after every transition. Under the full stationary law, the one-step probability of a \(0\to1\) hub flip is \(p_h/2\), by spin-complement symmetry. Consequently, under the chosen initial law, the probability of **any** such flip in the first \(t\) updates is at most \(t p_h\), by the union bound and domination. The probability that the hub is \(1\) at time \(t\) is therefore at most \(t p_h\), whereas its stationary probability is \(1/2\). Thus
\[
 \|\mu_t-\pi\|_{\mathrm{TV}}\ge\frac12-tp_h.
\]
Whenever \(t<1/(4p_h)\), this exceeds \(1/4\). The worst-initial-state mixing time is at least \(\lceil1/(4p_h)\rceil\), as asserted.

**6. One-vertex parity switch.** For \(r=2a\) and \(r'=2a+1\), the admissible number of private assignments per fixed hub is the **same**:
\[
 \binom{2a}{a-1}+\binom{2a}{a}
 =\binom{2a+1}{a}.
\]
The all-even case has one recurrent class, but after enlarging one blade to odd, the former moving Boolean-layer choices of that blade become \(\binom{2a+1}{a}\) frozen choices for each of two hub opinions. The formulas for \(R\) and \(K\) therefore give the asserted no-population-change fragmentation. This proves all claims.

## Verification

The standalone standard-library scripts `check_scc.py` and `check_local.py` implement separate exhaustive tests. Execute `python3 check_scc.py` and `python3 check_local.py` in their containing directory. Their exact captured standard outputs are in `check_scc.out` and `check_local.out`. The first constructs the entire finite transition graph and its closed strongly connected components on 88 small blade-size tuples, covering 28,276 labelled starting configurations; it also checks equality between the union of recurrent states and the entire maximum-cut set. The second independently enumerates local strict-cut improvement, admissible states and hub-flip flux on 637 blade tuples. These are finite consistency tests; the proof above, not extrapolation from enumeration, establishes all integer-size conclusions.

## Relationship to prior work

Rouquier, Regnault and Thierry's *Stochastic Minority on Graphs* (arXiv:1011.5119, first arXiv posting 2010-11-23) defines this precise update rule, shows monotonicity of the associated edge-energy, and classifies the complete-graph case (its Sections 2, 3.1 and Theorem 4.1). The one-blade special case of this theorem is consequently **not** a new result. An earlier specific calculation for a clique with one private leaf, and the triangle friendship-graph case, likewise cover two special subfamilies; neither implies the heterogeneous shared-hub classification without additional coupling arguments. The substantive extension here is the exact parity-pinning of the hub for arbitrary mixed clique blades, including a one-vertex discontinuity in irreducible-class count while the **entire** recurrent-state population is unchanged, plus the all-even stationary hub-crossing law and mixing obstruction. Kooij's work on generalized windmill graphs studies graph structure rather than this dynamics.

## Limitations

The result is specific to uniform single-site updates, closed-neighborhood minority, and exactly one shared hub; it makes no claim about simultaneous updates, open-neighbor updates, arbitrary block graphs with several articulation vertices, finite-temperature Glauber chains or nonuniform update rates. The mixing result is a lower bound, not a matching upper bound. Exact absorption times and absorption probabilities between frozen-hub classes are not determined. The historical-priority assessment is based on the accessible primary sources and search comparisons described in the review, not on an exhaustive survey of every unindexed paper. A separate independent scientific audit has not been performed.

## References

1. J.-B. Rouquier, D. Regnault and É. Thierry, *Stochastic Minority on Graphs*, arXiv:1011.5119 (first public arXiv version, 2010-11-23), https://arxiv.org/abs/1011.5119 ; accessible full HTML https://ar5iv.labs.arxiv.org/html/1011.5119 .
2. R. Kooij, *On generalized windmill graphs*, Linear Algebra and its Applications, DOI:10.1016/j.laa.2018.11.025 (graph-family terminology and structure only).
3. U. Yu, *Fate of Ising ferromagnets and antiferromagnets by zero-temperature Glauber dynamics on the two-dimensional Archimedean and 2-uniform lattices*, arXiv:1710.09946 (a related, different geometry and stochastic prescription).
