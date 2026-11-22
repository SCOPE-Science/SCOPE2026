# A Poisson cutoff in exact OR consensus clocks on de Bruijn networks

## Finding
Let \(q\ge2\) and \(d\ge1\) be integers. On the directed de Bruijn graph with vertex set \(\Sigma^d\), where \(|\Sigma|=q\), consider the synchronous binary disjunctive network \(F\) that replaces each vertex bit by the Boolean OR of its in-neighbours' bits. Define \(\tau(x)\) as the least nonnegative update at which the all-one state is reached, or \(\infty\) if this never occurs. For \(0\le t\le d\), put
\[
A_{q,d}(t)=\bigl(2^{q^t}-1\bigr)^{q^{d-t}}.
\]
**The exact first-hitting-time law** is
\[
\#\{x:\tau(x)=0\}=1,\qquad
\#\{x:\tau(x)=t\}=A_{q,d}(t)-A_{q,d}(t-1)\quad(1\le t\le d),
\]
with exactly one state satisfying \(\tau=\infty\), and none hitting at a later finite time. Consequently every nonzero state reaches all ones by the sharp time \(d\); zero and one are the only periodic configurations, both fixed. Precisely
\[
\#\{x:\tau(x)=d\}=2\bigl(2^{q^{d-1}}-1\bigr)
\]
when \(q=2\) (for general \(q\), the value is \(2^{q^d}-1-(2^{q^{d-1}}-1)^q\)).

For independent initial bits with probability \(p\in(0,1)\) of being one, the entire distribution has the closed form
\[
\Pr_p(\tau\le t)=\bigl(1-(1-p)^{q^t}\bigr)^{q^{d-t}},\qquad 0\le t\le d.
\]
For fair initial bits, the typical clock is **logarithmic in word length**: as \(d\to\infty\) with fixed \(q\), \(\tau/\log_q d\to1\) in probability (assigning \(\tau=\infty\) on the vanishing-probability zero configuration, or conditioning on nonzero initial states).

There is an exact nondegenerate cutoff window. For any fixed integer \(c\), set \(d_h=2^h+h+c\) for all sufficiently large integers \(h\). In the binary de Bruijn network at dimension \(d_h\), the number of length-\((d_h-h)\) suffix classes containing **no initially active vertex** is exactly binomial with parameters \(2^{2^h+c}\) and \(2^{-2^h}\), hence tends in distribution to \(\operatorname{Poisson}(2^c)\). In particular
\[
\lim_{h\to\infty}\Pr(\tau=h)=e^{-2^c},\quad
\lim_{h\to\infty}\Pr(\tau=h+1)=1-e^{-2^c},\quad
\lim_{h\to\infty}\Pr(\tau\notin\{h,h+1\})=0.
\]
This exhibits an explicit two-point consensus-time cutoff on a sparse subsequence of dimensions, despite the sharp worst-case clock growing linearly in dimension.

## Assumptions and scope
Write \(\Sigma=\{0,\ldots,q-1\}\). The directed graph has an arc \((a_1,\ldots,a_d)\to(a_2,\ldots,a_d,b)\) for each \(b\in\Sigma\). Self-loops are permitted when the words are constant, as in the usual de Bruijn digraph. Each vertex has exactly \(q\) in-neighbours; all updates are simultaneous, and the bit at \(v\) after one update is \(\bigvee_{u\to v}x_u\). Vertex bits are binary even when the graph alphabet has size greater than two. All \(2^{q^d}\) initial configurations are labelled by their word vertices, and \(t=0\) is allowed as a hitting time. A nonzero state means at least one initially active vertex. The exact counting identities hold for every integer \(q\ge2,d\ge1\), and the probability formula holds for every \(0<p<1\). Probabilistic asymptotics refer to fair independent bits unless a general bias is explicitly displayed.

## Proof
**Exact reachability.** By induction on \(t\), the bit at a word \(v=(v_1,\ldots,v_d)\) after \(t\) updates is the OR of the initially active bits at exactly the starting words \(u=(u_1,\ldots,u_d)\) having a directed walk of length \(t\) ending at \(v\). For \(0\le t\le d\), such a walk exists precisely when the final \(d-t\) symbols of \(u\) match the initial \(d-t\) symbols of \(v\); its first \(t\) symbols and its appended \(t\) symbols may be arbitrary. Thus, for each suffix \(r\in\Sigma^{d-t}\), the bit at all target words beginning with \(r\) is one exactly when the initial state contains at least one active word ending in \(r\). For \(t=d\), the empty suffix condition is vacuous and each target receives a walk from each source.

