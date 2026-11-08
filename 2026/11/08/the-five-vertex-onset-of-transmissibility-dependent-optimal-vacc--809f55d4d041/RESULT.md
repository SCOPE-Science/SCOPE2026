# The five-vertex onset of transmissibility-dependent optimal vaccination

## Finding

For every finite, simple, connected, undirected contact graph \(G\) on \(2\le n\le5\) vertices, vaccinate one vertex \(v\), permanently remove it and its incident edges, and choose the single epidemic seed uniformly from the \(n-1\) remaining vertices. In the independently transmissible-edge SIR model, each remaining edge independently transmits with probability \(p\in(0,1)\), and the final infected set is the open-edge component of the seed. Write \(M_G(v,p)\) for expected total infections including the seed.

**Classification.** For every connected graph on at most four vertices, and for nineteen of the twenty-one connected five-vertex isomorphism classes, the complete set of minimizers of \(M_G(v,p)\) is independent of \(p\in(0,1)\). Exactly two five-vertex isomorphism classes exhibit a change, and **both change only at \(p=1/4\)**. Representatives with vertices \(0,1,2,3,4\) are:

* \(G_A\), with edges \(\{01,02,03,12,13,24\}\). The full optimal sets are \(\{0,1\}\) for \(0<p<1/4\), \(\{0,1,2\}\) at \(p=1/4\), and \(\{2\}\) for \(1/4<p<1\).
* \(G_B\), with edges \(\{01,02,03,12,13,24,34\}\). The full optimal sets are \(\{0,1\}\) for \(0<p<1/4\), \(\{0,1,2,3\}\) at \(p=1/4\), and \(\{2,3\}\) for \(1/4<p<1\).

These two types account respectively for \(60\) and \(30\) labeled connected graphs on five vertices, out of \(728\). In both representatives the competing vertices all have degree three. Thus a degree-only rule cannot distinguish the exact optimum, and the best placement may reverse as edge transmissibility changes. At \(p=0\) all placements tie. At \(p=1\), only vertex \(2\) is optimal in \(G_A\), while every vertex ties in \(G_B\). The classification concerns the specified independent-bond epidemic, not continuous-time Markov SIR with a shared exponential recovery period.

## Assumptions and scope

The graph is connected, simple and undirected, with no loops or multiple edges and \(2\le n\le5\). The vaccine is perfectly protective; the chosen node is deleted before importation. Edge outcomes are independent Bernoulli random variables with identical parameter \(0\le p\le1\); infection reaches every vertex reachable from the initial seed by open edges. The objective is the expected *number* of infected unvaccinated individuals after a uniformly distributed single importation, not the epidemic probability exceeding a specified size, network giant-component size, time to peak or conditional severity. No assertion for graphs with six or more vertices is made.

For a percolated remaining graph \(H\) with connected components \(C\), introduce the unnormalized epidemic objective
\[
F_G(v,p)=(n-1)M_G(v,p)=\mathbb E\biggl[\sum_{C\text{ component of }H}|C|^2\biggr].
\]
The denominator \(n-1\) is constant across all vaccination choices, so minimizing \(F_G\) and \(M_G\) is equivalent.

## Proof

**Component identity.** Conditional on the open-edge subgraph, a uniformly selected seed lands in a component of size \(|C|\) with probability \(|C|/(n-1)\) and infects exactly \(|C|\) individuals. Therefore \((n-1)\mathbb E[\text{final outbreak size}\mid H]=\sum_C|C|^2\). If the post-deletion graph has \(m\) edges, independence gives the exact polynomial
\[
F_G(v,p)=\sum_{A\subseteq E(G-v)}p^{|A|}(1-p)^{m-|A|}\sum_{C\in\operatorname{comp}(V(G)\setminus\{v\},A)}|C|^2.
\]
In our domain, \(m\le\binom42=6\), so every objective polynomial has degree at most six and integer coefficients.

**Exact exhaustion and positivity certificate.** Enumerate every binary edge mask among the \(\binom n2\) possible edges for \(n=2,3,4,5\), retain only connected graphs, then for each possible deleted vertex enumerate every open-edge subgraph. Expanding the displayed finite formula using the binomial theorem produces integer coefficient lists for all \(F_G(v,p)\). There are exactly \(1,4,38,728\) connected labeled graphs of these respective orders; the enumeration and the identity \(\sum_C|C|^2=\sum_{x,y}\mathbf1\{x\leftrightarrow y\}\) are replayed by the attached standard-library checker.

For any two placements \(u,w\), let \(f(p)=F_G(w,p)-F_G(u,p)\). On the lower interval, put \(p=z/[4(1+z)]\); on the upper interval, put \(p=(1+4z)/[4(1+z)]\), with \(z>0\). The two exact transformations
\[
4^6(1+z)^6 f\bigl(z/[4(1+z)]\bigr),\qquad
4^6(1+z)^6 f\bigl((1+4z)/[4(1+z)]\bigr)
\]
are polynomials in \(z\) with integer coefficients. A coefficientwise nonnegative transformed polynomial certifies \(f\ge0\) throughout its corresponding interval; if at least one coefficient is strictly positive, it certifies \(f>0\) for every point strictly inside. For each graph, candidates are selected by exact rational evaluations at \(p=1/8\) and \(p=1/2\). For every candidate-to-competitor comparison, the checker establishes these two sign certificates, and also checks that candidates tied at the sample have identical objective polynomials. Consequently **the complete optimizer set is constant in each of the intervals** \((0,1/4)\) and \((1/4,1)\); the optimizer set at \(1/4\) is exactly their union. These are exact finite calculations, not floating-point sampling or extrapolation.

