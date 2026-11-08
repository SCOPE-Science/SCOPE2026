# Sink-deletion bijection for full sandpile avalanches and a wheel sink-location transition

## Finding
Let \(G\) be a finite connected undirected loopless graph, possibly with parallel edges, with sink \(s\). If a single grain is added at a fixed neighbor \(v\) of \(s\), the number of recurrent sandpile states for which the resulting avalanche topples **every** nonsink vertex is
\[
N_{G,s}(v)=\tau(G-s).
\]
Here \(G-s\) is the graph obtained by deleting the sink and all incident edges; \(\tau(H)\) is its spanning-tree count, taken as zero for disconnected \(H\). In particular, the count does not depend on the selected neighbor of \(s\).

For the wheel \(W_{n+1}=K_1\vee C_n\), with \(n\ge3\), let \(F_k\) and \(L_k\) denote the Fibonacci and Lucas numbers, with \(F_0=0,F_1=1,L_0=2,L_1=1\), and put \(\varphi=(1+\sqrt5)/2\). The exact probabilities for a uniformly recurrent initial sandpile and any fixed source adjacent to its sink are
\[
p_n^{\mathrm{rim\ sink}}=\frac{F_{2n-2}}{L_{2n}-2}\longrightarrow\frac{1}{\sqrt5\,\varphi^2},
\qquad
p_n^{\mathrm{hub\ sink}}=\frac{n}{L_{2n}-2}=O(n\varphi^{-2n}).
\]
Thus moving the sink from the hub to a rim vertex changes the full-system avalanche probability from exponentially vanishing to a positive limiting constant.

## Assumptions and scope
A stable sandpile \(c\) assigns \(0\le c(u)<d_G(u)\) grains to each nonsink vertex. A vertex with at least its degree in grains can topple, sending one grain along each incident edge, with grains entering \(s\) discarded. An initial configuration is recurrent according to the standard Dhar burning test. A *principal avalanche at* \(v\) means adding one grain at \(v\) to a recurrent stable configuration and legally stabilizing. Its *full-system event* means that every nonsink vertex topples at least once, not merely that the avalanche is large. Each initial recurrent configuration is equally likely. The theorem concerns \(v\) with at least one edge to \(s\), including the possibility of multiple such edges.

## Proof
Write \(b_u\) for the multiplicity of edges from \(u\) to \(s\), and \(m_{uv}\) for the multiplicity of edges between other vertices. Dhar's burning test says that a stable state \(c\) is recurrent exactly when stabilizing \(c+b\) legally topples each nonsink vertex once and returns \(c\). In a principal avalanche started at \(v\) adjacent to the sink, no vertex can topple twice. Indeed, consider the first hypothetical second toppling at a vertex \(w\), so every other vertex has toppled at most once. After its first toppling, \(w\) can have at most \(c(w)-b_w\) grains if \(w\ne v\), or at most \(c(v)+1-b_v\) grains if \(w=v\). The former is less than \(d_G(w)\) by stability, and the latter is less than \(d_G(v)\) because \(b_v\ge1\). Neither can topple again. Thus a full-system event makes every nonsink vertex topple **exactly once**.

Assume first that \(H=G-s\) is connected. If \(c\) gives a full avalanche at \(v\), then necessarily \(c(v)=d_G(v)-1\), because no other vertex can topple before the newly perturbed \(v\) does. At the end of the avalanche the heights at all \(u\ne s,v\) are \(c(u)-b_u\) and are nonnegative. Define a configuration on \(H\), now taking \(v\) as sink, by
\[
\eta(u)=c(u)-b_u,\qquad u\in V(H)\setminus\{v\}.
\]
It is stable because \(\eta(u)<d_G(u)-b_u=d_H(u)\). After the first topple at \(v\), each other vertex can topple in some legal order exactly once. In \(H\), start from \(\eta\) and add its sink-edge vector \((m_{uv})_{u\ne v}\). The same legal sequence is possible after accounting for the \(b_u\) grains held by each vertex before its first toppling: at every yet-unfired vertex, subtracting \(b_u\) gives exactly the corresponding height in the burning process on \(H\), and its instability threshold drops from \(d_G(u)\) to \(d_H(u)\). Once that vertex fires, the \(b_u\) reserve is lost to the old sink. Hence the same order is legal and its terminal state on \(H\) is \(\eta\). By the burning criterion, \(\eta\) is recurrent on \(H\) with sink \(v\).