**Exact census.** The \(q^{d-t}\) suffix classes of initial vertices are disjoint, and each class has size \(q^t\). Reaching all ones at time \(t\) is therefore equivalent to making a nonempty selection of active bits within every class. Each class has \(2^{q^t}-1\) nonempty binary assignments, giving \(A_{q,d}(t)\). Because the all-one state is fixed, the set of states that hit it by time \(t\) equals the set that is at it at exactly time \(t\). Subtract consecutive cumulative counts to obtain the claimed first-entry law. At \(t=0\), all ones is the unique hitting state. At \(t=d\), every nonzero state has reached it; the all-zero state remains fixed, so it alone has infinite hitting time. The digraph is strongly connected, and the only other periodic state is all ones: indeed, every nonzero state hits all ones, while all zero stays zero. A singleton active initial state does not occupy every class at time \(d-1\) (there are \(q\ge2\) classes), so the time \(d\) is attained. For \(q=2\), writing \(m=2^{d-1}\), the count in the final shell is \((2^{2m}-1)-(2^m-1)^2=2(2^m-1)\), as stated.

**Bias and uncovered classes.** Under independent Bernoulli-\(p\) initial bits, a given suffix class of size \(q^t\) is empty with probability \((1-p)^{q^t}\), independently of the other suffix classes. Thus its number \(Z_t\) of empty classes has the exact binomial law
\[
Z_t\sim\operatorname{Binomial}\bigl(q^{d-t},(1-p)^{q^t}\bigr),
\]
and \(\tau\le t\) exactly when \(Z_t=0\). This proves the probability formula.

**Typical logarithmic clock.** In the fair case put \(\lambda_t=q^{d-t}2^{-q^t}=\mathbb E Z_t\). Fix \(\varepsilon\in(0,1)\). For \(t_- =\lfloor(1-\varepsilon)\log_q d\rfloor\), the estimate \(\log\lambda_{t_-}=(d-t_-)\log q-(\log2)q^{t_-}\) tends to \(+\infty\), since \(q^{t_-}\le d^{1-\varepsilon}\). Therefore \(\Pr(\tau\le t_-)=(1-2^{-q^{t_-}})^{q^{d-t_-}}\le e^{-\lambda_{t_-}}\to0\). For \(t_+=\lceil(1+\varepsilon)\log_q d\rceil\), \(\lambda_{t_+}\to0\), since \(q^{t_+}\ge d^{1+\varepsilon}\); the union bound gives \(\Pr(\tau>t_+,\tau<\infty)\le\lambda_{t_+}\). The all-zero state has probability \(2^{-q^d}\to0\). Hence the asserted convergence in probability, with the convention for \(\infty\) noted above.

**Poisson window and two-point cutoff.** Set \(q=2\), \(d_h=2^h+h+c\), \(t=h\). The number of suffix classes is \(2^{d_h-h}=2^{2^h+c}\) and the independent probability that a class is empty is \(2^{-2^h}\). Their product equals \(2^c\) exactly, and the empty-class probability tends to zero. The binomial-to-Poisson limit yields \(Z_h\Rightarrow\operatorname{Poisson}(2^c)\), so \(\Pr(\tau\le h)\to e^{-2^c}\). At \(h-1\) the expected number of missing classes is \(2^{2^{h-1}+c+1}\to\infty\), making \(\Pr(\tau\le h-1)\le e^{-2^{2^{h-1}+c+1}}\to0\). At \(h+1\) the expected missing count is \(2^{c-1-2^h}\to0\), so \(\Pr(\tau\le h+1)\to1\). Subtracting these cumulative probabilities gives the two masses. All statements are for the original deterministic network under a random initial condition, not for a randomly changing network.

