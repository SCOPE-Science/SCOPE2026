# Exact freezing and rare three-seed nucleation on the Fano incidence graph

## Finding

Let \(H\) be the fourteen-vertex Heawood graph, the point–line incidence graph of the Fano plane. Give each vertex a ferromagnetic Ising spin \(\sigma_v\in\{-1,+1\}\). At independent rate-one exponential clocks, a vertex changes to the strict majority of its three neighbors; if it already agrees, nothing happens. Starting with independent positive spins of probability \(p\in[0,1]\), let \(Q_H(p)\) be the probability that the process eventually freezes in a nonconsensus configuration.

**Exact freezing law.** With \(q=p(1-p)\),
\[
\boxed{Q_H(p)=q^3\left(\frac{56}{15}+\frac{106896721}{2083725}q+\frac{216605875348939}{8509411968750}q^2+\frac{4672732892864737}{4778885761650000}q^3\right).}
\]
There are exactly \(58\) absorbing configurations: two unanimous ones and \(56\) mixed ones. Every mixed absorbing configuration has six disagreeing edges and consists of one spin on an induced six-cycle, with the opposite spin on its eight-vertex complement. The \(56\) configurations are the \(28\) six-cycles and their spin reversals. This fixed-state classification is known from the earlier synchronous Heawood majority study and is not claimed as new here.

**Sharp three-seed nucleation.** Condition on exactly three initially positive spins. The probability of eventual nonconsensus freezing is positive for exactly \(56\) of the \(\binom{14}{3}=364\) triples: the \(28\) noncollinear triples of Fano points and the corresponding \(28\) triples of Fano lines. Each succeeds with conditional probability exactly \(1/15\). Every other three-seed initial configuration reaches all negative spins. Consequently the mixed-freezing probability conditional on exactly three positives is \(2/195\), and the coefficient of \(p^3\) in \(Q_H(p)\) is \(56/15\).

At unbiased initial density,
\[
\boxed{Q_H(1/2)=\frac{27778302334027926533}{97871580398592000000}\approx0.28382398875034.}
\]
The freezing probability is strictly increasing on \([0,1/2]\) and strictly decreasing on \([1/2,1]\), hence attains its unique maximum at \(p=1/2\). In comparison, the **already known synchronous** majority dynamics has isolated mixed fixed states, so its probability of reaching a mixed fixed point from unbiased independent spins is only \(56/2^{14}=7/2048\). Thus sequential updates make those same fixed states approximately \(83.04\) times as accessible; this comparison does not identify synchronous oscillatory states as frozen.

## Assumptions and scope

Write the Fano points as integers \(0,1,\ldots,6\), and its seven lines as
\[
L_j=\{j,j+1,j+3\}\pmod7,\quad j=0,\ldots,6.
\]
The vertices of \(H\) are the seven points and seven line-symbols, with point \(i\) adjacent to line \(L_j\) exactly when \(i\in L_j\). Every vertex has degree three. All rate-one clocks are independent and exponential; an update changes a spin only if it disagrees with at least two neighboring spins. Failed clock rings have no effect. All probabilities concern eventual absorption, not a fixed finite time or an equilibrium Gibbs distribution.

The initial spins are independent Bernoulli \(p\) on all fourteen labelled vertices. \(Q_H(p)\) sums over all twelve-thousand-plus transient assignments as well as the absorbing ones, without spatial symmetry quotient. Positive-spin and negative-spin exchange leaves the model invariant.

## Proof

**1. Termination and absorbing geometry.** Let \(d(s)\) be the number of graph edges with opposite spins in a configuration \(s\). A legal flip has two or three incident discordant edges. It changes \(d\) by \(3-2r=-1\) or \(-3\), where \(r\in\{2,3\}\) is that number. Hence the process cannot return to a previous configuration and reaches an absorbing configuration almost surely after finitely many effective flips.

