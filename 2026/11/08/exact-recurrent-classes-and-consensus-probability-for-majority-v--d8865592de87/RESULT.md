# Exact recurrent classes and consensus probability for majority voting on a loose hyperstar

## Finding
Consider a fixed, connected, three-uniform loose hyperstar with \(k\geq 2\) petals: its vertices are a hub \(h\) and disjoint leaf pairs \(\{u_j,v_j\}\), with hyperedges \(\{h,u_j,v_j\}\) for \(1\leq j\leq k\). Every vertex has opinion \(\mathrm A\) or \(\mathrm B\). Each hyperedge has its own independent rate-one Poisson clock. When its clock rings, all three vertices adopt their common majority opinion. A ringing unanimous edge has no effect.

**Theorem.** The resulting finite continuous-time Markov chain has exactly \(2^k\) closed communicating classes: two singleton consensus states and, for every nonempty proper subset of petals, one two-state polarized class. In such a class, leaf pairs retain their respective opposite colors forever while the hub switches endlessly. In particular, exactly \(2^k-2\) recurrent classes have persistent disagreement.

For a fixed initial state, let \(a\) be the number of leaf pairs initially both \(\mathrm A\), \(b\) the number initially both \(\mathrm B\), \(m=k-a-b\) the number initially mixed, and \(H\) the initial hub opinion. The probability of eventual *global consensus* is exactly
\[
\mathcal P(a,b,m;H)=
\begin{cases}
0,& a>0,\ b>0,\\
1,& a=b=0,\\
1,& a>0,\ b=0,\ H=\mathrm A,\\
\dfrac{a}{a+m},&a>0,\ b=0,\ H=\mathrm B,\\
1,& b>0,\ a=0,\ H=\mathrm B,\\
\dfrac{b}{b+m},&b>0,\ a=0,\ H=\mathrm A.
\end{cases}
\]
(The lines with two constraints separated by a comma describe the same case.) If initially every vertex independently has opinion \(\mathrm A\) with probability \(q\in[0,1]\), then
\[
\boxed{\mathbb P(\text{eventual consensus}) =q^2(3-2q)(2q-q^2)^{k-1}+(1-q)^2(1+2q)(1-q^2)^{k-1}.}
\]
In particular, for unbiased initial opinions, the exact consensus probability is \((3/4)^{k-1}\), and hence the probability of *perpetual disagreement* tends to one exponentially fast with \(k\), even though the hypergraph is connected.

For \(m\geq 1\), the first time \(\tau\) when every initially mixed leaf pair has become monochromatic has distribution
\[
\mathbb P(\tau\leq t)=(1-e^{-t})^m\quad(t\geq0),\qquad \mathbb E\tau=H_m=\sum_{r=1}^{m}\frac1r.
\]
For \(m=0\), set \(\tau=0\). After this time, the leaves never change again. Conditional on \(a'\geq1\) final \(\mathrm A\) petals and \(b'\geq1\) final \(\mathrm B\) petals, the hub evolves as a two-state chain with rates \(\mathrm A\to\mathrm B\) equal to \(b'\) and \(\mathrm B\to\mathrm A\) equal to \(a'\), and stationary probabilities \(a'/(a'+b')\), \(b'/(a'+b')\).

## Assumptions and scope
All clocks are independent Poisson processes of rate one, and hyperedge majority adoption simultaneously changes the opinions of all three members. The hyperedge set is fixed: there is **no rewiring**, no mutation, no external field and no single-vertex asynchronous update rule. The Markov chain runs for arbitrary times; a two-state recurrent class is not an absorbing *configuration*. The word consensus refers to global unanimous opinion, not merely the disappearance of mixed leaf pairs. Both colors and petal labels are distinguished. The theorem holds for every integer \(k\geq2\), with the same formulas incidentally valid for \(k=1\).

## Proof
**1. Permanence of an equal leaf pair.** If \(u_j=v_j=\mathrm A\), then the three-person majority in its petal is \(\mathrm A\), independently of the hub opinion, so its next update leaves that pair at \(\mathrm A\). The same is true for a \(\mathrm B\mathrm B\) pair. In particular, a monochromatic leaf pair cannot ever change color. Conversely, an initially mixed pair has one leaf of each color, so at its first hyperedge update the hub breaks the tie: the triple adopts the hub's opinion. The pair therefore becomes monochromatic and remains so. That first update occurs at an independent rate-one Poisson time for each initially mixed pair. Consequently the maximum of their \(m\) independent first times gives the displayed freezing-time CDF; integrating the survival probability yields the harmonic expectation. All pairs eventually freeze almost surely.

**2. Closed communicating classes.** Once all pairs are monochromatic, their opinions are frozen forever. If they all have one color, each event from any opposite-colored petal makes the hub join them; the chain reaches a singleton consensus almost surely. If some pairs are \(\mathrm A\mathrm A\) and others \(\mathrm B\mathrm B\), an update of a disagreeing petal changes only the hub. The hub jumps from \(\mathrm A\) to \(\mathrm B\) at rate \(b'\) and back at rate \(a'\). Both rates are positive; thus these two states communicate and form a closed irreducible class. Every other configuration contains a mixed pair; its first update strictly decreases the number of mixed pairs, which never increases. Hence no such state belongs to a recurrent communicating class. Every one of the \(2^k\) choices of final petal colors therefore yields exactly one recurrent class, with only the two uniform choices singleton. Standard two-state balance gives the stationary probabilities.

