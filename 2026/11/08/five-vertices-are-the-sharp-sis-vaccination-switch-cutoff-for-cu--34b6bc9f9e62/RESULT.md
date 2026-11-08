# Five vertices are the sharp SIS vaccination-switch cutoff for cumulative infection burden

## Finding

In the continuous-time susceptible-infected-susceptible (SIS) epidemic model described below, every graph with two, three, or four vertices has a common optimal single-vertex vaccination target for **all** transmission rates: any vertex of maximum degree. A connected graph of order five already has no transmission-rate-independent optimum. Its exact optimizer changes once, at \(\lambda_*=1.0282979668263175\ldots\).

The explicit witness has labelled vertex set \(\{0,1,2,3,4\}\) and edges \(\{01,02,04,12,13,23\}\). When \(0<\lambda<\lambda_*\), the optimal vaccinated vertices are exactly \(\{1,2\}\). At \(\lambda=\lambda_*\), the optimal vertices are exactly \(\{0,1,2\}\). When \(\lambda>\lambda_*\), the unique optimal vertex is \(0\).

## Assumptions and scope

The network is a finite, undirected, unweighted, loopless simple graph \(G=(V,E)\) of order \(n\ge2\). Exactly one vertex \(v\) is perfectly vaccinated and removed before disease introduction; it cannot be infected or transmit. An initial infection is placed uniformly at random at one of the \(n-1\) remaining vertices. While the set of currently infected vertices is \(I_t\), each infected vertex independently recovers at rate one, becoming susceptible again. Each susceptible vertex becomes infected at rate \(\lambda\) times the number of its infected neighbors. Here \(\lambda>0\) is the common per-edge transmission-to-recovery rate ratio. There is no external importation. The all-susceptible state is absorbing, with a finite almost-sure extinction time \(\tau\).

The intervention objective is **expected cumulative infected person-time**, not extinction time or the number of distinct people ever infected:
\[
B_G(v;\lambda)=\mathbb E\left[\int_0^\tau |I_t|\,dt\right].
\]
The infected individual may recover and become infected again; repeat infectious episodes contribute to the integral. All expectations are finite for a finite graph and fixed rate.

## Proof

**1. Monotonicity under adding an edge.** For two graphs on the same vertices with one edge set included in the other, couple the SIS processes via common recovery Poisson clocks and common infection-arrow clocks on shared edges, plus independent arrows on the extra edges. The infected-set inclusion is preserved pathwise from the same initial infected set (the attractive graphical construction). Consequently the integral \(\int|I_t|dt\) is no smaller on the larger graph. If an edge is added between two distinct vertices, a uniformly seeded initial infection starts at one endpoint with positive probability; an infection arrow across the added edge before all recovery events, while the corresponding vertex remains uninfected in the smaller process, has positive probability, giving strict increase for \(\lambda>0\). This also extends to graphs in which the extra edge makes two previously disconnected components communicate.

**2. No switching through four vertices.** Deleting vertex \(v\) from an \(n\)-vertex graph leaves \(n-1\) vertices and exactly \(|E(G)|-\deg_G(v)\) edges. For at most three residual vertices, there is exactly one unlabelled simple graph with each admissible edge count \(0,1,2,3\): the empty graph, a single edge plus isolated vertex, a three-vertex path, and a triangle, respectively (with the obvious reductions for one or two residual vertices). These four isomorphism types form a nested edge-inclusion chain. Since the uniform-seed burden is isomorphism invariant and strictly increases along this chain, minimizing the number of residual edges is equivalent to minimizing the burden for every \(\lambda>0\). Precisely the maximum-degree vaccination targets do this.

**3. The order-five witness reduces to a comparison of two residual graphs.** Deleting vertex \(0\) produces \(K_3\sqcup K_1\), while deleting either \(1\) or \(2\) produces the path \(P_4\). Deleting \(3\) or \(4\) leaves a residual graph strictly containing a copy of \(K_3\sqcup K_1\), and hence gives a strictly larger burden than vaccinating \(0\). Thus the complete optimization is exactly the comparison of \(K_3\sqcup K_1\) and \(P_4\).