Every vertex of a stable color class has at least two neighbors of its own color. Each nonempty class must therefore contain a cycle, so girth six requires at least six vertices. If both colors occur, each class has at least six vertices. A stable class of size seven is impossible: it would contain a six-cycle, and its seventh vertex would need two neighbors on that cycle, producing a cycle of length at most five. Thus the two class sizes must be six and eight. The six-class is necessarily one induced six-cycle. Every vertex outside a six-cycle has at most one neighbor on it, again by girth six, so the complementary eight-class is also stable. There are \(28\) hexagons, corresponding to noncollinear Fano point triples and their three pair-joining lines. This proves the \(56\) mixed stable states plus the two unanimous states, independently of the later stochastic calculation.

**2. Three-seed nucleation.** For three initially positive spins, consider the monotone two-neighbor closure obtained by permitting positive additions without negative deletions. It contains every vertex that could ever become positive in the actual majority process. The Fano incidence axioms imply that the closure has at least six vertices precisely when the initial triple lies entirely on one shore and is noncollinear. In that case it is exactly the six-cycle of the three selected points (or lines) and the three pair-joining lines (or intersection points). A collinear same-shore triple activates at most one line and has closure four. A mixed-shore triple has closure of size at most five: with two selected points and one selected line, the only possible new line is the line joining those points, and any new point must be their line intersection; the dual case is identical. Hence other triples cannot reach any mixed absorbing state, which needs at least six positive spins, nor unanimous positive consensus.

For a noncollinear same-shore triple, the three original positive sites are initially flippable to negative, and the three complementary bridge sites are flippable to positive. Each of the six effective flips has the same instantaneous rate. Successful capture of the six-cycle requires a bridge activation first (probability \(3/6\)), a second bridge activation before an original site is lost (probability \(2/5\)), and activation of the remaining bridge before either of the two still vulnerable original sites is lost (probability \(1/3\)). Once all three bridge sites are positive, all six are stable and the complement is stable. An original positive site lost before completion precludes recovery to that hexagon. Therefore the success probability is \((3/6)(2/5)(1/3)=1/15\). There are \(2(\binom73-7)=56\) eligible three-seed sets.

**3. Exact finite-state absorption recurrence.** Encode a configuration by a \(14\)-bit integer \(s\), with bits identifying positive vertices. Let \(U(s)\) be the set of vertices currently opposed to the majority of their three neighbors. Let \(h(s)\) be the probability of eventual absorption in a mixed fixed state. The exact backward equations are
\[
h(s)=\begin{cases}
0,&s\text{ is unanimous},\\
1,&s\text{ is mixed and stable},\\
\displaystyle\frac1{|U(s)|}\sum_{v\in U(s)}h(s\triangle\{v\}),&U(s)\ne\varnothing.
\end{cases}
\]
This recurrence is well-founded because each successor has strictly fewer discordant edges. Sorting all \(2^{14}=16384\) states by \(d(s)\) uniquely determines every rational \(h(s)\); no approximation or truncation is involved.

For \(0\le k\le14\), set \(B_k=\sum_{|s|=k}h(s)\). Exact application of the recurrence gives, in order \(k=0,1,\ldots,14\),
\[
\begin{aligned}
(B_0,\ldots,B_{14})=\big(&0,0,0,\tfrac{56}{15},\tfrac{169130641}{2083725},
\tfrac{532194282778777}{1215630281250},
\tfrac{3691264645924565219}{3413489829750000},\\
&\tfrac{17228285644177485821}{11947214404125000},
\tfrac{3691264645924565219}{3413489829750000},
\tfrac{532194282778777}{1215630281250},
\tfrac{169130641}{2083725},\tfrac{56}{15},0,0,0\big).
\end{aligned}
\]
The exact Bernoulli initial-state law is \(Q_H(p)=\sum_{k=0}^{14}B_kp^k(1-p)^{14-k}\). Elementary rational polynomial expansion yields the boxed expression in \(q=p(1-p)\). Its four coefficients are strictly positive, hence the maximum claim follows from the monotonicity of \(q\) on either side of \(1/2\).