## Verification
The standalone Python programs `verify_exhaustive.py` and `verify_reachability.py` are included with their actual outputs. The first directly updates every binary configuration on de Bruijn digraphs \((q,d)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2)\) (\(65{,}536\) states for the largest binary example), compares the full first-hitting census to the formula, and independently cross-checks the suffix-class criterion for \(2{,}000\) pseudorandom configurations in larger graphs. The second checks every source-to-target exact-walk reachability relation against the claimed word-overlap rule at the same small dimensions, enumerates disjoint-block counts, and uses exact fractions to verify the critical-window binomial means for several dimensions. These are finite diagnostic tests; the infinite-family and limiting assertions rest on the proof above, not on simulation or a numerical extrapolation.

Representative binary counts for \(d=2,3,4\) at successive finite hitting times are respectively \((1,8,6)\), \((1,80,144,30)\), and \((1,6560,44064,14400,510)\); each additionally has one non-hitting all-zero configuration.

## Relationship to prior work
Jarrah, Laubenbacher and Veliz-Cuba (first posted 2008-05-02) establish the general representation of conjunctive/disjunctive Boolean dynamics by directed graph walks, relate convergence to primitive matrix exponents and determine recurrent orbit types for strongly connected networks. Gadouleau (arXiv:2104.04403, Sections 2 and 3) reviews disjunctive network images and periodic points, including the result that a primitive strongly connected network has only the two fixed configurations. These general results imply the qualitative attractor statement here, **which is not claimed as novel**, but do not present the de Bruijn suffix-class first-hitting census or its dimension-indexed Poisson cutoff.

The classical de Bruijn digraph is a standard communication network. Bermond and Fraigniaud (1994) study deterministic broadcasting/gossip protocols on these graphs, not the distribution across independent random initial binary vertex states under automatic simultaneous OR updates. The accessible source for that paper was its abstract and bibliographic information rather than its full manuscript; potential unseen overlap is retained as a priority risk. The related published result *A logarithmic typical convergence clock in the quadratic-exponent Wielandt OR network* (2026) gives a longest-zero-run comparison on a different primitive digraph, but neither its statements nor its proof cover the suffix-block exact count or the Poisson window here. A separate de Bruijn cellular-automata study of randomly colored **edges** and absent constant outputs concerns a different random object and is not an implicit first-hitting result for deterministically updated vertex bits.

The contribution here is specifically the all-size labelled first-entry law, the exact binomial obstruction statistic at every update, and the nondegenerate two-point cutoff in a sharply defined family of dimensions. General propagation identities and the classical binomial-to-Poisson limit are used as known tools, not claimed as original inventions.

## Limitations
Only synchronous in-neighbour OR dynamics on full directed de Bruijn graphs is treated. The biases are independent across vertex bits, not correlated inputs, random graph edges or stochastic updates. No result is asserted for arbitrary primitive digraphs, undirected de Bruijn graphs, faults, asynchronous updates or vertex-dependent thresholds. The exact count is an all-size proof; the two programs validate only stated finite cases. Historical uniqueness is not guaranteed, especially for unindexed communications-network work and the inaccessible full text of a directly related broadcasting article. The binary critical window depends on the lattice of graph dimensions and is not claimed to converge to a single nondegenerate law for every dimension.

## References
1. A. S. Jarrah, R. Laubenbacher and A. Veliz-Cuba, *The Dynamics of Conjunctive and Disjunctive Boolean Networks*, arXiv:0805.0275v1, publicly posted 2008-05-02, https://arxiv.org/pdf/0805.0275.
2. M. Gadouleau, *Dynamical properties of disjunctive Boolean networks*, arXiv:2104.04403, first version 2021, https://arxiv.org/pdf/2104.04403.
3. N. G. de Bruijn, *A combinatorial problem*, Proceedings of the Section of Sciences of the Koninklijke Nederlandse Akademie van Wetenschappen 49 (1946), 758–764, https://research.tue.nl/en/publications/a-combinatorial-problem/ (year verified; no day asserted).
4. J.-C. Bermond and P. Fraigniaud, *Broadcasting and Gossiping in de Bruijn Networks*, SIAM J. Comput. 23 (1994), 212–225, https://doi.org/10.1137/S0097539791197852 (full text not inspected).
5. *A logarithmic typical convergence clock in the quadratic-exponent Wielandt OR network*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-logarithmic-typical-convergence-clock-in-the-quadratic-exponen--4cb49f213f10.
6. *Two-sided fluctuation bounds for acyclic color classes in critical random digraphs*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-sided-fluctuation-bounds-for-acyclic-color-classes-in-critic--6df120673c37.
