# Five-vertex cutoff for transmissibility-dependent optimal single-node vaccination

## Finding

For every finite simple undirected contact graph \(G=(V,E)\) with \(2\le |V|\le4\), and every edge-retention probability \(p\in[0,1]\), vaccinating any vertex of maximum degree minimizes the expected final outbreak size in the uniform-seed, independent-undirected-bond transmission model defined below. Thus, on these networks there is a fixed optimal vaccination target for all transmission probabilities.

**The order bound is sharp, even for connected graphs.** Let the five-vertex contact graph have vertices \(a,b,c,d,e\) and edges
\[
E=\{ab,bd,be,cd,ce,de\}.
\]
For every \(0<p<1/4\), vaccinating \(d\) or \(e\) is optimal, and no other vertex is optimal. At \(p=1/4\), exactly \(b,d,e\) tie. For every \(1/4<p<1\), only vaccinating \(b\) is optimal. In particular, no vertex is optimal uniformly over \(0<p<1\).

If \(Q_v(p)\) denotes the expected outbreak size after vaccination of vertex \(v\), then the exact comparison is
\[
Q_b(p)-Q_d(p)=\frac{p^2(1-4p)}{2},\qquad Q_d(p)=Q_e(p).
\]
The switch is between vertices of the *same maximum degree* (three): static degree ranking alone is insufficient to choose between them.

## Assumptions and scope

A perfect vaccine completely removes exactly one vertex \(v\) and all of its incident edges **before** importation. One initially infected vertex is then sampled uniformly among the \(n-1\) unvaccinated vertices, independently of transmission. Every remaining **undirected** edge is retained independently with probability \(p\), with the same retained/absent status for transmission in either direction. The final infected set is exactly the connected component of the source in the retained subgraph. The loss is the expected number of ultimately infected unvaccinated vertices, including the source. This is an explicitly specified bond-percolation outbreak model, not an assertion of equivalence with arbitrary continuous-time SIR laws or independently sampled directional contacts.

Write \(G-v\) for the residual graph, and let \(\mathcal C_p(G-v)\) be the collection of connected components of its independently retained subgraph. Then
\[
Q_v(p)=\frac{1}{n-1}\mathbb E\left[\sum_{C\in\mathcal C_p(G-v)}|C|^2\right].
\]
The equality follows because a uniform seed falls in a size-\(k\) component with probability \(k/(n-1)\). Equivalently, for the residual vertex set \(W=V\setminus\{v\}\),
\[
(n-1)Q_v(p)=n-1+2\sum_{\{x,y\}\subset W}\Pr_p(x\leftrightarrow y).
\]

## Proof

**Lower bound.** At most three vertices remain after vaccination if \(n\le4\). Every simple graph on at most three vertices is determined up to isomorphism by its number of edges, and those isomorphism types form an edge-inclusion chain: empty graph, one edge, two-edge path, triangle (truncate the chain when fewer vertices remain). Coupling each added edge with an independent Bernoulli-\(p\) variable shows that the expected sum of squared component sizes cannot decrease as edges are added. Thus \(Q_v(p)\) is nondecreasing in the number \(|E|-\deg_G(v)\) of residual edges. A maximum-degree vertex minimizes that number, and hence minimizes \(Q_v(p)\) for every \(p\in[0,1]\). This also handles disconnected contact graphs. The bound is trivial for \(n=2\).

**Five-vertex witness.** Vaccinating \(b\) leaves a triangle on \(c,d,e\) and an isolated vertex \(a\). Any fixed pair in the triangle is connected after percolation with probability \(p+(1-p)p^2=p+p^2-p^3\). Accordingly,
\[
4Q_b(p)=4+6p+6p^2-6p^3.
\]
Vaccinating \(d\) or \(e\) leaves a four-vertex path. Its unordered vertex pairs have path distances \(1,2,3\) in multiplicities \(3,2,1\), so
\[
4Q_d(p)=4Q_e(p)=4+6p+4p^2+2p^3.
\]
Subtracting gives \(Q_b(p)-Q_d(p)=p^2(1-4p)/2\).