**4. Exact finite-state Poisson equations.** For a residual four-vertex graph \(H\), write \(f_H(S)\) for the expected cumulative infected person-time from the nonempty infected set \(S\), with \(f_H(\varnothing)=0\). First-step analysis gives, for every \(S\ne\varnothing\),
\[
\left(|S|+\lambda\sum_{u\notin S}d_S(u)\right)f_H(S)
-\sum_{u\in S}f_H(S\setminus\{u\})
-\lambda\sum_{u\notin S}d_S(u)f_H(S\cup\{u\})=|S|,
\]
where \(d_S(u)\) is the number of neighbors of \(u\) in \(S\). The objective is \(B_H(\lambda)=\frac14\sum_{u\in V(H)}f_H(\{u\})\). There are exactly fifteen nonempty subsets, and their generator submatrix is invertible at every positive rate because absorption occurs almost surely. Exact elimination yields
\[
B_{K_3\sqcup K_1}(\lambda)=\frac{3\lambda^2+3\lambda+2}{2},
\]
and
\[
B_{P_4}(\lambda)=\frac{48\lambda^8+328\lambda^7+1075\lambda^6+2250\lambda^5+3233\lambda^4+3196\lambda^3+2088\lambda^2+816\lambda+144}{2(4\lambda^2+9\lambda+6)(12\lambda^3+31\lambda^2+32\lambda+12)}.
\]
Subtracting and factoring gives
\[
B_{P_4}-B_{K_3\sqcup K_1}=
\frac{\lambda^2(\lambda+1)(48\lambda^5+136\lambda^4+99\lambda^3-78\lambda^2-156\lambda-72)}{2(4\lambda^2+9\lambda+6)(12\lambda^3+31\lambda^2+32\lambda+12)}.
\]
All denominator factors are positive for \(\lambda>0\). The quintic numerator's coefficients in descending order have exactly one sign change. Descartes' rule of signs bounds the number of positive roots by one; since the quintic is negative at zero and tends to positive infinity, exactly one such root exists. Its sign is negative below \(\lambda_*\) and positive above. Because lower burden is better, this yields the asserted unique transition and optimizer sets. The lower-order theorem proves sharpness.

## Verification

The accompanying `verify_sis.py` reconstructs the fifteen-state Poisson systems directly from each four-vertex graph, symbolically solves the two relevant cases, verifies the complete numerator, denominator, factorization, and unique-positive-root criterion, checks the witness residual graph classes, and independently recomputes every vaccination option at five rational transmission rates. Run `python verify_sis.py` with Python 3.10 or later and SymPy 1.12 or later. All identities are exact except the printed decimal approximation of the algebraic root. The script's finite rational evaluations are additional checks, not a substitute for the proof's positive-real-parameter arguments.

## Relationship to prior work

Ball, Britton and Neal (2014, arXiv:1408.0641) analyze expected accumulated infectious lifetimes and SIS dynamics in homogeneous-mixing birth–death models, not single-vertex removal over arbitrary finite contact graphs. Van de Bovenkamp and Van Mieghem (2015, DOI 10.1103/PhysRevE.92.032806) give an exact SIS extinction-time framework, focusing on complete and star graphs and extinction time rather than cumulative burden under intervention. Holme (2017, arXiv:1708.06456) studies exact vaccination problems for the *SIR* process with permanent removal, using the number ever infected; that target is not the cumulative infection time of a reinfecting SIS process. Holme and Tupikina (2018, arXiv:1802.08849) solve *SIS extinction time* exactly for small graphs and examine rankings of **initial infection configurations**, not single-vertex vaccination minimizing cumulative person-time. Those studies motivate exact small-network theory but their stated results do not entail the present optimization cutoff.

## Limitations

This is a mathematical characterization of one perfectly vaccinated vertex, one uniformly seeded index case, homogeneous Markovian infection/recovery, no further imports, and the specified cumulative person-time loss. It is not a claim about empirical vaccine allocation, clinical effectiveness, SIR final epidemic sizes, SIS extinction time, simultaneous multiple vaccinations, heterogeneity, or large-graph optimum strategies. The selected references and searched sources support but do not independently certify historical originality; results using different terminology for integrated prevalence could remain overlooked. 

## References

1. F. Ball, T. Britton, P. Neal (2014), *On expected durations of birth-death processes, with applications to branching processes and SIS epidemics*, arXiv:1408.0641, first public version 2014-08-04, https://arxiv.org/abs/1408.0641.
2. R. van de Bovenkamp, P. Van Mieghem (2015), *Survival time of the susceptible-infected-susceptible infection process on a graph*, Physical Review E 92, 032806, https://doi.org/10.1103/PhysRevE.92.032806.
3. P. Holme (2017), *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456, https://arxiv.org/abs/1708.06456.
4. P. Holme, L. Tupikina (2018), *Epidemic extinction in networks: Insights from the 12,110 smallest graphs*, arXiv:1802.08849, https://arxiv.org/abs/1802.08849.
