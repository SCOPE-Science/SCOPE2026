# Arithmetic saturation clocks for three-color excitable dynamics on cactus graphs

## Finding

For any finite connected simple cactus graph, the complete distribution of asymptotic excitation rates of both three-color cyclic cellular automaton (CCA) and threshold-one Greenberg–Hastings dynamics (GHM), over all uniformly chosen initial colorings, factors over the individual cycle blocks. This yields an arithmetic, sharp two-rate saturation window for bouquets of an exponentially growing number of equal-length cycles.

Let the cycle-block lengths be \(\ell_1,\ldots,\ell_r\ge3\), and let \(b\ge0\) be the number of bridges. Define the central trinomial coefficients
\[
 A_\ell(t)=[z^t](z^{-1}+1+z)^\ell,
 \qquad
 B_\ell(a)=\sum_{\substack{t\in\mathbb Z,\;3\mid t\\|t|\le a\ell}}A_\ell(t)
 \quad(a\ge0).
\]
Write \(\alpha_{\mathrm C}\) for the limiting fraction of time a vertex advances in CCA and \(\alpha_{\mathrm G}\) for the limiting fraction of time it changes from state zero to one in GHM. Each exists, is independent of vertex, and is determined by the initial coloring. For any real \(a\ge0\), the **exact number** of initial colorings for which \(\alpha_{\mathrm C}\le a\) is
\[
 \boxed{3^{b+1}\prod_{j=1}^r B_{\ell_j}(a).}
\]
The corresponding GHM count is \(3^{b+1}\prod_j B_{\ell_j}(3a)\). In particular, for each initial coloring,
\[
 \boxed{\alpha_{\mathrm C}=3\alpha_{\mathrm G},}
 \qquad
 \boxed{\#\{\text{synchronizing colorings}\}=3^{b+1}\prod_{j=1}^r A_{\ell_j}(0).}
\]
An empty product is one, covering trees. The cumulative distribution gives every exact rate population by subtraction at consecutive attainable rational rates. The graph has \(1+b+\sum_j(\ell_j-1)\) vertices and hence \(3^{1+b+\sum_j(\ell_j-1)}\) initial colorings.

A sharper phenomenon occurs in the bouquet \(H_{n,r}\) of \(r\) distinct cycles of length \(n\ge3\) sharing exactly one vertex. Let \(s\in\{0,1,2\}\) be the residue of \(n\) modulo three, and \(m=n-s\). The largest possible CCA activity is \(m/n\); the next smaller attainable activity for sufficiently large \(n\) is \((m-3)/n\). If \(n\to\infty\) through a fixed residue class and
\[
 r=r_n\sim c\,3^n/n^s,\qquad c>0,
\]
then the number of cycle blocks individually attaining \(|t|=m\) converges to a Poisson variable of mean \(6c/s!\). Consequently,
\[
 \boxed{\lim \Pr\!\left(\alpha_{\mathrm C}=m/n\right)=1-e^{-6c/s!},}
 \qquad
 \boxed{\lim \Pr\!\left(\alpha_{\mathrm C}=(m-3)/n\right)=e^{-6c/s!}.}
\]
All other activity values have total probability tending to zero. The corresponding GHM rates are precisely one third as large. More generally, the probability of attaining the maximal rate tends to zero when \(r_nn^s/3^n\to0\), and to one when \(r_nn^s/3^n\to\infty\). Thus the three circumference residues have distinct sharp scales \(3^n\), \(3^n/n\), and \(3^n/n^2\).

## Assumptions and scope

A finite simple cactus is a finite connected undirected loopless graph in which every edge lies on at most one simple cycle. Each cycle block is given an arbitrary orientation, irrelevant to absolute winding. Vertices have colors \(0,1,2\); all colorings are labelled and counted once. For CCA, a vertex of color \(i\) advances to \(i+1\pmod3\) if and only if a neighbor has that next color. For GHM, colors one and two always advance, while zero advances to one if and only if it has a neighbor of color one. Both updates are synchronous. Initial colors are uniform and independent when probabilities are stated. No stochastic forcing occurs after initialization.

The bouquet limit uses integer \(r_n\ge1\), fixed \(s\), and the limit along integers \(n\equiv s\pmod3\). The assertion about the next smaller rate concerns sufficiently large \(n\) so that \(m-3>0\). The limit probabilities are statements about varying graph size, not a fixed infinite graph or a limit of the dynamical time variable.

## Proof

**Step 1: Circulation and rate reduction.** Assign to an oriented edge \((u,v)\) the unique integer \(\delta(u,v)\in\{-1,0,1\}\) congruent to \(X(v)-X(u)\pmod3\), where \(X\) is the initial coloring. For a directed simple cycle \(C\) let \(T_C=\sum_{e\in C}\delta(e)\). Necessarily \(3\mid T_C\). The finite-graph circulation/activity theorem of Gravner, Lyu and Sivakoff [1, Theorem 3], applied to CCA, gives \(\alpha_{\mathrm C}=\max_C |T_C|/|C|\), taking the maximum to be zero when there are no cycles.

For GHM the source theorem uses a different edge form: \(+1\) on \(0\to1\), \(-1\) on \(1\to0\), and zero otherwise. For a directed closed cycle, conservation of occurrences of each of the three vertex colors makes the signed transition currents \(0\to1\), \(1\to2\), and \(2\to0\) equal. Therefore the CCA cycle sum is exactly three times the GHM cycle sum. The cited theorem consequently gives \(\alpha_{\mathrm G}=\alpha_{\mathrm C}/3\). Doba [2] independently gives the GHM maximum-cycle-density characterization. In a cactus, the simple cycles are precisely its cycle blocks, so no additional cycles need be considered.

**Step 2: Exact counting without independence assumptions at cut vertices.** Remove one edge from each of the \(r\) cycle blocks, obtaining a spanning tree. Specifying an initial color at one root and independently specifying all edge increments in \(\{-1,0,1\}\) along that spanning tree uniquely specifies the coloring. To extend a chosen increment for the deleted edge, the entire corresponding cycle sum must be divisible by three. Conversely, every assignment of increments to all original edges satisfying these \(r\) modular cycle constraints and one root color gives exactly one vertex coloring. Since the cactus cycle edge sets are disjoint, the \(r\) constraints involve disjoint edge variables. Every bridge supplies one unrestricted choice among three increments and the root supplies three choices. Thus for any prescribed cycle sums \(t_j\equiv0\pmod3\), the number of colorings is exactly
\[
 3^{b+1}\prod_{j=1}^r A_{\ell_j}(t_j).
\]
Taking the maximum of their normalized absolute values yields the claimed cumulative distribution. For zero activity, each \(t_j=0\); by [1, Theorem 3] this is exactly synchronization. The proof covers shared articulation vertices and bridge attachments, not only disjoint cycle components.

**Step 3: Rare maximal winds.** For one bouquet petal of length \(n\), uniform coloring induces a uniformly distributed edge-increment sequence among the \(3^{n-1}\) sequences with sum divisible by three. Different petals have independent sequences, despite sharing the hub, because the hub color determines the common additive origin but not their increments. The largest possible absolute cycle sum is \(m=n-s\), and its probability is exactly
\[
 p_n=\frac{2 A_n(m)}{3^{n-1}}.
\]
For any fixed nonnegative integer \(d\), the coefficient of maximal displacement deficit \(d\) obeys the exact finite identity
\[
 A_n(n-d)=\sum_{j=0}^{\lfloor d/2\rfloor}
  \binom{n}{j}\binom{n-j}{d-2j}
 =\frac{n^d}{d!}+O(n^{d-1}).
\]
Hence \(p_n\sim (6/s!)n^s3^{-n}\). The number of maximal-wind petals is binomial with parameters \(r_n,p_n\), giving the stated Poisson limit and maximal-activity probability.

**Step 4: Two-rate saturation.** The next possible nonnegative absolute winding is \(m-3\), attained on one petal with probability
\[
 q_n=\frac{2A_n(m-3)}{3^{n-1}}
 \sim\frac{6n^{s+3}}{(s+3)!3^n}
\]
for sufficiently large \(n\). Thus \(r_nq_n\to\infty\), while \(r_np_n\to6c/s!\). The probability that no petal attains either of these two largest windings is \((1-p_n-q_n)^{r_n}\to0\). The event of second-highest global activity is the event of no maximal petal but at least one second-highest petal, with limit \(e^{-6c/s!}\). If \(r_nn^s3^{-n}\) tends to zero or infinity, the elementary binomial zero-count probability \((1-p_n)^{r_n}\) gives the asserted outside-window dichotomy.

## Verification

The package contains four standalone Python 3 programs and their plain-text outputs. `exact_formula.py` enumerates coefficient histograms by integer dynamic programming and checks total configuration populations for bouquets, mixed cycles and bridges. `dynamics_check.py` independently enumerates **every initial state** of each of six labelled cactus graphs and simulates both dynamics to eventual cycles, comparing empirical activity histograms to the exact formulas. The largest tested space has \(59,049\) states per update rule. `nonbouquet_check.py` independently reconstructs the complete dynamics on three further cactus topologies (including a chain of cycles and bridge-joined cycles). `critical_check.py` checks exact near-endpoint coefficients and finite-binomial two-rate probabilities for several lengths in each residue class. The proofs above, not these finite computations, establish the assertions for arbitrary graphs and all large \(n\).

To reproduce from the package directory, run `python3 exact_formula.py`, `python3 dynamics_check.py`, `python3 nonbouquet_check.py`, and `python3 critical_check.py` in that order. The second program imports the first locally. The supplied output records come from these exact files and were replayed after extraction. The algorithms use only Python's standard library.

## Relationship to prior work

The finite-graph cycle-integral characterization for one initial state is **not new**: it is [1, Theorem 3]. Doba's independent GHM result [2] likewise already identifies the limiting excitation rate as a maximum cycle density. The contribution assessed here is the **exact population distribution over all initial states for all cactus topologies**, and the **arithmetic two-rate Poisson saturation threshold** when the number of loops scales exponentially with their length. These counts and asymptotic limits require an independent modular edge-increment count and a two-scale rare-event argument. Fisch and Gravner [3] analyze one-dimensional excitable automata with different geometries and do not give this network-wide distribution.

## Limitations

No claim is made about exact transient-entry times, individual periodic orbit lengths, or arbitrary noncactus graphs. The main result is an exact distribution of excitation *rates* for deterministic dynamics after uniform random initialization, not a stochastic cellular automaton. The finite verifiers test examples, not the infinite family. The argument relies on the published general cycle-integral theorem. Searches and targeted comparisons did not find prior exact cactus-population or saturation-window statements, but this is not proof of absolute historical priority: a previous equivalent enumeration, perhaps stated via independent modular-flow variables rather than automata, remains possible. The Poisson limit is a consequence of rare events with independent petals, not a claim of a new general Poisson approximation theorem.

## References

[1] J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, initially posted 2016-10-24; Annals of Applied Probability 28 (2018), 3324–3357. DOI: 10.1214/17-AAP1350. Open full text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf.

[2] N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126. DOI: 10.25088/ComplexSystems.27.2.101. Open full text: https://content.wolfram.com/uploads/sites/13/2018/09/27-2-1.pdf.

[3] R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems 9 (1995), 329–348. Open full text: https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf.
