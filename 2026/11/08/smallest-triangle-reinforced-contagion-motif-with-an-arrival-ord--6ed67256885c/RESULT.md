# Smallest triangle-reinforced contagion motif with an arrival-order reversal

## Finding

For the continuous-time susceptible–infected (SI) process on a finite connected *simple, unweighted* graph, each susceptible vertex is infected at rate \(\beta\) per infected neighbor plus rate \(\gamma\) for each incident graph triangle whose other two vertices are infected. Initially exactly one vertex is infected; infection is permanent. Let \(q=\gamma/\beta\), with \(\beta>0\) and \(\gamma\geq0\). For two other distinct vertices \(u,v\), write \(P_{u\prec v}(q)\) for the probability that \(u\) is infected before \(v\).

There is **no sign reversal** of \(P_{u\prec v}(q)-1/2\) as \(q\) varies over \([0,\infty)\) on *any* connected graph with at most four vertices, or on *any* connected five-vertex graph with at most five edges, for any choice of seed and target pair. These bounds are sharp together.

On the five-vertex six-edge graph

\[
V=\{0,1,2,3,4\},\quad E=\{01,02,03,12,13,24\},
\]

with the two filled triangles \(012\) and \(013\), seed vertex \(2\), and targets \(u=3\), \(v=4\), one has exactly

\[
P_{3\prec4}(q)=\frac{2(q^2+5q+7)}{3(q+3)(q+4)}.
\]

It increases strictly from \(7/18\) at \(q=0\) to \(2/3\) as \(q\to\infty\) and crosses \(1/2\) once, at the **sharp reinforcement ratio**

\[
q_*=\frac{1+\sqrt{33}}{2}.
\]

Thus the direct leaf of the seed is more likely to be reached first under weak triangular reinforcement, but the nonadjacent vertex in the second triangle is more likely to be reached first for \(q>q_*\).

## Assumptions and scope

Graphs are finite, simple, undirected, unweighted, and connected. Every complete graph triangle supports exactly one three-person interaction, and there are no independent hyperedges or higher-order interaction channels. Transmission clocks are independent exponential events in continuous time; the total infection rate of a susceptible vertex equals the sum of its active pairwise and triangular event rates. The single initially infected seed never recovers. Because every edge has positive infection rate and the graph is connected, all vertices are eventually infected with probability one, with no simultaneous infections almost surely.

The result concerns the probability order of two labeled first infection times from one specified seed, **not** which infecting edge is credited for an event, nor aggregate infection-pattern matrices, SIS persistence, a process with recovery, directed or weighted graphs, or independent triads not supported by triangles.

## Proof

**The six-edge witness.** Scaling time sets \(\beta=1\). Starting from infected vertex \(2\), the initially susceptible vertices \(0,1,4\) have rate \(1\) and vertex \(3\) rate \(0\). If \(4\) is infected first, the event \(3\prec4\) fails. With probability \(2/3\), one of the symmetric core vertices \(0,1\) is infected first. Conditional on, say, vertex \(0\) being infected, the infection rates of \(1,3,4\) are respectively \(2+q,1,1\). Thus \(3\) is next with probability \(1/(q+4)\), and \(1\) is next with probability \((q+2)/(q+4)\). In the latter case, the two remaining targets \(3,4\) have respective rates \(2+q,1\), so the conditional probability of \(3\) winning is \((q+2)/(q+3)\). Consequently,

\[
P_{3\prec4}(q)=\frac23\left(\frac1{q+4}+\frac{q+2}{q+4}\frac{q+2}{q+3}\right)=\frac{2(q^2+5q+7)}{3(q+3)(q+4)}.
\]

The exact sign and monotonicity identities are

\[
P_{3\prec4}(q)-\tfrac12=\frac{q^2-q-8}{6(q+3)(q+4)},\qquad
P'_{3\prec4}(q)=\frac{2(2q^2+10q+11)}{3(q+3)^2(q+4)^2}>0.
\]

The quadratic has exactly one nonnegative root \((1+\sqrt{33})/2\), proving the strict reversal.

**Sharp minimality.** A graph without triangles has no \(q\)-dependent transition rates and hence no reinforcement-dependent reversal. It therefore suffices to enumerate connected triangle-containing graphs. Up to isomorphism, there is exactly one such graph with three vertices, exactly three with four vertices (triangle with pendant edge, diamond, complete graph), and exactly three with five vertices and at most five edges (a triangle together with two attached tree edges: a two-edge chain, two leaves at the same triangle vertex, or leaves at distinct triangle vertices). No graph with fewer vertices can have a different shape relevant here.