## Verification

The standalone Python 3 programs `check_cyclic.py` and `check_xor.py` use only the standard library and implement independent graph presentations and rational solution methods. Run separately from the directory containing this document:

```bash
python3 check_cyclic.py
python3 check_xor.py
```

`check_cyclic.py` uses the cyclic Fano lines and an iterative topological traversal in increasing discordant-edge count. `check_xor.py` constructs the Fano lines as triples of nonzero binary vectors and uses memoized rational Bellman recursion. Both enumerate all \(16{,}384\) states, independently recover the full fifteen-entry coefficient list, and establish the symmetric \(q\)-polynomial identity by evaluation at fifteen distinct rational values (sufficient for polynomials of degree at most fourteen). The first checker additionally verifies the fixed-state histogram, cut count, monotone-comparison symmetry and exact three-seed geometric classification. The second independently checks the \(56\) exceptional initial triples and their common absorption probability. Both ran successfully on the delivered source bytes.

## Relationship to prior work

Castellano, Loreto, Barrat, Cecconi and Parisi (arXiv:cond-mat/0501599, first public 2005-01-25) examine voter and zero-temperature Glauber ordering on complete, random and scale-free networks and report nonconsensus metastability. Baek, Ha and Jeong (arXiv:1112.5927, first public 2011-12-27) study numerical saturation distributions and interface-density peaks on random networks. Their equations and finite-size observations do not furnish this labelled Heawood exact absorption polynomial or its three-seed Fano criterion.

The previously published *A two-step majority projection and exact attraction basins on the Heawood graph* studies **synchronous** updates. It already proves the 58 fixed-state classification and isolation of the 56 mixed fixed points, credited in this article. The new stochastic claim instead determines the **asynchronous rate-one** absorption probabilities. Changing the update rule is essential: the synchronous basin sizes are not the harmonic measures of the asynchronous Markov chain. A related earlier computation of asynchronous freezing on the icosahedral graph uses a different graph, six-spin-cap geometry and probability polynomial, and does not imply the present Fano-incidence law.

## Limitations

The absorption formula is exact only for the labelled fourteen-vertex Fano incidence graph, zero field, equal positive ferromagnetic bonds, independent rate-one clocks, and independent Bernoulli initial spins. It is not a limit theorem for larger cubic cages, not a formula for synchronous dynamics, and not a finite-temperature result. The exact arithmetic proof is a finite exhaustive calculation with two included reproducible implementations, not an externally certified formal proof. The literature comparison establishes noncoverage by the inspected sources, not absolute historical priority; inaccessible or unindexed equivalent work remains possible. Independent scientific audit has not been performed.

## References

1. C. Castellano, V. Loreto, A. Barrat, F. Cecconi and D. Parisi, *Comparison of voter and Glauber ordering dynamics on networks*, arXiv:cond-mat/0501599, first posted 2005-01-25, https://arxiv.org/abs/cond-mat/0501599 ; published Phys. Rev. E 71, 066107 (2005).
2. Y. Baek, M. Ha and H. Jeong, *Absorbing states of zero-temperature Glauber dynamics in random networks*, arXiv:1112.5927, first posted 2011-12-27, https://arxiv.org/abs/1112.5927 ; published Phys. Rev. E 85, 031123 (2012).
3. *A two-step majority projection and exact attraction basins on the Heawood graph*, published full text, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-two-step-majority-projection-and-exact-attraction-basins-on-th--8cd2964a9d93 . This is prior fixed-state and synchronous-dynamics work, not a source of the asynchronous absorption probabilities.
4. *Asynchronous spin updates can nucleate otherwise inaccessible frozen states* (icosahedral Ising example), earlier exact finite-network study; this provides methodological context but does not contain a Heawood calculation.