Canonical labeling by all vertex permutations shows that the lower and upper optimizer sets differ only in the two edge sets displayed in the Finding section, appearing \(60\) and \(30\) times among the \(728\) labeled connected five-vertex graphs. Thus no connected graph on fewer than five vertices has a strict optimizer switch. For the two exceptions the relevant objective polynomials are
\[
\begin{aligned}
F_{G_A}(0,p)=F_{G_A}(1,p)&=4+6p+4p^2+2p^3,\\
F_{G_A}(2,p)&=4+6p+6p^2-6p^3,\\
F_{G_B}(0,p)=F_{G_B}(1,p)&=4+8p+8p^2+8p^3-12p^4,\\
F_{G_B}(2,p)=F_{G_B}(3,p)&=4+8p+10p^2-2p^3-4p^4.
\end{aligned}
\]
Hence their cost differences factor exactly as
\[
F_{G_A}(2,p)-F_{G_A}(0,p)=2p^2(1-4p),
\quad
F_{G_B}(2,p)-F_{G_B}(0,p)=2p^2(1-p)(1-4p).
\]
The other placements have strictly greater objective for \(0<p<1\), certified by the same exhaustive integer procedure. The sign factors settle the claimed optimal sets and the unique interior boundary. Direct evaluation of the finite formula at \(p=0,1\) settles the endpoints.

## Verification

Run `python3 verify.py` with Python 3.9 or later. No external packages, internet access, files or random choices are needed. The script enumerates all \(1098\) labeled simple graphs on \(2\) through \(5\) vertices (including disconnected ones before filtering), checks the \(771\) connected instances, and verifies \(6932\) strict placement-comparison certificates by exact integer arithmetic. It independently checks each component-square total by an ordered-pair connectivity count, the two exceptional canonical edge sets, the labeled orbit counts, and the two explicit polynomial factor identities. The expected terminal output consists of five lines beginning `PASS:`.

The certificate's exhaustiveness is limited to the explicitly stated finite range, which suffices for this theorem. No claim about all finite graphs, arbitrary epidemic transmission correlation or empirical optimality is inferred from the census.

## Relationship to prior work

Newman (2002), originally public on arXiv on 2002-04-30, establishes the epidemic/bond-percolation correspondence and large-network generating-function framework. That correspondence is an assumed starting point here, not a new result. Masuda (2009) studies network immunization and community structure using spectral and fragmentation heuristics, rather than the present exact four-survivor objective. Holme (2017) performs exact small-graph vaccination calculations for *continuous-time* SIR with infection rate \(\beta\) and exponential recovery rate one, not the independent Bernoulli-bond law here; its common random infectious period produces correlated transmissions to multiple neighbors. For example, the probability of infecting two initially susceptible neighbors before an exponential recovery is \(2\beta^2/[(1+\beta)(1+2\beta)]\), not the independent-edge expression \(\beta^2/(1+\beta)^2\). Thus its exact small-graph expressions do not imply the present \(p=1/4\) classification by parameter substitution. The reviewed sources do not identify the two exceptional independent-bond graph classes and their shared exact crossover. This is a best-knowledge distinction, not a claim of complete historical priority.

## Limitations

The theorem is about one perfect vaccination, one uniform importation, homogeneous independent edges and only up to five vertices. Its endpoint \(p=1\) ties differ from the strict interior classification. It does not rank vaccination choices in more realistic SIR models with heterogeneous or dependent contacts, and it is not a recommendation for vaccination decisions in real networks. Earlier graph-percolation literature or finite classification tables not located in the inspected searches could have equivalent observations; independent literature review remains to be performed.

## References

1. M. E. J. Newman, “The spread of epidemic disease on networks,” arXiv:cond-mat/0205009v1 (2002-04-30), https://arxiv.org/abs/cond-mat/0205009; *Physical Review E* **66**, 016128 (2002), https://doi.org/10.1103/PhysRevE.66.016128.
2. N. Masuda, “Immunization of networks with community structure,” arXiv:0909.1945 (initially posted 2009-09-10), https://arxiv.org/abs/0909.1945; *New Journal of Physics* **11**, 123018 (2009), https://doi.org/10.1088/1367-2630/11/12/123018.
3. P. Holme, “Three faces of node importance in network epidemiology: Exact results for small graphs,” arXiv:1708.06456 (initially posted 2017-08-22), https://arxiv.org/abs/1708.06456; *Physical Review E* **96**, 062305 (2017), https://doi.org/10.1103/PhysRevE.96.062305.
4. F. Morone and H. A. Makse, “Influence maximization in complex networks through optimal percolation,” *Nature* **524**, 65–68 (2015), https://doi.org/10.1038/nature14604. This addresses a different large-network fragmentation objective.