For *each* isomorphism class, every seed and every unordered pair of nonseed targets is checked by the following exact recurrence. If \(S\) is the currently infected set and neither target is infected, let

\[
\lambda_x(S)=\beta\,|N(x)\cap S|+\gamma\,|\{T:\ T\text{ is a triangle},\ x\in T,\ T\setminus\{x\}\subseteq S\}|.
\]

Define \(h(S)=1\) when the first target is already infected and \(h(S)=0\) when the second is already infected. Otherwise use the exact exponential race recurrence

\[
h(S)=\frac{\sum_{x\notin S}\lambda_x(S)\,h(S\cup\{x\})}{\sum_{x\notin S}\lambda_x(S)}.
\]

The denominator is strictly positive because the graph is connected and \(\beta>0\). Every recursion strictly increases the infected set, so induction on the number of susceptible vertices proves the recurrence and the computed rational functions. Exhaustive labeled-edge-mask enumeration followed by canonical relabeling produces exactly \(1+3+3=7\) relevant graph classes. Across their \(3+36+90=129\) choices of seed and unordered target pair, the reduced numerator of \(2h(\{s\})-1\), as a polynomial in \(q\), either vanishes identically or has only nonnegative coefficients or only nonpositive coefficients. The denominator has no pole for nonnegative \(q\), being a simplification of a finite composition of positive exponential-race denominators. Therefore the sign cannot reverse on \(q\ge0\). The stand-alone \(\texttt{verify.py}\) generates all graph classes from *every* labeled graph and checks all 129 rational-function identities and numerator signs using exact symbolic arithmetic; the graph-class list is not assumed as an input.

## Verification

From the package directory run \(\texttt{python verify.py}\) with Python 3 and SymPy 1.14. The verifier reconstructs the witness's formula by the full infected-subset recursion, verifies its derivative, endpoints and unique algebraic crossing, then checks nine rational parameter values independently without reusing the symbolic expression. It also exhausts every connected graph on up to five vertices within the stated smaller edge bounds, canonically merges isomorphic graphs, and checks all 129 rational-function signs. The tests use integer/rational polynomial arithmetic; no random simulation, numerical root fitting, truncation, or partial graph sample is used to support the finite minimality statement. The short direct proof of the witness is independent of the verifier.

## Relationship to prior work

The pairwise-plus-triangle contagion mechanism follows the 2023 work of Cencetti, Contreras, Mancastroppa and Barrat on distinguishing simple from complex contagion via infection order, and the 2023/2024 work of Contreras, Cencetti and Barrat on transmission-pattern sensitivity. Their primary studies employ larger empirical networks and simulations and do not provide the above minimal-motif classification or exact \(q_*\) for the present continuous-time SI specialization. Earlier simplicial contagion work establishes higher-order phase effects at a different scale, rather than this finite first-arrival ordering boundary. The first-arrival probability here is also distinct from those studies' edge-attribution matrices and correlation summaries.

## Limitations

The five-vertex threshold is not asserted universal for larger graphs, weighted contacts, recovery, synchronous time steps, higher-order hyperedges not supported by graph triangles, or variable initial seed sets. The exhaustive cutoff concerns graph order at most four and, *within order five*, edge count at most five. It does not classify larger graphs. Searches and full-text comparisons have not established independent external priority certification; an equivalent unpublished or poorly indexed result cannot be ruled out.

## References

1. G. Cencetti, D. A. Contreras, M. Mancastroppa, A. Barrat, *Distinguishing Simple and Complex Contagion Processes on Networks*, arXiv:2301.09407v1 (23 January 2023), Physical Review Letters 130, 247401 (2023). https://arxiv.org/abs/2301.09407 ; https://doi.org/10.1103/PhysRevLett.130.247401
2. D. A. Contreras, G. Cencetti, A. Barrat, *Infection patterns in simple and complex contagion processes on networks*, arXiv:2309.10486v1 (19 September 2023), PLOS Computational Biology 20(6), e1012206 (2024). https://arxiv.org/abs/2309.10486 ; https://doi.org/10.1371/journal.pcbi.1012206
3. I. Iacopini, G. Petri, A. Barrat, V. Latora, *Simplicial models of social contagion*, Nature Communications 10, 2485 (2019). https://doi.org/10.1038/s41467-019-10431-6