Vaccinating \(a\) leaves the diamond with edges \(bd,be,cd,ce,de\), which contains the spanning path \(b-d-c-e\) as a proper subgraph. Vaccinating \(c\) leaves a triangle with a pendant vertex, containing the spanning path \(a-b-d-e\) as a proper subgraph. Under an independent-bond coupling, adding edges cannot lower the squared-component sum; for \(0<p<1\), each added edge is strictly beneficial with positive probability. Hence \(Q_a(p)>Q_d(p)\) and \(Q_c(p)>Q_d(p)\) throughout \(0<p<1\). The previously computed sign comparison between \(b\) and \(d,e\) now gives the asserted *complete* optimal-vertex classification. The example is connected, so five is the least possible connected order for such a switch.

## Verification

The standalone `verify.py` enumerates every retained-edge configuration and constructs exact integer power-basis coefficients of the residual squared-component expectation. It independently checks all 75 labelled simple graphs of orders one through four, the five witness vertex-deletion polynomials, and the two strict path inclusions. The polynomials for \(4Q_v(p)\), in vertex order \((a,b,c,d,e)\), are
\[
\begin{aligned}
&4+10p+16p^2-28p^4+14p^5,\\
&4+6p+6p^2-6p^3,\\
&4+8p+10p^2-2p^3-4p^4,\\
&4+6p+4p^2+2p^3,\\
&4+6p+4p^2+2p^3.
\end{aligned}
\]
These computations cross-check exact formulas; the lower bound and witness classification above do not depend on finite numerical sampling.

Run with a standard Python 3 interpreter: `python verify.py`. The program has no third-party dependencies.

## Relationship to prior work

Newman's 2002 study connects epidemic spread with bond percolation, providing the motivating transmission framework; the present result is specifically about optimal **single-vertex removal** on every graph of sufficiently small order and an exact five-vertex switch. Kenah and Miller's 2011 epidemic-percolation-network study discusses vaccination target selection more generally, including models with directional transmission, but does not state this finite undirected-graph cutoff. Altarelli and collaborators' 2013 preprint and 2014 article compare degree-based immunization with optimization techniques; the present statement is an exact minimal-order theorem and does not follow merely from their large-network heuristic comparisons. Existing exact tree-only vaccination calculations do not imply a bound for graphs containing cycles.

## Limitations

The claim concerns one perfect vaccination, one uniform seed chosen among remaining vertices, common independently retained **undirected** edges, and expected *outbreak size*, not outbreak-tail risk, intervention cost, multiple vaccinations, heterogeneous contacts, arbitrary SIR contact laws, or empirical effectiveness. A more general epidemic model need not obey the same cutoff. The historical-priority comparison covers the primary works listed below and targeted searches, not every possible publication; independent review remains necessary. The phrase "degree ranking is insufficient" refers to the need to break a maximum-degree tie using transmissibility, not to the failure to choose a maximum-degree vertex in this particular witness.

## References

1. M. E. J. Newman, *The spread of epidemic disease on networks*, arXiv:cond-mat/0205009v1 (first submitted 2002-04-30); *Physical Review E* 66, 016128 (2002). https://arxiv.org/abs/cond-mat/0205009
2. E. Kenah and J. C. Miller, *Epidemic Percolation Networks, Epidemic Outcomes, and Interventions*, *Interdisciplinary Perspectives on Infectious Diseases* 2011, 543520 (first published 2011-02-21). https://doi.org/10.1155/2011/543520
3. F. Altarelli, A. Braunstein, L. Dall'Asta, J. R. Wakeling, and R. Zecchina, *Containing epidemic outbreaks by message-passing techniques*, arXiv:1309.2805v1 (first submitted 2013-09-11); *Physical Review X* 4, 021024 (2014). https://arxiv.org/abs/1309.2805
4. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, arXiv:q-bio/0610057 (2006); *Physical Review E* 76, 036113 (2007). https://arxiv.org/abs/q-bio/0610057