**3. Conditional consensus probability.** If both monochromatic colors are present initially, both remain forever, making consensus impossible. If no pair is monochromatic, the hub never changes before any mixed pair is updated, so every mixed pair locks to its initial opinion, giving consensus surely. Suppose initially only \(\mathrm A\mathrm A\) monochromatic pairs exist. If the hub is \(\mathrm A\), every mixed pair locks to \(\mathrm A\) and consensus follows. If the hub is \(\mathrm B\), the first effective event occurs among \(a\) opposite-color fixed petals, each at rate one, and \(m\) mixed petals, each also at rate one. An event in a fixed \(\mathrm A\mathrm A\) petal converts the hub to \(\mathrm A\), then every mixed pair locks \(\mathrm A\) and consensus follows. But if a mixed petal updates first, it becomes a permanent \(\mathrm B\mathrm B\) pair in the presence of a permanent \(\mathrm A\mathrm A\) pair; consensus becomes impossible. By the exponential race, the success probability is \(a/(a+m)\). Exchanging opinions proves the remaining case. Ringing hyperedges already unanimous can be ignored by Poisson thinning and does not alter this race.

**4. Independent initial opinions.** For one petal, the initial probabilities of \(\mathrm A\mathrm A\), \(\mathrm B\mathrm B\) and mixed are, respectively, \(q^2\), \((1-q)^2\), \(2q(1-q)\). Condition on a hub initially at \(\mathrm A\). Final \(\mathrm A\) consensus occurs exactly when no petal is initially \(\mathrm B\mathrm B\), with probability \((2q-q^2)^k\). Final \(\mathrm B\) consensus requires no initial \(\mathrm A\mathrm A\) petal, and among the remaining locked-\(\mathrm B\) and mixed petals the first effective event must come from a locked-\(\mathrm B\) petal. If there are \(b\) such petals, the probability is \(b/k\). Using the binomial identity \(\sum_b \binom{k}{b} b x^b y^{k-b} = kx(x+y)^{k-1}\), the latter event has probability \((1-q)^2(1-q^2)^{k-1}\). Thus
\[
\mathbb P(\mathrm{consensus}\mid H=\mathrm A)=(2q-q^2)^k+(1-q)^2(1-q^2)^{k-1}.
\]
By color reversal,
\[
\mathbb P(\mathrm{consensus}\mid H=\mathrm B)=(1-q^2)^k+q^2(2q-q^2)^{k-1}.
\]
Multiplying these by \(q\) and \(1-q\) and collecting terms proves the boxed formula. Setting \(q=1/2\) gives \((3/4)^{k-1}\). If \(0<q<1\), both exponential bases in the formula are strictly less than one, proving exponential decay.

## Verification
A standalone Python 3 script, `verify.py`, independently constructs the exact finite Markov transition graph for all labeled configurations for \(1\leq k\leq5\), identifies terminal strongly connected components, evaluates exact rational first-step consensus probabilities, and sums those probabilities against several rational initial Bernoulli distributions. It reports `PASS: 2835 exact certificates, all reachable states through k=5, recurrent classes and iid formula verified`. Those finite calculations are reproducibility checks, not the proof for unbounded \(k\). The all-size result is the preceding sample-path argument.

## Relationship to prior work
Golovin, Mölter and Kuehn introduce hyperedge-majority propagation and competing adaptive rewiring rules; their model includes the no-rewiring specialization used here, but their studied random hypergraphs, moment equations and simulations do not provide the fixed loose-hyperstar recurrent-class census or the exact Bernoulli consensus formula. Noonan and Lambiotte study triple-majority dynamics on complete, tripartite and modular hypergraphs through mean-field and Fokker–Planck descriptions, including metastable community polarization; those hypergraphs are different from the present sparse one-hub overlap, and the exact permanently recurrent two-state classes are not derived there. Papanikolaou and coauthors analyze adaptive group-voter interactions and magnetization, not this exact fixed-hyperstar Markov chain. Lanchier and Neufer analyze rate-one hyperedge majority on spatial lattice blocks, not the all-size loose-star recurrent structure. These comparisons concern mathematical coverage, not merely title similarity. No claim of exhaustive global novelty or independent external certification is made.

## Limitations
The exact formulas rely on the simultaneous group-majority rule and the leaves belonging to exactly one hyperedge. A different update rule, even if called majority voting, may remove the permanently locked leaf-pair mechanism. The result does not extend without additional work to hyperedges larger than three, nontrivial rewiring, cross-petal overlaps beyond the hub, mutations, unequal hyperedge rates, or other initial distributions. The harmonic time concerns *leaf freezing*, not necessarily the first time the chain reaches a recurrent class with a consensus hub; in polarized classes no single configuration is reached permanently. Priority relative to uncatalogued equivalent results remains uncertain.

## References
1. A. Golovin, J. Mölter and C. Kuehn, *Polyadic Opinion Formation: The Adaptive Voter Model on a Hypergraph*, arXiv:2308.03640 (first public August 7, 2023), https://arxiv.org/abs/2308.03640.
2. J. Noonan and R. Lambiotte, *Dynamics of Majority Rule on Hypergraphs*, arXiv:2101.03632 (2021), https://arxiv.org/abs/2101.03632.
3. N. Papanikolaou, G. Vaccario, E. Hormann, R. Lambiotte and F. Schweitzer, *Consensus from group interactions: An adaptive voter model on hypergraphs*, arXiv:2201.06421 (2022), https://arxiv.org/abs/2201.06421.
4. N. Lanchier and J. Neufer, *Stochastic dynamics on hypergraphs and the spatial majority rule model*, arXiv:1301.0151 (2013), https://arxiv.org/abs/1301.0151.