Conversely, from any recurrent stable \(\eta\) on \(H\) with sink \(v\), set
\[
c(v)=d_G(v)-1,\qquad c(u)=\eta(u)+b_u\quad(u\notin\{s,v\}).
\]
This is stable on \(G\). Adding a grain at \(v\) forces an immediate topple there. The remaining nonsink vertices then follow the complete once-per-vertex burning sequence of \(\eta\) in \(H\). The resulting heights are \(\eta(u)\) at all other vertices and \(d_G(v)-b_v<d_G(v)\) at \(v\); hence this is a legal full-system principal avalanche. It remains to verify that \(c\) is recurrent on \(G\). Start instead with \(c+b\). Since \(b_v\ge1\), topple \(v\) first and use the same legal sequence for all remaining vertices (the extra nonnegative contributions at other vertices cannot invalidate legal topplings). Every nonsink vertex has toppled once; by conservation the resulting heights are exactly \(c\). Dhar's burning test therefore proves recurrence of \(c\). The two maps are inverse bijections. By the matrix-tree theorem the number of recurrent states of \(H\) with sink \(v\) is \(\tau(H)\), establishing the first assertion. If \(H\) is disconnected, adding a grain at \(v\) cannot reach a component outside its component in \(H\), so no full-system avalanche exists, matching \(\tau(H)=0\).

For the wheel, total recurrent states equal \(\tau(W_{n+1})\). With the hub as sink the deletion graph is \(C_n\), hence exactly \(n\) full-system states for each fixed rim source. With a rim vertex as sink the deletion graph is the fan \(K_1\vee P_{n-1}\), whose spanning-tree counts \(t_1=1,t_2=3,t_k=3t_{k-1}-t_{k-2}\) give \(t_{n-1}=F_{2n-2}\). The cycle-rim reduced Laplacian for the hub sink is \(3I-A(C_n)\), so
\[
\tau(W_{n+1})=\prod_{j=0}^{n-1}\left(3-2\cos\frac{2\pi j}{n}\right)=L_{2n}-2.
\]
The two probability formulas now follow. Finally, Binet's formulas yield \(F_{2n-2}\sim\varphi^{2n-2}/\sqrt5\) and \(L_{2n}-2\sim\varphi^{2n}\), proving both limits.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It checks the count directly from legal topplings and the burning-test enumeration against an independent integer matrix-tree determinant on 207 connected random graphs of orders three through six (469 eligible source comparisons). It additionally checks both sink placements on wheels with rim sizes three through seven by enumeration, and prints exact Fibonacci/Lucas counts through size ten. Run `python verify.py`. All finite checks passed. The proof above, rather than the finite sample, establishes the unrestricted theorem.

## Relationship to prior work
Dartois and Rossin (2006) derive full avalanche distributions for wheels with the standard hub sink using word-language and automata. Austin et al. (2016) give multivariate avalanche polynomials for trees, cycles, wheels and complete graphs and explicitly state the one-topple bound when a grain is added next to the sink. Those known wheel counts and the burning criterion are **not** claimed as new. The claimed addition is a general sink-deletion bijection for the maximal principal avalanche and its exact quantitative comparison of two non-equivalent wheel sink positions. Wu, Zhang and Chen (2017) study spanning-tree/recurrent-configuration correspondences and avalanche toppling totals; their full text was inaccessible at review, so overlapping formulations remain a specific priority risk.

## Limitations
This result does not describe all smaller avalanches or their size distribution. The event and the uniform recurrent law are essential. The full probability is source-independent only **among neighbors of a fixed sink**. The historical novelty assessment is based on accessible literature and searches, not on a proof of global priority; a plausible 2017 source could be inspected only at abstract level. No independent audit has been performed.

## References
- A. Dartois and D. Rossin, *Sandpile avalanche distribution on the wheel*, preprint ccsd-00016372v1, publicly dated 2006-01-02; https://www.researchgate.net/publication/239761073_Sandpile_avalanche_distribution_on_the_wheel .
- D. Austin, M. Chambers, R. Funke, L. D. García Puente and L. Keough, *The Avalanche Polynomial of a Graph*, arXiv:1605.02713, first posted 2016-05-09; https://arxiv.org/abs/1605.02713 .
- X. Wu, L. Zhang and H. Chen, *Spanning trees and recurrent configurations of a graph*, Applied Mathematics and Computation 314 (2017), 25–30, doi:10.1016/j.amc.2017.06.030 (abstract inspected; full text inaccessible).
